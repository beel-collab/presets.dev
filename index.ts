import fs from "fs";
import path from "path";
import matter from "gray-matter";
import slugify from "slugify";
import type { Rule, RuleCategory, RuleTool, RuleFrontmatter, Section } from "./types";
import { categorizeFile } from "./categorize";

const DATA_DIR = path.join(process.cwd(), "src/data");

function parseMarkdownFile(
    filePath: string,
    tool: RuleTool,
    category: RuleCategory
): Rule | null {
    try {
        const fileContent = fs.readFileSync(filePath, "utf-8");
        const { data, content } = matter(fileContent);
        const frontmatter = data as RuleFrontmatter;

        const titleMatch = content.match(/^#\s+(.+)$/m);
        const fileName = path.basename(filePath);
        const slug = fileName
            .replace(/\.(agent|instructions|prompt)\.md$/, "")
            .replace(/\.(md|mdc)$/, "");

        let title = frontmatter.title || titleMatch?.[1] || slug.replace(/-/g, " ");
        title = title.replace(/\.(agent|instructions|prompt)/gi, "").trim();

        let author = frontmatter.author;
        if (author && !author.avatar) {
            if (author.name === "Community") {
                author = { ...author, avatar: "https://github.com/github.png" };
            } else if (author.url) {
                try {
                    const urlObj = new URL(author.url);
                    if (urlObj.hostname === "github.com" || urlObj.hostname === "www.github.com") {
                        const username = urlObj.pathname.split("/").filter(Boolean)[0];
                        if (username) {
                            author = { ...author, avatar: `https://github.com/${username}.png` };
                        }
                    }
                } catch (e) {
                    // ignore invalid URLs
                }
            }
        }

        return {
            slug,
            title,
            content: content.trim(),
            tags: frontmatter.tags || [],
            tool,
            category,
            description: frontmatter.description,
            libs: frontmatter.libs,
            author,
            globs: frontmatter.globs,
            alwaysApply: frontmatter.alwaysApply,
            trigger: frontmatter.trigger,
            also_for: frontmatter.also_for,
        };
    } catch (error) {
        console.error(`Error parsing ${filePath}:`, error);
        return null;
    }
}

// Category folder names used by the claude tool's structured layout
const CLAUDE_CATEGORY_DIRS: Record<string, RuleCategory> = {
    agents:       "agents",
    skills:       "skills",
    instructions: "instructions",
};

function loadClaudeRules(): Rule[] {
    const rules: Rule[] = [];
    const claudeDir = path.join(DATA_DIR, "claude");
    if (!fs.existsSync(claudeDir)) return rules;

    for (const [categoryFolder, category] of Object.entries(CLAUDE_CATEGORY_DIRS)) {
        const categoryDir = path.join(claudeDir, categoryFolder);
        if (!fs.existsSync(categoryDir)) continue;

        for (const techEntry of fs.readdirSync(categoryDir, { withFileTypes: true })) {
            if (!techEntry.isDirectory()) continue;
            const techDir = path.join(categoryDir, techEntry.name);

            for (const child of fs.readdirSync(techDir, { withFileTypes: true })) {
                const childPath = path.join(techDir, child.name);

                if (child.isDirectory()) {
                    // Skill subdirectory — look for SKILL.md
                    const skillFile = path.join(childPath, "SKILL.md");
                    if (fs.existsSync(skillFile)) {
                        const rule = parseMarkdownFile(skillFile, "claude", "skills");
                        if (rule) {
                            rule.slug = child.name;
                            if (!rule.title || rule.title === "SKILL") {
                                rule.title = child.name.replace(/-/g, " ").replace(/\b\w/g, l => l.toUpperCase());
                            }
                            rule.technology = techEntry.name;
                            if (!rule.tags.includes(techEntry.name)) rule.tags.push(techEntry.name);
                            rules.push(rule);
                        }
                    }
                } else if (child.name.endsWith(".md")) {
                    const rule = parseMarkdownFile(childPath, "claude", category);
                    if (rule) {
                        if (child.name === "CLAUDE.md") rule.slug = techEntry.name;
                        rule.technology = techEntry.name;
                        if (!rule.tags.includes(techEntry.name)) rule.tags.push(techEntry.name);
                        rules.push(rule);
                    }
                }
            }
        }
    }
    return rules;
}

function loadToolRules(tool: RuleTool): Rule[] {
    if (tool === "claude") return loadClaudeRules();

    const rules: Rule[] = [];
    const toolDir = path.join(DATA_DIR, tool);

    if (!fs.existsSync(toolDir)) return rules;

    const techDirs = fs.readdirSync(toolDir, { withFileTypes: true });

    for (const techEntry of techDirs) {
        if (!techEntry.isDirectory()) continue;

        const techDir = path.join(toolDir, techEntry.name);
        const techItems = fs.readdirSync(techDir, { withFileTypes: true });

        for (const child of techItems) {
            const childPath = path.join(techDir, child.name);

            if (child.isDirectory()) {
                const skillFile = path.join(childPath, "SKILL.md");
                if (fs.existsSync(skillFile)) {
                    const rule = parseMarkdownFile(skillFile, tool, "skills");
                    if (rule) {
                        rule.slug = child.name;
                        if (!rule.title || rule.title === "SKILL") {
                            rule.title = child.name.replace(/-/g, " ").replace(/\b\w/g, l => l.toUpperCase());
                        }
                        rule.technology = techEntry.name;
                        if (!rule.tags.includes(techEntry.name)) rule.tags.push(techEntry.name);
                        rules.push(rule);
                    }
                }
            } else if (child.name.endsWith(".md") || child.name.endsWith(".mdc")) {
                const category = categorizeFile(child.name, tool);

                const rule = parseMarkdownFile(childPath, tool, category);
                if (rule) {
                    // AGENTS.md and CLAUDE.md use the tech folder name as slug to avoid collisions
                    if (child.name === "AGENTS.md" || child.name === "CLAUDE.md") rule.slug = techEntry.name;
                    rule.technology = techEntry.name;
                    if (!rule.tags.includes(techEntry.name)) rule.tags.push(techEntry.name);
                    rules.push(rule);
                }
            }
        }
    }

    return rules;
}

export function loadAllRules(): Rule[] {
    return [
        ...loadToolRules("copilot"),
        ...loadToolRules("cursor"),
        ...loadToolRules("windsurf"),
        ...loadToolRules("antigravity"),
        ...loadToolRules("cline"),
        ...loadToolRules("codex"),
        ...loadToolRules("claude"),
    ];
}

let cachedRules: Rule[] | null = null;

function loadFromManifest(): Rule[] | null {
    const manifestPath = path.join(DATA_DIR, "manifest.json");
    if (!fs.existsSync(manifestPath)) return null;

    try {
        const raw = fs.readFileSync(manifestPath, "utf-8");
        const manifest = JSON.parse(raw);
        return manifest.rules as Rule[];
    } catch (error) {
        console.error("Failed to load manifest.json, falling back to filesystem scan:", error);
        return null;
    }
}

export function getRules(): Rule[] {
    if (process.env.NODE_ENV === "development") {
        return loadAllRules();
    }
    if (!cachedRules) {
        cachedRules = loadFromManifest() || loadAllRules();
    }
    return cachedRules;
}

export function getSections(): Section[] {
    const rules = getRules();
    const tags = Array.from(new Set(rules.flatMap((rule) => rule.tags)));

    return tags
        .map((tag) => ({
            tag,
            slug: slugify(tag, { lower: true }),
            rules: rules.filter((rule) => rule.tags.includes(tag)),
        }))
        .sort((a, b) => b.rules.length - a.rules.length);
}

export function getSectionBySlug(slug: string): Section | undefined {
    return getSections().find((section) => section.slug === slug);
}

export function getRuleBySlug(slug: string, tool?: string, category?: string): Rule | undefined {
    return getRules().find((rule) =>
        rule.slug === slug &&
        (!tool || rule.tool === tool) &&
        (!category || rule.category === category)
    );
}

export function getRulesByCategory(category: RuleCategory): Rule[] {
    return getRules().filter((rule) => rule.category === category);
}

export function getRulesByTag(tag: string): Rule[] {
    return getRules().filter((rule) =>
        rule.tags.some((t) => t.toLowerCase() === tag.toLowerCase())
    );
}

export function searchRules(query: string): Rule[] {
    const lowerQuery = query.toLowerCase();
    return getRules().filter(
        (rule) =>
            rule.title.toLowerCase().includes(lowerQuery) ||
            rule.description?.toLowerCase().includes(lowerQuery) ||
            rule.tags.some((tag) => tag.toLowerCase().includes(lowerQuery))
    );
}

export function getRulesByTechnology(technology: string): Rule[] {
    return getRules().filter((rule) => rule.technology === technology);
}

export function getRulesByCategoryAndTechnology(category: RuleCategory, technology: string): Rule[] {
    return getRules().filter((rule) => rule.category === category && rule.technology === technology);
}

export function getUniqueTechnologies(): string[] {
    const rules = getRules();
    return Array.from(new Set(rules.map((r) => r.technology).filter(Boolean))) as string[];
}

export function getTechnologiesByCategory(category: RuleCategory): string[] {
    const rules = getRules().filter((r) => r.category === category);
    return Array.from(new Set(rules.map((r) => r.technology).filter(Boolean))) as string[];
}

export function getStats() {
    const rules = getRules();
    return {
        total: rules.length,
        copilot:  rules.filter((r) => r.tool === "copilot").length,
        cursor:   rules.filter((r) => r.tool === "cursor").length,
        windsurf:    rules.filter((r) => r.tool === "windsurf").length,
        antigravity: rules.filter((r) => r.tool === "antigravity").length,
        cline:       rules.filter((r) => r.tool === "cline").length,
        codex:       rules.filter((r) => r.tool === "codex").length,
        claude:      rules.filter((r) => r.tool === "claude").length,
        agents: rules.filter((r) => r.category === "agents").length,
        instructions: rules.filter((r) => r.category === "instructions").length,
        skills: rules.filter((r) => r.category === "skills").length,
        rules: rules.filter((r) => r.category === "rules").length,
    };
}

export type { Rule, Section, RuleCategory, RuleTool, RuleFrontmatter } from "./types";
