---
title: "Known limitations"
visible: true
slug: "known-limitations"
---

App projects in Studio Web present certain limitations.

When designing an app:

1. Apps cannot be generated using Autopilot from a Data Service entity.
2. Apps cannot be opened in Studio Desktop.
3. Apps do not support [page export and import](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/export-and-import-app-pages).
4. Apps do not use the Query Builder. Instead, you must add a **Query Entity Record** automation to your workflow.
5. Apps do not support entity choice sets and the `GetChoiceSet` and `GetChoiceSetValue` functions.Do not support the `Fetch` and `FetchOne` functions. Instead, you must add a **Query Entity Record** automation to your workflow.

When deploying an app project:

1. Apps cannot be published to a personal workspace or to folder feeds. Instead, you publish at the tenant level.
2. Apps cannot be imported and exported as packages in Orchestrator. You can instead import and export them as Solutions.
3. Apps cannot currently be deployed as Public Apps. This is a temporary limitation which will be removed in an upcoming release.