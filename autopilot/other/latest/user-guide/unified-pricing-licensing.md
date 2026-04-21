---
title: "Unified Pricing licensing"
visible: true
slug: "unified-pricing-licensing"
---


:::important
The information on this page applies to you if you opted for the Unified Pricing licensing model. If you are on Flex, refer to [Flex licensing for Autopilot](https://docs.uipath.com/autopilot/other/latest/overview/flex-licensing).
:::


:::important
Make sure that the **User License Management** option is enabled in your organization settings. Find out more about [user license management](https://docs.uipath.com/overview/other/latest/overview/license-management-options#user-license-management).
:::

## Licensing plans

All license plans allow access to Autopilot and Autopilot for Everyone.

| Feature | Community | Basic Trial | Basic | Standard Trial | Standard | Enterprise | Application Test Standard | Application Test Enterprise |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Autopilot | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Autopilot for Everyone | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## User licenses for Autopilot for Everyone

The following table provides details on the user licenses you need to perform various operations with Autopilot for Everyone:

Table 1. Available capabilities based on user licenses

| Feature | Unlicensed | User Express | Basic | Plus | Pro | App Tester | App test Developer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Access to Autopilot for Everyone | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Analyze uploaded files | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Chat with Context Grounding | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Copy and paste with ClipboardAI | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Run Toolset automations | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Run personal automations | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Run shared, or non-Personal Workspace automations | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Autopilot actions

Autopilot activities are measured and licensed through Autopilot actions. One such action is counted for every:

* Prompt (**Generate tests** in Test Manager, **Generate code** in Studio, user prompt in Autopilot for Everyone chat)
* Successful Clipboard AI paste (for Autopilot for Everyone)

<table cellpadding="4" cellspacing="0">
 <caption>
  Table 2. Action entitlements per user licenses
 </caption>
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Feature </p> </th>
   <th> <p> Unlicensed </p> </th>
   <th> <p> Express </p> </th>
   <th> <p> Basic </p> </th>
   <th> <p> Plus </p> </th>
   <th> <p> Pro </p> </th>
   <th> App Tester </th>
   <th> App test Developer </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p> Autopilot for Everyone </p> </td>
   <td> <p> ❌ </p> </td>
   <td colspan="6"> <p> 50 Actions / year (not poolable) </p> </td>
  </tr>
  <tr>
   <td> <p> Autopilot </p> </td>
   <td> <p> ❌ </p> </td>
   <td colspan="6"> <p> Unlimited </p> </td>
  </tr>
 </tbody>
</table>

## Platform units consumption for Autopilot for Everyone

Each Autopilot for Everyone action consumes 0.2 platform units. This consumption begins after all included action entitlements are used.

## Platform units consumption for running Autopilot for Everyone on Serverless robots

Autopilot for Everyone uses Serverless robots to run cross-platform automations. Each user receives a monthly grant of 300 free platform units. When you consume this grant, to continue running automations, Serverless robots draw platform units from the tenant allocated pool.