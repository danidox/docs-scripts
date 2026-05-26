# Localization Structural Comparison Guide

A walkthrough for using `compare-docs-localized.js` to validate the structure of localized UiPath documentation pages.

---

## What the script does

It compares two language versions of a UiPath docs guide and reports **structural** differences — counts of headings, list items, images, admonitions, tables, code blocks, video embeds, and specific symbol marks (✅, ❌).

It does **not** compare translation text. The goal is to catch localization bugs that break page layout (a missing image, a dropped table row, an admonition that lost its type) even when the text reads fine.

By default it compares:

- **The localized page** — e.g. `docs-dev.uipath.com/fr/maestro/.../about-maestro`
- against **the English source on the same environment** — e.g. `docs-dev.uipath.com/maestro/.../about-maestro`

Both come from the same content deployment, so any structural difference is due to localization rather than a content release timing gap.

---

## Setup (one-time)

You need Node.js (v18 or newer) and Git installed.

```
cd docs-scripts
npm install
npx playwright install chromium
```

You only run these three commands once per machine.

---

## Running a comparison

### The basic command

```
node compare-docs-localized.js --locale fr --path /fr/maestro/automation-cloud/latest/user-guide/about-maestro
```

That's the typical run: crawl the whole guide starting from this page, compare it to the English source, print the report. You can paste a full URL after `--path` and the script will strip the domain.

### Variations you'll use often

```bash
# Just one page — fastest, good for spot checks
node compare-docs-localized.js --locale fr --page /fr/maestro/.../about-maestro

# First 10 pages only
node compare-docs-localized.js --locale fr --path /fr/maestro/... --limit 10

# Pages 11 through 20
node compare-docs-localized.js --locale fr --path /fr/maestro/... --limit 11-20

# Save the report to a file
node compare-docs-localized.js --locale fr --path /fr/maestro/... --output report-fr-maestro.txt

# Show every extracted count (for diagnosing)
node compare-docs-localized.js --locale fr --page /fr/... --debug
```

### Supported locales

| Code    | Language               |
|---------|------------------------|
| `fr`    | French                 |
| `de`    | German                 |
| `es`    | Spanish                |
| `pt-br` | Portuguese (Brazil)    |
| `ja`    | Japanese               |
| `zh-cn` | Chinese (Simplified)   |

### First-run sign-in

The first time you run the script against `docs-dev.uipath.com` a browser window opens for Cloudflare Access login. Sign in with your UiPath credentials and wait for the docs page to appear — the script detects success automatically and saves your session to `auth-session.json` for future runs. If a session expires later, the login window reopens on its own.

### Choosing a different baseline (optional)

If you need to compare against a different source than docs-dev English:

```bash
# Compare against production English (what users see live)
node compare-docs-localized.js --locale fr --path /fr/... --baseline-base https://docs.uipath.com

# Compare two environments of the same locale (advanced, rarely needed)
node compare-docs-localized.js --locale fr --path /fr/... --baseline-base https://docs.uipath.com --baseline-locale fr
```

Most of the time the default is what you want.

---

## Reading the report

### Symbols

| Symbol  | Meaning                                                            |
|---------|--------------------------------------------------------------------|
| `[OK]`  | Check ran and passed                                               |
| `X`     | Missing on the localized side, or fewer than the baseline          |
| `+`     | Extra on the localized side (more than the baseline)               |
| `>`     | Reduced (fewer rows or columns in a table)                         |
| `~`     | Structural change (e.g. an ordered list rendered as unordered)     |
| `!`     | Ambiguous difference — needs a visual check                        |
| `P`     | Content moved between a list item and a paragraph                  |

### Sections, in order

1. **COMPARISON REPORT** — top-line counts: pages compared, missing, with issues.
2. **MISSING PAGES** — present on baseline, absent from the localized side.
3. **EXTRA PAGES IN [LOCALE]** — present on localized side, not on baseline (typically new content).
4. **PAGES NOT YET PUBLISHED ON [BASELINE]** — URL exists but has no content on the baseline yet. Listed for awareness, then **excluded** from the per-page comparison so they don't pollute the issue counts.
5. **CONTENT TYPE SUMMARY** — one line per content type, either `[OK]` or `X N/total pages with issues`. Start here when reading a large report.
6. **ISSUES BY CONTENT TYPE** — every page with an issue, grouped by content type. This is the detail you investigate.
7. **IMAGE COUNTS — ALL PAGES** — every page with its image count on both sides. Easy place to spot dropped images at a glance.
8. **AFFECTED PAGES — URL REFERENCE** — links to every affected page on both sides. URLs live at the bottom of the report so they don't break up the issue listings.

