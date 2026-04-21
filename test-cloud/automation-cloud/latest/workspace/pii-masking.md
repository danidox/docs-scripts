---
title: "PII masking"
visible: true
slug: "pii-masking"
---

## About PII in-flight masking

PII in-flight masking enhances the AI Trust Layer by ensuring that personally identifiable information (PII) is pseudonymized before reaching Large Language Models (LLMs) used in generative AI features. By intercepting and masking sensitive entities during runtime, this helps preserve data privacy and support compliance requirements, without interrupting automation flows or degrading LLM performance.

When enabled, PII in-flight masking detects and replaces PII entities with contextual placeholders (e.g., `person_1`, `email_1`) prior to transmission. Once the LLM returns a response, the system automatically rehydrates the original PII into the output, ensuring a seamless experience for users and downstream systems.

PII in-flight masking is currently supported in:

* Autonomous agents: Input routed through LLMs during agent execution.
* Gen AI Activities: Rewrite Text, Summarize, Semantic Matching activities.

## How it works

PII in-flight masking is a four-step process that ensures sensitive data is never exposed to the LLM during processing:

1. **Detection** – The system scans user input and identifies personally identifiable information (PII) using language-specific entity recognition models.
2. **Pseudonymization** – Detected PII entities are replaced with anonymized, context-aware placeholders (e.g., `John Doe` → `person_1`, `123-456-7890` → `phone_1`). This allows the LLM to process the input safely, without accessing real PII.
3. **LLM interaction** – The masked prompt is sent to the LLM. Since no actual PII is included, this step preserves privacy while still enabling accurate and useful responses.
4. **Rehydration** – After the LLM returns a response, the system automatically substitutes each placeholder with the original PII. This ensures the final output retains full context and accuracy, with no loss of information.

Example transformation:

* Input: "Call John Doe at 123-456-7890."
* Sent to LLM: "Call person_1 at phone_1."
* Output: "Calling John Doe at 123-456-7890."
:::note
PII masking uses Microsoft Azure Cognitive Service for detection, and no customer data is stored during processing.
:::

## Licensing

PII in-flight masking is available on the following licensing plans:

* Flex Pricing plan: Enterprise – Standard and Advanced tiers.
* Unified Pricing plan: Standard, Enterprise, App Test Platform Standard, App Test Platform Enterprise.
:::important
If you enable PII in-flight masking without an eligible tier entitlement, your agents will fail. The entitlement enforcement mechanism blocks data processing, leading to failures and workflow interruptions. This behavior is intentional — it prevents you from assuming that PII masking is active when, in reality, sensitive data might still be sent to language models. To avoid disruptions, ensure your organization is on a supported tier before enabling PII in-flight masking.
:::

## Limitations

To maintain service stability and ensure consistent performance, each tenant is limited to 200 LLM requests with PII per minute. This helps prevent excessive traffic from affecting overall service availability.

