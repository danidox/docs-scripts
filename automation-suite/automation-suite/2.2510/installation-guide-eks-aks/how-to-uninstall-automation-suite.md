---
title: "How to uninstall Automation Suite"
visible: true
slug: "how-to-uninstall-automation-suite"
---

This section explains how to uninstall Automation Suite from EKS/AKS environments using the provided uninstall script.

You will learn how to prepare your system, execute the script, troubleshoot issues, and extend the functionality for custom requirements.

## Understanding the script and requirements

This section gives you a high-level understanding of the uninstall script and outlines the prerequisites required to use it effectively.

The uninstall script supports selective deletion of Automation Suite components, dry-run simulations, verbose output, and the ability to exclude specific components via command-line flags or a JSON configuration file.

### Prerequisites

This subsection lists the tools you must have installed in your environment to successfully run the uninstall script:

* EKS/AKS:
  + `kubectl`
  + `helm`
* Optional:
  + `jq` - used for JSON parsing

## Downloading and preparing the script

To obtain the uninstall script and prepare it for execution, take the following steps:

1. [Download](https://github.com/UiPath/automation-suite-support-tools/blob/main/Scripts/24.10/Uninstall/byok/uninstall.sh) the `uninstall.sh` script.
2. Make the script executable by running the following command:
   ```
   chmod +x uninstall.sh
   ```

## Running the script and using options

This section describes how to run the uninstall script, including command syntax, supported environments, and available flags.

You can run the script using the following command:

```
./uninstall.sh [DISTRIBUTION] [OPTIONS]
```

You can use the following distribution options, based on your environments:

* `k8s`: Use standard Kubernetes commands (default).
* `openshift`: Use OpenShift commands and APIs.

The following table lists all the supported flags and arguments that you can use to customize the uninstall behavior for your specific environment.

| Option | Description |
| --- | --- |
| `-h`, `--help` | Show help information. |
| `-d`, `--dry-run` | Preview changes without deleting anything. |
| `-v`, `--verbose` | Enable detailed logging. |
| `--excluded COMPONENTS` | Comma-separated list of components to skip. |
| `--clusterconfig FILE` | Path to a JSON config file for exclusions. |
| `--istioNamespace NAMESPACE` | Override default Istio namespace. |
| `--uipathNamespace NAMESPACE` | Override default UiPath namespace. |
| `--argocdNamespace NAMESPACE` | Override default ArgoCD namespace. |

### Using basic examples

This section provides simple example commands to help you quickly start using the uninstall script with minimal options.

```
# Exclude istio from deletion in k8s
./uninstall.sh k8s --excluded istio

# Exclude istio and argocd in OpenShift
./uninstall.sh openshift --excluded istio,argocd
```

### Using advanced combinations

This section presents advanced examples that combine multiple options for more flexible and powerful uninstall scenarios.

```
# Dry run to preview changes
./uninstall.sh openshift --dry-run

# Use a JSON config file
./uninstall.sh k8s --clusterconfig input.json

# Custom namespaces
./uninstall.sh openshift --uipathNamespace uipath-prod --istioNamespace custom-istio

# Combined options with verbosity
./uninstall.sh k8s --excluded gatekeeper,falco --clusterconfig input.json --verbose
```

## Configuring components and exclusions

This section outlines which components the script manages, how to exclude them, and what dependencies to consider.

### Supported components

This section lists the Automation Suite components that the uninstall script is capable of managing and deleting:

* `istio` - Service mesh components
* `istio_configure` - Istio configuration
* `argocd` - ArgoCD deployment
* `uipath` - Core UiPath components
* `cert_manager` - Certificate management
* `network_policies` - Network policies
* `gatekeeper` - Gatekeeper enforcement
* `falco` - Gatekeeper enforcement

### Using configuration files

This section shows how to configure component exclusions using a JSON file.

You can exclude components via JSON, as follows:

```
{
  "exclude_components": [
    "istio",
    "argocd",
    "gatekeeper"
  ]
}
```

### Understanding component dependencies

This section explains the relationships between components to help you avoid issues when excluding specific items.

Some components have dependencies on others:

* If you keep `uipath`, consider also keeping `istio` and `argocd`.
* If you keep `cert_manager`, consider also keeping `uipath`.