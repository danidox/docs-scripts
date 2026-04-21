---
title: "August 2024"
visible: true
slug: "august-2024"
---

## 13 August 2024

### Introducing AI Trust Layer governance policy capabilities for Studio Web

The AI Trust Layer governance policy now includes control over AI-powered features in Studio Web, allowing you to prevent calls to third-party AI models. To learn more, refer to [Settings for AI Trust Layer policies](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies) in the Automation Ops guide.
:::note
To disable Autopilot UI features in Studio Web, you need to define a Studio Web governance policy that disables Autopilot capabilities.
:::

### Studio Web APIs

You can now use Studio Web APIs to manage Studio Web resources from an external application.

**Erratum - added December 11, 2024**: Studio Web APIs are currently not available.

## 12 August 2024

### Debug individual workflow files

You can now debug individual workflow files from the **Project explorer**. Simply right-click a workflow and select one of the two new options: **Test workflow** or **Test workflow step-by-step**. For more information, refer to.

### Create entities from the Data Manager

If you open a project that uses an entity and your tenant does not have access to that entity, you can now create the missing entity directly from the Data Manager. Simply select the new **Create missing entity** option from the **Actions** ![docs image](/images/studio-web/studio-web-docs-image-More_VT.png) menu next to the missing entity.

![Create entities from the Data Manager](/images/studio-web/studio-web-create-entities-from-the-data-manager-405143.webp)

### Easier way to manage connections

Connection properties are now displayed when hovering over a connection in the **Data Manager**. Additionally, it's now easier to set, edit, and delete the purpose of a connection by selecting the new **Connection purpose** button. For more information, refer to.

### Improvements

* In projects containing multiple workflows, the variable scope now reflects the current workflow name.

  ![Variable scope](/images/studio-web/studio-web-variable-scope-451601.webp)
* When trying to open an unavailable version of a project from the **Change History** panel, a message now informs you that the current version was opened instead.
* The **Set value** activity property now includes the builder specific to the variable data type (for example, **Text Builder** for variables of type **Text**, **Condition Builder** for variables of type **Boolean**, or **Date and Time Selector** for variables of type **Date with time**).

  ![Set value activity property](/images/studio-web/studio-web-set-value-activity-property-451942.webp)

### Recent activities updates

The following categories of activities are now in general availability:

* [Mailjet](https://docs.uipath.com/activities/other/latest/integration-service/uipath-sinch-mailjet-activities)
* [Pagerduty](https://docs.uipath.com/activities/other/latest/integration-service/uipath-pagerduty-pagerduty-activities)
* [Pipedrive](https://docs.uipath.com/activities/other/latest/integration-service/uipath-pipedrive-pipedrive-activities)
* [WhatsApp Business](https://docs.uipath.com/activities/other/latest/integration-service/uipath-meta-whatsapp-activities)

The following categories of activities have received updates:

* [Document Understanding](https://docs.uipath.com/activities/other/latest/document-understanding/release-notes-document-understanding-activities) (v2.9.5)
* [Google Workspace](https://docs.uipath.com/activities/other/latest/productivity/release-notes-uipath-gsuite-activities) (v2.6.24)
* [Microsoft 365](https://docs.uipath.com/activities/other/latest/productivity/release-notes-microsoftoffice365-activities) (v2.6.25)
* [UI Automation](https://docs.uipath.com/activities/other/latest/ui-automation/release-notes-uipath-uiautomation-activities-v23-10) (v23.10.13)

## 2 August 2024

### Introducing a streamlined automation design experience

We are excited to announce that creating and managing automations in Studio Web is now easier than ever! In an effort to simplify the experience of using Studio Web, we have consolidated the **Projects** and **Automations** pages under a single **Automations** page, which gives you quick access to all the project information you need. The **Runs** and **Connections** pages have also been consolidated as project-specific details under the new **Automation details** page. The **Templates** page remains unchanged. To learn more about these changes, see.

  ![The streamlined automation design experience](/images/studio-web/studio-web-the-streamlined-automation-design-experience-451567.webp)