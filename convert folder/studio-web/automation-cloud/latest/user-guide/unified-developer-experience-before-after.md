---
title: "From projects to solutions: before and after"
visible: true
slug: "unified-developer-experience-before-after"
---

This page compares the former development and deployment model using **projects** with the new unified **solutions** experience in UiPath®. You can check the key differences in design, packaging, deployment, and management across the development lifecycle.

## Design time

In **Studio Web**, any newly created project is automatically part of a **Solution**.

In **Studio Desktop**, developers can open and work on existing solutions and their contained RPA automations, but can still create standalone projects.

## Packaging

Expand Table

Table 1. Packaging differences

| Concept | Build and deploy projects | Build and deploy solution |
| --- | --- | --- |
| Packaging (produced by the **Publish** button in Studio Web | Produces a `nupkg` file containing one project. | Produces a `.zip` Solution Package containing multiple projects, their resource definitions, and deployment configuration. |
| Deployment | You create a project from a package using the **Add Process** button in Orchestrator. ![Screenshot of the Add Process button.](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614652) | You deploy a solution from a solution package via Tenant &gt; Solutions &gt; Packages. ![Screenshot of the Deploy button.](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614670) |
| Folders | Processes are added to folders. ![Screenshot of processes in folders.](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614662) | Solutions are deployed to solution folders, and all resources from that solution are automatically included. ![Screenshot of the Solutions folder.](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614677) |
| Package Requirement Resolution (Bindings) | Performed from the **Package Requirements** tab in Orchestrator. ![Screenshot of the Package Requirements tab](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614666) | For the moment, this can only be done via the **Package Requirements** tab in Orchestrator. ![Screenshot of the Package Requirements tab](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614666) |

## Publishing and deployment

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-13C618F1-F457-4F41-8C70-D8DE105030A9__TABLE_HQK_1MW_CHC" summary="">
 <caption>
  Table 2. Publishing and deployment
                        differences
 </caption>
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Deployed packages in Orchestrator
   </th>
   <th>
    Deployed solutions in Orchestrator
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d3683e230">
    Project logs, jobs, requirements, and upgrades are managed from
                           the folder where the project is deployed.
   </td>
   <td headers="d3683e233">
    Upgrades are handled from the
    <strong>
     Solutions
    </strong>
    tab. Project logs,
                           jobs, and requirements continue to be accessible from the
    <strong>
     Solution Folder
    </strong>
    .
   </td>
  </tr>
  <tr>
   <td headers="d3683e230">
    How to upgrade a project:
    <ol>
     <li>
      Go to the
                                 project folder.
     </li>
     <li>
      Navigate to
                                 the
      <strong>
       Automations
      </strong>
      tab.
     </li>
     <li>
      Go to the
      <strong>
       Processes
      </strong>
      tab.
     </li>
     <li>
      Choose the
                                 project you want to upgrade and select the
      <strong>
       Upgrade
      </strong>
      icon.
     </li>
     <li>
      Alternatively, you can select the
      <strong>
       More Actions
      </strong>
      button and choose
      <strong>
       Upgrade to latest version
      </strong>
      from the
                                 dropdown.
     </li>
    </ol>
    <br/>
    <button>
     <img alt="Screenshot of the Upgrade processes." src="https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614724"/>
    </button>
    <br/>
   </td>
   <td headers="d3683e233">
    How to upgrade a project:
    <ol>
     <li>
      Go to the
      <strong>
       Tenant
      </strong>
      page.
     </li>
     <li>
      Navigate to
                                 the
      <strong>
       Solutions
      </strong>
      tab.
     </li>
     <li>
      Go to the
      <strong>
       Deployments
      </strong>
      tab.
     </li>
     <li>
      Choose the
                                 solution you want to upgrade and select the
      <strong>
       More
                                    Actions
      </strong>
      icon.
     </li>
     <li>
      Choose
      <strong>
       Upgrade / Downgrade
      </strong>
      from the dropdown.
     </li>
    </ol>
    <br/>
    <button>
     <img alt="Screenshot of upgrading Solutions" src="https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614751"/>
    </button>
    <br/>
   </td>
  </tr>
  <tr>
   <td headers="d3683e230">
    How to view project logs or jobs:
    <ol>
     <li>
      Go to the
                                 project folder.
     </li>
     <li>
      Navigate to
                                 the
      <strong>
       Automations
      </strong>
      tab.
     </li>
     <li>
      Go to the
      <strong>
       Jobs
      </strong>
      tab to view project jobs.
     </li>
     <li>
      Go to the
      <strong>
       Logs
      </strong>
      tab to view project logs.
     </li>
    </ol>
    <br/>
    <button>
     <img alt="Screenshot of the how to view project logs and jobs." src="https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614787"/>
    </button>
    <br/>
   </td>
   <td headers="d3683e233">
    How to view project logs or jobs:
    <ol>
     <li>
      Go to the
                                 solutions folder.
     </li>
     <li>
      Navigate to
                                 the
      <strong>
       Automations
      </strong>
      tab.
     </li>
     <li>
      Go to the
      <strong>
       Jobs
      </strong>
      tab to view project jobs.
     </li>
     <li>
      Go to the
      <strong>
       Logs
      </strong>
      tab to view project logs.
     </li>
    </ol>
    <br/>
    <button>
     <img alt="Screenshot of the how to view solutions logs and jobs." src="https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614793"/>
    </button>
    <br/>
   </td>
  </tr>
 </tbody>
</table>