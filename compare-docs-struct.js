#!/usr/bin/env node
/**
 * UiPath Docs Comparison Tool
 * ────────────────────────────────────────────────────────────────────────────
 * Compares a guide between a non-prod docs site (docs-dev.uipath.com or
 * docs-staging.uipath.com) and prod (docs.uipath.com).
 * Checks both which pages are missing AND what content is missing within pages.
 * Reuses auth-session.json for Cloudflare Access authentication.
 *
 * Usage (run from docs-validator/doc_validator/):
 *   node compare-docs.js
 *   node compare-docs.js --path /apps/automation-cloud/latest/user-guide/introduction
 *   node compare-docs.js https://docs-staging.uipath.com/assistant/standalone/latest/user-guide/about-uipath-assistant
 *   node compare-docs.js --dev-base https://docs-staging.uipath.com --path /assistant/standalone/latest/user-guide/about-uipath-assistant
 *   node compare-docs.js --output report.json
 *
 * Content comparison runs by default. Every page present in both sites is
 * checked for missing headings/sections and significant text differences.
 */

'use strict';

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const readline = require('readline');

// ─── CLI args ────────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const getArg = (flag) => { const i = args.indexOf(flag); return i !== -1 ? args[i + 1] : null; };
const VALUE_FLAGS = new Set(['--path', '--output', '--dev-base', '--prod-base', '--limit', '--page']);
const positionalArgs = [];
for (let i = 0; i < args.length; i++) {
  const arg = args[i];
  if (VALUE_FLAGS.has(arg)) { i++; continue; }
  if (!arg.startsWith('--')) positionalArgs.push(arg);
}

function parseSeedInput(input) {
  if (!input) return null;
  try {
    const url = new URL(input);
    return { base: url.origin.replace(/\/$/, ''), path: normPath(url.pathname) };
  } catch {
    return { base: null, path: normPath(input) };
  }
}

const seedInput = parseSeedInput(positionalArgs[0] || getArg('--path'));

let GUIDE_PATH  = seedInput ? seedInput.path : null;
const OUTPUT_FILE = getArg('--output') || null;
let DEV_BASE = (getArg('--dev-base') || seedInput?.base || 'https://docs-dev.uipath.com').replace(/\/$/, '');
let PROD_BASE = (getArg('--prod-base') || 'https://docs.uipath.com').replace(/\/$/, '');
let DEV_HOST = new URL(DEV_BASE).hostname;
let DEV_LABEL = DEV_HOST === 'docs-staging.uipath.com' ? 'Staging' : 'Dev';
let PAGE_START = 0;
let PAGE_END   = null; // null = not yet set (prompt will ask)
if (getArg('--limit')) {
  const raw = getArg('--limit').trim().toLowerCase();
  if (raw.includes('-')) {
    const [from, to] = raw.split('-').map(s => parseInt(s.trim(), 10));
    PAGE_START = (isNaN(from) ? 1 : from) - 1;
    PAGE_END   = isNaN(to) ? Infinity : to;
  } else {
    PAGE_END = parseInt(raw, 10) || Infinity;
  }
}
// Single-page mode: compare just one page. Accepts a full URL or a pathname.
const PAGE_SINGLE = getArg('--page') ? normPath(getArg('--page')) : null;
const DEBUG       = args.includes('--debug');

// ─── Interactive prompts ──────────────────────────────────────────────────────
function prompt(rl, question) {
  return new Promise(resolve => rl.question(question, resolve));
}

async function promptInputs() {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

  if (!GUIDE_PATH) {
    const answer = await prompt(rl, '  Enter the guide URL or path to compare: ');
    GUIDE_PATH = normPath(answer.trim() || '/apps/automation-cloud/latest/user-guide/introduction');
  }

  if (PAGE_END === null) {
    const answer = await prompt(rl, '  Pages to crawl? (number, range "11-20", or "all") [all]: ');
    const raw = answer.trim().toLowerCase();
    if (!raw || raw === 'all') {
      PAGE_START = 0;
      PAGE_END   = Infinity;
    } else if (raw.includes('-')) {
      const [from, to] = raw.split('-').map(s => parseInt(s.trim(), 10));
      PAGE_START = (isNaN(from) ? 1 : from) - 1; // 1-based input → 0-based index
      PAGE_END   = isNaN(to) ? Infinity : to;
    } else {
      PAGE_START = 0;
      PAGE_END   = parseInt(raw, 10);
      if (isNaN(PAGE_END)) PAGE_END = Infinity;
    }
  }

  rl.close();
}

const SESSION_FILE = path.join(__dirname, 'auth-session.json');

// ─── Helpers ─────────────────────────────────────────────────────────────────
// All output goes to stdout so lines always appear in the correct order.
// Using console.error (stderr) alongside console.log (stdout) causes
// interleaving issues on Windows where the two streams are buffered separately.
const log  = (m) => process.stdout.write(m + '\n');
const warn = (m) => process.stdout.write('\x1b[33m' + m + '\x1b[0m\n');
const ok   = (m) => process.stdout.write('\x1b[32m' + m + '\x1b[0m\n');
const err  = (m) => process.stdout.write('\x1b[31m' + m + '\x1b[0m\n');
const dim  = (m) => process.stdout.write('\x1b[2m' + m + '\x1b[0m\n');

function normPath(url) {
  try { return new URL(url).pathname.replace(/\/$/, ''); }
  catch { return url.replace(/\/$/, ''); }
}

function toUrl(base, pathname) {
  return base.replace(/\/$/, '') + '/' + pathname.replace(/^\//, '');
}

function guideBasePath(seedPath) {
  const p = normPath(seedPath);
  return p.substring(0, p.lastIndexOf('/') + 1);
}

// ─── Session / Auth ───────────────────────────────────────────────────────────
function loadSession(devHost) {
  if (!fs.existsSync(SESSION_FILE)) return null;
  try {
    const data = JSON.parse(fs.readFileSync(SESSION_FILE, 'utf8'));
    const valid = data.cookies && data.cookies.some(
      c => (c.name === 'CF_AppSession' || c.name === 'CF_Authorization')
           && c.domain.includes(devHost)
    );
    return valid ? data : null;
  } catch { return null; }
}

function invalidateSession() {
  if (!fs.existsSync(SESSION_FILE)) return;
  try { fs.copyFileSync(SESSION_FILE, SESSION_FILE.replace('.json', '-expired.json')); } catch {}
  try { fs.unlinkSync(SESSION_FILE); } catch {}
  warn('  Session invalidated (backed up to auth-session-expired.json).');
}

function saveSession(storageState) {
  try {
    fs.writeFileSync(SESSION_FILE, JSON.stringify(storageState, null, 2));
    ok('  New session saved to auth-session.json');
  } catch (e) { warn('  Could not save session: ' + e.message); }
}

async function createBrowser(sessionState) {
  const headless = !!sessionState;
  const browser = await chromium.launch({
    headless,
    slowMo: headless ? 0 : 150,
    args: ['--disable-blink-features=AutomationControlled',
           ...(headless ? [] : ['--start-maximized'])],
  });
  const context = await browser.newContext({
    ignoreHTTPSErrors: true,
    storageState: sessionState || undefined,
    viewport: { width: 1920, height: 1080 },
  });
  return { browser, context, headless };
}

// ─── Auth-aware navigation ────────────────────────────────────────────────────
async function navigateWithAuth(page, url, context, isDevSite, isHeadless, devHost) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60_000 });
  if (!isDevSite) return 'ok';
  await page.waitForTimeout(2500);

  const onAuthPage = await page.evaluate(() =>
    document.body.textContent.includes('Sign in with') ||
    document.body.textContent.includes('Cloudflare Access') ||
    document.body.textContent.includes('Enter your credentials') ||
    document.title.toLowerCase().includes('access')
  );

  if (!onAuthPage) return 'ok';

  if (isHeadless) {
    warn('  Cloudflare session expired (headless browser detected).');
    return 'reauth';
  }

  warn('\n  Cloudflare Access login detected.');
  log('  ──────────────────────────────────────────────────────');
  log('  A browser window is open. Please:');
  log('  1. Enter your UiPath email and complete the login.');
  log('  2. Once the docs page loads, return here.');
  log('  ──────────────────────────────────────────────────────');
  log('  Waiting for login (no timeout)…');

  await page.bringToFront();
  await page.waitForFunction(
    (expectedHost) => window.location.hostname === expectedHost &&
          !document.body.textContent.includes('Sign in with') &&
          !document.title.toLowerCase().includes('access'),
    devHost,
    { timeout: 0 }
  );
  ok('  Authenticated!');
  saveSession(await context.storageState());
  return 'ok';
}

