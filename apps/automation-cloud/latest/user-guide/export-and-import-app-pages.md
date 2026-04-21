---
title: "Page export and import"
visible: true
slug: "export-and-import-app-pages"
---

To reuse the design of an existing page, its controls, rules, and corresponding bindings, you can export an app page, then import it in another app. This is an alternative to using the default app templates, available when you create a new app.

## Limitations

* Importing a page covers only controls and rules. Resource references, such as queues, processes, storage buckets, or app variables cannot be imported.
* Only uncorrupted page are valid for import.
* Simultaneous export of multiple pages is unavailable.
* Images that are referenced within an app page are excluded from the page export.

## Page reuse example

Say you need to design three distinct apps for your organization: an onboarding app, an expense reporting app, and a training app. These apps share a key data element – the employee profile.

You start by designing the onboarding app first, and you create the "Employee Profile" page specific for this application. Recognizing the commonality and aiming for efficiency, you decide not to duplicate the design effort for the other two apps. Instead, you export the "Employee Profile” page from the onboarding app and import it in both the expense-reporting and the training applications.

This export and import process may incur certain binding errors in the receiving apps due to resource discrepancies. You can resolve these errors by re-referencing the respective resources.

## Exporting an app page

1. In the source app, identify the app page you want to import, and click the three dots icon (**...**).
2. Select **Export page**. The page is downloaded to your device, with the following naming and extension syntax: &lt;app_page_name&gt;.uipage.

## Importing an app page

1. In the destination app, expand the **Add any** menu next to the **Add control** button.

   ![docs image](/images/apps/apps-docs-image-346564-734352b3.webp)
2. Select **Import page from file.**
3. Navigate to the location of the `.uipage` file you previously exported, select it, and click **Open**. The page you imported is displayed at the bottom of the tree view panel.
4. Resolve binding errors by referencing the same resources as in the source app.