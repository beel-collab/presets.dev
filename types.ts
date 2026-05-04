/**
 * Rule Interface
 * This is the main data structure for all rules, prompts, agents, and instructions
 */
export interface Rule {
    // Required fields
    slug: string;
    title: string;
    content: string;
    tags: string[];

    // Derived from file location
    tool: RuleTool;
    category: RuleCategory;
    technology?: string;

    // Optional fields from frontmatter
    description?: string;
    libs?: string[];

    // Author information
    author?: {
        name: string;
        url?: string;
        avatar?: string;
    };

    // Cursor-specific fields
    globs?: string | string[];
    alwaysApply?: boolean;
    // Windsurf-specific fields
    trigger?: "always_on" | "model_decision" | "glob" | "manual";

    // Cross-tool compatibility
    also_for?: RuleTool[];
}

export type RuleTool = "copilot" | "cursor" | "windsurf" | "claude" | "antigravity" | "cline" | "codex";
export type RuleCategory = "agents" | "instructions" | "skills" | "rules";

export interface Section {
    tag: string;
    slug: string;
    rules: Rule[];
}

/**
 * Frontmatter structure for markdown files
 */
export interface RuleFrontmatter {
    title?: string;
    description?: string;
    tags?: string[];
    libs?: string[];
    author?: {
        name: string;
        url?: string;
        avatar?: string;
    };
    // Cursor-specific frontmatter fields
    globs?: string | string[];
    alwaysApply?: boolean;
    // Windsurf-specific frontmatter fields
    trigger?: "always_on" | "model_decision" | "glob" | "manual";
    // Cross-tool compatibility
    also_for?: RuleTool[];
}
