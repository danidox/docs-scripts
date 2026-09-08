#!/usr/bin/env node
/**
 * UiPath Docs Localized Comparison Tool
 * ────────────────────────────────────────────────────────────────────────────
 * Validates localized content during the GDN → GitHub localization migration.
 *
 * Default mode (cross-locale): compares dev/[locale] against the English
 *   baseline on docs-dev. On the UiPath docs platform English URLs have NO
 *   language prefix (e.g. /maestro/... not /en/maestro/...) — language is
 *   selected by cookie. So /fr/maestro/X is rewritten to /maestro/X on the
 *   baseline side and the cookie is preset to "en" before navigation.
 *   Both sides come from the same GitHub deploy, so structural differences
 *   reflect pure localization drift — no GDN involvement, no prod release lag.
 *
 * Legacy mode (same-locale): compares dev/[locale] against prod/[locale].
 *   Triggered by passing --baseline-locale matching --locale, or by passing
 *   --baseline-base / --prod-base pointing at docs.uipath.com.
 *
 * Cookie handling: the locale cookie (UIPATH_DOCS_LOCALE) is preset on the
 *   browser context BEFORE any navigation, so the first request already
 *   carries the right preference and the site doesn't redirect from a stale
 *   cookie value. The two crawls run sequentially; the second crawl's preset
 *   overwrites the first's value on the shared cookie jar.
 *
 * Flags:
 *   --locale [fr|de|ja|es|pt-br|zh-cn][,locale2,...]
 *       Locale(s) of the dev side. Comma-separate to run several in one
 *       invocation (e.g. --locale fr,de,ja) — the English baseline is crawled
 *       ONCE and reused across every locale, instead of once per locale.
 *       The --path you pass should carry the FIRST listed locale's prefix;
 *       every other locale's path is derived by swapping that prefix in.
 *       Sets the language cookie before crawling so the site does not
 *       redirect away from the /[locale]/ URL.
 *   --baseline-locale [code]    (default: en)
 *       Locale of the baseline side. Path /[locale]/ is rewritten to
 *       /[baseline-locale]/ on the baseline crawl.
 *   --baseline-base [url]       (default: https://docs-dev.uipath.com)
 *       Environment serving the baseline. Alias: --prod-base (back-compat).
 *   --locale-key [key]          (default: i18nextLng)
 *       localStorage key the site uses for language preference (fallback).
 *
 * CJK support (ja, zh-cn):
 *   Text comparison uses character bigrams instead of space-split words for
 *   Japanese and Chinese content, where word boundaries are not marked by spaces.
 *
 * Usage:
 *   # Default — fr vs docs-dev/en
 *   node compare-docs-localized.js --locale fr --path /fr/maestro/.../introduction
 *
 *   # Compare fr vs prod/en (English on production)
 *   node compare-docs-localized.js --locale fr --path /fr/maestro/... --baseline-base https://docs.uipath.com
 *
 *   # Legacy: dev/fr vs prod/fr (same locale, across envs)
 *   node compare-docs-localized.js --locale fr --path /fr/maestro/... --baseline-base https://docs.uipath.com --baseline-locale fr
 *
 *   # Single page, debug
 *   node compare-docs-localized.js --locale ja --page /ja/maestro/.../introduction --debug
 *
 *   # Save report
 *   node compare-docs-localized.js --locale fr --path /fr/customer-portal/... --output report-fr.txt
 *
 *   # All locales in one run — baseline crawled once, one report file per locale
 *   node compare-docs-localized.js --locale fr,de,es,pt-br,ja,zh-cn \
 *       --path /fr/customer-portal/... --output report-customer-portal.txt
 *   #   -> report-customer-portal-fr.txt, report-customer-portal-de.txt, ...
 *
 *   # Chunk a large guide by subsection instead of crawling it whole:
 *   # seed from an actual PAGE one level inside the subsection you want — the
 *   # crawl scope is "everything before the last path segment of --path", so
 *   # seeding from the subsection name itself (no trailing page) widens the
 *   # scope back out to the whole guide instead of narrowing it.
 *   node compare-docs-localized.js --locale fr --path /fr/customer-portal/release-notes/2026-08-01 --output report-fr-release-notes.txt
 *   node compare-docs-localized.js --locale fr --path /fr/customer-portal/user-guide/about-customer-portal --output report-fr-user-guide.txt
 */

'use strict';

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const readline = require('readline');

// ─── CLI args ────────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const getArg = (flag) => { const i = args.indexOf(flag); return i !== -1 ? args[i + 1] : null; };
const HAS_EXPLICIT_DEV_BASE       = !!getArg('--dev-base');
const HAS_EXPLICIT_BASELINE_BASE  = !!(getArg('--baseline-base') || getArg('--prod-base'));
const VALUE_FLAGS = new Set(['--path', '--output', '--dev-base', '--prod-base', '--baseline-base', '--baseline-locale', '--limit', '--page', '--locale', '--locale-key', '--locale-cookie']);
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
const pageInput = parseSeedInput(getArg('--page'));

let GUIDE_PATH  = null;
const OUTPUT_FILE = getArg('--output') || null;
const RESOLVED_OUTPUT_FILE = OUTPUT_FILE
  ? (path.isAbsolute(OUTPUT_FILE) ? OUTPUT_FILE : path.join(process.cwd(), OUTPUT_FILE))
  : null;
let DEV_BASE  = (getArg('--dev-base')  || 'https://docs-dev.uipath.com').replace(/\/$/, '');
// Baseline = the side we treat as the structural source of truth.
// Default: docs-dev/en (raw English from same GitHub deploy as dev locale — no GDN, no prod release lag).
// Legacy: pass --prod-base (alias for --baseline-base) and --baseline-locale matching --locale.
let PROD_BASE = (getArg('--baseline-base') || getArg('--prod-base') || 'https://docs-dev.uipath.com').replace(/\/$/, '');
let DEV_HOST  = new URL(DEV_BASE).hostname;
let DEV_LABEL = labelForNonProdHost(DEV_HOST);
let PAGE_START = 0;
let PAGE_END   = null;
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
const PAGE_SINGLE  = pageInput ? pageInput.path : null;
const DEBUG        = args.includes('--debug');
// --locale accepts a comma-separated list (e.g. --locale fr,de,ja) to run every
// locale in one invocation. LOCALE stays the first entry — it's what the rest of
// the script (path derivation, labels, single-page mode) already treats as "the"
// locale; LOCALES is consulted only by the multi-locale loop in main().
const LOCALE_ARG     = getArg('--locale') || null;
const LOCALES        = LOCALE_ARG ? LOCALE_ARG.split(',').map(s => s.trim()).filter(Boolean) : [];
const LOCALE         = LOCALES[0] || null;
const KNOWN_LOCALES  = new Set(['fr', 'de', 'es', 'pt-br', 'ja', 'zh-cn']);
const LOCALE_KEY    = getArg('--locale-key') || 'i18nextLng';
const LOCALE_COOKIE = getArg('--locale-cookie') || 'UIPATH_DOCS_LOCALE';
const BASELINE_LOCALE = getArg('--baseline-locale') || 'en';
const STRUCTURAL    = !args.includes('--text'); // default: count-based structural comparison

// True when we're comparing a localized dev page against an English (or otherwise different-locale) baseline.
// False when the baseline locale matches the dev locale (legacy dev-vs-prod-same-locale mode).
const CROSS_LOCALE  = !!(LOCALE && BASELINE_LOCALE && LOCALE !== BASELINE_LOCALE);

