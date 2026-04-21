---
title: "Under the hood"
visible: true
slug: "under-the-hood"
---

Apps that use VB expressions work with Dynamic Link Library (DLL) files. This functionality is powered by the open-source technology Blazor. This framework supports compiling.NET code into DLL files, and then running the DLL files inside a browser. Refer to the official Microsoft documentation on [Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/) for more information.

When you first interact with a VB expression app, your browser accesses the UiPath content delivery network (CDN), and downloads the DLL files that are required to run VB expression apps. Whenever you run an app, the system loads the DLL files from the browser cache and adds them to memory.

There are two distinct sets of DLL files required to run VB expression apps:

* System DLL files that are required for the Blazor WASM. This set contains around 200 DLL files.
* App-specific DLL files that are generated based on the pages and integrations you add to your app. The number of DLL files in this set varies based on the number and types of resources in your app.

These DLL files, particularly app-specific DLL files, vary in their naming and format.

:::important
If your firewall blocks downloads of DLL files, allowlist the UiPath content delivery network in your firewall settings to use UiPath Apps. Refer to [Configuring the firewall](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/configuring-firewall#apps) for more details.
:::