import json
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main
from unittest.mock import patch

import yaml

import lint_presets
import standalone_presets
from assemble_release import emit_frontmatter


def write_preset(root: Path, rel: str, preset_id: str, kind: str, **extra) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "id": preset_id,
        "slug": lint_presets.expected_slug(rel),
        "title": "Astro content collections",
        "description": "Use this when working with Astro content collections.",
        "type": kind,
        "tools": [rel.split("/")[0]],
        "tags": ["astro"],
        "author": {"name": "Example contributor"},
        "license": "MIT",
        "origin": "original",
        "version": "1.0.0",
        "tested_with": ["Local fixture"],
        "created": "2026-11-23",
        "updated": "2026-11-23",
        **extra,
    }
    path.write_text(f"---\n{yaml.safe_dump(data)}---\n\n# Collections\n\nValidate collection entries.\n", encoding="utf-8")
    return path


class StandalonePresetsTest(TestCase):
    def package(self, root, originals=None):
        subprocess.run(["git", "init", "--quiet", str(root)], check=True)
        exports = {}
        with patch.object(lint_presets, "ROOT", root), patch.object(standalone_presets, "ROOT", root):
            stacks = standalone_presets.build_standalone(exports, originals or [], emit_frontmatter)
        return {stack["id"]: stack for stack in stacks}, exports

    def test_catalog_ids_package_each_type_and_preserve_skill_assets(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "cursor/astro/astro-collections.mdc", "cursor-astro-collections", "rule",
                         globs=["src/content/**/*.{md,mdx}"])
            write_preset(root, "copilot/astro/astro-collections.instructions.md", "copilot-astro-collections",
                         "instruction", globs=["src/content/**"])
            skill = write_preset(root, "codex/astro/astro-collection-review/SKILL.md", "codex-astro-collection-review", "skill")
            asset = skill.parent / "assets" / "fixture.bin"
            asset.parent.mkdir()
            asset.write_bytes(b"\xff\x00")
            (root / ".gitignore").write_text("*.pyc\n", encoding="utf-8")
            (asset.parent / "local.pyc").write_bytes(b"local cache")
            tracked = asset.parent / "committed.pyc"
            tracked.write_bytes(b"tracked asset")
            subprocess.run(["git", "init", "--quiet", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "add", "--force", str(tracked)], check=True)
            write_preset(root, "copilot/astro/astro-assistant.agent.md", "copilot-astro-assistant", "agent")
            stacks, exports = self.package(root, [{"id": "astro", "entries": []}])

        self.assertEqual(set(stacks), {"cursor-astro-collections", "copilot-astro-collections", "codex-astro-collection-review"})
        self.assertTrue(all(stack["status"] == "complete" and stack["kind"] == "standalone" for stack in stacks.values()))
        rule, = stacks["cursor-astro-collections"]["entries"]
        self.assertEqual(rule["exports"], ["release/cursor-astro-collections/native/cursor/.cursor/rules/cursor-astro-collections.mdc"])
        rule_front, _ = lint_presets.split_frontmatter(exports[rule["exports"][0]])
        self.assertEqual(yaml.safe_load(rule_front)["globs"], "src/content/**/*.{md,mdx}")
        self.assertNotIn("author:", rule_front)
        instruction, = stacks["copilot-astro-collections"]["entries"]
        instructions, _ = lint_presets.split_frontmatter(exports[instruction["exports"][0]])
        self.assertEqual(yaml.safe_load(instructions), {"applyTo": "src/content/**"})
        skill, = stacks["codex-astro-collection-review"]["entries"]
        self.assertIn("/native/agents/.agents/skills/astro-collection-review/SKILL.md", skill["exports"][0])
        assets = {Path(filename).name: exports[filename] for filename in skill["exports"][1:]}
        self.assertEqual(assets, {"committed.pyc": b"tracked asset", "fixture.bin": b"\xff\x00"})

    def test_contribution_cannot_reuse_official_stack_id_or_skill_name(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "cursor/astro/astro-collection-review/SKILL.md", "astro", "skill")
            original = {
                "id": "astro",
                "entries": [{
                    "catalog": "codex/astro/astro-collection-review/SKILL.md",
                    "role": "skill",
                    "type": "skill",
                    "exports": ["release/astro/native/agents/.agents/skills/astro-collection-review/SKILL.md"],
                }],
            }
            with self.assertRaisesRegex(SystemExit, "CLI install ID"):
                self.package(root, [original])
            original["id"] = "other"
            with self.assertRaisesRegex(SystemExit, "skill install name"):
                self.package(root, [original])

    def test_contributions_to_different_tools_cannot_share_skill_name(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            for tool in ("codex", "cursor"):
                write_preset(root, f"{tool}/astro/astro-collection-review/SKILL.md",
                             f"{tool}-astro-collection-review", "skill")
            with self.assertRaisesRegex(SystemExit, "skill install name"):
                self.package(root)

    def test_standalone_install_cannot_overwrite_original_export(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "cursor/nextjs/nextjs-collections.mdc", "nextjs-rules", "rule")
            original = {
                "id": "nextjs",
                "entries": [{
                    "catalog": "cursor/nextjs/nextjs-rules.mdc",
                    "role": "standards",
                    "type": "rule",
                    "exports": ["release/nextjs/native/cursor/.cursor/rules/nextjs-rules.mdc"],
                }],
            }
            with self.assertRaisesRegex(SystemExit, "install path .* conflicts"):
                self.package(root, [original])

    def test_contributions_cannot_share_a_normalized_catalog_id(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "copilot/astro/astro-collections.mdc", "astro-collections-rule", "rule")
            write_preset(root, "copilot/astro/astro-collections.md.prompt.md", "astro-collections-prompt", "rule")
            with self.assertRaisesRegex(SystemExit, "public catalog ID conflicts"):
                self.package(root)

    def test_retired_catalog_path_requires_a_fresh_filename(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            rel = "cursor/astro/astro-collections.mdc"
            write_preset(root, rel, "cursor-astro-collections", "rule")
            retirement_map = root / "release/original-2026-11/retirement-map.json"
            retirement_map.parent.mkdir(parents=True)
            retirement_map.write_text(json.dumps({"entries": [{"old_file": rel}]}), encoding="utf-8")
            with self.assertRaisesRegex(SystemExit, "catalog path is retired"):
                self.package(root)


if __name__ == "__main__":
    main()
