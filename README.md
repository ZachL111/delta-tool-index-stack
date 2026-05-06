# delta-tool-index-stack

`delta-tool-index-stack` is a Python project in cli tools. Its focus is to package a Python local lab for index analysis with capacity fixtures, allocation and spill reports, and documented operating limits.

## Purpose

This is intentionally local and self-contained so it can be inspected without credentials, services, or seeded history.

## Delta Tool Index Stack Review Notes

Start with `file span` and `terminal width`. Those cases create the widest score spread in this repo, so they are the best quick check when the model changes.

## What Is Covered

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/delta-tool-index-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `file span` and `terminal width`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Implementation Notes

The fixture data drives the tests. The code stays thin, while `metadata/domain-review.json` and `config/review-profile.json` explain what each case is meant to protect.

The added Python path is deliberately direct, with fixtures doing most of the explaining.

## Command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Audit Path

The verifier is intentionally local. It should fail if the fixture score math, lane assignment, or language-specific test drifts.

## Limits

This remains a local project with deterministic fixtures. It does not depend on credentials, hosted services, or live data. Future work should add richer malformed inputs before widening the public API.