// ─── Page-list extraction ─────────────────────────────────────────────────────
async function extractGuideLinks(page, guideBase) {
  return page.evaluate((guideBase) => {
    const seen = new Set();
    const results = [];
    for (const a of document.querySelectorAll('a[href]')) {
      const href = a.getAttribute('href');
      if (!href) continue;
      let pathname;
      try { pathname = new URL(href, window.location.href).pathname.replace(/\/$/, ''); }
      catch { continue; }
      if (!pathname.startsWith(guideBase.replace(/\/$/, ''))) continue;
      if (seen.has(pathname)) continue;
      seen.add(pathname);
      results.push({ label: a.textContent.trim().replace(/\s+/g, ' ') || pathname.split('/').pop(), pathname });
    }
    return results;
  }, guideBase);
}

// ─── Content extraction ───────────────────────────────────────────────────────

/**
 * Extract structured page data:
 *   - headings:  [{level, text}]           — all h1–h6 in document order
 *   - listItems: [{depth, type, text}]     — all li elements with nesting depth and ul/ol type
 *   - text:      full plain-text of the article (for word-count comparison)
 *   - wordCount: number of words
 */
async function extractPageData(page, isDevSite) {
  return page.evaluate((isDev) => {
    // Find the main content area — use the known container for each site.
    // Prod (Tridion):   #DocContainer
    // Dev  (Docusaurus): .theme-doc-markdown.markdown
    const primary = isDev
      ? document.querySelector('.theme-doc-markdown.markdown')
      : document.getElementById('DocContainer');
    const fallbacks = ['article', 'main article', '[class*="docItem"]', 'main'];
    let el = primary;
    if (!el) { for (const sel of fallbacks) { el = document.querySelector(sel); if (el) break; } }
    if (!el) el = document.body;

    const clone = el.cloneNode(true);
    // Remove navigation chrome and injected overlays (cookie consent, etc.)
    [
      'nav', 'aside', 'footer',
      '[class*="breadcrumb"]', '[class*="pagination"]', '[class*="tableOfContents"]',
      // Tridion (prod) sidebar navigation — rendered as divs/uls in the content
      // area rather than <nav>/<aside>, so must be stripped explicitly.
      '[class*="sidebar"]', '[class*="sidenav"]', '[class*="side-nav"]',
      '[class*="page-nav"]', '[class*="topic-nav"]', '[class*="guide-nav"]',
      '[class*="related-links"]', '[class*="relatedLinks"]',
      // OneTrust cookie consent modal — injected on prod, absent from dev
      '[id*="onetrust"]', '[class*="onetrust"]',
      '[id*="cookie-consent"]', '[class*="cookie-consent"]',
    ].forEach(s => clone.querySelectorAll(s).forEach(n => n.remove()));

    // Extract headings in document order.
    // Clone each heading and remove <a> children first — docs frameworks (Docusaurus,
    // Tridion) inject permalink anchor links inside headings, which contribute
    // invisible characters (zero-width spaces, U+200B) to textContent that survive
    // trim() and cause false-positive "missing heading" mismatches.
    const headings = [];
    clone.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(h => {
      const hClone = h.cloneNode(true);
      hClone.querySelectorAll('a').forEach(a => a.remove());
      const text = hClone.textContent
        .replace(/[\u200B-\u200D\uFEFF\u00AD]/g, '') // strip invisible chars
        .trim()
        .replace(/\s+/g, ' ');
      if (text) headings.push({ level: parseInt(h.tagName[1]), text });
    });

    // Extract list items with nesting depth and list type (ul/ol).
    // depth = number of ancestor ul/ol elements inside the content area.
    // Only capture the direct text of the li (not nested child list text).
    const listItems = [];
    clone.querySelectorAll('li').forEach(li => {
      // Compute nesting depth by counting ul/ol ancestors within the content clone
      let depth = 0;
      let node = li.parentElement;
      while (node && node !== clone) {
        if (node.tagName === 'UL' || node.tagName === 'OL') depth++;
        node = node.parentElement;
      }

      // Capture only the immediate text of this li, not text from child lists
      const liClone = li.cloneNode(true);
      liClone.querySelectorAll('ul, ol').forEach(n => n.remove());
      // In Docusaurus (dev), admonitions are sometimes nested directly inside a
      // <li> (as a sibling of the li's own text). Strip them before reading text
      // so the li text matches its prod counterpart, then flag the structural diff.
      const hasNestedNote = !!liClone.querySelector('#AdmonitionContainer');
      liClone.querySelectorAll('#AdmonitionContainer').forEach(n => n.remove());
      // Insert a space before elements to prevent word concatenation.
      // Tridion and Docusaurus emit adjacent elements with no whitespace text
      // nodes between them, causing e.g. "Add conditionto add" instead of
      // "Add condition to add". Covers inline elements AND block-level elements
      // like table cells, divs, and paragraphs that can appear inside <li>.
      liClone.querySelectorAll('a, span, strong, em, b, i, code, td, th, div, p').forEach(el => {
        el.parentNode.insertBefore(document.createTextNode(' '), el);
      });
      const text = liClone.textContent.trim().replace(/\s+/g, ' ');

      // Skip navigation-only items: li whose entire content is a single <a>.
      // Tridion sidebar renders every nav entry as <li><a>Title</a></li>.
      // Content list items always have prose text alongside or beyond any link.
      const anchors = liClone.querySelectorAll('a');
      if (anchors.length === 1 && anchors[0].textContent.trim().replace(/\s+/g, ' ') === text) return;

      if (text) {
        const type = li.parentElement.tagName.toLowerCase(); // 'ul' or 'ol'
        listItems.push({ depth, type, text, hasNestedNote });
      }
    });

    // Extract content images by src pattern.
    // Dev (Docusaurus) serves content images from cms.uipath.com/assets.
    // Prod (Tridion) serves content images from /api/binary/.
    // Alt texts differ between the two sites for the same image, so we match
    // by count only — alt text is stored for reference in reports.
    // Exception: prod uses images for availability indicators (alt="available" /
    // alt="not available") that dev renders as ✅/❌ emojis — exclude these
    // from the count to avoid false-positive "missing image" reports.
    const EMOJI_ALT = new Set(['available', 'not available']);
    const images = [];
    let currentImageSection = null;
    clone.querySelectorAll('h1, h2, h3, h4, h5, h6, img').forEach(el => {
      if (/^H[1-6]$/.test(el.tagName)) {
        const hClone = el.cloneNode(true);
        hClone.querySelectorAll('a').forEach(a => a.remove());
        currentImageSection = hClone.textContent
          .replace(/[\u200B-\u200D\uFEFF\u00AD]/g, '')
          .trim()
          .replace(/\s+/g, ' ');
        return;
      }
      const img = el;
      const src = img.getAttribute('src') || '';
      const isContentImage = src.includes('cms.uipath.com/assets') || src.includes('/api/binary/');
      if (!isContentImage) return;
      const alt = (img.getAttribute('alt') || '').trim().replace(/\s+/g, ' ');
      if (EMOJI_ALT.has(alt.toLowerCase())) return;
      images.push({ alt, src, section: currentImageSection });
    });

    // Extract admonitions (note, warning, tip, caution, danger).
    // Docusaurus renders them as divs with class "admonition" or "alert".
    // Tridion may use different class names, so we cast a wide net:
    //   - any element with a class containing "admonition", "note", "warning",
    //     "caution", "tip", "danger", "important"
    //   - also <aside> elements that look like call-outs
    const admonitions = [];
    const admonitionTypes = ['note', 'warning', 'caution', 'tip', 'danger', 'important', 'info'];

    const detectType = (el) => {
      const cls = (el.className || '').toLowerCase();
      for (const t of admonitionTypes) { if (cls.includes(t)) return t; }
      // Fallback: read the label text (Docusaurus puts "note", "warning", etc. in a <p> or <div>)
      const label = el.querySelector('.admonition-heading, .admonitionHeading, [class*="admonitionHeading"]');
      if (label) return label.textContent.trim().toLowerCase();
      return 'note';
    };

    const admonitionSel = [
      '[class*="admonition"]',
      '[class*="alert--"]',
      'aside[class*="note"], aside[class*="warn"], aside[class*="tip"], aside[class*="caution"]',
    ].join(', ');

    clone.querySelectorAll(admonitionSel).forEach(el => {
      // Skip nested admonitions (already captured by parent)
      if (el.closest('[class*="admonition"]:not(:scope)')) return;
      const type = detectType(el);
      // Get first ~120 chars of text content as a fingerprint
      const snippet = el.textContent.trim().replace(/\s+/g, ' ').slice(0, 120);
      // Count logical paragraphs inside the admonition.
      // Docusaurus uses <p> tags; Tridion sometimes separates lines with <br> instead.
      // Use <p> count when available, otherwise treat each <br> as a paragraph break.
      const pCount  = el.querySelectorAll('p').length;
      const brCount = el.querySelectorAll('br').length;
      const paragraphCount = pCount > 0 ? pCount : (brCount > 0 ? brCount + 1 : 1);
      if (snippet) admonitions.push({ type, snippet, paragraphCount });
    });

    // Extract body paragraphs for fine-grained content diffing.
    // Skip paragraphs that live inside admonitions (those are already captured
    // via the admonitions array) and short snippets (< 40 chars) that are
    // typically UI labels, captions, or list continuations.
    const admonitionEls = new Set(clone.querySelectorAll(
      '[class*="admonition"], [class*="alert--"]'
    ));

    // Walk h1–h6, p, td, th in document order so each block is tagged with
    // the section heading it falls under — used to show WHERE missing content is.
    const paragraphs = [];
    let currentSection = null;
    clone.querySelectorAll('h1, h2, h3, h4, h5, h6, p, td, th').forEach(el => {
      if (/^H[1-6]$/.test(el.tagName)) {
        const hClone = el.cloneNode(true);
        hClone.querySelectorAll('a').forEach(a => a.remove());
        currentSection = hClone.textContent
          .replace(/[\u200B-\u200D\uFEFF\u00AD]/g, '').trim().replace(/\s+/g, ' ');
        return;
      }
      // Skip anything inside an admonition (handled separately)
      let ancestor = el.parentElement;
      while (ancestor && ancestor !== clone) {
        if (admonitionEls.has(ancestor)) return;
        ancestor = ancestor.parentElement;
      }
      const text = el.textContent.trim().replace(/\s+/g, ' ');
      if (text.length >= 40) paragraphs.push({ text, section: currentSection });
    });

    // Extract table summaries for row-count comparison.
    const tables = [];
    clone.querySelectorAll('table').forEach(table => {
      const rows = Array.from(table.querySelectorAll('tr'));
      if (rows.length === 0) return;

      // Some CMSes (e.g. Docusaurus/dev) emit <thead><tr><th></th><th></th></tr></thead>
      // with no header text — a layout choice absent from Tridion/prod.
      // Detect this: count leading rows where every cell is empty.
      let emptyHeaderRows = 0;
      for (const row of rows) {
        const cells = Array.from(row.querySelectorAll('td, th'));
        if (cells.length > 0 && cells.every(c => !c.textContent.trim())) emptyHeaderRows++;
        else break;
      }
      const hasEmptyHeader = emptyHeaderRows > 0;

      // Use the first non-empty row for the match key.
      const dataRows = rows.slice(emptyHeaderRows);
      if (dataRows.length === 0) return;
      const headerCells = Array.from(dataRows[0].querySelectorAll('td, th'))
        .map(c => c.textContent.trim().replace(/\s+/g, ' '))
        .filter(Boolean);
      const firstCell = dataRows[0].querySelector('td, th');
      const headerText = (firstCell || dataRows[0]).textContent.trim().replace(/\s+/g, ' ').slice(0, 80);
      const colCount = rows[0].querySelectorAll('td, th').length;
      const cells = Array.from(table.querySelectorAll('td, th'))
        .map(c => c.textContent.trim().replace(/\s+/g, ' ')).filter(Boolean);
      const signature = `${colCount}::${headerCells.slice(0, 3).join(' | ').toLowerCase()}`;
      if (headerText) tables.push({ headerText, rowCount: rows.length, colCount, hasEmptyHeader, cells, signature });
    });

    const text = clone.innerText.replace(/\s+/g, ' ').trim();
    const wordCount = text.split(/\s+/).filter(Boolean).length;

    return { headings, listItems, images, admonitions, paragraphs, tables, text, wordCount };
  }, isDevSite);
}