// English on the UiPath docs platform has no language prefix in the URL —
// `/maestro/...` (not `/en/maestro/...`) — language is selected by cookie.
// So when rewriting to English we STRIP the dev locale prefix; for other
// target locales we replace it.
function rewriteLocaleInPath(pathname, fromLocale, toLocale) {
  if (!fromLocale || !toLocale || fromLocale === toLocale) return pathname;
  // English carries no prefix to strip, so it needs its own branch — matching
  // against '/en/' below would never succeed and the path would silently pass
  // through unrewritten (this is what caused missing-page reports to display
  // the dev URL as a bare copy of the English one, no locale prefix at all).
  let rest;
  if (fromLocale === 'en') {
    rest = pathname.replace(/^\//, '');
  } else {
    const fromPrefix = '/' + fromLocale + '/';
    if (!pathname.startsWith(fromPrefix)) return pathname;
    rest = pathname.slice(fromPrefix.length);
  }
  if (toLocale === 'en') return '/' + rest;
  return '/' + toLocale + '/' + rest;
}

// Strips a known locale prefix so /en/maestro/... and /fr/maestro/... share a key.
const LOCALE_PREFIX_REGEX = /^\/(en|fr|de|es|ja|zh-cn|pt-br)(\/|$)/i;
function localelessPath(pathname) {
  return (pathname || '').replace(LOCALE_PREFIX_REGEX, '/');
}

function hostNeedsAuth(hostname) {
  return hostname === 'docs-dev.uipath.com' || hostname === 'docs-staging.uipath.com';
}

// True when a baseline page has effectively no content — typical of a route that
// exists in the sidebar but resolves to an empty placeholder (e.g. new pages that
// shipped to dev/[locale] but not yet to the baseline /en/ tree).
function isEmptyPage(p) {
  if (!p) return true;
  const keptListItems = (p.listItems || []).filter(li => !li.selfSkip).length;
  const counts = (p.headings || []).length
              + keptListItems
              + (p.images || []).length
              + (p.admonitions || []).length
              + (p.tables || []).length
              + (p.codeBlocks || 0)
              + (p.videoEmbeds || 0);
  return counts === 0 && (p.wordCount || 0) < 50;
}

function baselineHostLabel(hostname) {
  if (hostname === 'docs.uipath.com')         return 'Prod';
  if (hostname === 'docs-staging.uipath.com') return 'staging';
  return 'Dev';
}

// Labels shown in the report. In cross-locale mode we use locale codes (EN / FR),
// which is more meaningful when both sides may be on docs-dev. In same-locale mode
// we fall back to the legacy environment labels (Prod / Dev / staging).
let BASELINE_LABEL = CROSS_LOCALE ? BASELINE_LOCALE.toUpperCase() : baselineHostLabel(new URL(PROD_BASE).hostname);
function refreshLabels() {
  BASELINE_LABEL = CROSS_LOCALE ? BASELINE_LOCALE.toUpperCase() : baselineHostLabel(new URL(PROD_BASE).hostname);
  if (CROSS_LOCALE && LOCALE) DEV_LABEL = LOCALE.toUpperCase();
  else DEV_LABEL = labelForNonProdHost(DEV_HOST);
}

function applySeedInput(parsed) {
  if (!parsed) return;
  GUIDE_PATH = parsed.path;
  if (parsed.base && !HAS_EXPLICIT_DEV_BASE) {
    const inputHost = new URL(parsed.base).hostname;
    if (!HAS_EXPLICIT_BASELINE_BASE && inputHost === 'docs.uipath.com') {
      PROD_BASE = parsed.base;
    } else {
      DEV_BASE  = parsed.base;
      DEV_HOST  = inputHost;
      DEV_LABEL = labelForNonProdHost(DEV_HOST);
    }
  }
}

applySeedInput(seedInput);
if (!seedInput) applySeedInput(pageInput);

// ─── Interactive prompts ──────────────────────────────────────────────────────
function prompt(rl, question) {
  return new Promise(resolve => rl.question(question, resolve));
}

async function promptInputs() {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

  if (!GUIDE_PATH) {
    const answer = await prompt(rl, '  Enter the guide URL or path to compare: ');
    const parsed = parseSeedInput(answer.trim() || '/apps/automation-cloud/latest/user-guide/introduction');
    applySeedInput(parsed);
  }

  if (PAGE_END === null) {
    const answer = await prompt(rl, '  Pages to crawl? (number, range "11-20", or "all") [all]: ');
    const raw = answer.trim().toLowerCase();
    if (!raw || raw === 'all') {
      PAGE_START = 0;
      PAGE_END   = Infinity;
    } else if (raw.includes('-')) {
      const [from, to] = raw.split('-').map(s => parseInt(s.trim(), 10));
      PAGE_START = (isNaN(from) ? 1 : from) - 1;
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

function labelForNonProdHost(hostname) {
  if (hostname === 'docs-staging.uipath.com') return 'staging';
  return 'Dev';
}

function guideBasePath(seedPath) {
  const p = normPath(seedPath);
  return p.substring(0, p.lastIndexOf('/') + 1);
}

// ─── CJK-aware tokenization ───────────────────────────────────────────────────
// Japanese and Chinese text has no spaces between words, so space-based word
// tokenization produces one giant token per phrase, making word-overlap
// similarity useless. Instead we use character bigrams, which work for any
// CJK script and tolerate minor character differences better than exact matches.

function isCJK(text) {
  const cjkCount = (text.match(/[぀-鿿가-힯]/g) || []).length;
  return cjkCount > text.length * 0.1;
}

// Returns a Set of character bigrams from CJK text (spaces stripped first).
// Falls back to a single-character set for strings shorter than 2 chars.
function bigramSet(text) {
  const chars = text.replace(/\s/g, '').split('');
  const bg = new Set();
  for (let i = 0; i < chars.length - 1; i++) bg.add(chars[i] + chars[i + 1]);
  if (chars.length === 1) bg.add(chars[0]);
  return bg;
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

// ─── Locale preference injection ──────────────────────────────────────────────
// Sets the site's language preference cookie (UIPATH_DOCS_LOCALE) and the
// localStorage key before the crawl begins, then reloads so the site serves
// the correct locale. Must be called after the page has loaded so we are on
// the right origin (cookies are domain-scoped).
// Set the locale cookie on the browser context BEFORE any page navigation,
// so the first request already carries the right preference. This avoids the
// load-then-reload round-trip that the previous post-navigation injection
// required, and prevents redirect chains caused by a stale cookie from
// auth-session.json mismatching the URL we're trying to load.
async function presetLocaleCookie(context, baseUrl, locale) {
  if (!locale) return;
  await context.addCookies([{
    name:   LOCALE_COOKIE,
    value:  locale,
    domain: new URL(baseUrl).hostname,
    path:   '/',
  }]);
}

// localStorage fallback — some platform components read this rather than the
// cookie. Must run on a loaded page (page.evaluate needs a document). No reload.
async function injectLocalePreference(page, origin, locale) {
  if (!locale) return;

  if (DEBUG) {
    const cookies = await page.context().cookies([origin]);
    log(`  [debug] ${origin} cookies (${cookies.length} total):`);
    for (const c of cookies) log(`    ${c.name}=${c.value}`);
    const ls = await page.evaluate(() => {
      const e = {};
      for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); e[k] = localStorage.getItem(k); }
      return JSON.stringify(e, null, 2);
    });
    log(`  [debug] ${origin} localStorage: ${ls}`);
  }

  // Cookie was preset on the context before navigation; this is the
  // localStorage fallback only.
  await page.evaluate(([key, value]) => {
    localStorage.setItem(key, value);
  }, [LOCALE_KEY, locale]);

  if (DEBUG) {
    const cookies = await page.context().cookies([origin]);
    const localeCookie = cookies.find(c => c.name === LOCALE_COOKIE);
    if (localeCookie) ok(`  [debug] ${LOCALE_COOKIE}=${localeCookie.value} confirmed`);
    else warn(`  [debug] ${LOCALE_COOKIE} not found in cookies — preset may have failed`);
  }
}

// ─── Retry / backoff ──────────────────────────────────────────────────────────
// Ported from the same pattern used for the migration scripts' HTTP fetches
// (uipath-docs-content/scripts/migration/{extract,compare}.py _get /
// _fetch_page_props): a big crawl makes hundreds of sequential requests, so
// the origin (Cloudflare) can throttle with 429/5xx partway through, or a
// request can just time out transiently. Retry with backoff — honouring a
// numeric Retry-After header when present — instead of recording a single
// hiccup as a real content difference.
function retryDelayMs(attempt, retryAfterHeader) {
  if (retryAfterHeader && /^\d+$/.test(retryAfterHeader.trim())) {
    return Math.min(parseInt(retryAfterHeader, 10), 30) * 1000;
  }
  return Math.min(2000 * 2 ** (attempt - 1), 30_000);
}

async function gotoWithRetry(page, url, { waitUntil = 'load', timeout = 30_000, retries = 4 } = {}) {
  let lastErr;
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const resp = await page.goto(url, { waitUntil, timeout });
      const status = resp ? resp.status() : 0;
      if ((status === 429 || status >= 500) && attempt < retries) {
        const wait = retryDelayMs(attempt, resp.headers()['retry-after']);
        warn(`  ~ HTTP ${status} (throttled) ${url}; retry ${attempt}/${retries - 1} in ${(wait / 1000).toFixed(0)}s`);
        await page.waitForTimeout(wait);
        continue;
      }
      return resp;
    } catch (e) {
      lastErr = e;
      if (attempt < retries) {
        const wait = retryDelayMs(attempt);
        await page.waitForTimeout(wait);
        continue;
      }
    }
  }
  throw lastErr || new Error(`Failed to load ${url} after ${retries} attempts`);
}

// True when the page we've landed on is the Cloudflare Access login page,
// not real content. Used both by navigateWithAuth (seed page) and by the
// per-page crawl loop below — a mid-crawl session expiry must not be treated
// as a run of pages that all really lost their content.
async function isOnAuthPage(page) {
  return page.evaluate(() => {
    // Real docs content always renders this container. A genuine Cloudflare Access
    // wall never does — so require its absence before trusting any text/title marker,
    // otherwise ordinary pages that merely *describe* signing in (e.g. a GitHub SSO
    // step in a docs article) false-trigger on "Sign in with" etc.
    if (document.querySelector('.theme-doc-markdown.markdown')) return false;
    return (
      document.body.textContent.includes('Sign in with') ||
      document.body.textContent.includes('Cloudflare Access') ||
      document.body.textContent.includes('Enter your credentials') ||
      document.title.toLowerCase().includes('cloudflare access')
    );
  });
}

// ─── Auth-aware navigation ────────────────────────────────────────────────────
// Auth requirement is determined by host (docs-dev or docs-staging), not by side.
// This matters now that the baseline side may also be docs-dev (e.g., docs-dev/en).
async function navigateWithAuth(page, url, context, isHeadless) {
  await gotoWithRetry(page, url, { waitUntil: 'domcontentloaded', timeout: 60_000 });
  const targetHost = new URL(url).hostname;
  if (!hostNeedsAuth(targetHost)) return 'ok';
  await page.waitForTimeout(2500);

  const onAuthPage = await isOnAuthPage(page);

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
          !document.title.toLowerCase().includes('cloudflare access'),
    targetHost,
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
async function extractPageData(page, isDevSite) {
  return page.evaluate(() => {
    const primary = document.querySelector('.theme-doc-markdown.markdown');
    const fallbacks = ['article', 'main article', '[class*="docItem"]', 'main'];
    let el = primary;
    if (!el) { for (const sel of fallbacks) { el = document.querySelector(sel); if (el) break; } }
    if (!el) el = document.body;

    const clone = el.cloneNode(true);
    [
      'nav', 'aside', 'footer',
      '[class*="breadcrumb"]', '[class*="pagination"]', '[class*="tableOfContents"]',
      '[class*="sidebar"]', '[class*="sidenav"]', '[class*="side-nav"]',
      '[class*="page-nav"]', '[class*="topic-nav"]', '[class*="guide-nav"]',
      '[class*="related-links"]', '[class*="relatedLinks"]',
      '[id*="onetrust"]', '[class*="onetrust"]',
      '[id*="cookie-consent"]', '[class*="cookie-consent"]',
    ].forEach(s => clone.querySelectorAll(s).forEach(n => n.remove()));

    const headings = [];
    clone.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(h => {
      const hClone = h.cloneNode(true);
      hClone.querySelectorAll('a').forEach(a => a.remove());
      const text = hClone.textContent
        .replace(/[​-‍﻿­]/g, '')
        .trim()
        .replace(/\s+/g, ' ');
      if (text) headings.push({ level: parseInt(h.tagName[1]), text });
    });

    const listItems = [];
    clone.querySelectorAll('li').forEach(li => {
      let depth = 0;
      let node = li.parentElement;
      while (node && node !== clone) {
        if (node.tagName === 'UL' || node.tagName === 'OL') depth++;
        node = node.parentElement;
      }
      const liClone = li.cloneNode(true);
      liClone.querySelectorAll('ul, ol').forEach(n => n.remove());
      const hasNestedNote = !!liClone.querySelector('[id="AdmonitionContainer"], [class*="admonition"]');
      liClone.querySelectorAll('[id="AdmonitionContainer"], [class*="admonition"]').forEach(n => n.remove());
      liClone.querySelectorAll('a, span, strong, em, b, i, code, td, th, div, p').forEach(el => {
        el.parentNode.insertBefore(document.createTextNode(' '), el);
      });
      const text = liClone.textContent.trim().replace(/\s+/g, ' ');
      const anchors = liClone.querySelectorAll('a');
      // Trailing punctuation (a period outside the <a> tag, or its absence —
      // Japanese/CJK convention often omits a Western-style terminal period)
      // must not decide whether a bullet is "just a link": strip it from both
      // sides before the exact-match check, or the same nav-link bullet gets
      // excluded on one locale and counted as real content on another,
      // producing a phantom list-item-count mismatch between languages.
      const stripTrailingPunct = (s) => s.replace(/\s*[.!?:;、。！？：；]+\s*$/u, '');
      const anchorText = stripTrailingPunct(anchors[0]?.textContent.trim().replace(/\s+/g, ' ') || '');
      const selfSkip = anchors.length === 1 && anchorText === stripTrailingPunct(text);
      if (text) {
        const type = li.parentElement.tagName.toLowerCase();
        listItems.push({ depth, type, text, hasNestedNote, selfSkip });
      }
    });

    const EMOJI_ALT = new Set(['available', 'not available']);
    const images = [];
    const rawImageSrcs = [];
    let currentImageSection = null;
    clone.querySelectorAll('h1, h2, h3, h4, h5, h6, img').forEach(el => {
      if (/^H[1-6]$/.test(el.tagName)) {
        const hClone = el.cloneNode(true);
        hClone.querySelectorAll('a').forEach(a => a.remove());
        currentImageSection = hClone.textContent
          .replace(/[​-‍﻿­]/g, '')
          .trim()
          .replace(/\s+/g, ' ');
        return;
      }
      const img = el;
      const src = img.getAttribute('src') || '';
      const alt = (img.getAttribute('alt') || '').trim().replace(/\s+/g, ' ');
      if (src) rawImageSrcs.push({ src, alt });
      const isContentImage = src.includes('cms.uipath.com/assets');
      if (!isContentImage) return;
      if (EMOJI_ALT.has(alt.toLowerCase())) return;
      images.push({ alt, src, section: currentImageSection });
    });

    const admonitions = [];
    const admonitionTypes = ['note', 'warning', 'caution', 'tip', 'danger', 'important', 'info'];
    const detectType = (el) => {
      const cls = (el.className || '').toLowerCase();
      for (const t of admonitionTypes) { if (cls.includes(t)) return t; }
      const label = el.querySelector('.admonition-heading, .admonitionHeading, [class*="admonitionHeading"]');
      if (label) return label.textContent.trim().toLowerCase();
      return 'note';
    };
    const admonitionSel = [
      '[id="AdmonitionContainer"]',    // platform (all environments)
      '[class*="admonition"]',
      '[class*="alert--"]',
      'aside[class*="note"], aside[class*="warn"], aside[class*="tip"], aside[class*="caution"]',
    ].join(', ');
    clone.querySelectorAll(admonitionSel).forEach(el => {
      if (el.closest('[id="AdmonitionContainer"]:not(:scope)') ||
          el.closest('[class*="admonition"]:not(:scope)')) return;
      const type = detectType(el);
      const snippet = el.textContent.trim().replace(/\s+/g, ' ').slice(0, 120);
      const pCount  = el.querySelectorAll('p').length;
      const brCount = el.querySelectorAll('br').length;
      const paragraphCount = pCount > 0 ? pCount : (brCount > 0 ? brCount + 1 : 1);
      if (snippet) admonitions.push({ type, snippet, paragraphCount });
    });

    const admonitionEls = new Set(clone.querySelectorAll(
      '[id="AdmonitionContainer"], [class*="admonition"], [class*="alert--"]'
    ));
    const paragraphs = [];
    let currentSection = null;
    clone.querySelectorAll('h1, h2, h3, h4, h5, h6, p, td, th').forEach(el => {
      if (/^H[1-6]$/.test(el.tagName)) {
        const hClone = el.cloneNode(true);
        hClone.querySelectorAll('a').forEach(a => a.remove());
        currentSection = hClone.textContent
          .replace(/[​-‍﻿­]/g, '').trim().replace(/\s+/g, ' ');
        return;
      }
      let ancestor = el.parentElement;
      while (ancestor && ancestor !== clone) {
        if (admonitionEls.has(ancestor)) return;
        ancestor = ancestor.parentElement;
      }
      const text = el.textContent.trim().replace(/\s+/g, ' ');
      if (text.length >= 40) paragraphs.push({ text, section: currentSection });
    });

    const tables = [];
    clone.querySelectorAll('table').forEach(table => {
      const rows = Array.from(table.querySelectorAll('tr'));
      if (rows.length === 0) return;
      let emptyHeaderRows = 0;
      for (const row of rows) {
        const cells = Array.from(row.querySelectorAll('td, th'));
        if (cells.length > 0 && cells.every(c => !c.textContent.trim())) emptyHeaderRows++;
        else break;
      }
      const hasEmptyHeader = emptyHeaderRows > 0;
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

      // Row-width self-consistency check (colspan-aware effective width per
      // row) — catches a dropped `|` that merges two markdown cells into one
      // without changing the table's total row count or its header-row cell
      // count (colCount above only looks at row 0, so a mid-table merge would
      // otherwise slip through undetected).
      const rowWidths = rows.map(r =>
        Array.from(r.querySelectorAll('td, th'))
          .reduce((sum, c) => sum + (parseInt(c.getAttribute('colspan'), 10) || 1), 0)
      ).filter(w => w > 0);
      const widthCounts = new Map();
      for (const w of rowWidths) widthCounts.set(w, (widthCounts.get(w) || 0) + 1);
      let modeWidth = rowWidths[0], modeCount = 0;
      for (const [w, n] of widthCounts) if (n > modeCount) { modeWidth = w; modeCount = n; }
      const jaggedRowCount = rowWidths.filter(w => w !== modeWidth).length;

      if (headerText) tables.push({ headerText, rowCount: rows.length, colCount, hasEmptyHeader, cells, signature, jaggedRowCount });
    });

    const codeBlocks = clone.querySelectorAll('pre').length;

    const videoEmbeds = clone.querySelectorAll('iframe, video').length;

    const text = clone.innerText.replace(/\s+/g, ' ').trim();
    const wordCount = text.split(/\s+/).filter(Boolean).length;

    // Markup-artifact self-check: these tokens should never survive into
    // rendered text — a correctly-parsed bold/italic/strike/table consumes
    // them entirely. Their literal presence signals a markdown construct the
    // renderer failed to parse (e.g. `**text **` — no space after the
    // opening `**` but one before the closing `**` trips some parsers,
    // leaving literal asterisks in the output instead of a <strong> tag).
    // pre/code/table are excluded first since they legitimately contain
    // these characters (dunder methods, shell pipes, real table markup).
    const artifactClone = clone.cloneNode(true);
    artifactClone.querySelectorAll('pre, code, table').forEach(n => n.remove());
    const artifactText = artifactClone.innerText;
    const countMatches = (re) => (artifactText.match(re) || []).length;
    const markupArtifacts = {
      strayBold:   countMatches(/\*\*/g),
      strayItalic: countMatches(/__/g),
      strayStrike: countMatches(/~~/g),
      strayPipe:   countMatches(/\|/g),
    };

    // Symbol marks used in compatibility/availability tables. Counted by exact
    // codepoint so NMT corruption that swaps to a lookalike (e.g. ✗ U+2717 or
    // plain ASCII "x") shows up as a drop in the original codepoint's count.
    //   ✅ U+2705 WHITE HEAVY CHECK MARK
    //   ❌ U+274C CROSS MARK
    const symbolMarks = {
      '✅': (text.match(/✅/g) || []).length,
      '❌': (text.match(/❌/g) || []).length,
    };

    return { headings, listItems, images, rawImageSrcs, admonitions, paragraphs, tables, codeBlocks, videoEmbeds, symbolMarks, markupArtifacts, text, wordCount };
  });
}

// ─── Site crawler ─────────────────────────────────────────────────────────────
// `isDevSide`: true for the dev-locale crawl, false for the baseline (English) crawl.
// `seedUrl` already carries the right locale and base for this side.
async function crawlSite(context, seedUrl, isDevSide, isHeadless, devLocaleOverride) {
  const base      = isDevSide ? DEV_BASE : PROD_BASE;
  const sideLocale = isDevSide ? (devLocaleOverride || LOCALE) : BASELINE_LOCALE;
  const pages     = new Map();

  // Preset the locale cookie BEFORE any navigation — the first request will
  // already carry the right preference, so the site won't redirect based on
  // a stale cookie left over from a previous run or the other side's crawl.
  await presetLocaleCookie(context, base, sideLocale);
  if (sideLocale) ok(`  Locale preset: ${LOCALE_COOKIE}=${sideLocale}  (${new URL(base).hostname})`);

  const page = await context.newPage();

  log(`  Seed: ${seedUrl}`);
  const status = await navigateWithAuth(page, seedUrl, context, isHeadless);
  if (status === 'reauth') { await page.close(); return null; }

  // Some locales get redirected to a differently-cased canonical URL by the
  // platform (e.g. /pt-br/... -> /pt-BR/..., /zh-cn/... -> /zh-CN/... — BCP-47
  // region subtags render uppercase). Derive the crawl scope from the URL we
  // actually landed on, not the one we requested, so the prefix filter below
  // matches the real (possibly re-cased) sidebar hrefs instead of silently
  // matching nothing.
  const guideBase = guideBasePath(new URL(page.url()).pathname);

  // localStorage fallback (cookie was already preset before navigation).
  const origin = isDevSide ? DEV_BASE : PROD_BASE;
  await injectLocalePreference(page, origin, sideLocale);

  try {
    await page.waitForSelector('.theme-doc-markdown.markdown', { timeout: 15_000 });
    await page.waitForTimeout(1000);
  } catch { await page.waitForTimeout(3000); }

  const links = await extractGuideLinks(page, guideBase);
  log(`  Found ${links.length} guide links`);

  if (links.length === 0) {
    warn('  No links matched the guide base path — check --path.');
    const seedPath = normPath(seedUrl);
    pages.set(localelessPath(seedPath), { label: 'Introduction', url: seedUrl, path: seedPath, ...(await extractPageData(page, isDevSide)) });
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
    const key     = localelessPath(pathname);
    process.stdout.write(`\r  [${PAGE_START + i + 1}/${PAGE_START + limited.length}] ${label.slice(0, 60).padEnd(60)}`);
    try {
      if (normPath(page.url()) !== pathname)
        await gotoWithRetry(page, fullUrl, { waitUntil: 'load', timeout: 30_000, retries: 4 });
      try {
        await page.waitForSelector('.theme-doc-markdown.markdown', { timeout: 15_000 });
        // The container mounts before long/complex pages finish hydrating their
        // full list of <li> elements — extracting immediately after the selector
        // resolves can under-count list items (confirmed on IXP pages with 80+
        // nested list items). A short settle delay lets hydration finish.
        await page.waitForTimeout(1000);
      } catch {
        await page.waitForTimeout(3000);
      }
      // A mid-crawl session expiry lands every subsequent page on the Cloudflare
      // Access login screen — without this check that silently records every
      // remaining page as "0 headings / 0 list items / ...", which reads as a
      // catastrophic (and entirely fake) content-loss bug rather than what it is.
      // Bail out via the same `null` contract the seed-page check already uses
      // (see navigateWithAuth) so main()'s existing reauth-and-retry handles it.
      if (hostNeedsAuth(new URL(fullUrl).hostname) && await isOnAuthPage(page)) {
        process.stdout.write('\n');
        warn(`  Cloudflare session expired mid-crawl at page ${PAGE_START + i + 1}/${PAGE_START + limited.length} — re-authenticating and restarting this side's crawl.`);
        await page.close();
        return null;
      }
      pages.set(key, { label, url: fullUrl, path: pathname, ...(await extractPageData(page, isDevSide)) });
    } catch (e) {
      pages.set(key, { label, url: fullUrl, path: pathname, headings: [], listItems: [], images: [], admonitions: [], paragraphs: [], tables: [], codeBlocks: 0, videoEmbeds: 0, text: '', wordCount: 0, error: e.message });
    }
  }
  process.stdout.write('\n');
  await page.close();
  return pages;
}

// ─── Single-page crawl ────────────────────────────────────────────────────────
async function crawlSinglePage(context, pathname, isDevSide, isHeadless) {
  const base    = isDevSide ? DEV_BASE : PROD_BASE;
  const sideLocale = isDevSide ? LOCALE : BASELINE_LOCALE;
  const fullUrl = toUrl(base, pathname);

  // Preset cookie before navigation — first request lands with correct locale.
  await presetLocaleCookie(context, base, sideLocale);
  if (sideLocale) ok(`  Locale preset: ${LOCALE_COOKIE}=${sideLocale}  (${new URL(base).hostname})`);

  const page    = await context.newPage();
  const status  = await navigateWithAuth(page, fullUrl, context, isHeadless);
  if (status === 'reauth') { await page.close(); return null; }

  // localStorage fallback (cookie already preset before navigation).
  const origin = isDevSide ? DEV_BASE : PROD_BASE;
  await injectLocalePreference(page, origin, sideLocale);

  try {
    await page.waitForSelector('.theme-doc-markdown.markdown', { timeout: 15_000 });
    await page.waitForTimeout(1000);
  } catch { await page.waitForTimeout(3000); }
  const label = pathname.split('/').pop();
  const data = await extractPageData(page, isDevSide);
  await page.close();
  return { label, url: fullUrl, path: pathname, ...data };
}

// ─── Content comparison ───────────────────────────────────────────────────────

/** Word-overlap (European) or bigram-overlap (CJK) similarity, 0–100.
 *  Measures what fraction of prod's unique tokens also appear in dev. */
function similarity(a, b) {
  if (!a || !b) return 0;
  const ta = a.slice(0, 4000).toLowerCase();
  const tb = b.slice(0, 4000).toLowerCase();
  let setA, setB;
  if (isCJK(ta)) {
    setA = bigramSet(ta);
    setB = bigramSet(tb);
  } else {
    setA = new Set(ta.split(/\s+/).filter(Boolean));
    setB = new Set(tb.split(/\s+/).filter(Boolean));
  }
  if (setA.size === 0) return 0;
  let overlap = 0;
  for (const token of setA) { if (setB.has(token)) overlap++; }
  return Math.round((overlap / setA.size) * 100);
}

/**
 * Compare list structures between prod and dev.
 * Uses character bigrams for CJK text instead of space-split words.
 */
function compareListStructure(prodItems, devItems, devParagraphs = []) {
  prodItems = (prodItems || []).filter(li => !li.selfSkip);
  devItems  = (devItems  || []).filter(li => !li.selfSkip);
  const norm = (s) => (s || '')
    .toLowerCase()
    .normalize('NFKC')
    .replace(/[^\p{L}\p{N} ]/gu, ' ')
    .replace(/\s+/g, ' ')
    .trim();

  // Language-aware token set: bigrams for CJK, space-words (len>3) for others.
  const wordSet = (s) => {
    const normalized = norm(s);
    if (isCJK(normalized)) return bigramSet(normalized);
    return new Set(normalized.split(' ').filter(w => w.length > 3));
  };

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

        // For CJK, bigrams are denser — lower the minimum token count for
        // similarity checks (a 4-character phrase = 3 bigrams, still meaningful).
        const minTokens = isCJK(prodItem.text) ? 2 : 4;
        const allowParagraphSimilarity = prodWords.size >= minTokens || bestParagraphRatio >= 0.95;
        const allowListSimilarity      = prodWords.size >= minTokens || bestListRatio      >= 0.95;

        if (bestParagraphRatio >= 0.6 && bestParagraphRatio >= bestListRatio && allowParagraphSimilarity) {
          issues.push({
            kind: 'present-as-paragraph',
            text: prodItem.text,
            prodDepth: prodItem.depth,
            similarityPct: Math.round(bestParagraphRatio * 100),
            devText: preview(bestParagraphMatch.text),
          });
        } else if (bestListRatio >= 0.6 && allowListSimilarity) {
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

// Decide which list items count as "real" content vs. purely-navigational
// link-only bullets, without letting each language's own translated text
// independently re-derive that judgment (translation shifts words across the
// anchor boundary, flipping skip/keep between locales for structurally
// identical content — see project memory for four confirmed false-positive
// classes this caused). When both sides have the same raw <li> count, trust
// document-order positional correspondence and apply EN's selfSkip decision,
// at each index, to both sides — each side's own depth is still used for
// bucketing, so a real nesting-shift defect is still caught. When raw counts
// differ, a mismatch already signals something else worth investigating on
// its own (e.g. an unclosed-admonition bug), and positional alignment can't
// be trusted there, so fall back to each side's own independent judgment.
function getKeptListItems(prodPage, devPage) {
  const prodRaw = prodPage.listItems || [];
  const devRaw  = devPage.listItems  || [];
  let prodKept, devKept;
  if (prodRaw.length === devRaw.length) {
    prodKept = []; devKept = [];
    for (let i = 0; i < prodRaw.length; i++) {
      if (prodRaw[i].selfSkip) continue;   // EN's decision governs both sides
      prodKept.push(prodRaw[i]);
      devKept.push(devRaw[i]);
    }
  } else {
    prodKept = prodRaw.filter(li => !li.selfSkip);
    devKept  = devRaw.filter(li => !li.selfSkip);
  }
  return { prodKept, devKept };
}

/**
 * Structural comparison: count-based, no text matching.
 * Used by default for localized content where translations differ between
 * GDN (prod) and GitHub (dev) but the page structure should be identical.
 */
function comparePageStructural(prodPage, devPage) {
  // Headings — compare count per h-level, flag any level with a different count.
  const prodLevels = {}, devLevels = {};
  for (const h of (prodPage.headings || [])) prodLevels[h.level] = (prodLevels[h.level] || 0) + 1;
  for (const h of (devPage.headings  || [])) devLevels[h.level]  = (devLevels[h.level]  || 0) + 1;
  const allLevels = new Set([...Object.keys(prodLevels), ...Object.keys(devLevels)]);
  const missingHeadings = [];
  for (const lvl of allLevels) {
    const p = prodLevels[lvl] || 0, d = devLevels[lvl] || 0;
    if (p !== d) missingHeadings.push({ structural: true, level: parseInt(lvl), prodCount: p, devCount: d });
  }

  // List items — compare count per nesting depth, after resolving which items
  // count as real content (see getKeptListItems above).
  const { prodKept, devKept } = getKeptListItems(prodPage, devPage);
  const prodDepths = {}, devDepths = {};
  for (const li of prodKept) prodDepths[li.depth] = (prodDepths[li.depth] || 0) + 1;
  for (const li of devKept)  devDepths[li.depth]  = (devDepths[li.depth]  || 0) + 1;
  const allDepths = new Set([...Object.keys(prodDepths), ...Object.keys(devDepths)]);
  const listIssues = [];
  for (const d of allDepths) {
    const p = prodDepths[d] || 0, dv = devDepths[d] || 0;
    if (p !== dv) listIssues.push({ structural: true, kind: 'depth-count', depth: parseInt(d), prodCount: p, devCount: dv });
  }

  // Images — total count only (section keys use translated heading text, unreliable cross-translation).
  const prodImgCount = (prodPage.images || []).length;
  const devImgCount  = (devPage.images  || []).length;
  const missingImages = [];
  if (prodImgCount !== devImgCount)
    missingImages.push({ kind: 'count', count: prodImgCount - devImgCount, prodTotal: prodImgCount, devTotal: devImgCount });

  // Admonitions — compare count per type.
  const prodAdmon = {}, devAdmon = {};
  for (const a of (prodPage.admonitions || [])) prodAdmon[a.type] = (prodAdmon[a.type] || 0) + 1;
  for (const a of (devPage.admonitions  || [])) devAdmon[a.type]  = (devAdmon[a.type]  || 0) + 1;
  const allTypes = new Set([...Object.keys(prodAdmon), ...Object.keys(devAdmon)]);
  const missingAdmonitions = [];
  for (const type of allTypes) {
    const p = prodAdmon[type] || 0, d = devAdmon[type] || 0;
    if (p !== d) missingAdmonitions.push({ structural: true, type, prodCount: p, devCount: d });
  }

  // Tables — match by position order (header text is translated, unusable as key).
  const prodTables = prodPage.tables || [];
  const devTables  = devPage.tables  || [];
  const tableIssues = [];
  const maxIdx = Math.max(prodTables.length, devTables.length);
  for (let i = 0; i < maxIdx; i++) {
    const pt = prodTables[i], dt = devTables[i];
    const label = `table ${i + 1}`;
    if  (pt && !dt) tableIssues.push({ kind: 'missing-table', headerText: label, prodRows: pt.rowCount, prodCols: pt.colCount });
    else if (!pt && dt) tableIssues.push({ kind: 'extra-in-dev', headerText: label, devRows: dt.rowCount, devCols: dt.colCount });
    else if (dt.rowCount < pt.rowCount) tableIssues.push({ kind: 'fewer-rows', headerText: label, prodRows: pt.rowCount, devRows: dt.rowCount });
    else if (dt.colCount < pt.colCount) tableIssues.push({ kind: 'fewer-cols', headerText: label, prodCols: pt.colCount, devCols: dt.colCount });
  }

  // Code blocks — count of <pre> elements.
  const prodCode = prodPage.codeBlocks || 0;
  const devCode  = devPage.codeBlocks  || 0;
  const codeIssues = prodCode !== devCode
    ? [{ prodCount: prodCode, devCount: devCode }]
    : [];

  // Video embeds — count of iframe and video elements.
  const prodVideo = prodPage.videoEmbeds || 0;
  const devVideo  = devPage.videoEmbeds  || 0;
  const videoIssues = prodVideo !== devVideo
    ? [{ prodCount: prodVideo, devCount: devVideo }]
    : [];

  // Symbol marks — per-codepoint count comparison. Flags when ✅/❌ are missing
  // or replaced by lookalike characters during translation (typically NMT).
  const prodSymbols = prodPage.symbolMarks || {};
  const devSymbols  = devPage.symbolMarks  || {};
  const symbolKeys  = new Set([...Object.keys(prodSymbols), ...Object.keys(devSymbols)]);
  const symbolIssues = [];
  for (const key of symbolKeys) {
    const p = prodSymbols[key] || 0;
    const d = devSymbols[key]  || 0;
    if (p !== d) symbolIssues.push({ symbol: key, prodCount: p, devCount: d });
  }

  const wordDiff    = prodPage.wordCount - devPage.wordCount;
  const wordDiffPct = prodPage.wordCount > 0 ? Math.round((wordDiff / prodPage.wordCount) * 100) : 0;
  const sim = similarity(prodPage.text, devPage.text);

  return { missingHeadings, listIssues, tableIssues, missingImages,
           missingAdmonitions, mergedAdmonitions: [], differentContent: [], condensedContent: [],
           codeIssues, videoIssues, symbolIssues, wordDiff, wordDiffPct, similarity: sim,
           listItemCounts: { prod: prodKept.length, dev: devKept.length } };
}

/**
 * Compare two pages. Returns an object describing what's missing or different.
 */
function comparePage(prodPage, devPage) {
  if (STRUCTURAL) return comparePageStructural(prodPage, devPage);
  const normText = (s) => (s || '')
    .toLowerCase()
    .normalize('NFKC')
    .replace(/[^\p{L}\p{N} ]/gu, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  const normH = (s) => normText(s);

  const IGNORED_HEADINGS = new Set([
    'subscribe to uipath release notes',
  ]);

  const devHeadings = new Set(devPage.headings.map(h => normH(h.text)));
  const missingHeadings = prodPage.headings.filter(
    h => !devHeadings.has(normH(h.text)) && !IGNORED_HEADINGS.has(normH(h.text))
  );

  const listIssues = compareListStructure(
    prodPage.listItems || [],
    devPage.listItems  || [],
    devPage.paragraphs || []
  );
  // compareListStructure filters selfSkip items internally (same-locale mode
  // has no cross-language drift problem, so each side just uses its own
  // judgment) — mirror that filter here so listItemCounts matches what was
  // actually compared, for print-site consistency with the structural mode.
  const listItemCounts = {
    prod: (prodPage.listItems || []).filter(li => !li.selfSkip).length,
    dev:  (devPage.listItems  || []).filter(li => !li.selfSkip).length,
  };

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
  const devImgBySection  = bySection(devPage.images);
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
      mergedAdmonitions.push({
        type: a.type, snippet: a.snippet,
        prodParagraphs: a.paragraphCount, devParagraphs: devA.paragraphCount,
      });
    }
  }

  // Paragraph-level content diff.
  // Uses character bigrams for CJK text; space-split words for European languages.
  const normPara = (s) => normText(s);

  const toEntry = (text) => {
    const normalized = normPara(text);
    let tokens;
    if (isCJK(normalized)) {
      // Bigrams for CJK: each character pair is a token.
      const chars = normalized.replace(/\s/g, '').split('');
      tokens = [];
      for (let i = 0; i < chars.length - 1; i++) tokens.push(chars[i] + chars[i + 1]);
      if (chars.length === 1) tokens.push(chars[0]);
    } else {
      tokens = normalized.split(' ').filter(w => w.length > 3);
    }
    return { wordSet: new Set(tokens), wordCount: tokens.length };
  };

  const allDevEntries = [
    ...(devPage.paragraphs || []).map(p => toEntry(p.text)),
    ...(devPage.listItems  || []).map(li => toEntry(li.text)),
  ];

  const differentContent = [];
  const condensedContent  = [];

  for (const prodPara of (prodPage.paragraphs || [])) {
    const normalized = normPara(prodPara.text);
    let prodTokens;
    if (isCJK(normalized)) {
      const chars = normalized.replace(/\s/g, '').split('');
      prodTokens = [];
      for (let i = 0; i < chars.length - 1; i++) prodTokens.push(chars[i] + chars[i + 1]);
      if (chars.length === 1) prodTokens.push(chars[0]);
    } else {
      prodTokens = normalized.split(' ').filter(w => w.length > 3);
    }
    if (prodTokens.length < 8) continue;
    const prodWordSet = new Set(prodTokens);

    let bestOverlap      = 0;
    let bestDevWordCount = 0;
    for (const { wordSet, wordCount } of allDevEntries) {
      const overlap = prodTokens.filter(w => wordSet.has(w)).length;
      const ratio   = overlap / prodWordSet.size;
      if (ratio > bestOverlap) { bestOverlap = ratio; bestDevWordCount = wordCount; }
    }

    if (bestOverlap < 0.55) {
      differentContent.push(prodPara);
    } else if (prodWordSet.size > 12 && bestDevWordCount < prodWordSet.size * 1.0) {
      condensedContent.push(prodPara);
    }
  }

  const tableKey  = (t) => normText(t.signature || t.headerText).slice(0, 120);
  const normCell  = (s) => s.toLowerCase().replace(/[^\p{L}\p{N} ]/gu, '').replace(/\s+/g, ' ').trim();
  const devTables = (devPage.tables || []).map((t, index) => ({ ...t, index }));
  const devTablesByKey = new Map();
  for (const t of devTables) {
    const key = tableKey(t);
    if (!devTablesByKey.has(key)) devTablesByKey.set(key, []);
    devTablesByKey.get(key).push(t);
  }
  const matchedDevIndexes = new Set();
  const tableIssues = [];
  for (const t of (prodPage.tables || [])) {
    const key      = tableKey(t);
    const prodCells = new Set((t.cells || []).map(normCell).filter(Boolean));
    const devCandidates = (devTablesByKey.get(key) || []).filter(dt => !matchedDevIndexes.has(dt.index));
    let devT = null;
    if (devCandidates.length === 1) {
      devT = devCandidates[0];
    } else if (devCandidates.length > 1) {
      let bestScore = -Infinity;
      for (const candidate of devCandidates) {
        const devCells = (candidate.cells || []).map(normCell).filter(Boolean);
        const overlap  = devCells.length === 0
          ? 0
          : devCells.filter(c => prodCells.has(c)).length / devCells.length;
        const rowDistance = Math.abs(candidate.rowCount - t.rowCount);
        const colDistance = Math.abs(candidate.colCount - t.colCount);
        const score = overlap * 100 - rowDistance * 5 - colDistance * 10;
        if (score > bestScore) { bestScore = score; devT = candidate; }
      }
    }
    if (!devT) {
      const coveringDevTables = devTables.filter(dt => {
        if (matchedDevIndexes.has(dt.index)) return false;
        const devCells = (dt.cells || []).map(normCell).filter(Boolean);
        if (devCells.length === 0) return false;
        const overlap = devCells.filter(c => prodCells.has(c)).length;
        return overlap / devCells.length >= 0.6;
      });
      const kind = coveringDevTables.length >= 2 ? 'possible-merge' : 'missing-table';
      tableIssues.push({ kind, headerText: t.headerText, prodRows: t.rowCount, prodCols: t.colCount,
        ...(kind === 'possible-merge' ? { devTableCount: coveringDevTables.length } : {}) });
    } else {
      matchedDevIndexes.add(devT.index);
      if (devT.hasEmptyHeader && !t.hasEmptyHeader) {
        tableIssues.push({ kind: 'empty-header', headerText: t.headerText, prodRows: t.rowCount, devRows: devT.rowCount });
      } else if (devT.rowCount < t.rowCount) {
        tableIssues.push({ kind: 'fewer-rows', headerText: t.headerText, prodRows: t.rowCount, devRows: devT.rowCount });
      } else if (devT.colCount < t.colCount) {
        tableIssues.push({ kind: 'fewer-cols', headerText: t.headerText, prodCols: t.colCount, devCols: devT.colCount });
      }
    }
  }

  const prodTableKeys = new Set((prodPage.tables || []).map(t => tableKey(t)));
  for (const dt of devTables) {
    if (!prodTableKeys.has(tableKey(dt)) && !matchedDevIndexes.has(dt.index)) {
      tableIssues.push({ kind: 'extra-in-dev', headerText: dt.headerText, devRows: dt.rowCount, devCols: dt.colCount });
    }
  }

  const wordDiff    = prodPage.wordCount - devPage.wordCount;
  const wordDiffPct = prodPage.wordCount > 0
    ? Math.round((wordDiff / prodPage.wordCount) * 100)
    : 0;
  const sim = similarity(prodPage.text, devPage.text);

  const prodCode = prodPage.codeBlocks || 0;
  const devCode  = devPage.codeBlocks  || 0;
  const codeIssues = prodCode !== devCode
    ? [{ prodCount: prodCode, devCount: devCode }]
    : [];

  const prodVideo = prodPage.videoEmbeds || 0;
  const devVideo  = devPage.videoEmbeds  || 0;
  const videoIssues = prodVideo !== devVideo
    ? [{ prodCount: prodVideo, devCount: devVideo }]
    : [];

  const prodSymbols = prodPage.symbolMarks || {};
  const devSymbols  = devPage.symbolMarks  || {};
  const symbolKeys  = new Set([...Object.keys(prodSymbols), ...Object.keys(devSymbols)]);
  const symbolIssues = [];
  for (const key of symbolKeys) {
    const p = prodSymbols[key] || 0;
    const d = devSymbols[key]  || 0;
    if (p !== d) symbolIssues.push({ symbol: key, prodCount: p, devCount: d });
  }

  // Markup-artifact self-check — each side is checked independently (this is
  // not a translation diff: a stray "**" or a jagged table row is a defect
  // regardless of whether the other side has the same defect).
  const ARTIFACT_LABEL = { strayBold: '**', strayItalic: '__', strayStrike: '~~', strayPipe: '|' };
  const markupIssues = [];
  for (const [side, page] of [[BASELINE_LABEL, prodPage], [DEV_LABEL, devPage]]) {
    const artifacts = page.markupArtifacts || {};
    for (const key of Object.keys(ARTIFACT_LABEL)) {
      const count = artifacts[key] || 0;
      if (count > 0) markupIssues.push({ kind: key, side, count });
    }
    for (const t of (page.tables || [])) {
      if ((t.jaggedRowCount || 0) > 0) markupIssues.push({ kind: 'jagged-table', side, header: t.headerText, count: t.jaggedRowCount });
    }
  }

  return { missingHeadings, listIssues, tableIssues, missingImages, missingAdmonitions, mergedAdmonitions, differentContent, condensedContent, codeIssues, videoIssues, symbolIssues, markupIssues, wordDiff, wordDiffPct, similarity: sim, listItemCounts };
}

// ─── Type-issue entry constants ───────────────────────────────────────────────
const TYPE_ORDER  = ['headings', 'listItems', 'tables', 'images', 'admonitions', 'codeBlocks', 'videoEmbeds', 'symbolMarks', 'markupArtifacts'];
const TYPE_LABELS = {
  headings:    'Headings',
  listItems:   'List items',
  tables:      'Tables',
  images:      'Images',
  admonitions: 'Admonitions',
  codeBlocks:  'Code blocks',
  videoEmbeds: 'Video embeds',
  symbolMarks: 'Symbol marks',
  markupArtifacts: 'Markup artifacts',
};
const TYPE_LABEL_PAD = Math.max(...Object.values(TYPE_LABELS).map(l => l.length));

/**
 * Returns an array of { style, text } pairs describing the issues for one
 * content type on one page.  style is one of: ok | err | warn | dim | log.
 * Used by both the console renderer (which applies colour) and the text
 * renderer (which uses the text verbatim, then runs toAsciiReportText).
 */
function typeIssueEntries(type, c, prodPage, devPage) {
  const D    = DEV_LABEL;
  const B    = BASELINE_LABEL;
  const push = (style, text) => ({ style, text });
  const entries = [];

  switch (type) {
    case 'headings': {
      entries.push(push('dim', `      ${B}:${prodPage.headings.length}   ${D}: ${devPage.headings.length}`));
      for (const h of c.missingHeadings) {
        if (h.structural) {
          const sym = h.devCount > h.prodCount ? '+' : '✗';
          entries.push(push(h.devCount > h.prodCount ? 'warn' : 'err',
            `      ${sym} h${h.level}: ${B} ${h.prodCount}, ${D} ${h.devCount}`));
        } else {
          entries.push(push('err', `      ✗ ${'#'.repeat(h.level)} ${h.text}`));
        }
      }
      break;
    }
    case 'listItems': {
      entries.push(push('dim', `      ${B}:${c.listItemCounts.prod}   ${D}: ${c.listItemCounts.dev}`));
      for (const i of c.listIssues) {
        if (i.structural) {
          const sym = i.devCount > i.prodCount ? '+' : '✗';
          entries.push(push(i.devCount > i.prodCount ? 'warn' : 'err',
            `      ${sym} depth-${i.depth} items: ${B} ${i.prodCount}, ${D} ${i.devCount}`));
        } else {
          const p = i.text.length > 80 ? i.text.slice(0, 77) + '…' : i.text;
          if      (i.kind === 'missing')               entries.push(push('err',  `      ✗ Missing from ${D} (depth ${i.prodDepth}) — "${p}"`));
          else if (i.kind === 'similar-list-item')     entries.push(push('warn', `      ⇄ Similar but differently phrased (depth ${i.prodDepth}; ${i.similarityPct}%) — "${p}"${i.devText ? ` → ${D}: "${i.devText}"` : ''}`));
          else if (i.kind === 'present-as-paragraph')  entries.push(push('warn', `      ¶ Present in ${D} as paragraph (depth ${i.prodDepth}; ${i.similarityPct}%) — "${p}"${i.devText ? ` → ${D}: "${i.devText}"` : ''}`));
          else if (i.kind === 'wrong-depth')           entries.push(push('warn', `      ⤵ Wrong depth (${D}: ${i.devDepth}, expected: ${i.prodDepth}) — "${p}"`));
          else if (i.kind === 'wrong-type')            entries.push(push('warn', `      ⇄ List type changed (${i.prodType}→${i.devType}) — "${p}"`));
          else if (i.kind === 'nested-note')           entries.push(push('warn', `      ⚠ Note nested in list item — "${p}"`));
          else if (i.kind === 'content-outside-list')  entries.push(push('warn', `      ⚠ Content moved outside list — "${p}"`));
          else if (i.kind === 'paragraph-longer-in-dev') entries.push(push('warn', `      ⚠ ${D} list item absorbs extra paragraph — "${p}"`));
        }
      }
      break;
    }
    case 'tables': {
      entries.push(push('dim', `      ${B}:${(prodPage.tables||[]).length}   ${D}: ${(devPage.tables||[]).length}`));
      for (const t of c.tableIssues) {
        const h = t.headerText.length > 60 ? t.headerText.slice(0, 57) + '…' : t.headerText;
        if      (t.kind === 'missing-table')   entries.push(push('err',  `      ✗ Missing table — "${h}" (${B}: ${t.prodRows}r × ${t.prodCols}c)`));
        else if (t.kind === 'possible-merge')  entries.push(push('warn', `      ⇄ Possible table merge — "${h}" (${B}: ${t.prodRows}r × ${t.prodCols}c; ${t.devTableCount} ${D} tables match)`));
        else if (t.kind === 'empty-header')    entries.push(push('warn', `      ⚠ Empty header row in ${D} not in ${B} — "${h}" (${B}: ${t.prodRows}r, ${D}: ${t.devRows}r)`));
        else if (t.kind === 'fewer-rows')      entries.push(push('warn', `      ⤵ Fewer rows — "${h}" (${B}: ${t.prodRows}, ${D}: ${t.devRows})`));
        else if (t.kind === 'fewer-cols')      entries.push(push('warn', `      ⤵ Fewer cols — "${h}" (${B}: ${t.prodCols}, ${D}: ${t.devCols})`));
        else if (t.kind === 'extra-in-dev')    entries.push(push('err',  `      ✗ Extra table in ${D} — "${h}" (${D}: ${t.devRows}r × ${t.devCols}c)`));
      }
      break;
    }
    case 'images': {
      entries.push(push('dim', `      ${B}:${(prodPage.images||[]).length}   ${D}: ${(devPage.images||[]).length}`));
      for (const img of c.missingImages) {
        if (img.kind === 'section')
          entries.push(push('warn', `      ⚠ ${img.count} image${img.count > 1 ? 's' : ''} missing under section "${img.section}" (${B}: ${img.prodTotal}, ${D}: ${img.devTotal})`));
        else
          entries.push(push('err',  `      ✗ ${img.count} image${img.count > 1 ? 's' : ''} missing from ${D} (${B}: ${img.prodTotal}, ${D}: ${img.devTotal || 0})`));
      }
      break;
    }
    case 'admonitions': {
      entries.push(push('dim', `      ${B}:${(prodPage.admonitions||[]).length}   ${D}: ${(devPage.admonitions||[]).length}`));
      for (const a of c.missingAdmonitions) {
        if (a.structural) {
          const sym = a.devCount > a.prodCount ? '+' : '✗';
          entries.push(push(a.devCount > a.prodCount ? 'warn' : 'err',
            `      ${sym} [${a.type}]: ${B} ${a.prodCount}, ${D} ${a.devCount}`));
        } else {
          entries.push(push('err', `      ✗ Missing [${a.type}] — "${a.snippet.slice(0, 80)}"`));
        }
      }
      for (const a of c.mergedAdmonitions || []) {
        entries.push(push('warn', `      ¶ Merged [${a.type}] — "${a.snippet.slice(0, 80)}" (${B}: ${a.prodParagraphs}p → ${D}: ${a.devParagraphs}p)`));
      }
      break;
    }
    case 'codeBlocks': {
      entries.push(push('dim', `      ${B}:${prodPage.codeBlocks || 0}   ${D}: ${devPage.codeBlocks || 0}`));
      for (const ci of c.codeIssues || []) {
        const sym = ci.devCount > ci.prodCount ? '+' : '✗';
        entries.push(push(ci.devCount > ci.prodCount ? 'warn' : 'err',
          `      ${sym} code blocks: ${B} ${ci.prodCount}, ${D} ${ci.devCount}`));
      }
      break;
    }
    case 'videoEmbeds': {
      entries.push(push('dim', `      ${B}:${prodPage.videoEmbeds || 0}   ${D}: ${devPage.videoEmbeds || 0}`));
      for (const vi of c.videoIssues || []) {
        const sym = vi.devCount > vi.prodCount ? '+' : '✗';
        entries.push(push(vi.devCount > vi.prodCount ? 'warn' : 'err',
          `      ${sym} video embeds: ${B} ${vi.prodCount}, ${D} ${vi.devCount}`));
      }
      break;
    }
    case 'symbolMarks': {
      const prodSym = prodPage.symbolMarks || {};
      const devSym  = devPage.symbolMarks  || {};
      const totals = (m) => Object.values(m).reduce((a, b) => a + b, 0);
      entries.push(push('dim', `      ${B}:${totals(prodSym)}   ${D}: ${totals(devSym)}`));
      for (const si of c.symbolIssues || []) {
        const sym = si.devCount > si.prodCount ? '+' : '✗';
        entries.push(push(si.devCount > si.prodCount ? 'warn' : 'err',
          `      ${sym} ${si.symbol}: ${B} ${si.prodCount}, ${D} ${si.devCount}`));
      }
      break;
    }
    case 'markupArtifacts': {
      const ARTIFACT_LABEL = { strayBold: '**', strayItalic: '__', strayStrike: '~~', strayPipe: '|' };
      for (const issue of c.markupIssues || []) {
        if (issue.kind === 'jagged-table') {
          const h = issue.header.length > 50 ? issue.header.slice(0, 47) + '…' : issue.header;
          entries.push(push('warn', `      ⚠ Jagged table rows in ${issue.side} — "${h}" (${issue.count} row(s) with mismatched cell count — check for a dropped "|")`));
        } else {
          const sym = ARTIFACT_LABEL[issue.kind] || issue.kind;
          entries.push(push('warn', `      ⚠ Literal "${sym}" found ${issue.count}× in ${issue.side} rendered text — markdown likely failed to parse`));
        }
      }
      break;
    }
  }
  return entries;
}

// ─── Report ───────────────────────────────────────────────────────────────────
function buildReport(prodPages, devPages) {
  const prodPaths = new Set(prodPages.keys());
  const devPaths  = new Set(devPages.keys());
  const missingInDev = [...prodPaths].filter(p => !devPaths.has(p));
  const extraInDev   = [...devPaths].filter(p => !prodPaths.has(p));
  const rawCommon    = [...prodPaths].filter(p => devPaths.has(p));

  // Pages whose baseline side resolved to an empty placeholder (route exists in the
  // sidebar but has no content). Hold these aside so they don't show up as "every
  // structural element missing on dev" — that's a baseline-not-published artifact,
  // not a localization defect.
  const baselineEmpty = rawCommon.filter(p => isEmptyPage(prodPages.get(p)));
  const baselineEmptySet = new Set(baselineEmpty);
  const common = rawCommon.filter(p => !baselineEmptySet.has(p));

  const pageComparisons = common.map(p => ({
    path: p,
    label: prodPages.get(p).label,
    prodUrl: prodPages.get(p).url,
    devUrl:  devPages.get(p).url,
    prodWordCount: prodPages.get(p).wordCount,
    devWordCount:  devPages.get(p).wordCount,
    ...comparePage(prodPages.get(p), devPages.get(p)),
  }));

  const pagesWithIssues = pageComparisons.filter(
    c => c.missingHeadings.length > 0 || c.listIssues.length > 0 ||
         c.missingImages.length > 0   || c.missingAdmonitions.length > 0 ||
         (c.mergedAdmonitions  || []).length > 0 ||
         (c.differentContent   || []).length > 0 || (c.condensedContent || []).length > 0 ||
         c.tableIssues.length > 0 ||
         (c.codeIssues  || []).length > 0 || (c.videoIssues || []).length > 0 ||
         (c.symbolIssues || []).length > 0 || (c.markupIssues || []).length > 0
  );

  const typeIssues = {
    headings:    pageComparisons.filter(c => (c.missingHeadings    || []).length > 0),
    listItems:   pageComparisons.filter(c => (c.listIssues         || []).length > 0),
    tables:      pageComparisons.filter(c => (c.tableIssues        || []).length > 0),
    images:      pageComparisons.filter(c => (c.missingImages      || []).length > 0),
    admonitions: pageComparisons.filter(c => (c.missingAdmonitions || []).length > 0 || (c.mergedAdmonitions || []).length > 0),
    codeBlocks:  pageComparisons.filter(c => (c.codeIssues         || []).length > 0),
    videoEmbeds: pageComparisons.filter(c => (c.videoIssues        || []).length > 0),
    symbolMarks: pageComparisons.filter(c => (c.symbolIssues       || []).length > 0),
    markupArtifacts: pageComparisons.filter(c => (c.markupIssues   || []).length > 0),
  };

  return { missingInDev, extraInDev, baselineEmpty, common, pageComparisons, pagesWithIssues, typeIssues,
           prodTotal: prodPaths.size, devTotal: devPaths.size };
}

// ─── Shared per-page detail renderer ─────────────────────────────────────────
function printPageDetail(c, prodPage, devPage) {
  const B = BASELINE_LABEL;
  log('\n' + '═'.repeat(72));
  log(` ${c.label.toUpperCase()}`);
  log('═'.repeat(72));
  dim(`  ${DEV_LABEL}:  ${c.devUrl}`);
  dim(`  ${B}: ${c.prodUrl}`);

  const toSentenceCase = (s) => s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();
  const section = (title, prodCount, devCount) => {
    log('\n' + '─'.repeat(72));
    log(` ${toSentenceCase(title)}  (${B}: ${prodCount}, ${DEV_LABEL}: ${devCount})`);
    log('─'.repeat(72));
  };

  // Headings
  section('HEADINGS', prodPage.headings.length, devPage.headings.length);
  if (c.missingHeadings.length === 0) {
    ok(`  [✓] Counts match`);
  } else {
    for (const h of c.missingHeadings) {
      if (h.structural) {
        const arrow = h.devCount > h.prodCount ? '+' : '✗';
        const fn    = h.devCount > h.prodCount ? warn : err;
        fn(`  ${arrow} h${h.level}: ${B} ${h.prodCount}, ${DEV_LABEL} ${h.devCount}`);
      } else {
        err(`  ✗ ${'#'.repeat(h.level)} ${h.text}`);
      }
    }
  }

  // List items
  section('LIST ITEMS', c.listItemCounts.prod, c.listItemCounts.dev);
  if (c.listIssues.length === 0) {
    ok(`  [✓] Counts match`);
  } else {
    for (const i of c.listIssues) {
      if (i.structural) {
        const arrow = i.devCount > i.prodCount ? '+' : '✗';
        const fn    = i.devCount > i.prodCount ? warn : err;
        fn(`  ${arrow} depth-${i.depth} items: ${B} ${i.prodCount}, ${DEV_LABEL} ${i.devCount}`);
      } else {
        const p = i.text.length > 80 ? i.text.slice(0, 77) + '…' : i.text;
        if (i.kind === 'missing')               err(`  ✗ Missing from ${DEV_LABEL} as list content (expected depth ${i.prodDepth}) — "${p}"`);
        else if (i.kind === 'similar-list-item') warn(`  ⇄ Similar list item in ${DEV_LABEL}, but phrased/structured differently (expected depth ${i.prodDepth}; match ${i.similarityPct}%) — "${p}"` + (i.devText ? ` → ${DEV_LABEL}: "${i.devText}"` : ''));
        else if (i.kind === 'present-as-paragraph') warn(`  ¶ Present in ${DEV_LABEL} as paragraph/text block, not list item (expected depth ${i.prodDepth}; match ${i.similarityPct}%) — "${p}"` + (i.devText ? ` → ${DEV_LABEL}: "${i.devText}"` : ''));
        else if (i.kind === 'wrong-depth')       warn(`  ⤵ Same list item found in ${DEV_LABEL}, but at a different nesting level (${DEV_LABEL}: ${i.devDepth}, expected: ${i.prodDepth}) — "${p}"`);
        else if (i.kind === 'wrong-type')        warn(`  ⇄ Same list item found in ${DEV_LABEL}, but list type changed (${i.prodType}→${i.devType}) — "${p}"`);
        else if (i.kind === 'nested-note')       warn(`  ⚠ Note nested in list item in ${DEV_LABEL} (sibling in ${B}) — "${p}"`);
        else if (i.kind === 'content-outside-list') warn(`  ⚠ Content moved outside the list in ${DEV_LABEL} (inside list item in ${B}) — "${p}"`);
        else if (i.kind === 'paragraph-longer-in-dev') warn(`  ⚠ ${DEV_LABEL} list item absorbs extra paragraph content — "${p}"`);
      }
    }
  }

  // Tables
  section('TABLES', (prodPage.tables || []).length, (devPage.tables || []).length);
  if (c.tableIssues.length === 0) {
    ok(`  [✓] Counts match`);
  } else {
    for (const t of c.tableIssues) {
      const h = t.headerText.length > 60 ? t.headerText.slice(0, 57) + '…' : t.headerText;
      if (t.kind === 'missing-table')       err(`  ✗ Missing table — "${h}" (${B}: ${t.prodRows}r × ${t.prodCols}c)`);
      else if (t.kind === 'possible-merge') warn(`  ⇄ Possible table merge — "${h}" (${B}: ${t.prodRows}r × ${t.prodCols}c; cell content matches ${t.devTableCount} ${DEV_LABEL} tables)`);
      else if (t.kind === 'empty-header')   warn(`  ⚠ Empty header row in ${DEV_LABEL} not present in ${B} — "${h}" (${B}: ${t.prodRows}r, ${DEV_LABEL}: ${t.devRows}r)`);
      else if (t.kind === 'fewer-rows')     warn(`  ⤵ Fewer rows — "${h}" (${B}: ${t.prodRows}, ${DEV_LABEL}: ${t.devRows})`);
      else if (t.kind === 'fewer-cols')     warn(`  ⤵ Fewer cols — "${h}" (${B}: ${t.prodCols}, ${DEV_LABEL}: ${t.devCols})`);
      else if (t.kind === 'extra-in-dev')   err(`  ✗ Extra table in ${DEV_LABEL} not in ${B} — "${h}" (${DEV_LABEL}: ${t.devRows}r × ${t.devCols}c)`);
    }
  }

  // Images
  section('IMAGES', (prodPage.images || []).length, (devPage.images || []).length);
  if (c.missingImages.length === 0) {
    ok(`  [✓] Counts match`);
  } else {
    for (const img of c.missingImages) {
      if (img.kind === 'section') warn(`  ⚠ ${img.count} image${img.count > 1 ? 's' : ''} missing in ${DEV_LABEL} under section "${img.section}" (${B}: ${img.prodTotal}, ${DEV_LABEL}: ${img.devTotal})`);
      else err(`  ✗ ${img.count} image${img.count > 1 ? 's' : ''} missing from ${DEV_LABEL}`);
    }
  }

  // Admonitions
  section('ADMONITIONS', (prodPage.admonitions || []).length, (devPage.admonitions || []).length);
  if (c.missingAdmonitions.length === 0 && c.mergedAdmonitions.length === 0) {
    ok(`  [✓] Counts match`);
  } else {
    for (const a of c.missingAdmonitions) {
      if (a.structural) {
        const arrow = a.devCount > a.prodCount ? '+' : '✗';
        const fn    = a.devCount > a.prodCount ? warn : err;
        fn(`  ${arrow} [${a.type}]: ${B} ${a.prodCount}, ${DEV_LABEL} ${a.devCount}`);
      } else {
        err(`  ✗ Missing [${a.type}] "${a.snippet.slice(0, 80)}"`);
      }
    }
    for (const a of c.mergedAdmonitions) warn(`  ¶ Merged [${a.type}] "${a.snippet.slice(0, 80)}" — ${B}: ${a.prodParagraphs}p → ${DEV_LABEL}: ${a.devParagraphs}p`);
  }

  // Code blocks
  section('CODE BLOCKS', prodPage.codeBlocks || 0, devPage.codeBlocks || 0);
  if ((c.codeIssues || []).length === 0) {
    ok(`  [✓] Counts match`);
  } else {
    for (const ci of c.codeIssues) {
      const sym = ci.devCount > ci.prodCount ? '+' : '✗';
      const fn  = ci.devCount > ci.prodCount ? warn : err;
      fn(`  ${sym} code blocks: ${B} ${ci.prodCount}, ${DEV_LABEL} ${ci.devCount}`);
    }
  }

  // Video embeds
  section('VIDEO EMBEDS', prodPage.videoEmbeds || 0, devPage.videoEmbeds || 0);
  if ((c.videoIssues || []).length === 0) {
    ok(`  [✓] Counts match`);
  } else {
    for (const vi of c.videoIssues) {
      const sym = vi.devCount > vi.prodCount ? '+' : '✗';
      const fn  = vi.devCount > vi.prodCount ? warn : err;
      fn(`  ${sym} video embeds: ${B} ${vi.prodCount}, ${DEV_LABEL} ${vi.devCount}`);
    }
  }

  // Symbol marks (✅ ❌)
  const prodSymTotals = Object.values(prodPage.symbolMarks || {}).reduce((a, b) => a + b, 0);
  const devSymTotals  = Object.values(devPage.symbolMarks  || {}).reduce((a, b) => a + b, 0);
  section('SYMBOL MARKS', prodSymTotals, devSymTotals);
  if ((c.symbolIssues || []).length === 0) {
    ok(`  [✓] Counts match`);
  } else {
    for (const si of c.symbolIssues) {
      const sym = si.devCount > si.prodCount ? '+' : '✗';
      const fn  = si.devCount > si.prodCount ? warn : err;
      fn(`  ${sym} ${si.symbol}: ${B} ${si.prodCount}, ${DEV_LABEL} ${si.devCount}`);
    }
  }

  // Markup artifacts (self-check — stray **/__/~~/| and jagged table rows)
  log('\n' + '─'.repeat(72));
  log(' MARKUP ARTIFACTS (self-check — not a translation diff)');
  log('─'.repeat(72));
  if ((c.markupIssues || []).length === 0) {
    ok(`  [✓] No artifacts found`);
  } else {
    const ARTIFACT_LABEL = { strayBold: '**', strayItalic: '__', strayStrike: '~~', strayPipe: '|' };
    for (const issue of c.markupIssues) {
      if (issue.kind === 'jagged-table') {
        const h = issue.header.length > 50 ? issue.header.slice(0, 47) + '…' : issue.header;
        warn(`  ⚠ Jagged table rows in ${issue.side} — "${h}" (${issue.count} row(s) with mismatched cell count — check for a dropped "|")`);
      } else {
        const sym = ARTIFACT_LABEL[issue.kind] || issue.kind;
        warn(`  ⚠ Literal "${sym}" found ${issue.count}× in ${issue.side} rendered text — markdown likely failed to parse`);
      }
    }
  }

  // Content blocks (text mode only — skipped in structural mode)
  if (!STRUCTURAL) {
    section('CONTENT BLOCKS', (prodPage.paragraphs || []).length, (devPage.paragraphs || []).length);
    if (c.differentContent.length === 0 && c.condensedContent.length === 0) {
      ok(`  [✓] No missing or condensed blocks`);
    } else {
      for (const p of c.differentContent) {
        const preview = p.text.split(/\s+/).slice(0, 10).join(' ');
        err(`  ✗ Absent — "${preview}…"${p.section ? ` [in "${p.section}"]` : ''}`);
      }
      for (const p of c.condensedContent) {
        const preview = p.text.split(/\s+/).slice(0, 10).join(' ');
        warn(`  ⤵ Condensed — "${preview}…"${p.section ? ` [in "${p.section}"]` : ''}`);
      }
    }
  }
}

function printReport(report, prodPages, devPages) {
  const { missingInDev, extraInDev, pagesWithIssues, prodTotal, devTotal } = report;
  const B = BASELINE_LABEL;

  // ── Header ────────────────────────────────────────────────────────────────
  log('\n' + '═'.repeat(72));
  log(' COMPARISON REPORT');
  log('═'.repeat(72));
  const pageCompleteness = prodTotal > 0 ? Math.round((devTotal / prodTotal) * 100) : 100;
  log(`  ${DEV_LABEL} pages${' '.repeat(Math.max(1, 11 - DEV_LABEL.length))}: ${devTotal} / ${prodTotal} in ${B}  (${pageCompleteness}% page coverage)`);
  log(`  Compared (common) : ${report.common.length}`);
  log(`  Missing from ${DEV_LABEL}${' '.repeat(Math.max(1, 4 - DEV_LABEL.length))}: ${report.missingInDev.length}`);
  log(`  Extra in ${DEV_LABEL}${' '.repeat(Math.max(1, 7 - DEV_LABEL.length))}: ${report.extraInDev.length}`);
  log(`  Pages with issues : ${pagesWithIssues.length}`);

  // ── Missing / extra pages ─────────────────────────────────────────────────
  log('\n' + '─'.repeat(72));
  log(` MISSING PAGES (present in ${B}, absent from ${DEV_LABEL})`);
  log('─'.repeat(72));
  if (missingInDev.length === 0) {
    ok(`  [✓] ${DEV_LABEL} contains all ${B} pages.`);
  } else {
    for (const p of missingInDev) {
      const prodPath = prodPages.get(p).path || p;
      const devPathHypothetical = rewriteLocaleInPath(prodPath, BASELINE_LOCALE, LOCALE);
      err(`  ✗  ${prodPages.get(p).label}`);
      dim(`     ${DEV_LABEL} (missing): ${toUrl(DEV_BASE, devPathHypothetical)}`);
      dim(`     ${B}:          ${prodPages.get(p).url}`);
    }
  }

  if (extraInDev.length > 0) {
    log('\n' + '─'.repeat(72));
    log(` EXTRA PAGES IN ${DEV_LABEL.toUpperCase()} (new/unreleased content not yet in ${B})`);
    log('─'.repeat(72));
    for (const p of extraInDev) {
      warn(`  +  ${devPages.get(p).label}`);
      dim(`     ${DEV_LABEL}:  ${devPages.get(p).url}`);
    }
  }

  // ── Pages not yet published on baseline ──────────────────────────────────
  // Routes that resolve to an empty page on the baseline side — the URL exists
  // (it's in the sidebar) but has no content yet. Excluded from comparisons.
  if ((report.baselineEmpty || []).length > 0) {
    log('\n' + '─'.repeat(72));
    log(` PAGES NOT YET PUBLISHED ON ${B.toUpperCase()} (route exists, content empty — excluded from comparison)`);
    log('─'.repeat(72));
    for (const p of report.baselineEmpty) {
      warn(`  ⚠  ${devPages.get(p).label}`);
      dim(`     ${DEV_LABEL}:  ${devPages.get(p).url}`);
      dim(`     ${B}: ${prodPages.get(p).url}`);
    }
  }

  // ── Content type summary ──────────────────────────────────────────────────
  log('\n' + '─'.repeat(72));
  log(' CONTENT TYPE SUMMARY');
  log('─'.repeat(72));
  for (const type of TYPE_ORDER) {
    const n     = report.typeIssues[type].length;
    const label = TYPE_LABELS[type].padEnd(TYPE_LABEL_PAD);
    if (n === 0) ok(`  ${label}  [OK]`);
    else         err(`  ${label}  ✗  ${n} / ${report.common.length} page${n > 1 ? 's' : ''} with issues`);
  }

  // ── Issues by content type ────────────────────────────────────────────────
  log('\n' + '─'.repeat(72));
  log(' ISSUES BY CONTENT TYPE');
  log('─'.repeat(72));

  const hasAnyIssues = TYPE_ORDER.some(t => report.typeIssues[t].length > 0);
  if (!hasAnyIssues) {
    ok('  [✓] No content issues found in any matching pages.');
  } else {
    const cfns = { ok, err, warn, dim, log };
    for (const type of TYPE_ORDER) {
      const affected = report.typeIssues[type];
      if (affected.length === 0) continue;
      log(`\n  ${TYPE_LABELS[type].toUpperCase()} — ${affected.length} page${affected.length > 1 ? 's' : ''} with issues`);
      log('  ' + '─'.repeat(68));
      for (const c of affected) {
        log('');
        log(`    ${c.label}`);
        for (const { style, text } of typeIssueEntries(type, c, prodPages.get(c.path), devPages.get(c.path)))
          cfns[style](text);
      }
    }
  }

  // ── Image counts — all pages ──────────────────────────────────────────────
  log('\n' + '─'.repeat(72));
  log(' IMAGE COUNTS — ALL PAGES');
  log('─'.repeat(72));
  for (const p of report.common) {
    const prod      = prodPages.get(p);
    const dev       = devPages.get(p);
    const prodCount = (prod.images || []).length;
    const devCount  = (dev.images  || []).length;
    const label     = (prod.label || p.split('/').pop()).slice(0, 45).padEnd(45);
    if (prodCount === devCount) ok(`  [✓] ${label}  ${B}: ${prodCount}   ${DEV_LABEL}: ${devCount}`);
    else                        err(`  ✗   ${label}  ${B}: ${prodCount}   ${DEV_LABEL}: ${devCount}`);
  }

  // ── Affected pages — URL reference ────────────────────────────────────────
  const affectedPaths = new Set();
  for (const type of TYPE_ORDER) for (const c of report.typeIssues[type]) affectedPaths.add(c.path);
  const hasRef = affectedPaths.size > 0 || report.missingInDev.length > 0;
  if (hasRef) {
    log('\n' + '─'.repeat(72));
    log(' AFFECTED PAGES — URL REFERENCE');
    log('─'.repeat(72));
    for (const path of report.common.filter(p => affectedPaths.has(p))) {
      const c = report.pageComparisons.find(x => x.path === path);
      if (!c) continue;
      log(`\n  ${c.label}`);
      dim(`    ${DEV_LABEL}:  ${c.devUrl}`);
      dim(`    ${B}: ${c.prodUrl}`);
    }
    for (const p of report.missingInDev) {
      const prodPath = prodPages.get(p).path || p;
      const devPathHypothetical = rewriteLocaleInPath(prodPath, BASELINE_LOCALE, LOCALE);
      log(`\n  ${prodPages.get(p).label}  [missing from ${DEV_LABEL}]`);
      dim(`    ${DEV_LABEL}:  ${toUrl(DEV_BASE, devPathHypothetical)}`);
      dim(`    ${B}: ${prodPages.get(p).url}`);
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
    log(` DEBUG — ${BASELINE_LABEL} extracted data`);
    log('─'.repeat(72));
    log(`  Headings    : ${prodPage.headings.length}`);
    log(`  List items  : ${c.listItemCounts.prod}`);
    log(`  Images      : ${(prodPage.images || []).length} (filtered) / ${(prodPage.rawImageSrcs || []).length} (total in content area)`);
    if ((prodPage.rawImageSrcs || []).length > 0) {
      log(`  All img srcs found (${BASELINE_LABEL}):`);
      (prodPage.rawImageSrcs || []).forEach(i => log(`    alt="${i.alt}"  src="${i.src}"`));
    }
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
    log(`  List items  : ${c.listItemCounts.dev}`);
    log(`  Images      : ${(devPage.images || []).length} (filtered) / ${(devPage.rawImageSrcs || []).length} (total in content area)`);
    if ((devPage.rawImageSrcs || []).length > 0) {
      log('  All img srcs found (dev):');
      (devPage.rawImageSrcs || []).forEach(i => log(`    alt="${i.alt}"  src="${i.src}"`));
    }
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

function pageDetailLines(c, prodPage, devPage) {
  const lines = [];
  const B = BASELINE_LABEL;
  const toSentenceCase = (s) => s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();
  const section = (title, prodCount, devCount) => {
    lines.push('');
    lines.push('─'.repeat(72));
    lines.push(` ${toSentenceCase(title)}  (${B}: ${prodCount}, ${DEV_LABEL}: ${devCount})`);
    lines.push('─'.repeat(72));
  };

  lines.push('');
  lines.push('═'.repeat(72));
  lines.push(` ${c.label.toUpperCase()}`);
  lines.push('═'.repeat(72));
  lines.push(`  ${DEV_LABEL}:  ${c.devUrl}`);
  lines.push(`  ${B}: ${c.prodUrl}`);

  section('HEADINGS', prodPage.headings.length, devPage.headings.length);
  if (c.missingHeadings.length === 0) {
    lines.push(`  [✓] Counts match`);
  } else {
    for (const h of c.missingHeadings) {
      if (h.structural) {
        const sym = h.devCount > h.prodCount ? '+' : '✗';
        lines.push(`  ${sym} h${h.level}: ${B} ${h.prodCount}, ${DEV_LABEL} ${h.devCount}`);
      } else {
        lines.push(`  ✗ ${'#'.repeat(h.level)} ${h.text}`);
      }
    }
  }

  section('LIST ITEMS', c.listItemCounts.prod, c.listItemCounts.dev);
  if (c.listIssues.length === 0) {
    lines.push(`  [✓] Counts match`);
  } else {
    for (const i of c.listIssues) {
      if (i.structural) {
        const sym = i.devCount > i.prodCount ? '+' : '✗';
        lines.push(`  ${sym} depth-${i.depth} items: ${B} ${i.prodCount}, ${DEV_LABEL} ${i.devCount}`);
      } else {
        const p = i.text.length > 80 ? i.text.slice(0, 77) + '…' : i.text;
        if (i.kind === 'missing')               lines.push(`  ✗ Missing from ${DEV_LABEL} as list content (expected depth ${i.prodDepth}) — "${p}"`);
        else if (i.kind === 'similar-list-item') lines.push(`  ⇄ Similar list item in ${DEV_LABEL}, but phrased/structured differently (expected depth ${i.prodDepth}; match ${i.similarityPct}%) — "${p}"` + (i.devText ? ` → ${DEV_LABEL}: "${i.devText}"` : ''));
        else if (i.kind === 'present-as-paragraph') lines.push(`  ¶ Present in ${DEV_LABEL} as paragraph/text block, not list item (expected depth ${i.prodDepth}; match ${i.similarityPct}%) — "${p}"` + (i.devText ? ` → ${DEV_LABEL}: "${i.devText}"` : ''));
        else if (i.kind === 'wrong-depth')       lines.push(`  ⤵ Same list item found in ${DEV_LABEL}, but at a different nesting level (${DEV_LABEL}: ${i.devDepth}, expected: ${i.prodDepth}) — "${p}"`);
        else if (i.kind === 'wrong-type')        lines.push(`  ⇄ Same list item found in ${DEV_LABEL}, but list type changed (${i.prodType}→${i.devType}) — "${p}"`);
        else if (i.kind === 'nested-note')       lines.push(`  ⚠ Note nested in list item in ${DEV_LABEL} (sibling in ${B}) — "${p}"`);
        else if (i.kind === 'content-outside-list') lines.push(`  ⚠ Content moved outside the list in ${DEV_LABEL} (inside list item in ${B}) — "${p}"`);
        else if (i.kind === 'paragraph-longer-in-dev') lines.push(`  ⚠ ${DEV_LABEL} list item absorbs extra paragraph content — "${p}"`);
      }
    }
  }

  section('TABLES', (prodPage.tables || []).length, (devPage.tables || []).length);
  if (c.tableIssues.length === 0) {
    lines.push(`  [✓] Counts match`);
  } else {
    for (const t of c.tableIssues) {
      const h = t.headerText.length > 60 ? t.headerText.slice(0, 57) + '…' : t.headerText;
      if (t.kind === 'missing-table')   lines.push(`  ✗ Missing table — "${h}" (${B}: ${t.prodRows}r × ${t.prodCols}c)`);
      else if (t.kind === 'possible-merge') lines.push(`  ⇄ Possible table merge — "${h}" (${B}: ${t.prodRows}r × ${t.prodCols}c; cell content matches ${t.devTableCount} ${DEV_LABEL} tables, likely merged into one in ${B})`);
      else if (t.kind === 'empty-header')   lines.push(`  ⚠ Empty header row in ${DEV_LABEL} not present in ${B} — "${h}" (${B}: ${t.prodRows}r, ${DEV_LABEL}: ${t.devRows}r incl. empty header)`);
      else if (t.kind === 'fewer-rows')     lines.push(`  ⤵ Fewer rows — "${h}" (${B}: ${t.prodRows}, ${DEV_LABEL}: ${t.devRows})`);
      else if (t.kind === 'fewer-cols')     lines.push(`  ⤵ Fewer cols — "${h}" (${B}: ${t.prodCols}, ${DEV_LABEL}: ${t.devCols})`);
      else if (t.kind === 'extra-in-dev')   lines.push(`  ✗ Extra table in ${DEV_LABEL} not in ${B} — "${h}" (${DEV_LABEL}: ${t.devRows}r × ${t.devCols}c)`);
    }
  }

  section('IMAGES', (prodPage.images || []).length, (devPage.images || []).length);
  if (c.missingImages.length === 0) {
    lines.push(`  [✓] Counts match`);
  } else {
    for (const img of c.missingImages) {
      if (img.kind === 'section') lines.push(`  ⚠ ${img.count} image${img.count > 1 ? 's' : ''} missing in ${DEV_LABEL} under section "${img.section}" (${B}: ${img.prodTotal}, ${DEV_LABEL}: ${img.devTotal})`);
      else lines.push(`  ✗ ${img.count} image${img.count > 1 ? 's' : ''} missing from ${DEV_LABEL}`);
    }
  }

  section('ADMONITIONS', (prodPage.admonitions || []).length, (devPage.admonitions || []).length);
  if (c.missingAdmonitions.length === 0 && c.mergedAdmonitions.length === 0) {
    lines.push(`  [✓] Counts match`);
  } else {
    for (const a of c.missingAdmonitions) {
      if (a.structural) {
        const sym = a.devCount > a.prodCount ? '+' : '✗';
        lines.push(`  ${sym} [${a.type}]: ${B} ${a.prodCount}, ${DEV_LABEL} ${a.devCount}`);
      } else {
        lines.push(`  ✗ Missing [${a.type}] "${a.snippet.slice(0, 80)}"`);
      }
    }
    for (const a of c.mergedAdmonitions)  lines.push(`  ¶ Merged [${a.type}] "${a.snippet.slice(0, 80)}" — ${B}: ${a.prodParagraphs}p → ${DEV_LABEL}: ${a.devParagraphs}p`);
  }

  section('CODE BLOCKS', prodPage.codeBlocks || 0, devPage.codeBlocks || 0);
  if ((c.codeIssues || []).length === 0) {
    lines.push(`  [✓] Counts match`);
  } else {
    for (const ci of c.codeIssues) {
      const sym = ci.devCount > ci.prodCount ? '+' : '✗';
      lines.push(`  ${sym} code blocks: ${B} ${ci.prodCount}, ${DEV_LABEL} ${ci.devCount}`);
    }
  }

  section('VIDEO EMBEDS', prodPage.videoEmbeds || 0, devPage.videoEmbeds || 0);
  if ((c.videoIssues || []).length === 0) {
    lines.push(`  [✓] Counts match`);
  } else {
    for (const vi of c.videoIssues) {
      const sym = vi.devCount > vi.prodCount ? '+' : '✗';
      lines.push(`  ${sym} video embeds: ${B} ${vi.prodCount}, ${DEV_LABEL} ${vi.devCount}`);
    }
  }

  const prodSymTotals = Object.values(prodPage.symbolMarks || {}).reduce((a, b) => a + b, 0);
  const devSymTotals  = Object.values(devPage.symbolMarks  || {}).reduce((a, b) => a + b, 0);
  section('SYMBOL MARKS', prodSymTotals, devSymTotals);
  if ((c.symbolIssues || []).length === 0) {
    lines.push(`  [✓] Counts match`);
  } else {
    for (const si of c.symbolIssues) {
      const sym = si.devCount > si.prodCount ? '+' : '✗';
      lines.push(`  ${sym} ${si.symbol}: ${B} ${si.prodCount}, ${DEV_LABEL} ${si.devCount}`);
    }
  }

  lines.push('');
  lines.push('─'.repeat(72));
  lines.push(' MARKUP ARTIFACTS (self-check — not a translation diff)');
  lines.push('─'.repeat(72));
  if ((c.markupIssues || []).length === 0) {
    lines.push(`  [✓] No artifacts found`);
  } else {
    const ARTIFACT_LABEL = { strayBold: '**', strayItalic: '__', strayStrike: '~~', strayPipe: '|' };
    for (const issue of c.markupIssues) {
      if (issue.kind === 'jagged-table') {
        const h = issue.header.length > 50 ? issue.header.slice(0, 47) + '…' : issue.header;
        lines.push(`  ⚠ Jagged table rows in ${issue.side} — "${h}" (${issue.count} row(s) with mismatched cell count — check for a dropped "|")`);
      } else {
        const sym = ARTIFACT_LABEL[issue.kind] || issue.kind;
        lines.push(`  ⚠ Literal "${sym}" found ${issue.count}× in ${issue.side} rendered text — markdown likely failed to parse`);
      }
    }
  }

  if (!STRUCTURAL && (c.differentContent.length > 0 || c.condensedContent.length > 0)) {
    section('CONTENT BLOCKS', prodPage.paragraphs.length, devPage.paragraphs.length);
    for (const p of c.differentContent) {
      const preview = p.text.split(/\s+/).slice(0, 10).join(' ');
      const loc = p.section ? ` [in "${p.section}"]` : '';
      lines.push(`  ✗ Absent — "${preview}…"${loc}`);
    }
    for (const p of c.condensedContent) {
      const preview = p.text.split(/\s+/).slice(0, 10).join(' ');
      const loc = p.section ? ` [in "${p.section}"]` : '';
      lines.push(`  ⤵ Condensed — "${preview}…"${loc}`);
    }
  }

  return lines;
}

function renderReportText(report, prodPages, devPages) {
  const lines = [];
  const B = BASELINE_LABEL;
  const { missingInDev, extraInDev, pagesWithIssues, prodTotal, devTotal } = report;
  const pageCompleteness = prodTotal > 0 ? Math.round((devTotal / prodTotal) * 100) : 100;

  // ── Header ────────────────────────────────────────────────────────────────
  lines.push('═'.repeat(72));
  lines.push(' COMPARISON REPORT');
  lines.push('═'.repeat(72));
  lines.push(`  ${DEV_LABEL} pages${' '.repeat(Math.max(1, 11 - DEV_LABEL.length))}: ${devTotal} / ${prodTotal} in ${B}  (${pageCompleteness}% page coverage)`);
  lines.push(`  Compared (common) : ${report.common.length}`);
  lines.push(`  Missing from ${DEV_LABEL}${' '.repeat(Math.max(1, 4 - DEV_LABEL.length))}: ${report.missingInDev.length}`);
  lines.push(`  Extra in ${DEV_LABEL}${' '.repeat(Math.max(1, 7 - DEV_LABEL.length))}: ${report.extraInDev.length}`);
  lines.push(`  Pages with issues : ${pagesWithIssues.length}`);

  // ── Missing / extra pages ─────────────────────────────────────────────────
  lines.push('');
  lines.push('─'.repeat(72));
  lines.push(` MISSING PAGES (present in ${B}, absent from ${DEV_LABEL})`);
  lines.push('─'.repeat(72));
  if (missingInDev.length === 0) {
    lines.push(`  [OK] ${DEV_LABEL} contains all ${B} pages.`);
  } else {
    for (const p of missingInDev) {
      const prodPath = prodPages.get(p).path || p;
      const devPathHypothetical = rewriteLocaleInPath(prodPath, BASELINE_LOCALE, LOCALE);
      lines.push(`  ✗  ${prodPages.get(p).label}`);
      lines.push(`     ${DEV_LABEL} (missing): ${toUrl(DEV_BASE, devPathHypothetical)}`);
      lines.push(`     ${B}:          ${prodPages.get(p).url}`);
    }
  }

  if (extraInDev.length > 0) {
    lines.push('');
    lines.push('─'.repeat(72));
    lines.push(` EXTRA PAGES IN ${DEV_LABEL.toUpperCase()} (new/unreleased content not yet in ${B})`);
    lines.push('─'.repeat(72));
    for (const p of extraInDev) {
      lines.push(`  +  ${devPages.get(p).label}`);
      lines.push(`     ${DEV_LABEL}:  ${devPages.get(p).url}`);
    }
  }

  // ── Pages not yet published on baseline ──────────────────────────────────
  if ((report.baselineEmpty || []).length > 0) {
    lines.push('');
    lines.push('─'.repeat(72));
    lines.push(` PAGES NOT YET PUBLISHED ON ${B.toUpperCase()} (route exists, content empty — excluded from comparison)`);
    lines.push('─'.repeat(72));
    for (const p of report.baselineEmpty) {
      lines.push(`  ⚠  ${devPages.get(p).label}`);
      lines.push(`     ${DEV_LABEL}:  ${devPages.get(p).url}`);
      lines.push(`     ${B}: ${prodPages.get(p).url}`);
    }
  }

  // ── Content type summary ──────────────────────────────────────────────────
  lines.push('');
  lines.push('─'.repeat(72));
  lines.push(' CONTENT TYPE SUMMARY');
  lines.push('─'.repeat(72));
  for (const type of TYPE_ORDER) {
    const n     = report.typeIssues[type].length;
    const label = TYPE_LABELS[type].padEnd(TYPE_LABEL_PAD);
    if (n === 0) lines.push(`  ${label}  [OK]`);
    else         lines.push(`  ${label}  ✗  ${n} / ${report.common.length} page${n > 1 ? 's' : ''} with issues`);
  }

  // ── Issues by content type ────────────────────────────────────────────────
  lines.push('');
  lines.push('─'.repeat(72));
  lines.push(' ISSUES BY CONTENT TYPE');
  lines.push('─'.repeat(72));

  const hasAnyIssues = TYPE_ORDER.some(t => report.typeIssues[t].length > 0);
  if (!hasAnyIssues) {
    lines.push('  [OK] No content issues found in any matching pages.');
  } else {
    for (const type of TYPE_ORDER) {
      const affected = report.typeIssues[type];
      if (affected.length === 0) continue;
      lines.push('');
      lines.push(`  ${TYPE_LABELS[type].toUpperCase()} — ${affected.length} page${affected.length > 1 ? 's' : ''} with issues`);
      lines.push('  ' + '─'.repeat(68));
      for (const c of affected) {
        lines.push('');
        lines.push(`    ${c.label}`);
        for (const { text } of typeIssueEntries(type, c, prodPages.get(c.path), devPages.get(c.path)))
          lines.push(text);
      }
    }
  }

  // ── Image counts — all pages ──────────────────────────────────────────────
  lines.push('');
  lines.push('─'.repeat(72));
  lines.push(' IMAGE COUNTS — ALL PAGES');
  lines.push('─'.repeat(72));
  for (const p of report.common) {
    const prod      = prodPages.get(p);
    const dev       = devPages.get(p);
    const prodCount = (prod.images || []).length;
    const devCount  = (dev.images  || []).length;
    const label     = (prod.label || p.split('/').pop()).slice(0, 45).padEnd(45);
    if (prodCount === devCount) lines.push(`  [OK] ${label}  ${B}: ${prodCount}   ${DEV_LABEL}: ${devCount}`);
    else                        lines.push(`  X   ${label}  ${B}: ${prodCount}   ${DEV_LABEL}: ${devCount}`);
  }

  // ── Affected pages — URL reference ────────────────────────────────────────
  const affectedPaths = new Set();
  for (const type of TYPE_ORDER) for (const c of report.typeIssues[type]) affectedPaths.add(c.path);
  const hasRef = affectedPaths.size > 0 || report.missingInDev.length > 0;
  if (hasRef) {
    lines.push('');
    lines.push('─'.repeat(72));
    lines.push(' AFFECTED PAGES — URL REFERENCE');
    lines.push('─'.repeat(72));
    for (const path of report.common.filter(p => affectedPaths.has(p))) {
      const c = report.pageComparisons.find(x => x.path === path);
      if (!c) continue;
      lines.push('');
      lines.push(`  ${c.label}`);
      lines.push(`    ${DEV_LABEL}:  ${c.devUrl}`);
      lines.push(`    ${B}: ${c.prodUrl}`);
    }
    for (const p of report.missingInDev) {
      const prodPath = prodPages.get(p).path || p;
      const devPathHypothetical = rewriteLocaleInPath(prodPath, BASELINE_LOCALE, LOCALE);
      lines.push('');
      lines.push(`  ${prodPages.get(p).label}  [missing from ${DEV_LABEL}]`);
      lines.push(`    ${DEV_LABEL}:  ${toUrl(DEV_BASE, devPathHypothetical)}`);
      lines.push(`    ${B}: ${prodPages.get(p).url}`);
    }
  }

  lines.push('');
  lines.push('═'.repeat(72));
  return lines.join('\n') + '\n';
}

function toAsciiReportText(text) {
  return text
    .replace(/═/g, '=')
    .replace(/─/g, '-')
    .replace(/✗/g, 'X')
    .replace(/⇄/g, '~')
    .replace(/⤵/g, '>')
    .replace(/⚠/g, '!')
    .replace(/\[✓\]/g, '[OK]')
    .replace(/[—–]/g, '-')
    .replace(/â€"/g, '-')
    .replace(/→/g, '->')
    .replace(/…/g, '...')
    .replace(/¶/g, 'P');
}

// Splits off the extension so a multi-locale run can suffix each report
// filename with its locale instead of every locale overwriting one file.
function outputFileForLocale(locale, multiple) {
  if (!RESOLVED_OUTPUT_FILE) return null;
  if (!multiple) return RESOLVED_OUTPUT_FILE;
  const m = RESOLVED_OUTPUT_FILE.match(/^(.*?)(\.[^./\\]+)?$/);
  return `${m[1]}-${locale}${m[2] || ''}`;
}

// ─── Main ─────────────────────────────────────────────────────────────────────
async function main() {
  log('\n' + '═'.repeat(72));
  log(' UiPath Docs Localized Comparison Tool');
  log('═'.repeat(72));

  await promptInputs();
  if (PAGE_END === null) PAGE_END = Infinity;
  refreshLabels();

  const batchLabel = PAGE_END === Infinity && PAGE_START === 0
    ? 'all'
    : `${PAGE_START + 1}–${PAGE_END === Infinity ? 'end' : PAGE_END}`;
  log(`  Path     : ${GUIDE_PATH}`);
  log(`  Pages    : ${batchLabel}`);
  log(`  Locale   : ${LOCALES.length ? LOCALES.join(', ') : '(none — set --locale to inject language preference)'}${LOCALES.length > 1 ? '  (baseline crawled once, reused across all locales)' : ''}`);
  log(`  Baseline : ${BASELINE_LOCALE}  (${CROSS_LOCALE ? 'cross-locale: dev/[locale] vs baseline /' + BASELINE_LOCALE + '/' : 'same-locale legacy mode'})`);
  if (LOCALE) log(`  Key      : ${LOCALE_KEY}`);
  log(`  Mode     : ${STRUCTURAL ? 'structural (count-based, no text matching)  —  use --text to enable text comparison' : 'text (full text matching)'}`);
  log(`  ${DEV_LABEL}${' '.repeat(Math.max(1, 7 - DEV_LABEL.length))}: ${DEV_BASE}`);
  log(`  ${BASELINE_LABEL}${' '.repeat(Math.max(1, 7 - BASELINE_LABEL.length))}: ${PROD_BASE}`);
  log('─'.repeat(72) + '\n');

  if (!LOCALE) {
    warn('  No --locale flag provided. If the site redirects based on stored language');
    warn('  preference, results may reflect the wrong language. Use --locale [fr|de|ja|es|pt-br|zh-cn].');
    warn('  Add --debug to inspect localStorage keys on the target origin.\n');
  }
  const unknownLocales = LOCALES.filter(l => !KNOWN_LOCALES.has(l));
  if (unknownLocales.length) {
    warn(`  Unrecognized locale code(s): ${unknownLocales.join(', ')} — known: ${[...KNOWN_LOCALES].join(', ')}.`);
    warn('  Proceeding anyway, but double-check for a typo before a long crawl.\n');
  }

  let sessionState = loadSession(DEV_HOST);
  if (sessionState) ok('  Loaded Cloudflare session from auth-session.json');
  else warn('  No valid session — browser will open for manual login.');

  let { browser, context, headless } = await createBrowser(sessionState);

  // ── Single-page mode ──────────────────────────────────────────────────────
  if (PAGE_SINGLE) {
    const baselinePagePath = rewriteLocaleInPath(PAGE_SINGLE, LOCALE, BASELINE_LOCALE);
    log(`\n[Single page] ${PAGE_SINGLE}`);
    if (CROSS_LOCALE) log(`              baseline: ${baselinePagePath}`);
    log(`[1/2] Fetching ${BASELINE_LABEL} page…`);
    const prodPage = await crawlSinglePage(context, baselinePagePath, false, false);

    log(`[2/2] Fetching ${DEV_LABEL} page…`);
    let devPage = await crawlSinglePage(context, PAGE_SINGLE, true, headless);
    if (devPage === null) {
      log('\n  Relaunching browser for re-authentication…');
      await browser.close();
      invalidateSession();
      ({ browser, context, headless } = await createBrowser(null));
      devPage = await crawlSinglePage(context, PAGE_SINGLE, true, false);
    }

    await browser.close();
    if (!devPage) { err(`\nCould not retrieve ${DEV_LABEL} page.`); process.exit(1); }
    const c = {
      path: PAGE_SINGLE,
      label: prodPage.label,
      prodUrl: prodPage.url,
      devUrl:  devPage.url,
      prodWordCount: prodPage.wordCount,
      devWordCount:  devPage.wordCount,
      ...comparePage(prodPage, devPage),
    };
    printSinglePage(prodPage, devPage, PAGE_SINGLE);
    if (RESOLVED_OUTPUT_FILE) {
      const singlePageText = toAsciiReportText([
        '═'.repeat(72),
        ' SINGLE PAGE REPORT',
        '═'.repeat(72),
        ...pageDetailLines(c, prodPage, devPage),
        '',
        '═'.repeat(72),
        '',
      ].join('\n'));
      fs.writeFileSync(RESOLVED_OUTPUT_FILE, singlePageText, 'utf8');
      ok(`  Report saved → ${RESOLVED_OUTPUT_FILE}`);
    }
    return;
  }

  // ── Baseline crawl (once — reused for every locale below) ────────────────
  const multi = LOCALES.length > 1;
  const baselineGuidePath = rewriteLocaleInPath(GUIDE_PATH, LOCALE, BASELINE_LOCALE);
  log(`\n[1/${LOCALES.length + 1}] Crawling ${BASELINE_LABEL}…`);
  if (CROSS_LOCALE) log(`  Baseline path: ${baselineGuidePath}`);
  let prodPages = await crawlSite(context, toUrl(PROD_BASE, baselineGuidePath), false, headless);

  if (prodPages === null) {
    log('\n  Relaunching browser in visible mode for re-authentication…');
    await browser.close();
    invalidateSession();
    ({ browser, context, headless } = await createBrowser(null));
    prodPages = await crawlSite(context, toUrl(PROD_BASE, baselineGuidePath), false, false);
  }

  if (!prodPages || prodPages.size === 0) {
    err(`\nCould not retrieve ${BASELINE_LABEL} pages. Check authentication and try again.`);
    process.exit(1);
  }

  // ── Dev crawl — once per locale, baseline held fixed ─────────────────────
  let anySucceeded = false;
  for (let i = 0; i < LOCALES.length; i++) {
    const locale = LOCALES[i];
    const devGuidePath = rewriteLocaleInPath(GUIDE_PATH, LOCALE, locale);
    const devLabel = locale.toUpperCase();
    log(`\n[${i + 2}/${LOCALES.length + 1}] Crawling ${devLabel}…`);
    if (multi) log(`  Path: ${devGuidePath}`);

    let devPages = await crawlSite(context, toUrl(DEV_BASE, devGuidePath), true, headless, locale);

    if (devPages === null) {
      log('\n  Relaunching browser in visible mode for re-authentication…');
      await browser.close();
      invalidateSession();
      ({ browser, context, headless } = await createBrowser(null));
      devPages = await crawlSite(context, toUrl(DEV_BASE, devGuidePath), true, false, locale);
    }

    if (!devPages || devPages.size === 0) {
      err(`\nCould not retrieve ${devLabel} pages. Check authentication and try again.`);
      continue; // keep going — one bad locale shouldn't abort the rest of the batch
    }
    anySucceeded = true;

    DEV_LABEL = devLabel; // buildReport/printReport/renderReportText read this global
    log('\nBuilding report…');
    const report = buildReport(prodPages, devPages);
    printReport(report, prodPages, devPages);

    const outFile = outputFileForLocale(locale, multi);
    if (outFile) {
      fs.writeFileSync(outFile, toAsciiReportText(renderReportText(report, prodPages, devPages)), 'utf8');
      ok(`  Report saved → ${outFile}`);
    }
  }

  await browser.close();

  if (!anySucceeded) {
    err('\nCould not retrieve dev pages for any requested locale.');
    process.exit(1);
  }
}

main().catch(e => { err('\nFatal: ' + e.message); process.exit(1); });
