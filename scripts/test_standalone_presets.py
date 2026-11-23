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
    def package(self, root, official_ids=None, official_skills=None):
        exports = {}
        with patch.object(lint_presets, "ROOT", root), patch.object(standalone_presets, "ROOT", root):
            stacks = standalone_presets.build_standalone(
                exports, official_ids or set(), official_skills or set(), emit_frontmatter,
            )
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
            write_preset(root, "copilot/astro/astro-assistant.agent.md", "copilot-astro-assistant", "agent")
            stacks, exports = self.package(root, {"astro"})

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
        self.assertEqual(exports[skill["exports"][1]], b"\xff\x00")

    def test_contribution_cannot_reuse_official_stack_id_or_skill_name(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "cursor/astro/astro-collection-review/SKILL.md", "astro", "skill")
            with self.assertRaisesRegex(SystemExit, "CLI install ID"):
                self.package(root, {"astro"})
            with self.assertRaisesRegex(SystemExit, "skill install name"):
                self.package(root, official_skills={"astro-collection-review"})


if __name__ == "__main__":
    main()
