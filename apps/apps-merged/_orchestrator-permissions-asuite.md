---
title: "Orchestrator Permissions"
visible: true
slug: "orchestrator-permissions"
---

In order to create apps and trigger robots at app runtime, users are required to have a minimum set of permissions to access processes from Orchestrator. This page describes the minimum permissions required for common personas and scenarios. For specific setup instructions, check out Orchestrator's documentation on [Managing Roles](https://docs.uipath.com/orchestrator/automation-suite/latest/user-guide/managing-roles).

Common Approaches to managing Orchestrator Permissions for UiPath Apps:

1. **Grant "Admin" Rights** - Assigning admin rights to everyone in your Automation Suite account is a quick and easy way for all users to experiment with the full capabilities of Automation Suite, but it is not recommended for production deployment.
2. **Modify Orchestrator's [Default Roles](https://docs.uipath.com/orchestrator/automation-suite/latest/user-guide/default-roles)** - The simplest way to provide the correct permissions to App Authors and App Users is to assign additional permissions to the roles that are provided out-of-the box.
3. **Create New Roles** - Create Tenant and Folder level Roles for App Authors and App Users. This allows the most control, but requires more orchestration overhead.

## App Studio

This section contains the minimum permissions required to author apps.

:::note
These are the absolute minimum permissions required to author apps that leverage RPA. Different permissions may be required to preview or run Apps created with App Studio. Additional permissions are required for users to add processes to Orchestrator.
:::

### Tenant Level

Define a user's access to resources at the tenant level.

* `Machines:View` - (Recommended) Used to get the machine key for setting up the robot. You also need `Machines: Create` if you have to create a new machine
* `Robots:Create` - (Recommended) Used to create a robot ( In case of Classic folders). For modern folders, this is not required
* `Folders:Edit` - (Recommended) Used to add app users to respective folders so that the app users can run the processes
* `Users:View` - (Recommended) Used to identify whether the relevant permissions are available for the respective users to whom we are sharing the app in Orchestrator
* `Webhooks: View, Create`: Used by App to start and retrieve results in case of unattended process run during preview

### Folder Level

In order to [import a process from Orchestrator](https://docs.uipath.com/apps/automation-suite/latest/user-guide/connecting-your-app-to-an-orchestrator-tenant#referencing-a-process-from-orchestrator) in App Studio, the user must have the following folder-level permissions on any folders that contain processes to be used by Apps.

* `Jobs:View` - Used to get the properties of complex objects (.Net objects/data table) by looking at last successful job run
* `Jobs:Create` - Used to run processes during preview
* `Processes:View` - Used to access the processes in a folder

## App Runtime - Attended Automation

* `Processes:View` - The app runtime user should have access to the processes in the corresponding folder used in App.
* `Jobs:Create` - Used to run processes during preview
* The user must also have a licensed Robot (with the [JavaScript Robot Add-On](https://docs.uipath.com/robot/standalone/2024.10/user-guide/about-the-robot-javascript-sdk) enabled) on their desktop.

## App Runtime - Unattended Automation

In order for users to trigger unattended automation at app runtime, a minimum of the following permissions are required:

### Tenant Level

Define a user's access to resources at the tenant level.

* `Webhooks: View, Create`: Used by App to start and retrieve results from the process run

### Folder Level

Define the user's access and ability within each [folder](https://docs.uipath.com/orchestrator/automation-suite/latest/user-guide/folders) they are assigned to.

* `Jobs: Create` - Used to start unattended jobs from Apps
  :::important
  If a user does not have `Webhook:Create` permissions at the tenant level, unattended jobs will not start at app runtime.
  :::