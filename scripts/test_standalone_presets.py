import json
import os
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main, skipIf
from unittest.mock import patch

import yaml

import assemble_release
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
        redirects = Path("website/path-redirects.json")
        (root / redirects.parent).mkdir(exist_ok=True)
        (root / redirects).write_bytes((standalone_presets.ROOT / redirects).read_bytes())
        exports = {}
        with (
            patch.object(lint_presets, "ROOT", root),
            patch.object(standalone_presets, "ROOT", root),
            patch.object(assemble_release, "ROOT", root),
        ):
            obsolete = assemble_release.obsolete_catalog_files(exports.keys())
            stacks = standalone_presets.build_standalone(exports, originals or [], emit_frontmatter, obsolete)
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
            agent_reference = asset.parent / "AGENTS.md"
            agent_reference.write_text("# Supporting notes\n", encoding="utf-8")
            self.assertFalse(lint_presets.is_catalog(agent_reference.relative_to(root).as_posix()))
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
        self.assertEqual(assets, {
            "AGENTS.md": b"# Supporting notes\n", "committed.pyc": b"tracked asset", "fixture.bin": b"\xff\x00",
        })

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
            with self.assertRaisesRegex(SystemExit, "Public catalog ID .* conflicts"):
                self.package(root)

    def test_catalog_only_agent_cannot_collide_with_an_installable_rule(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "cursor/astro/astro-review.prompt.md", "cursor-astro-agent", "agent")
            write_preset(root, "cursor/astro/astro-review.mdc", "cursor-astro-rule", "rule")
            with self.assertRaisesRegex(SystemExit, "Public catalog ID cursor-rules-astro-review conflicts"):
                self.package(root)

    def test_catalog_only_agent_must_use_a_discoverable_location(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "claude/astro/astro-review.agent.md", "claude-astro-agent", "agent")
            with self.assertRaisesRegex(SystemExit, "use a documented catalog path"):
                self.package(root)

    def test_website_parser_can_read_the_contribution(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            preset = write_preset(root, "cursor/astro/astro-review.mdc", "cursor-astro-review", "rule")
            text = preset.read_text(encoding="utf-8").replace("\ntitle:", "\ntitle: Duplicate title\ntitle:")
            preset.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(SystemExit, "cursor/astro/astro-review.mdc: .*duplicated mapping key"):
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

    def test_contribution_cannot_claim_a_permanent_redirect(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "cursor/angular/angular.md", "cursor-angular-conventions", "rule")
            with self.assertRaisesRegex(SystemExit, r"public route /cursor/rules/angular/angular is reserved"):
                self.package(root)

    def test_cleanup_only_removes_catalog_files_in_the_previous_index(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            skill = write_preset(root, "codex/astro/astro-review/SKILL.md", "codex-astro-review", "skill")
            reference = skill.parent / "references" / "release-notes.md"
            reference.parent.mkdir()
            reference.write_text(f"# Release notes\n\n{assemble_release.MARKER}\n", encoding="utf-8")
            previous = root / "cursor/astro/astro-old.mdc"
            previous.parent.mkdir(parents=True)
            previous.write_text(assemble_release.MARKER + "\n", encoding="utf-8")
            index = root / assemble_release.CATALOG_INDEX
            index.parent.mkdir(parents=True)
            old_catalog = previous.relative_to(root).as_posix()
            index.write_text(json.dumps({"entries": [{"catalog": old_catalog}]}), encoding="utf-8")
            stacks, exports = self.package(root)
            file = stacks["codex-astro-review"]["entries"][0]["exports"][1]
            self.assertEqual(exports[file], reference.read_bytes())
            with patch.object(assemble_release, "ROOT", root):
                self.assertEqual(assemble_release.managed_orphans(set(exports) | {assemble_release.CATALOG_INDEX}), [old_catalog])

    def test_filenames_are_portable_to_windows(self):
        for segment in ("AUX.txt", "nul", "Com1.log", "LPT9", "notes."):
            with self.subTest(segment=segment):
                self.assertFalse(standalone_presets.portable_segment(segment))
        self.assertTrue(standalone_presets.portable_segment("auxiliary.txt"))
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "codex/astro/astro-collections.md", "aux", "rule")
            with self.assertRaisesRegex(SystemExit, "generated install path"):
                self.package(root)

    @skipIf(os.name == "nt", "Windows cannot create this test fixture path.")
    def test_rejects_nonportable_catalog_source_path(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            write_preset(root, "cursor/aux/aux-notes.mdc", "cursor-aux-notes", "rule")
            with self.assertRaisesRegex(SystemExit, "use a source path that works on Windows"):
                self.package(root)


class ReleasePreflightTest(TestCase):
    def test_preflight_rejects_linked_parents_before_writing_any_output(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            output = root / "release" / "README.md"
            output.parent.mkdir()
            output.write_text("previous output", encoding="utf-8")
            actual = root / "other"
            actual.mkdir()
            try:
                (root / "cursor").symlink_to(actual, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"Cannot create fixture symlink: {exc}")
            planned = {"release/README.md": "new output", "cursor/astro/astro-notes.mdc": "new preset"}
            with (
                patch.object(assemble_release, "ROOT", root),
                patch.object(assemble_release, "build", return_value=planned),
                patch.object(sys, "argv", ["assemble_release.py"]),
                self.assertRaisesRegex(SystemExit, "regular checkout path without links"),
            ):
                assemble_release.main()
            self.assertEqual(output.read_text(encoding="utf-8"), "previous output")
            self.assertEqual(list(actual.iterdir()), [])

    def test_cleanup_scan_rejects_links_in_release_tree(self):
        with TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            release = root / "release"
            release.mkdir()
            other = root / "other"
            other.mkdir()
            (other / "keep.txt").write_text("keep", encoding="utf-8")
            try:
                (release / "old-output").symlink_to(other, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"Cannot create fixture symlink: {exc}")
            with patch.object(assemble_release, "ROOT", root):
                with self.assertRaisesRegex(SystemExit, "regular checkout path without links"):
                    assemble_release.managed_orphans(set())

if __name__ == "__main__":
    main()
