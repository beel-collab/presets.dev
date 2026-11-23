import { lstatSync, readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import matter from "gray-matter";
import layout from "./catalog-layout.json" with { type: "json" };
import { catalogPaths, presetId, presetPath } from "./catalog-identity.mjs";
import { validateRedirectGraph } from "./redirect-graph.mjs";

const tools = /** @type {const} */ (["copilot", "cursor", "windsurf", "antigravity", "cline", "codex", "claude"]);
const claudeFolders = /** @type {const} */ (["agents", "skills", "instructions"]);
const categories = /** @type {const} */ ({ rule: "rules", instruction: "instructions", skill: "skills", agent: "agents" });

/** @typedef {typeof tools[number]} Tool */
/** @typedef {keyof typeof categories} Kind */
/** @typedef {{sourcePath: string, tool: Tool, category: typeof categories[Kind], technology: string, slug: string}} Preset */
/** @typedef {{catalog: string, type: Kind}} Entry */

/** @param {string} filename @param {Tool} tool */
function legacyCategory(filename, tool) {
    if (filename === "AGENTS.md" || filename.endsWith(".agent.md")) return "agents";
    if (filename === "CLAUDE.md" || filename.endsWith(".instructions.md")) return "instructions";
    return tool !== "copilot" || filename.endsWith(".mdc") ? "rules" : "instructions";
}

/** @param {string} root @param {string} folder */
function children(root, folder) {
    try {
        const directory = join(root, folder);
        if (!lstatSync(directory).isDirectory()) return [];
        return readdirSync(directory, { withFileTypes: true });
    } catch (error) {
        if (/** @type {NodeJS.ErrnoException} */ (error).code === "ENOENT") return [];
        throw error;
    }
}

/**
 * The one place that maps a content path to its public identity.
 * `<tool>/<topic>/<file>`, `claude/<folder>/<topic>/<file>`, or a skill's `.../<topic>/<name>/SKILL.md`.
 * @param {string} sourcePath @param {Kind} [type] the registered type, when the release map names one
 * @returns {Preset | null}
 */
export function describeCatalogPath(sourcePath, type) {
    const parts = sourcePath.split("/");
    const tool = tools.find((valid) => valid === parts[0]);
    if (!tool || parts.some((part) => !part)) return null;
    const folder = tool === "claude" ? claudeFolders.find((valid) => valid === parts[1]) ?? "" : "";
    const topicIndex = folder ? 2 : 1;
    const technology = parts[topicIndex];
    const filename = parts.at(-1);
    if (!technology || !filename || parts.some((part) => layout.supportDirectories.includes(part)) ||
        layout.documentationFiles.includes(filename)) return null;

    if (filename === "SKILL.md" && parts.length === topicIndex + 3) {
        return { sourcePath, tool, technology, slug: parts[topicIndex + 1], category: categories[type ?? "skill"] };
    }
    if (parts.length !== topicIndex + 2) return null;
    if (!filename.endsWith(".md") && (folder || !filename.endsWith(".mdc"))) return null;
    const category = type ? categories[type] : folder || legacyCategory(filename, tool);
    return { sourcePath, tool, technology, slug: fileSlug(filename, technology, !folder), category };
}

/** @param {string} root @param {Entry[]} entries @param {Iterable<string>} [removed] */
export function readCatalog(root, entries, removed = []) {
    const registered = new Map(entries.map(({ catalog, type }) => [catalog, type]));
    const obsolete = new Set(removed);
    /** @type {Map<string, Preset>} */
    const catalog = new Map();

    /** @param {string} sourcePath */
    function add(sourcePath) {
        if (obsolete.has(sourcePath) || catalog.has(sourcePath)) return;
        const preset = describeCatalogPath(sourcePath, registered.get(sourcePath));
        if (preset) catalog.set(sourcePath, preset);
        else if (registered.has(sourcePath)) {
            throw new Error(`${sourcePath}: expected a topic directory and a documented catalog file name`);
        }
    }

    const claudeDirectories = new Set(children(root, "claude").filter((entry) => entry.isDirectory()).map((entry) => entry.name));
    for (const tool of tools) {
        // Claude rules outside the agents/skills/instructions folders are published only through the release map.
        const folders = tool === "claude" ? claudeFolders.filter((folder) => claudeDirectories.has(folder)) : [""];
        for (const folder of folders) {
            const base = folder ? `${tool}/${folder}` : tool;
            for (const topic of children(root, base)) {
                if (!topic.isDirectory()) continue;
                const dir = `${base}/${topic.name}`;
                for (const child of children(root, dir)) {
                    const source = `${dir}/${child.name}`;
                    if (child.isFile()) add(source);
                    else if (child.isDirectory() && children(root, source).some((file) => file.isFile() && file.name === "SKILL.md")) {
                        add(`${source}/SKILL.md`);
                    }
                }
            }
        }
    }
    for (const { catalog: source } of entries) add(source);
    return [...catalog.values()];
}

/** @param {string} file */
export function readPresetMarkdown(file) {
    return matter(readFileSync(file, "utf8"));
}

/** @param {string} filename @param {string} tech @param {boolean} useAgentTopic */
function fileSlug(filename, tech, useAgentTopic) {
    if (filename === "CLAUDE.md" || (useAgentTopic && filename === "AGENTS.md")) return tech;
    return filename.replace(/\.(agent|instructions|prompt)\.md$/, "").replace(/\.(md|mdc)$/, "");
}

/** @param {Preset[]} catalog @param {Record<string, string>} redirects
 * @param {Entry[]} [contributions] */
export function validateCatalog(catalog, redirects, contributions = []) {
    validateRedirectGraph(redirects);
    const ids = new Map();
    const bySource = new Map();
    for (const preset of catalog) {
        const id = presetId(preset);
        const previous = ids.get(id);
        if (previous) throw new Error(`Public catalog ID ${id} conflicts with ${previous} and ${preset.sourcePath}`);
        ids.set(id, preset.sourcePath);
        bySource.set(preset.sourcePath, preset);
        const detail = presetPath(preset);
        if (Object.hasOwn(redirects, detail)) {
            throw new Error(`${preset.sourcePath}: public route ${detail} is reserved by a permanent redirect. Choose a different file name.`);
        }
        for (const listing of catalogPaths(detail).slice(0, -1)) {
            // A listing redirect only exists because the listing was once empty. Publishing into it retires the redirect.
            if (Object.hasOwn(redirects, listing)) {
                throw new Error(`${preset.sourcePath}: this preset brings back the listing ${listing}. Remove "${listing}" from website/path-redirects.json in the same change.`);
            }
        }
    }
    for (const { catalog: source, type } of contributions) {
        const preset = bySource.get(source);
        if (!preset || preset.category !== categories[type]) {
            throw new Error(`${source}: use a documented catalog path for a preset of type ${type}`);
        }
    }
}
