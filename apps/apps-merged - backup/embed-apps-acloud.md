---
title: "Embed Apps"
visible: true
slug: "embed-apps"
---

You can easily embed apps in your applications or web pages.

## Public apps - accessing the syntax for embedding

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

1. Publish your app.
2. Deploy your app to an Orchestrator folder.

A dialog box displays the app public URL and the iFrame syntax you can use to embed your app, as shown in the following image:

   ![docs image](/images/apps/apps-docs-image-296731-13d098f7.webp)
3. Copy the iFrame syntax, for example:
   ```
   <iframe width="560" height="315" src="{baseURL_vanilla}/<organization_id>/apps_/default/run/production/<tenant_id>/<folder_id>/<app_id>/public" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   ```

## Non-public apps - accessing the syntax for embedding

1. Publish your app.
2. Deploy your app to an Orchestrator folder.
3. [Copy the app URL](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/accessing-the-production-url-of-an-app), and add `embed_` between `{baseURL_vanilla}/` and the organization ID. For example:
   ```
   {baseURL_vanilla}/embed_/<organization_id>/apps_/default/run/production/<tenant_id>/<folder_id>/<app_id>/public
   ```