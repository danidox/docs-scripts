---
title: "Running uipathctl"
visible: true
slug: "running-uipathctl"
---

`uipathctl` is a UiPath® command-line tool that allows you to perform various operations in [Automation Suite on EKS/AKS](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/automation-suite-overview), [Automation Suite on OpenShift](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-openshift/automation-suite-overview), and [Automation Suite on Linux](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide/automation-suite-overview).

You can use uipathctl to check prerequisites in your environment, install Automation Suite, as well as configure and manage it from a single unified CLI.

You can install `uipathctl` on the Linux, macOS, and Windows platforms.

Currently, uipathctl is only compatible with the x86 architecture. You cannot run uipathctl on machines based on the ARM architecture, such as Macs with Apple Silicon (M series) CPUs.

For more information, including a complete list of `uipathctl` operations, see the [uipathctl Reference Guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/reference-guide/uipathctl-reference).

## Running uipathctl on Linux

To run `uipathctl` on Linux, take the following steps:

1. Download the version of the `uipathctl` binary that you are interested in. For instructions, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#downloading-the-installation-packages).
2. Uncompress `uipathctl` and add it to your PATH:
   ```
   tar xzvf uipathctl-linux-amd64.tar.gz
   chmod +x uipathctl
   export PATH=$PATH:$(pwd)
   ```
3. Verify if `uipathctl` works:
   ```
   uipathctl version
   ```

The command prints some version information, as shown in the following example:

   ```
   Version:       2.2510.0
   ...
   ```

## Running uipathctl on Windows

To run `uipathctl` on Windows, take the following steps:

1. Download the version of the `uipathctl` binary that you are interested in. For instructions, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#downloading-the-installation-packages).
2. Uncompress `uipathctl` and add it to your PATH:
   ```
   tar xzvf uipathctl-windows-amd64.tar.gz
   ```

Append or prepend the `uipathctl` binary folder to your `PATH` environment variable.
3. Verify it is working:
   ```
   uipathctl version
   ```

The command prints some version information, as shown in the following example:

   ```
   Version:       2.2510.0
   ...
   ```

## Running uipathctl on MacOS

To run `uipathctl` on MacOS, take the following steps:

1. Download the version of the `uipathctl` binary that you are interested in. For instructions, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#downloading-the-installation-packages).
2. Uncompress `uipathctl` and add it to your PATH:
   ```
   tar xzvf uipathctl-darwin-amd64.tar.gz
   chmod +x uipathctl
   export PATH=$PATH:$(pwd)
   ```
3. Verify if `uipathctl` works:
   ```
   uipathctl version
   ```

The command prints some version information, as shown in the following example:

   ```
   Version:       2.2510.0
   ...
   ```

## Telemetry

By default, telemetry is sent from `uipathctl` to UiPath® at each command execution. This helps us improve our products and user experience.

To opt out of telemetry, set the `UIPATHCTL_TELEMETRY_OPTOUT` environment variable to `1`.