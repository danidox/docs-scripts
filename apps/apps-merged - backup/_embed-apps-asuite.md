---
title: "Embed Apps"
visible: true
slug: "embed-apps"
---

You can easily embed apps in your applications or web pages.

## Non-public apps - accessing the syntax for embedding

1. Publish your app.
2. Deploy your app to an Orchestrator folder.
3. [Copy the app URL](https://docs.uipath.com/apps/automation-suite/latest/user-guide/accessing-the-production-url-of-an-app), and add `embed_` between `https://{yourDomain}/` and the organization ID. For example:
   ```
   https://{yourDomain}/embed_/<organization_id>/apps_/default/run/production/<tenant_id>/<folder_id>/<app_id>/public
   ```