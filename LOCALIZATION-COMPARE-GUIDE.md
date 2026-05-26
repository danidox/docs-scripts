# Localization Structural Comparison Guide

## Context

The docs team is validating localized content during a migration from **Smartling GDN** (Global Delivery Network) to **GitHub-based localization**.

Both environments run the same proprietary docs platform frontend. The difference is the localization delivery mechanism:

| Environment | Content source | Localization mechanism |
|---|---|---|
| **Prod** | GitHub (English structure) | GDN injects translated plaintext into the stable English HTML skeleton at runtime — structure is reliable but content is text-overlaid in flight |
| **Dev** | GitHub (localized files) | Localized markup delivered directly from GitHub — may carry structural artifacts from the translation pipeline |

**Goal:** Validate that structural page components (images, admonitions, tables, lists, headings, code blocks) render correctly on dev. Text accuracy is not the concern — structure integrity is.

**Pilot guides in dev:** `customer-portal`, `maestro`
**Target locales:** `fr`, `de`, `ja`, `es`, `pt-br`, `zh-cn`

---

## Why baseline = docs-dev/en (default)

Earlier versions of the script compared **dev/[locale]** against **prod/[locale]** (same locale, different env). That seemed natural but produced two classes of noise:

1. **GDN in-flight delivery** — prod's locale pages are English HTML with translated text overlaid by GDN at runtime. Timing aside, this means structure originates from English and any "differences" reflect English-source state, not localized-file quality.
2. **Dev-ahead-of-prod release lag** — when new content lands in dev but hasn't shipped to prod yet, prod returns an empty placeholder. Every structural element shows up as "missing from prod" in the report. On Maestro fr, 60+ pages were affected this way.

**docs-dev/en eliminates both:**

- Both sides come from the same GitHub deploy → no release lag.
- The /en/ route is the raw English content (no GDN involvement).
- Translation is the only variable, which is exactly what we're validating.

If you specifically want to compare against prod (e.g., to confirm what users see live), pass `--baseline-base https://docs.uipath.com`.

---

## The Script: `docs-scripts/compare-docs-localized.js`

A Playwright-based tool that crawls two URL trees and compares structural content page by page.

### Defaults
| Side | Default base URL | Auth |
|------|-----------------|------|
| Dev (being validated) | `docs-dev.uipath.com/[locale]/...` | Cloudflare Access (session saved to `auth-session.json`) |
| Baseline (English source) | `docs-dev.uipath.com/...` (no locale prefix) | Cloudflare Access (same session) |

**URL pattern:** English on the UiPath docs platform has **no language prefix** — `/maestro/...`, not `/en/maestro/...`. Other locales have a prefix (`/fr/maestro/...`). The script auto-rewrites the path: `/fr/maestro/X` → `/maestro/X` for the English baseline.

**Cookie handling:** The `UIPATH_DOCS_LOCALE` cookie is preset on the browser context **before any navigation**, so the first request already carries the right language preference. This avoids redirect chains caused by a stale cookie from a previous run mismatching the URL we're about to load. The two crawls run sequentially; the second crawl's preset overwrites the first's value on the shared cookie jar — no race because they never run concurrently. The same Cloudflare session covers both crawls.

### What it compares
- **Page completeness** — pages present in baseline but missing from dev, or extra pages in dev
- **Headings** (h2–h6) — count per heading level (h1 is rendered outside the content area on both sides and is not captured)
- **List items** — count per nesting depth; also checks ul/ol type
- **Images** — count per page (served from `cms.uipath.com/assets` on all environments)
- **Admonitions** (notes, warnings, tips, cautions) — count per type
- **Code blocks** — count of `<pre>` elements
- **Tables** — matched by position; checks row count, column count
- **Video embeds** — count of `iframe`/`video` elements
- **Symbol marks** — exact-codepoint count of ✅ (U+2705) and ❌ (U+274C), used in compatibility/availability tables. Catches NMT corruption that swaps these emoji for ASCII or lookalike codepoints (e.g. German NMT replacing ❌ with `x`). Per-codepoint, not per-glyph — so visual similarity doesn't fool the check.

