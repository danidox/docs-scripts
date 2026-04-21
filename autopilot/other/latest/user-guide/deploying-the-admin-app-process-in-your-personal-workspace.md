---
title: "Deploying the Admin App process"
visible: true
slug: "deploying-the-admin-app-process-in-your-personal-workspace"
---

Prior to installing the Admin App, you need to deploy the corresponding process in a shared folder in Orchestrator.

To do that:

1. Navigate to the shared folder in Orchestrator where you want to deploy the process for the Admin App. Make sure users who need to use the Admin App have access to this folder.
2. Switch to the **Automations** > **Processes** tab, and select **Add process**.
3. In the new window, for the **Package Source Name**, select **Click to add file or drop package file here:**
   1. Browse for the `AFE_AutopilotAdminAppProcess_CitizenDeveloper.nupkg` file, then select **Submit**.
   2. Select the previously uploaded package in the **Package Source Name** field.
4. Select **Next** and, optionally, configure the process as you need.
5. To deploy the process, select **Create.**