If a tenant exceeds this threshold, additional requests will be temporarily throttled and will receive a HTTP 429 ("PII Masking rate limits exceeded. Please try again later”) response. The limit automatically resets after one minute, allowing requests to resume once usage is within the allowed rate.

## Enabling PII in-flight masking

To enable PII masking, follow these steps:

1. Navigate to **Admin > AI Trust Layer > AI Governance > Add Policy**.
2. Create a new AI Trust Layer policy or edit an existing one.
3. By default, PII in-flight masking is disabled for both UiPath Gen AI activities and Agents. You must explicitly enable it for one or both product types using the dedicated toggles:
   * Enable PII Masking for Agents
   * Enable PII Masking for UiPath Gen AI activities
4. Once enabled, the list of supported PII entities becomes visible in the configuration panel. Masking is applied only to the entities you explicitly configure.
5. For each entity, you can:
   * Choose the PII category (e.g., `USSocialSecurityNumber`, `URL`, `IPAddress`, etc.).
   * Enable or disable masking for that entity.
   * Set a confidence threshold for detection. Only data detected above this threshold will be masked. The default confidence threshold is set to 0.5. Changing this threshold affects the detection behavior as follows:
     + Increase threshold: Detection is more selective. It is less likely to mistakenly identify non-sensitive data as PII, but may overlook some valid entities.
     + Decrease threshold: Detection is more permissive. It identifies more potential PII, but may also include content that is not actually sensitive.
6. Save your configuration after editing each entity. You can adjust or remove entities individually.
7. Scope the policy by tenant, group, or user, depending on how broadly or narrowly you want the masking rules to apply.

## Supported entities

The following table lists the PII entity types currently supported, along with the languages in which detection and pseudonymization are available.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-A83B3E13-CECB-4238-A52A-F6B606B1A6F3__TABLE_GQC_SQ1_JGC" summary="">
 <caption>
  Table 1. Supported entities with language
                           code
 </caption>
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Category
   </th>
   <th>
    Entity
   </th>
   <th>
    Languages
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d124079e228" rowspan="8">
    General
   </td>
   <td headers="d124079e231">
    Date
    <p>
     Can be used in for birth date, admission date, discharge or date of
                                 death.
    </p>
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, af, ca, da, el,
                              ga, gl, ku, nl, no, ss, ro, sq, ur, ar, bg, bs, cy, fa, hr, id, mg, mk, ms, ps,
                              ru, sl, so, sr, sw, am, as, cs, et, eu, fi, he, hu, km, lo, lt, lv, mr, my, ne,
                              or, pa, pl, sk, th, uk, az, bn, gu, hy, ka, kk, kn, ky, ml, mn, ta, te, ug, uz,
                              vi
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    Phone number
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, zh-hans, ja, ko, pt-pt pt-br
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    EU GPS coordinates
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, da, nl, no, ro,
                              ar, bg, hr, ms, ru, sl, cs, et, fi, he, hu, lv, sk, th, uk
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    Email
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, zh, ja, ko, pt-pt, pt-br, nl, sv, tr, hi
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    Person
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, af, ca, da, el,
                              ga, gl, ku, nl, no, ss, ro, sq, ur, ar, bg, bs, cy, fa, hr, id, mg, mk, ms, ps,
                              ru, sl, so, sr, sw, am, as, cs, et, eu, fi, he, hu, km, lo, lt, lv, mr, my, ne,
                              or, pa, pl, sk, th, uk, az, bn, gu, hy, ka, kk, kn, ky, ml, mn, ta, te, ug, uz,
                              vi
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    Address
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, af, ca, da, el,
                              ga, gl, ku, nl, no, ss, ro, sq, ur, ar, bg, bs, cy, fa, hr, id, mg, mk, ms, ps,
                              ru, sl, so, sr, sw, am, as, cs, et, eu, fi, he, hu, km, lo, lt, lv, mr, my, ne,
                              or, pa, pl, sk, th, uk, az, bn, gu, hy, ka, kk, kn, ky, ml, mn, ta, te, ug, uz,
                              vi
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    URL
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, zh, ja, ko, pt-pt, pt-br, nl, sv, tr, hi
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    IP address
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, zh, ja, ko, pt-pt, pt-br, nl, sv, tr, hi
   </td>
  </tr>
  <tr>
   <td headers="d124079e228" rowspan="4">
    Financial information
   </td>
   <td headers="d124079e231">
    IBAN
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, af, ca, da, el,
                              ga, gl, ku, nl, no, ss, ro, sq, ur, ar, bg, bs, cy, fa, hr, id, mg, mk, ms, ps,
                              ru, sl, so, sr, sw, am, as, cs, et, eu, fi, he, hu, km, lo, lt, lv, mr, my, ne,
                              or, pa, pl, sk, th, uk, az, bn, gu, hy, ka, kk, kn, ky, ml, mn, ta, te, ug, uz,
                              vi
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    Credit card numbers
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, af, ca, da, el,
                              ga, gl, ku, nl, no, ss, ro, sq, ur, ar, bg, bs, cy, fa, hr, id, mg, mk, ms, ps,
                              ru, sl, so, sr, sw, am, as, cs, et, eu, fi, he, hu, km, lo, lt, lv, mr, my, ne,
                              or, pa, pl, sk, th, uk, az, bn, gu, hy, ka, kk, kn, ky, ml, mn, ta, te, ug, uz,
                              vi
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    ABA routing number
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, af, ca, da, el,
                              ga, gl, ku, nl, no, ss, ro, sq, ur, ar, bg, bs, cy, fa, hr, id, mg, mk, ms, ps,
                              ru, sl, so, sr, sw, am, as, cs, et, eu, fi, he, hu, km, lo, lt, lv, mr, my, ne,
                              or, pa, pl, sk, th, uk, az, bn, gu, hy, ka, kk, kn, ky, ml, mn, ta, te, ug, uz,
                              vi
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    Swift code
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, af, ca, da, el,
                              ga, gl, ku, nl, no, ss, ro, sq, ur, ar, bg, bs, cy, fa, hr, id, mg, mk, ms, ps,
                              ru, sl, so, sr, sw, am, as, cs, et, eu, fi, he, hu, km, lo, lt, lv, mr, my, ne,
                              or, pa, pl, sk, th, uk, az, bn, gu, hy, ka, kk, kn, ky, ml, mn, ta, te, ug, uz,
                              vi
   </td>
  </tr>
  <tr>
   <td headers="d124079e228" rowspan="7">
    Country-specific
   </td>
   <td headers="d124079e231">
    U.S. Bank Account Number
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, da, nl, no, ro,
                              ar, bg, hr, ms, ru, sl, cs, et, fi, he, hu, lv, sk, th, uk
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    U.S. Social Security Number (SSN)
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, da, nl, no, ro,
                              ar, bg, hr, ms, ru, sl, cs, et, fi, he, hu, lv, sk, th, uk
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    U.S. Driver's License Number
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, da, nl, no, ro,
                              ar, bg, hr, ms, ru, sl, cs, et, fi, he, hu, lv, sk, th, uk
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    U.S. or U.K. Passport Number
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, da, nl, no, ro,
                              ar, bg, hr, ms, ru, sl, cs, et, fi, he, hu, lv, sk, th, uk
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    U.S. Individual Taxpayer Identification Number (ITIN)
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, da, nl, no, ro,
                              ar, bg, hr, ms, ru, sl, cs, et, fi, he, hu, lv, sk, th, uk
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    U.K. Driver's License Number
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, da, nl, no, ro,
                              ar, bg, hr, ms, ru, sl, cs, et, fi, he, hu, lv, sk, th, uk
   </td>
  </tr>
  <tr>
   <td headers="d124079e231">
    U.K. Unique Taxpayer Reference Number
   </td>
   <td headers="d124079e234">
    en, es, fr, de, it, pt-pt, pt-br, zh, ja, ko, nl, sv, tr, hi, da, nl, no, ro,
                              ar, bg, hr, ms, ru, sl, cs, et, fi, he, hu, lv, sk, th, uk
   </td>
  </tr>
 </tbody>
</table>