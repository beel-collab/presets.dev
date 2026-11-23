import { readFileSync } from "node:fs";
import { join } from "node:path";
import { readCatalog, readPresetMarkdown, validateCatalog } from "./catalog.mjs";

const root = process.argv[2];
const { entries, obsolete, contributions } = JSON.parse(readFileSync(0, "utf8"));
const redirects = JSON.parse(readFileSync(join(root, "website/path-redirects.json"), "utf8"));
try {
    validateCatalog(readCatalog(root, entries, obsolete), redirects, contributions);
    for (const { catalog, type } of contributions) {
        try {
            const { data } = readPresetMarkdown(join(root, catalog));
            if (data.type !== type || typeof data.title !== "string" || !Array.isArray(data.tags)) {
                throw new Error("website parser could not read the preset type, title or tags");
            }
        } catch (error) {
            throw new Error(`${catalog}: ${error.message}`);
        }
    }
} catch (error) {
    console.error(error.message);
    process.exitCode = 1;
}
