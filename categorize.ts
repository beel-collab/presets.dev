import type { RuleCategory, RuleTool } from "./types";

const RULES_TOOLS: ReadonlySet<RuleTool> = new Set([
    "cursor", "windsurf", "antigravity", "cline", "codex",
]);

export function categorizeFile(fileName: string, tool: RuleTool): RuleCategory {
    if (fileName === "AGENTS.md" || fileName.endsWith(".agent.md")) return "agents";
    if (fileName === "CLAUDE.md" || fileName.endsWith(".instructions.md")) return "instructions";
    if (fileName.endsWith(".mdc") || RULES_TOOLS.has(tool)) return "rules";
    return "instructions";
}
