#!/usr/bin/env python3
"""Lint presets added or edited in this branch.

Legacy files that the diff does not touch are not schema-checked, markdown-linted,
length-checked, or secret-scanned. Slug and id uniqueness still looks at the whole
tree so a new id cannot collide with an existing one.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ci_common import ROOT, changed_files, resolve_base

TOOLS = ("copilot", "cursor", "claude", "windsurf", "cline", "codex", "antigravity")
SUPPORTING_DIRS = {"references", "assets", "scripts"}
DOC_NAMES = {"README.md", "CONTRIBUTING.md"}
TEMPLATE_FILES = (
    "templates/rule.md",
    "templates/instruction.md",
    "templates/agent.md",
    "templates/skill/SKILL.md",
)
MAX_CHARS = 40_000
SCHEMA_PATH = ROOT / "schema" / "preset.frontmatter.schema.json"

SECRET_PATTERNS = (
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Slack webhook", re.compile(r"https://hooks\.slack\.com/services/\S+")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b")),
    ("OpenAI-style key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_\-]{20,}\b")),
    ("Stripe live key", re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{16,}\b")),
    ("npm token", re.compile(r"\bnpm_[A-Za-z0-9]{36}\b")),
)
PLACEHOLDER_LINE = re.compile(
    r"(example|placeholder|redacted|changeme|your[-_ ]?(key|token|secret)|xxxx+)",
    re.IGNORECASE,
)


def expected_slug(rel: str) -> str:
    name = rel.rsplit("/", 1)[-1]
    parent = rel.rsplit("/", 1)[0] if "/" in rel else ""
    if name.endswith(".mdc"):
        stem = name[:-4]
    elif name.endswith(".md"):
        stem = name[:-3]
    else:
        stem = name
    return f"{parent}/{stem}" if parent else stem


def is_supporting(rel: str) -> bool:
    return any(part in SUPPORTING_DIRS for part in rel.split("/"))


def is_catalog(rel: str) -> bool:
    path = Path(rel)
    if path.suffix.lower() not in {".md", ".mdc"}:
        return False
    if path.name in DOC_NAMES:
        return False
    parts = path.parts
    if not parts or parts[0] not in TOOLS:
        return False
    conventional = path.name in {"SKILL.md", "AGENTS.md", "CLAUDE.md"} or path.name.endswith(
        (".agent.md", ".instructions.md")
    )
    if is_supporting(rel) and not conventional:
        return False
    return True


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if text.startswith("\ufeff"):
        text = text[1:]
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "".join(lines[1:index]), "".join(lines[index + 1 :])
    return None, text


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def normalize_dates(data: dict) -> dict:
    normalized = dict(data)
    for key in ("created", "updated"):
        value = normalized.get(key)
        if isinstance(value, dt.datetime):
            normalized[key] = value.date().isoformat()
        elif isinstance(value, dt.date):
            normalized[key] = value.isoformat()
    return normalized


def expected_type(rel: str) -> str | None:
    name = Path(rel).name
    if name == "SKILL.md":
        return "skill"
    if name == "AGENTS.md":
        return "agent"
    if name == "CLAUDE.md":
        return "instruction"
    if name.endswith(".agent.md"):
        return "agent"
    if name.endswith(".instructions.md"):
        return "instruction"
    if name.endswith(".mdc"):
        return "rule"
    return None


def validate_data(rel: str, data: dict, schema: dict, *, require_tool_dir: bool) -> list[str]:
    errors: list[str] = []
    validator = Draft7Validator(schema)
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        location = "/".join(str(part) for part in error.path) or "(root)"
        errors.append(f"{rel}: {location}: {error.message}")
    if errors:
        return errors
    slug = expected_slug(rel)
    if data["slug"] != slug:
        errors.append(f"{rel}: slug must be {slug!r} to match the file path")
    kind = expected_type(rel)
    if kind and data["type"] != kind:
        errors.append(f"{rel}: type must be {kind!r} for this filename")
    top = rel.split("/", 1)[0]
    if require_tool_dir and top in TOOLS and top not in data["tools"]:
        errors.append(f"{rel}: tools must include {top!r}")
    author = data.get("author")
    name = ""
    if isinstance(author, dict) and isinstance(author.get("name"), str):
        name = author["name"].strip()
    if isinstance(author, dict) and (not name or name.casefold() == "community"):
        errors.append(
            f"{rel}: author.name must name the person or organization who wrote the preset"
        )
    for key in ("created", "updated"):
        try:
            dt.datetime.strptime(data[key], "%Y-%m-%d")
        except ValueError:
            errors.append(f"{rel}: {key} must be a real YYYY-MM-DD date")
    if not errors and data["updated"] < data["created"]:
        errors.append(f"{rel}: updated is earlier than created")
    return errors


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def parse_frontmatter(rel: str) -> tuple[dict | None, list[str]]:
    try:
        text = read_text(rel)
    except UnicodeDecodeError:
        return None, [f"{rel}: file is not UTF-8"]
    raw, _body = split_frontmatter(text)
    if raw is None:
        return None, [f"{rel}: missing YAML frontmatter"]
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return None, [f"{rel}: frontmatter YAML could not be parsed ({exc})"]
    if not isinstance(data, dict):
        return None, [f"{rel}: frontmatter must be a mapping"]
    return normalize_dates(data), []


def loose_frontmatter(rel: str) -> dict | None:
    try:
        text = (ROOT / rel).read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None
    raw, _body = split_frontmatter(text)
    if raw is None:
        return None
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def lint_markdown(rel: str, text: str) -> list[str]:
    errors: list[str] = []
    if "\r" in text:
        errors.append(f"{rel}: use Unix line endings")
    lines = text.splitlines()
    blank_run = 0
    fence: tuple[str, int] | None = None
    for number, line in enumerate(lines, start=1):
        if "\t" in line:
            errors.append(f"{rel}:{number}: MD010 hard tab")
        if line.endswith(" "):
            errors.append(f"{rel}:{number}: MD009 trailing whitespace")
        if line.strip() == "":
            blank_run += 1
            if blank_run > 1:
                errors.append(f"{rel}:{number}: MD012 extra blank line")
        else:
            blank_run = 0
        if re.match(r"^#{1,6}[^ #\n]", line):
            errors.append(f"{rel}:{number}: MD018 heading needs a space after #")
        marker = re.match(r"^(```+|~~~+)", line)
        if marker and fence is None:
            fence = (marker.group(1)[0], len(marker.group(1)))
        elif fence and line.startswith(fence[0]):
            closer = line.strip()
            if closer and set(closer) == {fence[0]} and len(closer) >= fence[1]:
                fence = None
    if fence:
        errors.append(f"{rel}: unclosed code fence")
    if not text.endswith("\n"):
        errors.append(f"{rel}: MD047 file must end with a single newline")
    elif text.endswith("\n\n"):
        errors.append(f"{rel}: MD047 extra blank line at end of file")
    return errors


def scan_secrets(rel: str, text: str) -> list[str]:
    if "\0" in text:
        return []
    errors: list[str] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if PLACEHOLDER_LINE.search(line):
            continue
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(line):
                errors.append(f"{rel}:{number}: possible {name}")
                break
    return errors


def length_error(rel: str, text: str) -> str | None:
    if len(text) > MAX_CHARS:
        return f"{rel}: length {len(text)} exceeds {MAX_CHARS} characters"
    return None


def wants_length_check(rel: str) -> bool:
    suffix = Path(rel).suffix.lower()
    if suffix not in {".md", ".mdc"}:
        return False
    if Path(rel).name in DOC_NAMES:
        return False
    if rel.startswith("templates/"):
        return True
    return bool(rel.split("/", 1)[0] in TOOLS)


def catalog_files() -> list[str]:
    found: list[str] = []
    for tool in TOOLS:
        base = ROOT / tool
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if path.is_file():
                rel = path.relative_to(ROOT).as_posix()
                if is_catalog(rel):
                    found.append(rel)
    return found


def index_keys(files: list[str], key: str) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for rel in files:
        data = loose_frontmatter(rel)
        if not data:
            continue
        value = data.get(key)
        if isinstance(value, str) and value:
            index.setdefault(value, []).append(rel)
    return index


def collision_messages(index: dict[str, list[str]], hot: set[str], label: str) -> list[str]:
    messages: list[str] = []
    for value, paths in sorted(index.items()):
        unique = sorted(set(paths))
        if len(unique) < 2:
            continue
        if set(unique) & hot:
            joined = ", ".join(unique)
            messages.append(f"duplicate {label} {value!r} in {joined}")
    return messages


def self_test(schema: dict) -> list[str]:
    errors: list[str] = []
    Draft7Validator.check_schema(schema)
    assert expected_slug("templates/skill/SKILL.md") == "templates/skill/SKILL"
    assert expected_slug("cursor/react/rules.mdc") == "cursor/react/rules"
    assert expected_slug("copilot/go/go.instructions.md") == "copilot/go/go.instructions"
    starter: dict | None = None
    starter_path = TEMPLATE_FILES[0]
    for rel in TEMPLATE_FILES:
        data, parse_errors = parse_frontmatter(rel)
        errors.extend(parse_errors)
        if data is None:
            continue
        if rel == starter_path:
            starter = data
        errors.extend(validate_data(rel, data, schema, require_tool_dir=False))
        broken = dict(data)
        broken["origin"] = "copied"
        if not validate_data(rel, broken, schema, require_tool_dir=False):
            errors.append(f"self-test: {rel} accepted origin other than original")
    if starter is not None:
        cases = {
            "string author was accepted": {"author": "Your Name"},
            "Community author was accepted": {"author": {"name": "Community", "github": "octocat"}},
            "author without name was accepted": {"author": {"github": "octocat"}},
            "invalid github username was accepted": {"author": {"name": "Your Name", "github": "not a user"}},
        }
        for message, override in cases.items():
            candidate = dict(starter)
            candidate.update(override)
            if not validate_data(starter_path, candidate, schema, require_tool_dir=False):
                errors.append(f"self-test: {message}")
        accepted = dict(starter)
        accepted["tools"] = ["antigravity"]
        accepted["stack"] = "nextjs"
        accepted["updated_for"] = "Next.js 16.4.6"
        if validate_data(starter_path, accepted, schema, require_tool_dir=False):
            errors.append("self-test: antigravity stack metadata was rejected")
        full_list = dict(starter)
        full_list["tools"] = list(TOOLS)
        if validate_data(starter_path, full_list, schema, require_tool_dir=False):
            errors.append("self-test: the eight-tool list was rejected")
        unknown = dict(starter)
        unknown["tools"] = ["not-a-tool"]
        if not validate_data(starter_path, unknown, schema, require_tool_dir=False):
            errors.append("self-test: unknown tool id was accepted")
        extra = dict(starter)
        extra["freshness"] = "Next.js 16.4.6"
        if not validate_data(starter_path, extra, schema, require_tool_dir=False):
            errors.append("self-test: unknown frontmatter field was accepted")
    sample = "\n".join(["# Title", "", "A paragraph.", ""])
    if lint_markdown("sample.md", sample):
        errors.append("self-test: clean markdown was rejected")
    if not lint_markdown("sample.md", "# Title \n"):
        errors.append("self-test: trailing whitespace was accepted")
    if not lint_markdown("sample.md", "# Title\n\n```\nopen\n"):
        errors.append("self-test: unclosed fence was accepted")
    key = "AKIA" + "1234567890ABCDEF"
    if not scan_secrets("sample.txt", f"token = {key}\n"):
        errors.append("self-test: access key was accepted")
    if scan_secrets("sample.txt", f"example token = {key}\n"):
        errors.append("self-test: example access key was rejected")
    hot = {"new.md"}
    collided = collision_messages({"same": ["old.md", "new.md"]}, hot, "id")
    if not collided:
        errors.append("self-test: id collision was ignored")
    legacy_only = collision_messages({"same": ["old.md", "older.md"]}, hot, "id")
    if legacy_only:
        errors.append("self-test: untouched legacy collision failed the build")
    return errors


def main() -> int:
    schema = load_schema()
    errors = self_test(schema)
    if errors:
        print("self-test failed:")
        print("\n".join(errors))
        return 1

    changed = changed_files(resolve_base())
    schema_targets = {rel for rel in changed if is_catalog(rel)}
    schema_targets.update(TEMPLATE_FILES)

    for rel in sorted(schema_targets):
        data, parse_errors = parse_frontmatter(rel)
        errors.extend(parse_errors)
        if data is None:
            continue
        errors.extend(
            validate_data(
                rel,
                data,
                schema,
                require_tool_dir=not rel.startswith("templates/"),
            )
        )

    indexed = catalog_files() + list(TEMPLATE_FILES)
    hot = schema_targets
    errors.extend(collision_messages(index_keys(indexed, "id"), hot, "id"))
    errors.extend(collision_messages(index_keys(indexed, "slug"), hot, "slug"))

    for rel in changed:
        suffix = Path(rel).suffix.lower()
        if suffix not in {".md", ".mdc"}:
            continue
        try:
            text = read_text(rel)
        except UnicodeDecodeError:
            errors.append(f"{rel}: file is not UTF-8")
            continue
        errors.extend(lint_markdown(rel, text))
        if wants_length_check(rel):
            message = length_error(rel, text)
            if message:
                errors.append(message)

    for rel in changed:
        path = ROOT / rel
        try:
            blob = path.read_bytes()
        except OSError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if b"\0" in blob[:4096]:
            continue
        try:
            text = blob.decode("utf-8")
        except UnicodeDecodeError:
            continue
        errors.extend(scan_secrets(rel, text))

    if errors:
        print(f"preset lint failed ({len(errors)} issue(s)):")
        print("\n".join(errors))
        return 1
    print(
        "preset lint ok: "
        f"{len(changed)} changed file(s), "
        f"{len(schema_targets)} schema target(s), "
        f"limit {MAX_CHARS} characters"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