### What it does NOT compare
- **Icons** rendered via CSS classes or SVG inline elements (not `<img>` tags) — invisible to the script
- Styling, color, layout
- Link targets
- Text translation quality

### Pages excluded from comparison
- **Baseline-empty pages** — if the baseline URL resolves to an empty page (placeholder for unreleased content), the script peels it out into a "PAGES NOT YET PUBLISHED ON BASELINE" section. These are listed but not counted as having structural issues, since the absence of content on the baseline is not a dev-side defect.

---

## How to Run

### Prerequisites
```
cd docs-scripts
npm install   # installs Playwright and dependencies (first time only)
npx playwright install chromium
```

### Basic usage

```bash
# Default: dev/fr vs docs-dev/en
node compare-docs-localized.js --locale fr --path /fr/customer-portal/other/latest/user-guide/about-customer-portal

# Single page (fastest — good for spot-checking)
node compare-docs-localized.js --locale fr --page /fr/customer-portal/other/latest/user-guide/about-customer-portal

# First N pages
node compare-docs-localized.js --locale fr --path /fr/customer-portal/... --limit 10

# Page range
node compare-docs-localized.js --locale fr --path /fr/customer-portal/... --limit 11-20

# Save report (relative path saves in docs-scripts\; absolute path saves anywhere)
node compare-docs-localized.js --locale fr --path /fr/customer-portal/... --output report-fr-customer-portal.txt

# Baseline = prod English (instead of docs-dev English)
node compare-docs-localized.js --locale fr --path /fr/customer-portal/... --baseline-base https://docs.uipath.com

# Legacy mode: dev/fr vs prod/fr (same locale, across envs)
node compare-docs-localized.js --locale fr --path /fr/customer-portal/... --baseline-base https://docs.uipath.com --baseline-locale fr

# Debug — element counts and raw image srcs
node compare-docs-localized.js --locale fr --page /fr/customer-portal/... --debug
```

### URL pattern for localized content

```
docs-dev.uipath.com/fr/customer-portal/other/latest/user-guide/...   ← dev (with locale prefix)
docs-dev.uipath.com/customer-portal/other/latest/user-guide/...      ← baseline (no prefix, English)
```

You pass only the dev path with `--path` or `--page`. The script strips the `/fr/` prefix for the baseline side. You can also paste the full URL — the script strips the domain.

### Authentication
On first run, a browser window opens for Cloudflare Access login. After completing login, the session is saved to `auth-session.json` and reused. The session works for both sides since they share the host (`docs-dev.uipath.com` by default).

---

## Output / Report Sections

Every page detail always shows all sections with counts. A `[OK] Counts match` line means the check was performed and passed.

| Symbol | Meaning |
|--------|---------|
| `X` / `✗` | Missing from dev, or fewer than baseline |
| `+` | Extra in dev (more than baseline) |
| `>` / `⤵` | Present but reduced (fewer rows/cols) |
| `~` / `⇄` | Structural change (list type, similar but different) |
| `!` / `⚠` | Ambiguous difference — check manually |
| `P` / `¶` | Content moved from list item to paragraph or vice versa |

Report sections per page:
- **HEADINGS** — count difference per heading level
- **LIST ITEMS** — count difference per nesting depth
- **TABLES** — missing table, fewer rows/cols, extra table in dev
- **IMAGES** — count difference
- **ADMONITIONS** — count difference per type
- **CODE BLOCKS** — count difference
- **VIDEO EMBEDS** — count difference

---

## False Positives and Pitfalls

### General (any language)

