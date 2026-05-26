# Localization Comparison Runbook

## Prerequisites (one-time setup)

```
cd C:\Users\roxana.mocanu\CodeWork\CompareScript\docs-scripts
npm install
npx playwright install chromium
```

---

## How the comparison works (read this first)

The script compares two sides per page and reports structural differences:

| Side | What it is | Why |
|------|-----------|-----|
| **Dev** | `docs-dev.uipath.com/[locale]/[guide]` | The localized GitHub deliverable being validated |
| **Baseline** | `docs-dev.uipath.com/[guide]` (default — English, **no locale prefix**) | The English source — what the localized content is supposed to match structurally |

**URL pattern:** On the UiPath docs platform, English URLs have **no language prefix** (just `/maestro/...`). Other locales carry a prefix (`/fr/maestro/...`). Language is selected by the `UIPATH_DOCS_LOCALE` cookie, which the script presets on the browser context before any navigation — so the first request already carries the right preference and the site doesn't redirect from a stale cookie. The path is auto-rewritten on the baseline side: `/fr/maestro/X` → `/maestro/X`.

By default the baseline is **docs-dev (English)** (same env as dev, English content). This is the cleanest comparison: both sides come from the same GitHub deploy, so structural drift = pure localization drift. GDN is not in the loop, and prod-vs-dev release lag does not cause false positives.

Other baselines are available via flags if needed (see "Choosing a different baseline" below).

---

## Standard runs

### Full guide (default — dev/fr vs docs-dev/en)
```
node compare-docs-localized.js --locale fr --path /fr/customer-portal/other/latest/user-guide/about-customer-portal --output report-fr-customer-portal.txt
```

> Report saves in the `docs-scripts\` folder. Use an absolute path to save elsewhere:
> `--output "C:\Users\roxana.mocanu\Documents\report-fr.txt"`

### Single page (spot check)
```
node compare-docs-localized.js --locale fr --page /fr/customer-portal/other/latest/user-guide/about-customer-portal
```

### Limit to first N pages
```
node compare-docs-localized.js --locale fr --path /fr/customer-portal/other/latest/user-guide/about-customer-portal --limit 5
```

### Page range
```
node compare-docs-localized.js --locale fr --path /fr/... --limit 11-20
```

---

## Choosing a different baseline

| Goal | Flags |
|------|-------|
| Default — dev/[locale] vs docs-dev/en | (none) |
| Compare against English on **prod** | `--baseline-base https://docs.uipath.com` |
| Compare against English on **staging** | `--baseline-base https://docs-staging.uipath.com` |
| Legacy mode: dev/[locale] vs prod/[locale] (same locale, across envs) | `--baseline-base https://docs.uipath.com --baseline-locale fr` (or whatever locale matches `--locale`) |
| Compare against another language's English (rare) | `--baseline-locale en --baseline-base https://docs-staging.uipath.com` |

> `--prod-base` is still accepted as an alias for `--baseline-base` for older scripts.

---

## Locales

| Code | Language |
|------|----------|
| `fr` | French |
| `de` | German |
| `es` | Spanish |
| `pt-br` | Portuguese (Brazil) |
| `ja` | Japanese |
| `zh-cn` | Chinese (Simplified) |

---

## Comparison mode

| Flag | Behavior |
|------|----------|
| *(default)* | **Structural** — compares counts only (headings per level, list items per depth, admonitions per type, image totals, table row/col counts, code block totals). No text matching. Correct for localization. |
| `--text` | **Text** — full text matching. Only useful when comparing the same locale or for English-to-English checks. |

---

## Debug

Add `--debug` to any command to see:
- Cookies and localStorage before/after locale injection
- Page URL after reload (confirms locale redirect worked)
- Extracted element counts for both baseline and dev
- All `<img>` sources found on the page (to diagnose image count = 0)

```
node compare-docs-localized.js --locale fr --page /fr/... --debug
```

---

## Output / report symbols

| Symbol | Meaning |
|--------|---------|
| `X` (in text reports) / `✗` (console) | Missing from dev or fewer than baseline |
| `+` | Extra in dev (more than baseline) |
| `>` / `⤵` | Present but reduced (fewer rows/cols) |
| `~` / `⇄` | Structural change (list type, table merge) |
| `!` / `⚠` | Ambiguous difference, check manually |

Every section always appears in the report with counts. `[OK] Counts match` means the check was performed and passed — not that the check was skipped.

---

## Report sections

1. **COMPARISON REPORT** — page coverage stats
2. **MISSING PAGES** — present in baseline, absent from dev
3. **EXTRA PAGES IN DEV** — present in dev, absent from baseline
4. **PAGES NOT YET PUBLISHED ON BASELINE** — route exists but content is empty on baseline (excluded from per-page comparison — these are dev-ahead-of-baseline pages, not structural defects)
5. **CONTENT TYPE SUMMARY** — at-a-glance: one line per content type, `[OK]` or `✗ N/total pages with issues`. Content types tracked: Headings, List items, Tables, Images, Admonitions, Code blocks, Video embeds, **Symbol marks** (✅ U+2705, ❌ U+274C — exact-codepoint count, catches NMT lookalike substitution).
6. **ISSUES BY CONTENT TYPE** — grouped by type, then page; details only, no URLs
7. **IMAGE COUNTS — ALL PAGES** — every page with `[OK]` or `✗`
8. **AFFECTED PAGES — URL REFERENCE** — all dev + baseline URLs for pages with issues or missing pages, at the very end

---

## Authentication

- The baseline being docs-dev means **both sides need Cloudflare auth** by default.
- First run opens a browser for Cloudflare login. Session saved to `auth-session.json` and reused.
- If session expires, the browser reopens for re-login.
- Auth detection is by host: `docs-dev.uipath.com` and `docs-staging.uipath.com` need it; `docs.uipath.com` does not.

---

## Path format

The path is everything after the domain. Copy from the browser URL bar:

```
https://docs-dev.uipath.com/fr/customer-portal/other/latest/user-guide/about-customer-portal
                            ↓
/fr/customer-portal/other/latest/user-guide/about-customer-portal
```

You can also paste the full URL — the script strips the domain. The baseline path is auto-derived by replacing the locale prefix (`/fr/` → `/en/` by default).

---

## Known false positives

- **Word count differences**: Localized content phrasing legitimately differs in length from English. Word counts will differ; structural mode does not flag this.
- **Heading differences**: May reflect content updates that landed in baseline (English source) but not yet in the localized files. Verify visually.
- **PAGES NOT YET PUBLISHED ON BASELINE**: Maestro and other heavily-updated guides may have routes that exist in the sidebar but resolve to empty pages on the baseline side. These are surfaced separately and excluded from the comparison, so they no longer pollute "Pages with issues" the way they did in the previous dev-vs-prod-same-locale mode.

---

## Migration note (May 2026)

Previously the default comparison was dev/[locale] vs **prod/[locale]** — same locale across environments. That produced a noisy report on guides where dev was ahead of prod (e.g. Maestro: 60+ pages with prod showing zero counts because the page hadn't shipped to prod yet).

The new default — dev/[locale] vs **docs-dev/en** — eliminates that class of false positive because the baseline is on the same GitHub deploy as the dev locale.

To get the old behavior back: `--baseline-base https://docs.uipath.com --baseline-locale [your-locale]`.
