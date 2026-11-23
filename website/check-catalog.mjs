import { readFileSync } from "node:fs";
import { join } from "node:path";
import { readCatalog, readPresetMarkdown, validateCatalog } from "./catalog.mjs";

const root = process.argv[2];
const { entries, obsolete, contributions } = JSON.parse(readFileSync(0, "utf8"));
const redirects = JSON.parse(readFileSync(join(root, "website/path-redirects.json"), "utf8"));
try {
    validateCatalog(readCatalog(root, entries, obsolete), redirects, contributions);
    const parsed = [];
    for (const { catalog, type } of contributions) {
        try {
            const { data } = readPresetMarkdown(join(root, catalog));
            if (data.type !== type) throw new Error("website parser read a different preset type");
            const metadata = { ...data };
            for (const key of ["created", "updated"]) {
                if (metadata[key] instanceof Date) {
                    metadata[key] = metadata[key].toISOString().slice(0, 10);
                }
            }
            parsed.push({ catalog, metadata });
        } catch (error) {
            throw new Error(`${catalog}: ${error.message}`);
        }
    }
    // Only the date fields are normalized. Dates in other fields must fail the string schema.
    process.stdout.write(JSON.stringify(parsed, function (key, value) {
        return this[key] instanceof Date ? null : value;
    }));
} catch (error) {
    console.error(error.message);
    process.exitCode = 1;
}
