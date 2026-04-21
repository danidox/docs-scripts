---
title: "Managing external OAuth applications"
visible: true
slug: "managing-external-applications"
---

As an admin, using the OAuth framework, you can delegate authorization to external applications. Once registered, these applications can make API calls to UiPath applications or resources scoped to the APIs you designate.

## Adding an external application

To register an external application so that it can use OAuth to access your UiPath resources:

1. Navigate to Orchestrator at tenant level.
2. Select the **Manage Access** tab.
3. Select **Manage Accounts and Groups**.
4. From the **UiPath Administration** header, select the **External Applications** card.
5. Select **Add Application** in the top right.
6. Fill in the **Application Name** field
7. Select an option for **Application Type**.

If you select **Confidential application**, you receive an app secret at the end, so make sure your application can store it securely. If it can't, select **Non-confidential application**.
8. Under **Resources**, select **Add Scopes**.

The **Edit Resource** panel opens on the right, where you can select the resources to which the application should have access.
9. From the **Resource** drop-down list, select the UiPath API that the application can use.
   :::note
   You can only add scope for one resource at a time. If you want to allow access to multiple resources, repeat this process to add scope for each resource.
   :::
10. On the **User Scope(s)** tab, select the check boxes for the logical API permissions that you want to grant, as needed.

Granting permissions under user scope means that the external application can access those resources within a user context and a user with the appropriate permissions must be logged in.
11. If this is a confidential application, you can switch to the **Application Scope(s)** tab to also grant application-level permissions for the selected resource, as needed.

With permissions under application scope, the external application has access to application-wide data for the selected scopes without the need for user interaction.

Non-confidential applications cannot access application scope.
12. Select **Save**.

The panel closes and the selected resource and scopes are added to the **Resources** table in the form.
13. If the external application has been registered with **user** scopes, you must add a **Redirect URL** where the external application should receive the authorization response.

If **only** application scopes are selected, providing a **Redirect URL** is optional.
14. Select **Add** to create the registration.

A confirmation message opens. For confidential applications, the confirmation message includes the **app secret** that the registered external application can use to request authorization. Make sure you save it in a secure location because you cannot view it again.

## Changing the scope for an existing application

Scopes are the permissions of the external application in relation to your UiPath resources.

1. Go to **Admin** > **Organization** > **External Applications**.
2. Select the **Editing** icon.
3. Change the scope to which the application has access:
   * Use the icons at the right of a resource row to edit existing scope or to delete the resource.
   * Select **Add Scopes** to add an additional resource and then select scopes for it.
4. Select **Save**.

## Generating a new app secret

If you don't know the application secret that was generated for an external application, you cannot recover it. But you can generate a new one.
:::note
If you generate a new app secret, make sure to share it with the developer who is maintaining the integration with the external application. They must update the authentication mechanism, otherwise the existing integration no longer works.
:::

To generate a new app secret:

1. Go to **Admin** > **Organization** > **External Applications**.
2. Select the **Editing** icon.
3. Under **App Secret**, select **Generate New**.

A new app secret is generated and displayed. The app secret remains visible until you select **Cancel** to close the page.
4. Copy it and make sure you store it in a safe place.

## Providing details to developers

After you register an external application, a developer must also set up the external application so that it properly authenticates, requests authorization from UiPath Identity Server, and then access the allowed UiPath resources.

To be able to perform those tasks, you must share the following information with them:

* the **Application Type** and **Application ID**, both of which are visible on the **Admin** > **External Applications** page
* the scopes added for each scope type. For some resources, the same name is used under both user and application scopes, so the type is also important.
* if this is a confidential application, the **application secret** generated when you registered the external application.
  :::note
  If you do not have the secret anymore, generate a new one as previously described.
  :::

For more details on how to authenticate and authorize external apps as a developer, refer to [External Apps](https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/accessing-uipath-resources-using-external-applications) in the API guide.