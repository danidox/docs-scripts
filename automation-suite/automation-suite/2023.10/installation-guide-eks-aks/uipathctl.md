---
title: "About uipathctl"
visible: true
slug: "uipathctl"
---

`uipathctl` is a UiPath® command-line tool that allows you to perform various operations in [Automation Suite on EKS/AKS](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-overview) and [Automation Suite on Linux](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/automation-suite-overview).

You can use uipathctl to check prerequisites in your environment, install Automation Suite, as well as configure and manage it from a single unified CLI.

Note, however, that not all commands referenced in this guide are suitable for both Automation Suite on EKS/AKS and Automation Suite on Linux. If certain commands are exclusive to one Automation Suite flavor, they should be marked accordingly.

It is important to be aware of the specific naming conventions we employ for the Automation Suite configuration file. The `input.json` name is used for Automation Suite on EKS/AKS, whereas `cluster_config.json` is specific to Automation Suite on Linux only.

For more information, including a complete list of `uipathctl` operations, see the [uipathctl reference documentation](https://docs.uipath.com/automation-suite/automation-suite/2023.10/reference-guide/uipathctl-reference#uipathctl-reference-documentation).

You can install `uipathctl` on the Linux, macOS, and Windows platforms.

:::note
Currently, `uipathctl` is only compatible with the x86 architecture. You cannot run `uipathctl` on machines based on the ARM architecture, such as Macs with Apple Silicon (M series) CPUs.
:::