// ─── Site crawler ─────────────────────────────────────────────────────────────
async function crawlSite(context, seedUrl, isDevSite, isHeadless) {
  const base      = isDevSite ? DEV_BASE : PROD_BASE;
  const guideBase = guideBasePath(GUIDE_PATH);
  const pages     = new Map();
  const page      = await context.newPage();

  log(`  Seed: ${seedUrl}`);
  const status = await navigateWithAuth(page, seedUrl, context, isDevSite, isHeadless, DEV_HOST);
  if (status === 'reauth') { await page.close(); return null; }

  // Wait for content container before extracting links (Cloudflare challenge may be in progress).
  const seedContentSel = isDevSite ? '.theme-doc-markdown.markdown' : '#DocContainer';
  try { await page.waitForSelector(seedContentSel, { timeout: 15_000 }); }
  catch { await page.waitForTimeout(3000); }

  const links = await extractGuideLinks(page, guideBase);
  log(`  Found ${links.length} guide links`);

  if (links.length === 0) {
    warn('  No links matched the guide base path — check --path.');
    pages.set(normPath(seedUrl), { label: 'Introduction', url: seedUrl, ...(await extractPageData(page, isDevSite)) });
    await page.close();
    return pages;
  }

  const end = Math.min(PAGE_END, links.length);
  const limited = links.slice(PAGE_START, end);
  if (PAGE_START > 0 || end < links.length)
    log(`  Batch: pages ${PAGE_START + 1}–${PAGE_START + limited.length} of ${links.length}`);
  log(`  Crawling content for ${limited.length} pages…`);
  for (let i = 0; i < limited.length; i++) {
    const { label, pathname } = limited[i];
    const fullUrl = toUrl(base, pathname);
    process.stdout.write(`\r  [${PAGE_START + i + 1}/${PAGE_START + limited.length}] ${label.slice(0, 60).padEnd(60)}`);
    try {
      if (normPath(page.url()) !== pathname)
        await page.goto(fullUrl, { waitUntil: 'domcontentloaded', timeout: 30_000 });
      // Wait for the actual content container, not a fixed timeout.
      // Cloudflare challenge pages on prod can take several seconds to resolve.
      const contentSel = isDevSite
        ? '.theme-doc-markdown.markdown'
        : '#DocContainer';
      try {
        await page.waitForSelector(contentSel, { timeout: 15_000 });
      } catch {
        // Fallback: wait a bit longer and extract whatever is on the page
        await page.waitForTimeout(3000);
      }
      pages.set(pathname, { label, url: fullUrl, ...(await extractPageData(page, isDevSite)) });
    } catch (e) {
      pages.set(pathname, { label, url: fullUrl, headings: [], listItems: [], images: [], admonitions: [], paragraphs: [], tables: [], text: '', wordCount: 0, error: e.message });
    }
  }
  process.stdout.write('\n');
  await page.close();
  return pages;
}

