"""Packaging / shipped-asset guard tests for cochrane-data-extractor.

This repository is documentation-only (no extraction pipeline is committed),
so there is no parser/downloader code to unit-test. These tests instead guard
the static assets that ARE shipped and served via GitHub Pages, locking in the
fixes for two audit findings:

  * F3 - the GitHub source/dashboard links must use the real repo slug
          "cochrane-data-extractor", never the un-hyphenated typo
          "cochranedataextractor" (which 404s).
  * F4 - no shipped, publicly-served asset may leak a hardcoded local machine
          path (e.g. C:\\Projects\\...). CLAUDE.md is intentionally exempt: it
          is a skip-file-marked write-up that documents local paths as data
          and is not application config.

They also confirm config.json stays valid JSON after the F4 edit.
"""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Correct repo slug. The wrong form is this string with the hyphens removed.
CORRECT_SLUG = "cochrane-data-extractor"
WRONG_SLUG = CORRECT_SLUG.replace("-", "")  # "cochranedataextractor"

# Publicly-served / documentation assets that must be clean. CLAUDE.md is
# excluded on purpose (sentinel:skip-file; paths-as-data write-up).
SHIPPED_ASSETS = [
    "index.html",
    "E156-PROTOCOL.md",
    "README.md",
    "e156-submission/index.html",
    "e156-submission/assets/index.html",
    "e156-submission/assets/debug_page.html",
    "e156-submission/config.json",
    "e156-submission/paper.json",
    "e156-submission/paper.md",
    "e156-submission/protocol.md",
    "docs/protocol.md",
]

# Matches an absolute Windows drive path such as C:\Users or C:/Projects.
# The negative lookbehind for an alphanumeric char keeps URL schemes such as
# "https://" (the "s:/" fragment) from being mistaken for a drive path.
HARDCODED_PATH_RE = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]")


def _existing_assets():
    for rel in SHIPPED_ASSETS:
        p = REPO_ROOT / rel
        if p.exists():
            yield rel, p


def test_no_wrong_slug_in_shipped_assets():
    """F3: no shipped asset may reference the un-hyphenated repo slug."""
    offenders = []
    for rel, path in _existing_assets():
        text = path.read_text(encoding="utf-8", errors="replace")
        # Isolate the wrong slug so the correct hyphenated slug never matches.
        if re.search(rf"(?<![\w-]){WRONG_SLUG}(?![\w-])", text):
            offenders.append(rel)
    assert not offenders, f"Un-hyphenated slug '{WRONG_SLUG}' found in: {offenders}"


def test_no_hardcoded_local_path_in_shipped_assets():
    """F4: no publicly-served asset may leak an absolute local machine path."""
    offenders = []
    for rel, path in _existing_assets():
        text = path.read_text(encoding="utf-8", errors="replace")
        if HARDCODED_PATH_RE.search(text):
            offenders.append(rel)
    assert not offenders, f"Hardcoded local path found in: {offenders}"


def test_config_json_is_valid_and_has_no_path_field():
    """F4: config.json parses and no longer carries the local 'path' field."""
    cfg_path = REPO_ROOT / "e156-submission" / "config.json"
    assert cfg_path.exists(), "config.json is missing"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    assert "path" not in cfg, "config.json still ships a local 'path' field"
    # slug metadata should be the correct hyphenated form.
    assert cfg.get("slug") == CORRECT_SLUG
