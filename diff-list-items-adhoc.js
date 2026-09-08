// Ad hoc: dump every <li> (depth + text) for EN vs a target locale on one page, then diff.
// Throwaway script for pinpointing exactly which list item differs when aggregate
// depth-bucket counts disagree. Reuses the same depth/extraction rules as
// compare-docs-localized.js's extractPageData (ancestor UL/OL count for depth,
// flatten inline tags for text, skip li's that are entirely a link) — including
// the 2026-09-07 fix: each li is tagged with selfSkip only, and EN's decision is
// applied positionally to both sides when raw <li> counts match, so this
// diagnostic doesn't show its own stale "kept" counts while pinpointing a
// different real mismatch (see compare-docs-localized.js and project memory).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const SESSION_FILE = path.join(__dirname, 'auth-session.json');
const LOCALE_COOKIE = 'UIPATH_DOCS_LOCALE';

async function extractListItems(page) {
  return await page.evaluate(() => {
    const container = document.querySelector('.theme-doc-markdown.markdown');
    if (!container) return null;
    const clone = container.cloneNode(true);
    const items = [];
    clone.querySelectorAll('li').forEach(li => {
      let depth = 0;
      let node = li.parentElement;
      while (node && node !== clone) {
        if (node.tagName === 'UL' || node.tagName === 'OL') depth++;
        node = node.parentElement;
      }
      const liClone = li.cloneNode(true);
      liClone.querySelectorAll('ul, ol').forEach(n => n.remove());
      liClone.querySelectorAll('a, span, strong, em, b, i, code, td, th, div, p').forEach(el => {
        el.parentNode.insertBefore(document.createTextNode(' '), el);
      });
      const text = liClone.textContent.trim().replace(/\s+/g, ' ');
      const anchors = liClone.querySelectorAll('a');
      const strip = (s) => s.replace(/\s*[.!?:;、。！？：；]+\s*$/u, '');
      const anchorText = strip(anchors[0]?.textContent.trim().replace(/\s+/g, ' ') || '');
      const selfSkip = anchors.length === 1 && anchorText === strip(text);
      items.push({ depth, text: text.slice(0, 80), selfSkip });
    });
    return items;
  });
}

(async () => {
  const [,, enUrl, devUrl, depthArg] = process.argv;
  const targetDepth = depthArg ? parseInt(depthArg, 10) : 2;
  const sessionState = JSON.parse(fs.readFileSync(SESSION_FILE, 'utf8'));
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ ignoreHTTPSErrors: true, storageState: sessionState, viewport: { width: 1920, height: 1080 } });

  const localeMatch = devUrl.match(/docs-dev\.uipath\.com\/([a-z]{2}(-[A-Za-z]{2})?)\//);
  const locale = localeMatch ? localeMatch[1] : null;

  // Explicit 'en' cookie for the EN load — do NOT leave the dev-locale cookie set
  // on the shared context, or it leaks into the EN page too (same context = same cookies).
  await context.addCookies([{ name: LOCALE_COOKIE, value: 'en', domain: 'docs-dev.uipath.com', path: '/' }]);
  const pageEn = await context.newPage();
  await pageEn.goto(enUrl, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await pageEn.waitForSelector('.theme-doc-markdown.markdown', { timeout: 15000 });
  await pageEn.waitForTimeout(1500);
  const enItems = await extractListItems(pageEn);
  await pageEn.close();

  if (locale) {
    await context.addCookies([{ name: LOCALE_COOKIE, value: locale, domain: 'docs-dev.uipath.com', path: '/' }]);
  }
  const pageDev = await context.newPage();
  await pageDev.goto(devUrl, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await pageDev.waitForSelector('.theme-doc-markdown.markdown', { timeout: 15000 });
  await pageDev.waitForTimeout(1500);
  const devItems = await extractListItems(pageDev);
  await pageDev.close();

  await browser.close();

  console.log(`EN raw <li> count: ${enItems.length}, DEV raw <li> count: ${devItems.length}`);

  // Same alignment rule as compare-docs-localized.js's getKeptListItems: when raw
  // counts match, trust positional correspondence and apply EN's selfSkip decision
  // at each index to both sides, so a translation shifting a word across the anchor
  // boundary doesn't look like a phantom mismatch here either. When raw counts
  // differ, fall back to each side's own independent judgment and say so — a
  // raw-count mismatch means positional alignment can't be trusted anyway.
  let enKept, devKept;
  if (enItems.length === devItems.length) {
    enKept = []; devKept = [];
    for (let i = 0; i < enItems.length; i++) {
      if (enItems[i].selfSkip) continue;
      enKept.push(enItems[i]);
      devKept.push(devItems[i]);
    }
    console.log('(raw counts match — EN\'s self-skip decision applied positionally to both sides)');
  } else {
    enKept = enItems.filter(i => !i.selfSkip);
    devKept = devItems.filter(i => !i.selfSkip);
    console.log('(raw counts differ — falling back to each side\'s own independent self-skip judgment)');
  }
  console.log(`EN kept: ${enKept.length}, DEV kept: ${devKept.length}`);

  const enDepth2 = enKept.filter(i => i.depth === targetDepth);
  const devDepth2 = devKept.filter(i => i.depth === targetDepth);
  console.log(`\nEN depth-${targetDepth} kept: ${enDepth2.length}, DEV depth-${targetDepth} kept: ${devDepth2.length}`);
  console.log(`\n--- EN depth-${targetDepth} items ---`);
  enDepth2.forEach((i, idx) => console.log(`${idx + 1}. "${i.text}"`));
  console.log(`\n--- DEV depth-${targetDepth} items ---`);
  devDepth2.forEach((i, idx) => console.log(`${idx + 1}. "${i.text}"`));
})();
