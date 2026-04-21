---
title: "CX Companion Salesforce plugin"
visible: true
slug: "cx-companion-salesforce-plugin"
---

The **UiPath CX Companion SF Plugin** enables the out-of-the-box integration of CX Companion with Salesforce when using [external events](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/set-an-external-context-using-external-events). Read the following sections to learn how to install and configure the plugin.

## Prerequisites

Before you begin, please make sure that:

* You have **System Administrator** profile access.
  :::note
  You can use your current Salesforce org or test in a development org.
  :::

* Your Salesforce edition is **Enterprise**, **Unlimited**, or **Developer**.

## Installing the managed package

1. Access the AppExchange listing.

Follow these steps to install the **UiPath-CX-Companion-SF-Plugin** managed package:

   1. Open a web browser and go to the [Salesforce AgentExchange](https://agentexchange.salesforce.com/).
   2. In the search bar, type: **UiPath CX Companion SF Plugin**.
   3. Click the app listing, and then select **Get It Now**.
   4. Log in using your Salesforce credentials.
   :::important
   The CX Companion SF Plugin is currently in preview, pending approval from Salesforce. You can obtain the preview version in one of the following ways:
   * Download using the
   managed package URL: &lt;https://login.salesforce.com/packaging/installPackage.apexp?p0=04tPa000002FWpeIAG&gt;
   * Download from
   `https://&lt;yourSalesforceDomain&gt;.lightning.force.com/packaging/installPackage.apexp?p0 p0=04tPa000002FWpeIAG` where `&lt;yourSalesforceDomain&gt;` is your actual Salesforce organization domain.
   :::
2. Choose where to install and for whom.
   1. Select which environment you want to install to:
      * **Production**
        - Choose this if you are ready to use the app in your live Salesforce environment.
      * **Sandbox** - Choose this if you want to test the app before using it in Production.
      :::note
      This step is not available if you are using the preview version of the plugin.
      :::
   2. Select **Install for Specific Users**.

You can choose to make this managed package available to some or all users.
   3. Select “I acknowledge that I’m installing a Non-Salesforce Application that is not authorized for distribution as part of Salesforce’s AppExchange Partner Program.”.
   4. Click **Install**.
   5. Approve Third-Party Access for `https://*.uipath.com`, which will enable trusted access to the CX Companion App hosted on uipath.com.
   6. After the installation finishes, click **Done**.

After installation, the newly installed managed package **UiPath CX Companion SF Plugin** is displayed in the Installed Packages list.

   ![docs image](/images/studio-web/studio-web-docs-image-591103.webp)

## Assigning permissions and platform cache

1. Assign Permission Sets

Follow these steps to ensure the required permissions are available for the users for which you have installed the managed package.

   1. Navigate to **Setup** &gt; **Users** &gt; **Permission Set** and locate **UiPath CX Companion**.
   2. Select **Manage Assignments** &gt; **Add Assignments**.
   3. Select the required users.
   4. Click **Next**, and then click **Assign**.
2. Assign Platform Cache

We need to configure the Platform Cache as reusable memory for this app to store the data of the active Salesforce Record ID. Make sure that the Platform Cache is allocated as follows:

   1. Navigate to **Setup** &gt; **Platform Cache**.
   2. Locate **CxCompanionCache** and click **Edit**.
   3. Specify the following capacity (MB)
      * **Session Cache Allocation** - **Organization or Trial** (whichever is available): **2**
      * **Org Cache Allocation** - **Organization or Trial** (whichever is available): **1**
      :::note
      For Salesforce Developer Edition (DE), if Trial capacity is not available, you can request for the same by clicking **Request Trial Capacity**.
      :::
   4. Click **Save**,

   ![docs image](/images/studio-web/studio-web-docs-image-591120.webp)

## Connecting the CX Companion app to the plugin

1. Identify the URL where CX Companion is hosted. For information about getting the app URL, see [Configuring the CX Companion app](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/configuring-the-cx-companion-app) &gt; *Embedding the app*.
2. Set up a trusted URL.

To allow CX Companion’s iframe to render within the Lightning Web Component (LWC), the Salesforce instance must be configured to trust the site where CX Companion is hosted.

   1. Navigate to **Setup** &gt; **Trusted URLs**.
   2. Find *CXCompanion_Iframe* in the list, and click **Edit**.
   3. Select **CSP Context** as **All**.
   4. Select the options **connect-src** and **frame-src** and click **Save**
3. Modify custom metadata types.

The LWC requires custom metadata to be configured for CX Companion to deliver content into the CX Companion iframe application.

   1. Navigate to **Setup** &gt; **Custom Metadata Types**.
   2. For the label **CX Companion Setting**, select **Manage Records**. This label is automatically created when you install the managed package.

   ![docs image](/images/studio-web/studio-web-docs-image-591417.webp)
   3. For the **Default** label, click **Edit**.
   4. Paste your CX Companion’s app URL in the **App URL** field.
   5. Mention the **Target Origin** as the hostname of your CX Companion’s URL, e.g. `https://cloud.uipath.com`.
   6. If CX Companion is launched from an action button in a SF record page, the following fields define the dimensions of the invoked window. These can be changed as needed. The default values are:
      * **Record Action Component Width**: 1200
      * **Record Action Component Height**: 800
      :::note
      These dimensions and the title will be applicable only when CX Companion is configured as an action button on the object Record Page.
      :::
   7. Click **Save**,

   ![docs image](/images/studio-web/studio-web-docs-image-594561.webp)

## Positioning CX Companion

There are two options to position the CX Companion launch button in the Salesforce UI:

* As a Utility Bar item that is visible across all objects.
* As an action button on the object record page.

### Position as Utility Bar item

Follow these steps for each app where you want to enable CX Companion (e.g. Sales Console). This will ensure CX Companion is visible in the Utility Tray when the user is in that app.

In the following instructions, CX Companion is added as a Utility Bar item in Service Console.

1. Navigate to **Setup** &gt; **App Manager**.
2. Select **Edit** for **Service Console**.
3. Under **Utility Items (Desktop Only)** on the left panel, click **Add Utility Item**.
   * Search for the Lightning Web Component `cxCompanion` in the pop-up and select it.
   * Enter the **Label** that will appear in the Utility Bar (e.g. **CX Companion**) and select an appropriate icon.
   * Specify the **Panel Width** (recommended **1000** px) and **Panel Height** (recommended **520** px).
   * Select **Enable Refresh Button** which appears inside the LWC and allows CX Companion to be refreshed with data from the active SF object.
   * Click **Save**.

   ![docs image](/images/studio-web/studio-web-docs-image-591847.webp)
4. For **Utility Bar Alignment**, select the desired alignment, and then click **Save**.
   * If you select **Default**, the utility bar appears on the lower-left side of the screen.
   * If you select **Mirrored**, the utility bar appears on the lower-right side of the screen.

### Position as an action button on the object Record Page

Follow these steps for each object where you want to create the new action button for the Object Record page. The below instructions will guide you to adding CX Companion as an action button on the Case Record page.

1. Navigate to **Setup** &gt; **Object Manager** to create a new action for an object.
2. Search for an object for which you want to add a quick action (e.g. **case**) and open it.
3. Select **Buttons, Links, and Actions** on the left panel, and then, click **New Action**.
4. For **Action Type**, select **Lightning Web Component**.
5. For **Lightning Web Component**, select **uipathsf:cxCompanionRecordAction**.
6. In the **Label** box, enter the label that will appear on the button (e.g. `CX Companion`) and select an appropriate icon. The **Name** field will be automatically populated.
7. Click **Save**.

   ![docs image](/images/studio-web/studio-web-docs-image-591429.webp)
8. Navigate to **Setup** &gt; **Object Manager** to add this action to a lightning record page.
9. Search for an object for which you want to add a quick action (e.g. **case**) and open it.
10. Click **Lightning Record Pages** on left hand panel.
11. Go to any Salesforce record page, and click **Edit**.
12. Select the highlight panel on the record page and, on the right panel, click **Add Action** to add a dynamic action.
13. Search for *CX Companion* and click **Done**.
14. Click **Save**.

    ![docs image](/images/studio-web/studio-web-docs-image-591425.webp)
15. A button is added on the case record page that launches the CX Companion in a new pop-up window.
    :::note
    The dimensions and title of the CX Companion window will be determined by what was specified in the earlier step **Modify Custom Metadata Types**.
    :::

## Passing SF object fields to CX Companion

Follow these steps to configure the object fields from CX Companion Setup App.

1. Click **App Launcher**, search for and select the app **CX Companion Setup**.
2. Select the **CX Companion Object Configuration** tab.
3. In the **Object** dropdown, select any object that you have previously enabled with CX Companion (e.g. Account object).

If the object you want to add is not available in the Object dropdown:

   1. Select the option **Other**.
   2. Specify the Salesforce record ID (15 or 18 digits) of the object in the text box, and then click **Retrieve Metadata**. For example, to add the **Contact** object, enter any valid contact’s SF record ID, e.g. 003Ox00000eUIKSIA4 in the text box.
   3. The fields for the object are now displayed. Continue to step 4.
4. In the **Fields** section, select the fields that must be sent to CX Companion. Make sure that end users have access permissions to the selected fields.

   ![docs image](/images/studio-web/studio-web-docs-image-591421.webp)
5. Select up to two fields from the **Header** section that will be displayed as CX Companion’s header.
6. Click **Save** to save the configuration. It may take some time for the values to be saved and for the changes to be reflected in CX Companion.