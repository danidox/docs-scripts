---
title: "Flex licensing"
visible: true
slug: "flex-licensing"
---

Autopilot activities are measured and licensed through Autopilot actions. One such action is counted from the time you click a button or write a prompt, up until the time you receive a result from that click or prompt. An example of an action is **Generate tests** in Test Manager, **Generate code** in Studio Desktop, or a successful paste in Clipboard AI.


:::important
Make sure that the **User License Management** option is enabled in your organization settings. Find out more about [user license management](https://docs.uipath.com/overview/other/latest/overview/license-management-options#user-license-management).
:::

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p><strong>Autopilot service</strong></p> </th>
   <th> <p><strong>License</strong></p> </th>
   <th> <p><strong>Licensing plan</strong></p> </th>
   <th> <p><strong>Entitlements</strong></p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td rowspan="8"> <p> Autopilot for Everyone <sup> 2 </sup></p> </td>
   <td rowspan="2"> <p> Attended - Named User </p> </td>
   <td> <p> Community/Free </p> </td>
   <td> <p> Not available </p> </td>
  </tr>
  <tr>
   <td> <p> Pro Trial/Enterprise </p> </td>
   <td> <p> 50 Autopilot actions/user/year <sup> 1 </sup> , with a limit of 6 actions/user/minute </p> </td>
  </tr>
  <tr>
   <td rowspan="2"> <p> Citizen Developer - Named User </p> </td>
   <td> <p> Community/Free </p> </td>
   <td> <p> Not available </p> </td>
  </tr>
  <tr>
   <td> <p> Pro Trial/Enterprise </p> </td>
   <td> 50 Autopilot actions/user/year <sup> 1 </sup> , with a limit of 6 actions/user/minute </td>
  </tr>
  <tr>
   <td rowspan="2"> <p> Automation Developer - Named User </p> </td>
   <td> <p> Community/Free </p> </td>
   <td> <p> Not available </p> </td>
  </tr>
  <tr>
   <td> Pro Trial/Enterprise </td>
   <td> 50 Autopilot actions/user/year <sup> 1 </sup> , with a limit of 6 actions/user/minute </td>
  </tr>
  <tr>
   <td rowspan="2"> <p> Autopilot Express - Named User </p> </td>
   <td> <p> Community </p> </td>
   <td> <p> Not available </p> </td>
  </tr>
  <tr>
   <td> <p> Free/Pro Trial/Pro/Enterprise </p> </td>
   <td> <p> 50 Autopilot actions/user/year <sup> 1 </sup> , with a maximum of 6 actions/user/minute. </p><p> Limited to only running the following: </p>
      <ul>
        <li> <p> Personal workspace automations </p> </li>
        <li> <p> Out-of-the-box automations for personal productivity, cross-team collaboration, project and task management, and customer relationships management </p> </li>
      </ul>
</td>
  </tr>
  <tr>
   <td rowspan="4"> <p> Generating automations with Autopilot in Studio, Studio Web, Apps </p> </td>
   <td rowspan="2"> <p> Citizen Developer - Named User </p> </td>
   <td> <p> Community/Free </p> </td>
   <td> <p> 5 Autopilot actions/user/day </p> </td>
  </tr>
  <tr>
   <td> <p> Pro Trial/Enterprise </p> </td>
   <td> <p> Unlimited </p> </td>
  </tr>
  <tr>
   <td rowspan="2"> <p> Automation Developer - Named User </p> </td>
   <td> <p> Community/Free </p> </td>
   <td> <p> 5 Autopilot actions/user/day </p> </td>
  </tr>
  <tr>
   <td> <p> Pro Trial/Enterprise </p> </td>
   <td> <p> Unlimited </p> </td>
  </tr>
  <tr>
   <td rowspan="4"> <p> Generating tests with Autopilot in Test Manager, Studio </p> </td>
   <td rowspan="2"> <p> Automation Developer - Named User </p> </td>
   <td> <p> Community/Free </p> </td>
   <td> <p> 5 Autopilot actions/user/day </p> </td>
  </tr>
  <tr>
   <td> <p> Pro Trial/Enterprise </p> </td>
   <td> <p> Unlimited </p> </td>
  </tr>
  <tr>
   <td rowspan="2"> <p> Tester - Named User </p> </td>
   <td> <p> Community/Free </p> </td>
   <td> <p> Not available </p> </td>
  </tr>
  <tr>
   <td> <p> Pro Trial/Enterprise </p> </td>
   <td> <p> Unlimited </p> </td>
  </tr>
 </tbody>
</table>

<sup>1</sup> Allows overages. These will soon be tracked as AI units in the dedicated [Insights dashboard](https://docs.uipath.com/insights/automation-cloud/latest/user-guide/autopilot-usage).

<sup>2</sup> For Autopilot for Everyone, the following limitations apply:

* **Personal Workspace**—Automations created by users
* **Autopilot**—Automations installed and deployed with the Autopilot for Everyone installation
* **Tool Automations** and subfolders—Out-of-the-box automations deployed by Autopilot for Everyone administrators


:::important
If you, as an administrator, previously deployed out-of-the-box automations from the Marketplace solution, we recommend:
* reinstalling the out-of-the-box automation bundles from the Autopilot for Everyone Admin experience, and
* removing any manually deployed out-of-the-box automations.
:::

## Autopilot actions

Autopilot activities are measured and licensed through Autopilot actions. One such action is counted for every:

* Prompt (**Generate tests** in Test Manager, **Generate code** in Studio, user prompt in Autopilot for Everyone chat)
* Successful Clipboard AI paste (for Autopilot for Everyone)

## AI units consumption for Autopilot for Everyone

Each Autopilot for Everyone action consumes one AI unit. This consumption begins after all included action entitlements are used.