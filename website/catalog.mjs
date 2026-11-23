import { lstatSync, readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import matter from "gray-matter";
import layout from "./catalog-layout.json" with { type: "json" };
import { catalogPaths, presetId, presetPath } from "./catalog-identity.mjs";

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

/** @param {string} root @param {Entry[]} entries @param {Iterable<string>} [removed] */
export function readCatalog(root, entries, removed = []) {
    const registered = new Map(entries.map(({ catalog, type }) => [catalog, categories[type]]));
    const obsolete = new Set(removed);
    /** @type {Map<string, Preset>} */
    const catalog = new Map();

    /** @param {string} sourcePath @param {Tool} tool @param {Preset["category"]} category
     * @param {string} technology @param {string} slug */
    function add(sourcePath, tool, category, technology, slug) {
        const parts = sourcePath.split("/");
        if (obsolete.has(sourcePath) || parts.some((part) => layout.supportDirectories.includes(part)) ||
            layout.documentationFiles.includes(parts.at(-1))) return;
        catalog.set(sourcePath, { sourcePath, tool, technology, slug, category: registered.get(sourcePath) ?? category });
    }

    const claudeDirectories = new Set(children(root, "claude").filter((entry) => entry.isDirectory()).map((entry) => entry.name));
    for (const tool of tools) {
        const folders = tool === "claude" ? claudeFolders.filter((folder) => claudeDirectories.has(folder)) : [""];
        for (const folder of folders) {
            const base = folder ? `${tool}/${folder}` : tool;
            for (const topic of children(root, base)) {
                if (!topic.isDirectory()) continue;
                const dir = `${base}/${topic.name}`;
                for (const child of children(root, dir)) {
                    const source = `${dir}/${child.name}`;
                    if (child.isDirectory()) {
                        if (children(root, source).some((file) => file.isFile() && file.name === "SKILL.md")) {
                            add(`${source}/SKILL.md`, tool, "skills", topic.name, child.name);
                        }
                    } else if (child.isFile() && (child.name.endsWith(".md") || (!folder && child.name.endsWith(".mdc")))) {
                        const category = folder || legacyCategory(child.name, tool);
                        add(source, tool, category, topic.name, fileSlug(child.name, topic.name, !folder));
                    }
                }
            }
        }
    }

    for (const { catalog: source, type } of entries) {
        if (catalog.has(source)) continue;
        const parts = source.split("/");
        const [tool, first, second] = parts;
        const tech = tool === "claude" && claudeFolders.some((folder) => folder === first) ? second : first;
        const slug = type === "skill" ? parts.at(-2) : fileSlug(parts.at(-1), tech, true);
        if (!tools.some((valid) => valid === tool) || !tech || !slug) throw new Error(`Invalid catalog path: ${source}`);
        add(source, /** @type {Tool} */ (tool), categories[type], tech, slug);
    }
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
    const ids = new Map();
    const bySource = new Map();
    for (const preset of catalog) {
        const id = presetId(preset);
        const previous = ids.get(id);
        if (previous) throw new Error(`Public catalog ID ${id} conflicts with ${previous} and ${preset.sourcePath}`);
        ids.set(id, preset.sourcePath);
        bySource.set(preset.sourcePath, preset);
        for (const route of catalogPaths(presetPath(preset))) {
            if (Object.hasOwn(redirects, route)) {
                throw new Error(`${preset.sourcePath}: public route ${route} is reserved by a permanent redirect. Choose a different path.`);
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
