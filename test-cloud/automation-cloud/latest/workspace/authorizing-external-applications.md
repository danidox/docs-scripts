---
title: "OAuth apps"
visible: true
slug: "authorizing-external-applications"
---

External OAuth applications exist outside of the UiPath® platform and integrate with it to extend its capabilities. External apps can securely access your UiPath resources without requiring you to share your credentials, via the OAuth framework which allows authorization delegation to these external entities.

By registering external apps with UiPath, they gain the ability to make API calls to access [UiPath resources](https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/available-resources).

## App types

UiPath classifies OAuth external applications into two main categories - confidential and non-confidential. The app type determines its authentication flow, the level of access to resources, and the way it communicates with UiPath's Identity Server.

* **Confidential apps with application scopes:** Confidential apps with application scopes are intended to be used in cases where the application can securely store credentials. For example, a program that stores the password in a vault.
* **Confidential apps with user scopes**: Confidential apps with user scopes are intended to be used in cases where the application can securely store credentials and act on behalf of a user. For example, a CRM application that creates queue items in Orchestrator. It does this on behalf of the user but it also stores the credentials it uses in a database.
* **Non-confidential apps with user scopes**: Non-confidential apps do not rely on securely stored credentials. Instead, they rely on the user authenticating to an application and delegating access to the app via temporary credentials. The credentials are short lived and the user may have to reauthenticate the app periodically. These are best for attended automation or automations where a user is available to re-authenticate the app. For example, a user has an attended automation that executes an automation using O365 activities to access SharePoint. The first time it runs, it prompts the user to authorize the app (the automation). Periodically, the user might have to reauthorize the application after the credentials expire.

## Scopes

When an external application is set up to integrate with UiPath, it is assigned specific permissions and access, referred to as "scopes". Essentially, scopes define what an application can and cannot do or access within UiPath.
:::note
When granting access to external applications, always provide the minimum permissions necessary for the app to function. This measure helps limit potential damage by making unauthorized access less likely.
:::

At the organization level, a scope is defined in the format `Service.Resource.Accesslevel` or `Service.Resource`. For example, with `OR.Machines.Read`, the external application has read access to machines in Orchestrator across all folders and tenants in the organization, with `OR.Machines`, the external app has read and write access across all folders and tenants in the organization.

For confidential applications, UiPath allows the assignment of fine-grained scopes that specifically apply to Orchestrator's resources. These specific permissions enable an administrator to control and customize the access down to the tenant folder level.

Fine-grained assignment occurs when an organization's administrator assigns the external confidential app to a specific tenant or a folder in Orchestrator, and associates it with a particular role.

Scopes are either geared on a user (user scope) or on the app itself (application scope).

* Application scopes grant the app an identity of its own wherein it performs functions as a standalone entity.
* In user scopes, the app performs functions on behalf of an authenticated user and hence the actions are limited by the user's permissions. For example, the app can only access the assets that the user is allowed to access.

## Implementation

The process of using UiPath external apps covers different stages, from the creation and setup by an administrator to its integration and usage by a developer.

A. Creation and setup by the administrator

1. **External app registration**: The first step involves [adding an external app to the organization](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-external-applications#adding-an-external-application). The administrator sets details such as name, redirect URL, and selects the suitable application type. Once the app with its scopes is created at the admin level, it gains those permissions at the organization level. The admin can [configure fine-grained permissions for confidential apps](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-access-for-external-apps#configuring-fine-grained-access-for-confidential-apps) by assigning them a role at the tenant and folder levels in Orchestrator.
2. **User assignment**: In case of non-confidential or confidential apps with user scopes, the administrator must ensure that the users who need to use the app have access to the system, by assigning the user a role at the organization, tenant, or folder levels.
3. **Storing application details**: After completing the setup, the administrator retrieves application details, such as the application ID. For confidential apps, an application secret is also generated. The administrator securely stores these details, later sharing them with developers.

B. Integration and usage by the developer

1. **Authentication and authorization**: The developer uses the application ID (and secret for confidential apps) given by the administrator to initiate an OAuth 2.0 access token request to UiPath Identity Server. In doing so, the developer includes the necessary scopes within the request. The OAuth 2.0 flow is successful when the server validates the application's ID, its secret (for confidential apps) and approves the specified scopes.
   :::note
   For external apps with user scopes, user identity validation also takes place. This is an additional layer of security ensuring that the requests are legitimately coming from authenticated and authorized users.
   :::
2. **Access token generation:** Once the server successfully authenticates the application and the scopes, it returns an access token to the developer. This access token represents the application's authorization to access the specified scopes.
3. **Integrating the external app:** The developer uses the received access token in the header of API calls made to UiPath. This grants the specified level of access to the requested resources, thereby integrating the external application with UiPath resources.

For more details on how to authenticate and authorize external apps as a developer, refer to [External Apps](https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/accessing-uipath-resources-using-external-applications) in the API guide.