// ─── Single-page crawl ────────────────────────────────────────────────────────
async function crawlSinglePage(context, pathname, isDevSite, isHeadless) {
  const base    = isDevSite ? DEV_BASE : PROD_BASE;
  const fullUrl = toUrl(base, pathname);
  const page    = await context.newPage();
  const status  = await navigateWithAuth(page, fullUrl, context, isDevSite, isHeadless, DEV_HOST);
  if (status === 'reauth') { await page.close(); return null; }
  const singleSel = isDevSite ? '.theme-doc-markdown.markdown' : '#DocContainer';
  try { await page.waitForSelector(singleSel, { timeout: 15_000 }); }
  catch { await page.waitForTimeout(3000); }
  const label = pathname.split('/').pop();
  const data = await extractPageData(page, isDevSite);
  await page.close();
  return { label, url: fullUrl, ...data };
}

// ─── Content comparison ───────────────────────────────────────────────────────

/** Word-overlap similarity 0–100.
 *  Measures what fraction of prod's unique vocabulary also appears in dev.
 *  Both sides are deduplicated so the score is always capped at 100%. */
function similarity(a, b) {
  if (!a || !b) return 0;
  const wordsA = new Set(a.slice(0, 4000).toLowerCase().split(/\s+/).filter(Boolean));
  const wordsB = new Set(b.slice(0, 4000).toLowerCase().split(/\s+/).filter(Boolean));
  if (wordsA.size === 0) return 0;
  let overlap = 0;
  for (const w of wordsA) { if (wordsB.has(w)) overlap++; }
  return Math.round((overlap / wordsA.size) * 100);
}

/**
 * Compare list structures between prod and dev.
 *
 * Normalises each list item's text, then for every item in prod:
 *   - if it's missing from dev entirely → "missing item"
 *   - if it exists but at a different depth → "wrong depth" (indentation broken)
 *   - if it exists but changed type ul↔ol → "wrong type"
 *
 * Returns an array of issue objects.
 */
