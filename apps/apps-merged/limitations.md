---
title: "Limitations"
visible: true
slug: "limitations"
---

* Due to limitations in the VB expression language, using Japanese characters in the names of pages, controls, processes, or integrations in your app is not supported. You can, however, use Japanese characters in values and in the names of variables, and they display correctly.
* You cannot configure **Custom List** controls with VB expressions.
* You cannot chain processes via input override. For example, binding the object output of process A to the input override of process B.
* Apps built during the VB preview and published before May 25th may need to be republished and deployed in Orchestrator folders.