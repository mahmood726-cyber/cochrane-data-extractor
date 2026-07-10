# cochrane-data-extractor

Cochrane Data Extractor: Automated Dataset Harvesting from Cochrane Systematic Reviews

_Status: Needs triage (portfolio registry)._

## Repository contents (important)

This repository is **documentation-only**. It ships the E156 micro-paper,
protocol, and project write-up (`CLAUDE.md`), but it does **not** contain the
runnable extraction pipeline (`bulk_downloader.py`), its `progress.json`
checkpoint, the downloaded CSV datasets, or a `requirements.txt`. Those live in
a separate local working directory that was never committed here.

Consequently the quantitative validation numbers quoted in the E156 body
(e.g. "11 pairwise datasets totaling 1,295 rows, 100 percent concordance")
are **not reproducible from what is checked into this repository**. Treat the
manuscript as a DRAFT report (see `e156-submission/config.json`:
`validation: "DRAFT"`, `submitted: false`) until the implementation, its
dependency manifest, and the test-set CSVs are committed alongside it.

The only Python file included is `conftest.py`; there is no `tests/` suite for
the extraction code. `tests/test_packaging.py` covers only the shipped static
assets (link slug consistency and no hardcoded local paths), not the pipeline.
