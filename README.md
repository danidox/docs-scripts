# Localization comparison for UiPath docs

Validates localized UiPath documentation pages against their English source. Catches structural localization bugs — dropped images, missing list items, broken admonitions, mangled symbol marks — without comparing translation text accuracy.

## What's here

- **`compare-docs-localized.js`** — the comparison script (Node.js + Playwright)
- **`LOCALIZATION-COMPARE-GUIDE.md`** — full walkthrough: setup, commands, reading the report, troubleshooting, common false positives
- **`RUNBOOK.md`** — quick command reference

## Quick start

```bash
cd docs-scripts
npm install
npx playwright install chromium

node compare-docs-localized.js --locale fr --path /fr/maestro/automation-cloud/latest/user-guide/about-maestro
```

First run opens a browser for Cloudflare Access login. Subsequent runs reuse the saved session in `auth-session.json`.

See **LOCALIZATION-COMPARE-GUIDE.md** for full usage and **RUNBOOK.md** for the cheat sheet.

## Supported locales

`fr` · `de` · `es` · `pt-br` · `ja` · `zh-cn`

## What gets compared

Structural elements counted on both sides and matched up:

- Headings (per level)
- List items (per nesting depth)
- Tables (rows & columns)
- Images
- Admonitions (notes, warnings, tips, cautions)
- Code blocks
- Video embeds
- Symbol marks — ✅ (U+2705) and ❌ (U+274C), by exact codepoint

Text content and translation accuracy are intentionally **not** checked — that's a separate concern handled elsewhere.

## Requirements

- Node.js v18 or newer
- A UiPath account with access to `docs-dev.uipath.com`
