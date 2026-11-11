# Next.js masters

These two files are the original source for the first stack. They are not catalog entries.

| Master | File | Catalog role |
| --- | --- | --- |
| Standards | [standards.md](standards.md) | One rule or instruction for each tool |
| Skill | [skill.md](skill.md) | One `SKILL.md` audit for each tool |

Tool-specific install notes live in `preamble/` (catalog page only) and `host/` (included in the native file). `sources.md` is the shared source list appended to each catalog page.

`python scripts/assemble_release.py` writes the 14 catalog files and the native install files. The site should install the native files, not the catalog frontmatter.