function compareListStructure(prodItems, devItems, devParagraphs = []) {
  const norm = (s) => (s || '')
    .toLowerCase()
    .normalize('NFKC')
    .replace(/[^\p{L}\p{N} ]/gu, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  const wordSet = (s) => new Set(norm(s).split(' ').filter(w => w.length > 3));
  const preview = (s, limit = 100) => {
    const clean = (s || '').replace(/\s+/g, ' ').trim();
    return clean.length > limit ? clean.slice(0, limit - 1) + '…' : clean;
  };
  const overlapRatio = (aWords, bWords) => {
    if (aWords.size === 0 || bWords.size === 0) return 0;
    let overlap = 0;
    for (const w of aWords) { if (bWords.has(w)) overlap++; }
    return overlap / aWords.size;
  };

  // Build a lookup from normalised text → {depth, type} for dev
  const devMap = new Map();
  for (const item of devItems) {
    const key = norm(item.text);
    if (key && !devMap.has(key)) devMap.set(key, item);
  }

  const devParagraphEntries = (devParagraphs || []).map(p => ({
    text: p.text,
    words: wordSet(p.text),
  }));

  const issues = [];
  for (const prodItem of prodItems) {
    const key = norm(prodItem.text);
    if (!key) continue;
    const prodWords = wordSet(prodItem.text);

    const devItem = devMap.get(key);
    if (!devItem) {
      // Before flagging as missing, check two nesting-difference patterns
      // (prod is baseline — all checks are "prod item vs dev items"):
      //
      // 1. Content outside list in dev: prod li is longer because a trailing
      //    paragraph is inside the li in prod but a sibling outside the list
      //    in dev. → key.startsWith(devKey)
      //
      // 2. Paragraph longer in dev: dev li is longer because a sibling
      //    paragraph in prod got appended to the last li in dev.
      //    → devKey.startsWith(key)  (stricter 50% threshold)
      let structuralMatch = false;
      for (const [devKey] of devMap) {
        if (key.startsWith(devKey) && devKey.length >= key.length * 0.3) {
          issues.push({ kind: 'content-outside-list', text: prodItem.text, depth: prodItem.depth });
          structuralMatch = true;
          break;
        }
        if (devKey.startsWith(key) && key.length >= devKey.length * 0.5) {
          issues.push({ kind: 'paragraph-longer-in-dev', text: prodItem.text, depth: prodItem.depth });
          structuralMatch = true;
          break;
        }
      }
      if (!structuralMatch) {
        let bestListMatch = null;
        let bestListRatio = 0;
        for (const candidate of devItems) {
          const ratio = overlapRatio(prodWords, wordSet(candidate.text));
          if (ratio > bestListRatio) {
            bestListRatio = ratio;
            bestListMatch = candidate;
          }
        }

        let bestParagraphMatch = null;
        let bestParagraphRatio = 0;
        for (const candidate of devParagraphEntries) {
          const ratio = overlapRatio(prodWords, candidate.words);
          if (ratio > bestParagraphRatio) {
            bestParagraphRatio = ratio;
            bestParagraphMatch = candidate;
          }
        }

        if (bestParagraphRatio >= 0.6 && bestParagraphRatio >= bestListRatio && prodWords.size >= 4) {
          issues.push({
            kind: 'present-as-paragraph',
            text: prodItem.text,
            prodDepth: prodItem.depth,
            similarityPct: Math.round(bestParagraphRatio * 100),
            devText: preview(bestParagraphMatch.text),
          });
        } else if (bestListRatio >= 0.6 && prodWords.size >= 4) {
          issues.push({
            kind: 'similar-list-item',
            text: prodItem.text,
            prodDepth: prodItem.depth,
            devDepth: bestListMatch.depth,
            devType: bestListMatch.type,
            similarityPct: Math.round(bestListRatio * 100),
            devText: preview(bestListMatch.text),
          });
        } else {
          issues.push({ kind: 'missing', text: prodItem.text, prodDepth: prodItem.depth });
        }
      }
    } else {
      if (devItem.hasNestedNote && !prodItem.hasNestedNote) {
        // In dev, this li has an admonition nested inside it; in prod the admonition
        // is a sibling outside the list. Only flag when nesting actually differs.
        issues.push({ kind: 'nested-note', text: prodItem.text, depth: prodItem.depth });
      } else if (devItem.depth !== prodItem.depth && prodItem.depth > 1) {
        issues.push({
          kind: 'wrong-depth',
          text: prodItem.text,
          prodDepth: prodItem.depth,
          devDepth: devItem.depth,
        });
      } else if (devItem.type !== prodItem.type) {
        issues.push({
          kind: 'wrong-type',
          text: prodItem.text,
          prodType: prodItem.type,
          devType: devItem.type,
          depth: prodItem.depth,
        });
      }
    }
  }
  return issues;
}

/**
 * Compare two pages. Returns an object describing what's missing or different.
 */
function comparePage(prodPage, devPage) {
  const normText = (s) => (s || '')
    .toLowerCase()
    .normalize('NFKC')
    .replace(/[^\p{L}\p{N} ]/gu, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  // Normalise heading text for comparison: lowercase + strip any residual
  // invisible/punctuation characters that differ between Tridion and Docusaurus.
  const normH = (s) => normText(s);

  // Headings that appear by design on all pages (navigation chrome, not content)
  const IGNORED_HEADINGS = new Set([
    'subscribe to uipath release notes',
  ]);

  // Headings present in prod but absent from dev
  const devHeadings = new Set(devPage.headings.map(h => normH(h.text)));
  const missingHeadings = prodPage.headings.filter(
    h => !devHeadings.has(normH(h.text)) && !IGNORED_HEADINGS.has(normH(h.text))
  );

  // List structure issues (wrong depth / missing nested items / ul↔ol swaps)
  const listIssues = compareListStructure(
    prodPage.listItems || [],
    devPage.listItems  || [],
    devPage.paragraphs || []
  );

  // Images: compare by count. Alt texts differ between Tridion (prod) and
  // Docusaurus (dev) for the same image, so matching by alt is unreliable.
  // Content images are already filtered by src pattern at extraction time.
  const prodImageCount = (prodPage.images || []).length;
  const devImageCount  = (devPage.images  || []).length;
  const missingImages  = [];
  if (prodImageCount > devImageCount) {
    missingImages.push({ kind: 'count', count: prodImageCount - devImageCount, prodTotal: prodImageCount, devTotal: devImageCount });
  }
  const bySection = (imgs) => {
    const map = new Map();
    for (const img of (imgs || [])) {
      const key = normH(img.section || '(no section)');
      map.set(key, (map.get(key) || 0) + 1);
    }
    return map;
  };
  const prodImgBySection = bySection(prodPage.images);
  const devImgBySection = bySection(devPage.images);
  for (const [section, prodCount] of prodImgBySection) {
    const devCount = devImgBySection.get(section) || 0;
    if (prodCount > devCount) {
      missingImages.push({
        kind: 'section',
        section,
        count: prodCount - devCount,
        prodTotal: prodCount,
        devTotal: devCount,
      });
    }
  }

  // Admonitions: match by type + normalised snippet prefix (first 60 chars).
  // For matched admonitions, also compare paragraph counts to detect cases
  // where multiple paragraphs in prod are merged into one in dev.
  const normSnippet = (s) => normText(s).slice(0, 60);
  const devAdmonMap = new Map(
    (devPage.admonitions || []).map(a => [`${a.type}::${normSnippet(a.snippet)}`, a])
  );

  const missingAdmonitions = [];
  const mergedAdmonitions  = [];
  for (const a of (prodPage.admonitions || [])) {
    const key  = `${a.type}::${normSnippet(a.snippet)}`;
    const devA = devAdmonMap.get(key);
    if (!devA) {
      missingAdmonitions.push(a);
    } else if (a.paragraphCount > 1 && devA.paragraphCount < a.paragraphCount) {
      // Prod has more paragraphs than dev — likely collapsed into one block in dev
      mergedAdmonitions.push({
        type:          a.type,
        snippet:       a.snippet,
        prodParagraphs: a.paragraphCount,
        devParagraphs:  devA.paragraphCount,
      });
    }
  }

  // Paragraph-level content diff.
  // For each prod paragraph we look for the best-matching dev paragraph (by
  // content-word overlap). Three outcomes:
  //   • No match (< 55% overlap)  → "differentContent"  (paragraph absent from dev)
  //   • Match but dev is much shorter (≤ 65% of prod's word count) → "condensedContent"
  //     (paragraph exists but was condensed / content stripped in dev)
  //   • Good match with similar length → OK, skip
  const normPara = (s) => normText(s);

  // Build {wordSet, wordCount} entries for dev paragraphs and list items.
  // In Tridion (prod), list items are sometimes wrapped in <p> tags and appear as
  // paragraphs; in Docusaurus (dev) the same content renders as plain <li> text.
  // Including list items in the pool avoids false-positive "missing paragraph" hits.
  const toEntry = (text) => {
    const words = normPara(text).split(' ').filter(w => w.length > 3);
    return { wordSet: new Set(words), wordCount: words.length };
  };
  const allDevEntries = [
    ...(devPage.paragraphs || []).map(p => toEntry(p.text)),
    ...(devPage.listItems  || []).map(li => toEntry(li.text)),
  ];

  const differentContent = [];
  const condensedContent  = [];

  for (const prodPara of (prodPage.paragraphs || [])) {
    const prodWords   = normPara(prodPara.text).split(' ').filter(w => w.length > 3);
    if (prodWords.length < 8) continue; // too short for reliable matching
    const prodWordSet = new Set(prodWords);

    let bestOverlap      = 0;
    let bestDevWordCount = 0;
    for (const { wordSet, wordCount } of allDevEntries) {
      const overlap = prodWords.filter(w => wordSet.has(w)).length;
      const ratio   = overlap / prodWordSet.size;
      if (ratio > bestOverlap) { bestOverlap = ratio; bestDevWordCount = wordCount; }
    }

    if (bestOverlap < 0.55) {
      differentContent.push(prodPara); // {text, section} — absent from dev
    } else if (prodWordSet.size > 12 && bestDevWordCount < prodWordSet.size * 1.0) {
      condensedContent.push(prodPara); // {text, section} — present but shorter in dev
    }
  }

  // Table comparison: match by normalised header text, flag missing tables and row deficits.
  const tableKey = (t) => normText(t.signature || t.headerText).slice(0, 120);
  const devTableMap = new Map(
    (devPage.tables || []).map(t => [tableKey(t), t])
  );
  // Track which dev tables are already matched so merge detection only considers unmatched ones.
  const matchedDevKeys = new Set();
  const tableIssues = [];
  for (const t of (prodPage.tables || [])) {
    const key  = tableKey(t);
    const devT = devTableMap.get(key);
    if (!devT) {
      // Check if this prod table is a merge of multiple dev tables by cell-content overlap.
      // Normalise each cell the same way as headers; build a set of prod cell texts.
      const normCell = (s) => s.toLowerCase().replace(/[^\p{L}\p{N} ]/gu, '').replace(/\s+/g, ' ').trim();
      const prodCells = new Set((t.cells || []).map(normCell).filter(Boolean));
      const coveringDevTables = (devPage.tables || []).filter(dt => {
        if (matchedDevKeys.has(tableKey(dt))) return false;
        const devCells = (dt.cells || []).map(normCell).filter(Boolean);
        if (devCells.length === 0) return false;
        const overlap = devCells.filter(c => prodCells.has(c)).length;
        return overlap / devCells.length >= 0.6; // ≥60% of dev cells found in prod table
      });
      const kind = coveringDevTables.length >= 2 ? 'possible-merge' : 'missing-table';
      tableIssues.push({ kind, headerText: t.headerText, prodRows: t.rowCount, prodCols: t.colCount,
        ...(kind === 'possible-merge' ? { devTableCount: coveringDevTables.length } : {}) });
    } else {
      matchedDevKeys.add(key);
      if (devT.hasEmptyHeader && !t.hasEmptyHeader) {
        // Same table, but dev has an empty header row that prod omits (author choice in Tridion).
        tableIssues.push({ kind: 'empty-header', headerText: t.headerText, prodRows: t.rowCount, devRows: devT.rowCount });
      } else if (devT.rowCount < t.rowCount) {
        tableIssues.push({ kind: 'fewer-rows', headerText: t.headerText, prodRows: t.rowCount, devRows: devT.rowCount });
      } else if (devT.colCount < t.colCount) {
        tableIssues.push({ kind: 'fewer-cols', headerText: t.headerText, prodCols: t.colCount, devCols: devT.colCount });
      }
    }
  }

  // Dev tables not matched to any prod table — present in dev but removed from prod.
  const prodTableKeys = new Set((prodPage.tables || []).map(t => tableKey(t)));
  for (const dt of (devPage.tables || [])) {
    if (!prodTableKeys.has(tableKey(dt)) && !matchedDevKeys.has(tableKey(dt))) {
      tableIssues.push({ kind: 'extra-in-dev', headerText: dt.headerText, devRows: dt.rowCount, devCols: dt.colCount });
    }
  }

  // Word count difference
  const wordDiff = prodPage.wordCount - devPage.wordCount;
  const wordDiffPct = prodPage.wordCount > 0
    ? Math.round((wordDiff / prodPage.wordCount) * 100)
    : 0;

  const sim = similarity(prodPage.text, devPage.text);

  return { missingHeadings, listIssues, tableIssues, missingImages, missingAdmonitions, mergedAdmonitions, differentContent, condensedContent, wordDiff, wordDiffPct, similarity: sim };
}

// ─── Report ───────────────────────────────────────────────────────────────────
function buildReport(prodPages, devPages) {
  const prodPaths = new Set(prodPages.keys());
  const devPaths  = new Set(devPages.keys());

  const missingInDev = [...prodPaths].filter(p => !devPaths.has(p));
  const extraInDev   = [...devPaths].filter(p => !prodPaths.has(p));
  const common       = [...prodPaths].filter(p => devPaths.has(p));

  const pageComparisons = common.map(p => ({
    path: p,
    label: prodPages.get(p).label,
    prodUrl: prodPages.get(p).url,
    devUrl:  devPages.get(p).url,
    prodWordCount: prodPages.get(p).wordCount,
    devWordCount:  devPages.get(p).wordCount,
    ...comparePage(prodPages.get(p), devPages.get(p)),
  }));

  // Pages with issues: structural checks only — word count is excluded as unreliable
  // (Tridion injects hidden accessibility text that inflates prod word counts).
  const pagesWithIssues = pageComparisons.filter(
    c => c.missingHeadings.length > 0 || c.listIssues.length > 0 ||
         c.missingImages.length > 0 || c.missingAdmonitions.length > 0 ||
         c.mergedAdmonitions.length > 0 ||
         c.differentContent.length > 0 || c.condensedContent.length > 0 ||
         c.tableIssues.length > 0
  );

  return { missingInDev, extraInDev, common, pageComparisons, pagesWithIssues,
           prodTotal: prodPaths.size, devTotal: devPaths.size };
}

// ─── Shared per-page detail renderer ─────────────────────────────────────────
// Used by both the multi-page report (for each flagged page) and single-page mode.
function printPageDetail(c, prodPage, devPage) {
  log('\n' + '═'.repeat(72));
  log(` ${c.label.toUpperCase()}`);
  log('═'.repeat(72));
  dim(`  Dev:  ${c.devUrl}`);
  dim(`  Prod: ${c.prodUrl}`);

  const toSentenceCase = (s) => s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();
  const section = (title, prodCount, devCount) => {
    log('\n' + '─'.repeat(72));
    log(` ${toSentenceCase(title)}  (prod: ${prodCount}, dev: ${devCount})`);
    log('─'.repeat(72));
  };

  // Headings — only show if there are issues
  if (c.missingHeadings.length > 0) {
    section('HEADINGS', prodPage.headings.length, devPage.headings.length);
    for (const h of c.missingHeadings) err(`  ✗ ${'#'.repeat(h.level)} ${h.text}`);
  }

  // List items — only show if there are issues
  if (c.listIssues.length > 0) {
    section('LIST ITEMS', prodPage.listItems.length, devPage.listItems.length);
    for (const i of c.listIssues) {
      const p = i.text.length > 80 ? i.text.slice(0, 77) + '…' : i.text;
      if (i.kind === 'missing')          err(`  ✗ Missing from dev as list content (expected depth ${i.prodDepth}) — "${p}"`);
      else if (i.kind === 'similar-list-item') warn(`  ⇄ Similar list item in dev, but phrased/structured differently (expected depth ${i.prodDepth}; match ${i.similarityPct}%) — "${p}"` + (i.devText ? ` → dev: "${i.devText}"` : ''));
      else if (i.kind === 'present-as-paragraph') warn(`  ¶ Present in dev as paragraph/text block, not list item (expected depth ${i.prodDepth}; match ${i.similarityPct}%) — "${p}"` + (i.devText ? ` → dev: "${i.devText}"` : ''));
      else if (i.kind === 'wrong-depth') warn(`  ⤵ Same list item found in dev, but at a different nesting level (dev: ${i.devDepth}, expected: ${i.prodDepth}) — "${p}"`);
      else if (i.kind === 'wrong-type')  warn(`  ⇄ Same list item found in dev, but list type changed (${i.prodType}→${i.devType}) — "${p}"`);
      else if (i.kind === 'nested-note') warn(`  ⚠ Note nested in list item in dev (sibling in prod) — "${p}"`);
      else if (i.kind === 'content-outside-list') warn(`  ⚠ Content moved outside the list in dev (inside list item in prod) — "${p}"`);
      else if (i.kind === 'paragraph-longer-in-dev') warn(`  ⚠ Dev list item absorbs extra paragraph content — "${p}"`);
    }
  }

  // Tables — only show if there are issues
  if (c.tableIssues.length > 0) {
    section('TABLES', prodPage.tables.length, devPage.tables.length);
    for (const t of c.tableIssues) {
      const h = t.headerText.length > 60 ? t.headerText.slice(0, 57) + '…' : t.headerText;
      if (t.kind === 'missing-table') err(`  ✗ Missing table — "${h}" (prod: ${t.prodRows}r × ${t.prodCols}c)`);
      else if (t.kind === 'possible-merge') warn(`  ⇄ Possible table merge — "${h}" (prod: ${t.prodRows}r × ${t.prodCols}c; cell content matches ${t.devTableCount} dev tables, likely merged into one in prod)`);
      else if (t.kind === 'empty-header') warn(`  ⚠ Empty header row in dev not present in prod — "${h}" (prod: ${t.prodRows}r, dev: ${t.devRows}r incl. empty header; author choice in Tridion)`);
      else if (t.kind === 'fewer-rows') warn(`  ⤵ Fewer rows — "${h}" (prod: ${t.prodRows}, dev: ${t.devRows})`);
      else if (t.kind === 'fewer-cols') warn(`  ⤵ Fewer cols — "${h}" (prod: ${t.prodCols}, dev: ${t.devCols})`);
      else if (t.kind === 'extra-in-dev') err(`  ✗ Extra table in dev not in prod — "${h}" (dev: ${t.devRows}r × ${t.devCols}c)`);
    }
  }

  // Images — only show if there are issues
  if (c.missingImages.length > 0) {
    const mi = c.missingImages[0];
    section('IMAGES', (prodPage.images || []).length, (devPage.images || []).length);
    for (const img of c.missingImages) {
      if (img.kind === 'section') {
        warn(`  ⚠ ${img.count} image${img.count > 1 ? 's' : ''} missing in dev under section "${img.section}" (prod: ${img.prodTotal}, dev: ${img.devTotal})`);
      } else {
        err(`  ✗ ${img.count} image${img.count > 1 ? 's' : ''} missing from dev`);
      }
    }
  }

  // Admonitions — only show if there are issues
  if (c.missingAdmonitions.length > 0 || c.mergedAdmonitions.length > 0) {
    section('ADMONITIONS', prodPage.admonitions.length, devPage.admonitions.length);
    for (const a of c.missingAdmonitions) {
      err(`  ✗ Missing [${a.type}] "${a.snippet.slice(0, 80)}"`);
    }
    for (const a of c.mergedAdmonitions) {
      warn(`  ¶ Merged [${a.type}] "${a.snippet.slice(0, 80)}" — prod: ${a.prodParagraphs}p → dev: ${a.devParagraphs}p`);
    }
  }

  // Content blocks — only show if there are issues
  if (c.differentContent.length > 0 || c.condensedContent.length > 0) {
    section('CONTENT BLOCKS', prodPage.paragraphs.length, devPage.paragraphs.length);
    for (const p of c.differentContent) {
      const preview = p.text.split(/\s+/).slice(0, 10).join(' ');
      const loc = p.section ? ` [in "${p.section}"]` : '';
      err(`  ✗ Absent — "${preview}…"${loc}`);
    }
    for (const p of c.condensedContent) {
      const preview = p.text.split(/\s+/).slice(0, 10).join(' ');
      const loc = p.section ? ` [in "${p.section}"]` : '';
      warn(`  ⤵ Condensed — "${preview}…"${loc}`);
    }
  }

}

function printReport(report, prodPages, devPages) {
  const { missingInDev, extraInDev, pagesWithIssues, prodTotal, devTotal } = report;

  log('\n' + '═'.repeat(72));
  log(' COMPARISON REPORT');
  log('═'.repeat(72));
  const pageCompleteness = prodTotal > 0 ? Math.round((devTotal / prodTotal) * 100) : 100;
  log(`  Dev pages         : ${devTotal} / ${prodTotal} in prod  (${pageCompleteness}% page coverage)`);
  log(`  Compared (common) : ${report.common.length}`);
  log(`  Missing from dev  : ${report.missingInDev.length}`);
  log(`  Extra in dev      : ${report.extraInDev.length}`);
  log(`  Pages with issues : ${pagesWithIssues.length}`);

  // ── Missing pages ──────────────────────────────────────────────────────────
  log('\n' + '─'.repeat(72));
  log(' MISSING PAGES (present in prod, absent from dev)');
  log('─'.repeat(72));
  if (missingInDev.length === 0) {
    ok('  [✓] Dev contains all production pages.');
  } else {
    for (const p of missingInDev) {
      err(`  ✗  ${prodPages.get(p).label}`);
      dim(`     ${DEV_LABEL} (missing): ${toUrl(DEV_BASE, p)}`);
      dim(`     Prod:          ${prodPages.get(p).url}`);
    }
  }

  // ── Extra pages ────────────────────────────────────────────────────────────
  if (extraInDev.length > 0) {
    log('\n' + '─'.repeat(72));
    log(' EXTRA PAGES IN DEV (new/unreleased content not yet in prod)');
    log('─'.repeat(72));
    for (const p of extraInDev) {
      warn(`  +  ${devPages.get(p).label}`);
      dim(`     ${DEV_LABEL}:  ${devPages.get(p).url}`);
    }
  }

  // ── Content issues per page ────────────────────────────────────────────────
  log('\n' + '─'.repeat(72));
  log(' CONTENT ISSUES IN MATCHING PAGES');
  log('─'.repeat(72));

  if (pagesWithIssues.length === 0) {
    ok('  [✓] No content issues found in matching pages.');
  } else {
    for (const c of pagesWithIssues.sort((a, b) => a.similarity - b.similarity)) {
      printPageDetail(c, prodPages.get(c.path), devPages.get(c.path));
    }
  }

  log('\n' + '═'.repeat(72) + '\n');
}

// ─── Single-page detail report ────────────────────────────────────────────────
function printSinglePage(prodPage, devPage, pathname) {
  const c = {
    path: pathname,
    label: prodPage.label,
    prodUrl: prodPage.url,
    devUrl:  devPage.url,
    prodWordCount: prodPage.wordCount,
    devWordCount:  devPage.wordCount,
    ...comparePage(prodPage, devPage),
  };

  if (DEBUG) {
    log('\n' + '─'.repeat(72));
    log(' DEBUG — PROD extracted data');
    log('─'.repeat(72));
    log(`  Headings    : ${prodPage.headings.length}`);
    log(`  List items  : ${(prodPage.listItems || []).length}`);
    log(`  Images      : ${(prodPage.images || []).length}`);
    log(`  Admonitions : ${(prodPage.admonitions || []).length}`);
    (prodPage.admonitions || []).forEach((a, i) => {
      log(`    [${i}] type="${a.type}"  paragraphCount=${a.paragraphCount}  snippet="${a.snippet.slice(0, 80)}"`);
    });
    log(`  Paragraphs  : ${(prodPage.paragraphs || []).length}`);
    log(`  Tables      : ${(prodPage.tables || []).length}`);
    log(`  Word count  : ${prodPage.wordCount}`);

    log('\n' + '─'.repeat(72));
    log(' DEBUG — DEV extracted data');
    log('─'.repeat(72));
    log(`  Headings    : ${devPage.headings.length}`);
    log(`  List items  : ${(devPage.listItems || []).length}`);
    log(`  Images      : ${(devPage.images || []).length}`);
    log(`  Admonitions : ${(devPage.admonitions || []).length}`);
    (devPage.admonitions || []).forEach((a, i) => {
      log(`    [${i}] type="${a.type}"  paragraphCount=${a.paragraphCount}  snippet="${a.snippet.slice(0, 80)}"`);
    });
    log(`  Paragraphs  : ${(devPage.paragraphs || []).length}`);
    log(`  Tables      : ${(devPage.tables || []).length}`);
    log(`  Word count  : ${devPage.wordCount}`);
  }

  log('\n' + '═'.repeat(72));
  log(' SINGLE PAGE REPORT');
  log('═'.repeat(72));
  printPageDetail(c, prodPage, devPage);
  log('\n' + '═'.repeat(72) + '\n');
}

// ─── Main ─────────────────────────────────────────────────────────────────────
async function main() {
  log('\n' + '═'.repeat(72));
  log(' UiPath Docs Comparison Tool');
  log('═'.repeat(72));

  await promptInputs();
  if (PAGE_END === null) PAGE_END = Infinity;

  const batchLabel = PAGE_END === Infinity && PAGE_START === 0
    ? 'all'
    : `${PAGE_START + 1}–${PAGE_END === Infinity ? 'end' : PAGE_END}`;
  log(`  Path  : ${GUIDE_PATH}`);
  log(`  Pages : ${batchLabel}`);
  log(`  ${DEV_LABEL.padEnd(7)}: ${DEV_BASE}`);
  log(`  Prod  : ${PROD_BASE}`);
  log('─'.repeat(72) + '\n');

  let sessionState = loadSession(DEV_HOST);
  if (sessionState) ok('  Loaded Cloudflare session from auth-session.json');
  else warn('  No valid session — browser will open for manual login.');

  let { browser, context, headless } = await createBrowser(sessionState);

  // ── Single-page mode ──────────────────────────────────────────────────────
  if (PAGE_SINGLE) {
    log(`\n[Single page] ${PAGE_SINGLE}`);
    log('[1/2] Fetching PRODUCTION page…');
    const prodPage = await crawlSinglePage(context, PAGE_SINGLE, false, false);

    log(`[2/2] Fetching ${DEV_LABEL.toUpperCase()} page…`);
    let devPage = await crawlSinglePage(context, PAGE_SINGLE, true, headless);
    if (devPage === null) {
      log('\n  Relaunching browser for re-authentication…');
      await browser.close();
      invalidateSession();
      ({ browser, context, headless } = await createBrowser(null));
      devPage = await crawlSinglePage(context, PAGE_SINGLE, true, false);
    }

    await browser.close();
    if (!devPage) { err(`\nCould not retrieve ${DEV_LABEL.toLowerCase()} page.`); process.exit(1); }
    printSinglePage(prodPage, devPage, PAGE_SINGLE);
    return;
  }

  // ── Prod crawl ────────────────────────────────────────────────────────────
  log('\n[1/2] Crawling PRODUCTION…');
  const prodPages = await crawlSite(context, toUrl(PROD_BASE, GUIDE_PATH), false, false);

  // ── Dev crawl (with automatic relaunch if session expired) ────────────────
  log(`\n[2/2] Crawling ${DEV_LABEL.toUpperCase()}…`);
  let devPages = await crawlSite(context, toUrl(DEV_BASE, GUIDE_PATH), true, headless);

  if (devPages === null) {
    log('\n  Relaunching browser in visible mode for re-authentication…');
    await browser.close();
    invalidateSession();
    ({ browser, context, headless } = await createBrowser(null));
    devPages = await crawlSite(context, toUrl(DEV_BASE, GUIDE_PATH), true, false);
  }

  await browser.close();

  if (!devPages || devPages.size === 0) {
    err(`\nCould not retrieve ${DEV_LABEL.toLowerCase()} pages. Check authentication and try again.`);
    process.exit(1);
  }

  // ── Report ────────────────────────────────────────────────────────────────
  log('\nBuilding report…');
  const report = buildReport(prodPages, devPages);
  printReport(report, prodPages, devPages);

  if (OUTPUT_FILE) {
    const json = {
      generatedAt: new Date().toISOString(),
      guidePath: GUIDE_PATH,
      summary: {
        prodTotal: report.prodTotal,
        devTotal: report.devTotal,
        missingPages: report.missingInDev.length,
        extraPages: report.extraInDev.length,
        pagesWithContentIssues: report.pagesWithIssues.length,
      },
      missingPages: report.missingInDev.map(p => ({
        path: p, label: prodPages.get(p).label, prodUrl: prodPages.get(p).url,
      })),
      extraPages: report.extraInDev.map(p => ({
        path: p, label: devPages.get(p).label, devUrl: devPages.get(p).url,
      })),
      contentIssues: report.pagesWithIssues.map(c => ({
        path: c.path,
        label: c.label,
        similarity: c.similarity,
        prodWordCount: c.prodWordCount,
        devWordCount: c.devWordCount,
        wordDiffPct: c.wordDiffPct,
        missingSections: c.missingHeadings.map(h => `${'#'.repeat(h.level)} ${h.text}`),
        missingImages: c.missingImages.length > 0 ? `${c.missingImages[0].count} missing` : [],
        missingAdmonitions: c.missingAdmonitions.map(a => `[${a.type}] ${a.snippet}`),
        mergedAdmonitions: c.mergedAdmonitions.map(a =>
          `[${a.type}] "${a.snippet.slice(0, 80)}" — prod: ${a.prodParagraphs}p, dev: ${a.devParagraphs}p`
        ),
        tableIssues: (c.tableIssues || []).map(t => {
          if (t.kind === 'missing-table') return `[missing-table] "${t.headerText}" — prod ${t.prodRows}r×${t.prodCols}c`;
          if (t.kind === 'fewer-rows')    return `[fewer-rows] "${t.headerText}" — prod ${t.prodRows}, dev ${t.devRows}`;
          if (t.kind === 'fewer-cols')    return `[fewer-cols] "${t.headerText}" — prod ${t.prodCols}c, dev ${t.devCols}c`;
          return JSON.stringify(t);
        }),
        differentContent: (c.differentContent || []).map(p => ({ section: p.section, text: p.text.slice(0, 120) })),
        condensedContent: (c.condensedContent || []).map(p => ({ section: p.section, text: p.text.slice(0, 120) })),
        listIssues: c.listIssues.map(i => {
          if (i.kind === 'similar-list-item')
            return `[similar-list-item] "${i.text}" — similar list item found in dev at depth ${i.devDepth} (${i.devType}), match ${i.similarityPct}%${i.devText ? `; dev: "${i.devText}"` : ''}`;
          if (i.kind === 'present-as-paragraph')
            return `[present-as-paragraph] "${i.text}" — content appears in dev as paragraph/text block instead of list item, match ${i.similarityPct}%${i.devText ? `; dev: "${i.devText}"` : ''}`;
          if (i.kind === 'wrong-depth')
            return `[wrong-depth] "${i.text}" — prod depth ${i.prodDepth}, dev depth ${i.devDepth}`;
          if (i.kind === 'missing')
            return `[missing-list-item] "${i.text}" — not found in dev as list content; expected depth ${i.prodDepth}`;
          if (i.kind === 'wrong-type')
            return `[wrong-type] "${i.text}" — prod ${i.prodType}, dev ${i.devType}`;
          if (i.kind === 'nested-note')
            return `[nested-note] "${i.text}" — note nested in li in dev, sibling in prod`;
          if (i.kind === 'content-outside-list')
            return `[content-outside-list] "${i.text}" — paragraph outside list in dev, inside li in prod`;
          if (i.kind === 'paragraph-longer-in-dev')
            return `[paragraph-longer-in-dev] "${i.text}" — extra content appended to list item in dev`;
          return JSON.stringify(i);
        }),
        prodUrl: c.prodUrl,
        devUrl: c.devUrl,
      })),
    };
    fs.writeFileSync(OUTPUT_FILE, JSON.stringify(json, null, 2));
    ok(`  Report saved → ${OUTPUT_FILE}`);
  }
}

main().catch(e => { err('\nFatal: ' + e.message); process.exit(1); });