| Issue | What you'll see | Why it happens |
|-------|----------------|----------------|
| **Word count differences** | High word-count differences | Translations differ in phrasing and length. Word count is excluded from the "pages with issues" filter for this reason. |
| **Empty header row in tables** | `! Empty header row in Dev` | The platform may emit an empty `<thead>` row depending on how the source content is authored. Check visually if flagged. |
| **`present-as-paragraph`** | List item flagged as present in dev as paragraph | Same content rendered with different HTML structure between baseline and dev. Usually benign. |
| **`content-outside-list`** | Content flagged as moved outside list | Baseline and dev handle content following a list item differently. Usually benign. |
| **`nested-note`** | Note inside vs alongside a list item | Admonition placement may differ between baseline and dev. Visually fine on both. |
| **`possible-merge`** | Table flagged as possible merge | Two small tables in dev correspond to one in baseline. Check visually. |
| **Extra table in dev** | `X Extra table in Dev` | The platform sometimes renders non-table structures as tables depending on content markup. |
| **Availability indicators** | (Should not appear) | Images with alt="available"/"not available" are explicitly excluded from image counts. |
| **Pages not yet on baseline** | (Listed in dedicated section, excluded from comparison) | New content that's in dev but hasn't shipped to baseline yet. No longer pollutes content-type counts. |

### Localization-specific

| Issue | Affects | What you'll see | Root cause |
|-------|---------|----------------|-----------|
| **Translation phrasing differences** | All locales (text mode only) | `~ similar-list-item` or `X missing` on list items | Translations naturally differ from the source. Structural mode (default) is not affected. |
| **Fullwidth vs halfwidth punctuation** | `zh-cn`, `ja` | Heading or admonition flagged as missing | NFKC normalization handles most cases but edge cases remain if one side uses fullwidth ASCII and the other doesn't. |
| **CJK word-overlap metrics unreliable** | `ja`, `zh-cn` | Many false `X Absent` in CONTENT BLOCKS (text mode only) | Word-overlap relies on space-separated tokens. Japanese and Chinese have no word spaces. Bigram fallback mitigates but is approximate. |
| **Translation artifacts in headings** | All locales | `X Missing heading` | If translation introduced an extra character/tag/whitespace, heading counts per level may differ. Investigate the specific heading. |

### What the script is reliable for with localized content

| Check | Reliable for all locales? |
|-------|--------------------------|
| Missing pages | Yes |
| Heading count per level | Yes |
| Image count | Yes — language-independent |
| Table row/column count | Yes — language-independent |
| Admonition count per type | Yes — type detected from CSS class, not translated label |
| Code block count | Yes — language-independent |
| Video embed count | Yes — language-independent |
| List item depth count | Yes (structural mode); approximate for CJK in text mode |

### What the script cannot detect
- **Icons** rendered via CSS classes or inline SVG — not captured as images
- **Broken image display** (image exists in HTML but 404s or fails to load)
- **Layout regressions** (component present but misaligned)
- **Translation quality or accuracy**

---

## Recommended Workflow

1. **Start with a single page** using `--page` and `--debug` to sanity-check that the script is finding the right content on the localized pages.

2. **Use the default baseline** (docs-dev/en) for routine validation — it's the cleanest comparison.

3. **Switch to `--baseline-base https://docs.uipath.com`** if you specifically need to know what's shipping vs what's not.

4. **For `ja` and `zh-cn`**: focus on language-independent checks (counts), and treat CJK text-mode metrics as approximate.

5. **Save reports** with `--output report-[locale]-[guide].txt` for tracking. Use the **PAGES NOT YET PUBLISHED ON BASELINE** section to track release-lag items separately from structural defects.

6. **Use `--limit` for large guides** — run in batches of 20–30 pages to avoid session timeouts.

7. **Visual spot-check** any flags the script raises for CJK content.

---

## Migration history note

The legacy default was dev/[locale] vs prod/[locale]. That produced two real problems on Maestro fr (May 2026):
- 60+ pages reported with `prod: 0` for all element counts (release lag — pages existed in the sidebar on prod but resolved to empty placeholders, since the new Maestro content hadn't shipped to prod yet).
- GDN's in-flight text delivery introduced theoretical concerns about extraction timing on prod, even though in practice it doesn't affect structural counts.

The new default (dev/[locale] vs docs-dev/en) eliminates both as confounders. The PAGES NOT YET PUBLISHED ON BASELINE section catches any remaining cases where baseline content is empty.