---

## What's checked

- **Page completeness** — pages on the baseline absent from localized, or extras
- **Headings** — count per heading level (h2 through h6)
- **List items** — count per nesting depth, plus ordered vs unordered
- **Tables** — row and column counts, matched by position
- **Images** — total count per page
- **Admonitions** — notes, warnings, tips, cautions, etc., counted per type
- **Code blocks** — count of code blocks
- **Video embeds** — count of embedded videos
- **Symbol marks** — exact-codepoint count of ✅ (U+2705) and ❌ (U+274C), used in feature-availability tables. The check is per-codepoint, so a visually similar substitute (an ASCII `x` in place of ❌, for example) is caught as a missing mark.

## What's NOT checked

- **Translation accuracy** — text content is ignored
- **Icons** rendered as CSS classes or inline SVG (only `<img>` tags are counted)
- **Broken images** that exist in the HTML but fail to load in the browser
- **Layout regressions** — if structure is present but misaligned, the script can't see it

---

## Common false positives

These often look like problems but usually aren't:

| What you see                              | What's actually going on                                                                              |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Word count is different**               | Translations naturally differ in length. Not flagged as an issue.                                     |
| `! Empty header row in [LOCALE]`          | The platform sometimes renders an extra empty header row. Usually benign — check visually.            |
| `P Present as paragraph`                  | Same content rendered as a paragraph rather than a list item. Different markup, same meaning.         |
| `! Content moved outside list`            | Content following a list rendered slightly differently between sides. Usually benign.                 |
| `! Note nested in list item`              | An admonition appears inside a list item on one side, alongside it on the other. Same content.        |
| `~ Possible table merge`                  | Two small tables on the localized side may correspond to one combined table on the baseline.          |
| `X Extra table`                           | The platform sometimes renders non-table content as a table depending on source markup.               |
| **PAGES NOT YET PUBLISHED ON [BASELINE]** | The localized side has a page that the baseline doesn't yet — release lag, not a localization bug.    |

When in doubt, open both URLs from the **AFFECTED PAGES** section and compare visually.

---

## Tips

- **Start with one page** using `--page` and `--debug` to confirm the script is finding real content on the pages you care about before scaling up.
- **Use `--limit` for large guides** — running in batches of 20–30 pages reduces the risk of session timeouts and makes the report easier to review.
- **For CJK locales (`ja`, `zh-cn`)**, the structural checks are language-independent and reliable. Stick to structural mode (the default) — `--text` mode is approximate for these languages.
- **Save reports for later** with `--output report-[locale]-[guide].txt`. The text files render correctly in any editor.

---

## Troubleshooting

**Browser opens but the script seems stuck after I log in.**
The script is waiting for the docs page itself to load. Make sure you've finished Cloudflare Access and are on a real docs page, then return to the terminal — it detects success and continues.

**"Session expired" or "Cloudflare Access" message.**
Your saved login is no longer valid. The script automatically invalidates `auth-session.json` and reopens the browser. Just sign in again.

**Empty report or "No links matched the guide base path".**
The seed path is probably wrong, or the page you pointed at doesn't have a sidebar. Re-run with `--debug` and check the extracted link count. Make sure the path starts with the locale prefix (e.g. `/fr/...`).

**A page shows counts of 0 but I can see content on it.**
Try again — it may be a one-off timing hiccup. If it happens consistently for one page, run that page alone with `--page` and `--debug` to see what was extracted.

**The report flags many pages on a single content type.**
Check the **CONTENT TYPE SUMMARY** first. If everything else is `[OK]` and only one type is failing, the cause is probably a single underlying issue (e.g. a platform-wide rendering change) rather than a per-page localization bug.
