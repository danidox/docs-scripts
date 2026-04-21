---
title: "Installing Automation Suite"
visible: true
slug: "installing-automation-suite"
---

## Installation overview

This page walks you through the high-level installation instructions for Automation Suite.

Before you begin, consider the following:

* To deploy and manage Automation Suite, you must have knowledge of Kubernetes and cloud resource management. If you encounter issues installing and configuring Automation Suite, contact UiPath® Professional Services.
* Before choosing your deployment profile, see [Deployment scenarios](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/deployment-scenarios#deployment-scenarios).
* The installation process generates self-signed certificates on your behalf if you grant the installer admin privileges. You should replace them with certificates signed by a trusted Certificate Authority (CA) as soon as installation completes. For instructions, see [Managing the certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#managing-the-certificates).
* Automation Suite supports enabling Federal Information Processing Standard 140-2 (FIPS 140-2). For details, see [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/security-and-compliance#fips-140-2).

## Running the installation

To check which deployment scenarios are available for Automation Suite, refer to [Deployment scenarios](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/deployment-scenarios#deployment-scenarios).

To install Automation Suite, take the following steps:

1. After successfully validating the prerequisites, you install Automation Suite by running the following command:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```

For an output example, see [Output example: Automation Suite installation](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/output-example-automation-suite-installation#output-example%3A-automation-suite-installation).

   :::note
   If you encounter issues while running the installation, rerun the command the installation commands with all the arguments and flags. For details on the issues you might encounter, refer to [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/troubleshooting#troubleshooting).
   :::
2. Validate that your installation is successful and services are healthy by running the following command:
   ```
   uipathctl health check
   ```