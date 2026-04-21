---
title: "Troubleshooting"
visible: true
slug: "troubleshooting"
---

## Common installation and configuration errors

### Autopilot folder is missing for selected tenant

You may encounter this error after having Autopilot installed in your tenant. This is because a different user installed Autopilot, therefore you might need access to the Autopilot folder.

Assign yourself to the Autopilot folder in the selected tenant.

### Failed to install Autopilot solution - Network error

You may encounter this error while trying to install Autopilot, even with a stable network connection.

Clear your cache, and retry the installation.

### Autopilot does not install after leaving screen

Autopilot for everyone installation completes in three to five minutes, you need to keep the screen active until it finishes.

### Autopilot installation fails with an error

1. In Orchestrator, go to **Tenant** > **Solutions** > **Deployments**.
2. Delete the Autopilot solution in the draft state.
3. Reattempt to install Autopilot from the AI trust layer tab.

### No robot configured for the current user

Check tenant permissions for the user and ensure that the corresponding **Enable user to run automations** option is selected:

1. In Orchestrator, go to **Tenant** > **Manage Access** > **Assign Roles** > **User**.
2. Select the user.
3. In the **Personal automations setup** tab, select the **Enable user to run automations** option.

### Unable to see the Autopilot tab in Assistant

* Make sure you have a valid user license: Automation Developer, RPA Developer, Citizen Developer, Attended.
* If an Assistant policy is active, open its **Widgets** tab and check for **UiPath.Autopilot.Widget**. To use Autopilot for Everyone, make sure this entry exists and that the **Is enabled** option is set to **Yes**.

### Couldn't install widget

Upgrade your Assistant version to at least 2024.10.5 Enterprise edition.

### ExternalHostShowTimeout error

* Upgrade your Assistant version to at least 2024.10.5 Enterprise edition.
* If an Assistant policy is active, open its **Widgets** tab and check for **UiPath.Autopilot.Widget**. To use Autopilot for Everyone, make sure this entry exists and that the **Is enabled** option is set to **Yes**.

### You need a personal workspace to use Autopilot

Check tenant permissions for the user and ensure that the corresponding **Create a personal workspace for this user and enable optimal Studio Web experience** option is selected:

1. In Orchestrator, go to **Tenant** > **Manage Access** > **Assign Roles** > **User**.
2. Select the user.
3. In the **Personal automations setup** tab, select the **Create a personal workspace for this user and enable optimal Studio Web experience** option.

### Status code 424 - Unable to process uploaded PDF file

* Make sure Document Understanding is enabled for your tenant.
* You must have at least 1 AI unit allocated to your organization before you can enable Document Understanding in any tenant.

### No UiPath automations are available in Autopilot

* Autopilot solution only comes with core processes (Autopilot, FAQ, Google, Wikipedia).
* Download additional toolset automations from Marketplace.

### UiPath automation fails due to invalid connection issue

* Restart Assistant.
* Go to **Integration Service** > **Personal Workspace**:
  + Check the connection to ensure it is valid.
  + Remove the connection, recreate it, then restart Assistant.

### Autopilot tab is stuck on loading screen

Restart the Assistant.

## Autopilot for Everyone FAQ

This section aims to answer the most common questions related to Autopilot for Everyone:

### How do I install UiPath Assistant?

You need UiPath Assistant version 2024.10.5+ to use Autopilot for Everyone. Assistant comes bundled in the UiPath Studio installer.

Download links: [Windows](https://download.uipath.com/UiPathStudioCommunity.msi) | [macOS Intel](https://download.uipath.com/latest/UiPath%20Assistant%20(x64).dmg) | [macOS Apple Silicon](https://download.uipath.com/latest/UiPath%20Assistant%20(arm64).dmg)

Installation steps:

1. Download UiPath Studio and Assistant 2024.10.5, then run the installer.
2. Accept the license agreement.
3. For a simplified installation, make the following selections in the installation wizard:
   1. **Custom** installation, then select **Configure**.
   2. **Install for me only**, then select **Choose Packages**.
   3. **Automation Developer**, then select **Advanced Settings**.
   4. In the **Orchestrator URL** field, write the URL of your Automation Cloud organization. It should resemble `https://cloud.uipath.com/<my_organization>/<my_tenant>, and replace <my_organization> and <my_tenant>` with your values.
   5. Select the Automatically sign in checkbox, then select Install.
   6. Once the installation is complete, close the confirmation window, as you do not want to Launch UiPath Studio.
4. Launch UiPath Assistant.

### How do I check the Assistant version?

1. Open UiPath Assistant.
2. From your user icon, or **Preferences** menu, select **Help**.
3. The version is displayed under the **Build and runtime information** section.