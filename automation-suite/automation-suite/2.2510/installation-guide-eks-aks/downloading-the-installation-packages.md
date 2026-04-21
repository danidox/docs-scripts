---
title: "Downloading the installation packages"
visible: true
slug: "downloading-the-installation-packages"
---

You must install the following software on your management machine. Management machine refers to the machine you use to operate your cluster and that can access your cluster via the `kubeconfig` file. Your management machine can run Linux, Windows, or MacOS.

The following tools are required to successfully run the prerequisite checks, installation, and post-installation steps on your cluster via the client machine.

| Tool | Description | Download |
| --- | --- | --- |
| `uipathctl` | **Required**. `uipathctl` is a UiPath® command-line tool that allows you to run commands against Automation Suite Kubernetes.  You can use `uipathctl` to check prerequisites in your environment, install Automation Suite, configure and manage it from a single unified CLI. For more information, including a complete list of `uipathctl` operations, see the [uipathctl Reference Guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/reference-guide/about-uipathctl). | [Download uipathctl](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#uipathctl) |
| `versions.json` | **Required**. Needed to perform prerequisite checks and installation steps. | [Download versions.json](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#versionsjson) |
| `kubectl` | **Optional**. Ensure that `kubectl` matches the version of your cluster | [Download kubectl](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#kubectl) |
| `as-cmk.tar.gz` | `as-cmk.tar.gz` contains the container images and deployment manifests of UiPath® shared capabilities and UiPath® products. | [Download as-cmk.tar.gz](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#as-cmktargz) |
| `mirror-registry.sh` | `mirror-registry.sh` is required to configure an external Docker registry. | [Download mirror-registry.sh](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#mirror-registrysh) |
| `hydrate-registry.sh` | `hydrate-registry.sh` is required for configuring your external OCI-compliant registry for offline installations. | [Download hydrate-registry.sh](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#hydrate-registrysh) |
| `as-images.txt` | `as-images.txt` contains the name and version of the container images that you must pull and upload into the external Docker registry. | [Download as-images.txt](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#as-imagestxt) |
| `as-helm-charts.txt` | `as-helm-charts.txt` contain the details for the UiPath® application helm chart that you must pull and upload to an external Docker registry hosted on your environment. | [Download as-helm-charts.txt](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#as-helm-chartstxt) |
| `uipathtools` | `uipathtools` is a CLI tool that contains a subset of `uipathctl` capabilities specific to health commands. | [Download uipathtools](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#uipathtools) |

This page provides a list of download links for all the artifacts you may need to install or configure Automation Suite. Make sure to select the version of the artifacts you target.

## uipathctl

**Required**. `uipathctl` is a UiPath® command-line tool that allows you to run commands against Automation Suite. You can use `uipathctl` to check prerequisites in your environment, install Automation Suite, configure and manage it from a single unified CLI.
:::note
Currently, `uipathctl` is only compatible with the x86 architecture. You cannot run `uipathctl` on machines based on the ARM architecture, such as Macs with Apple Silicon (M series) CPUs.
:::

### 2.2510.1

To download `uipathctl` for Automation Suite 2.2510.1, run one of the following commands, depending on your OS:

* **Linux**:
  ```
  wget -O ~/uipathctl-linux-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.1/uipathctl-2.2510.1-linux-amd64.tar.gz
  ```
* **Windows:**
  ```
  wget -O ~/uipathctl-windows-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.1/uipathctl-2.2510.1-windows-amd64.tar.gz
  ```
* **MacOS:**
  ```
  wget -O ~/uipathctl-darwin-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.1/uipathctl-2.2510.1-darwin-amd64.tar.gz
  ```

### 2.2510.0

To download `uipathctl` for Automation Suite 2.2510.0, run one of the following commands, depending on your OS:

* **Linux**:
  ```
  wget -O ~/uipathctl-linux-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.0/uipathctl-2.2510.0-linux-amd64.tar.gz
  ```
* **Windows:**
  ```
  wget -O ~/uipathctl-windows-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.0/uipathctl-2.2510.0-windows-amd64.tar.gz
  ```
* **MacOS:**
  ```
  wget -O ~/uipathctl-darwin-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.0/uipathctl-2.2510.0-darwin-amd64.tar.gz
  ```

## versions.json

**Required**. Needed to perform prerequisite checks and installation steps.

### 2.2510.1

To download `versions.json` for Automation Suite 2.2510.1, run the following command:

```
wget -O ~/versions.json https://download.uipath.com/automation-suite/2.2510.1/versions.json
```

### 2.2510.0

To download `versions.json` for Automation Suite 2.2510.0, run the following command:

```
wget -O ~/versions.json https://download.uipath.com/automation-suite/2.2510.0/versions.json
```

## kubectl

**Optional**. Make sure that `kubectl` matches the version of your cluster.

To download `kubectl`, see [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/).

## as-cmk.tar.gz

`as-cmk.tar.gz` contains the container images and deployment manifests of UiPath® Shared Capabilities and UiPath® Product.

If you opt for the offline installation profile, you must download `as-cmk.tar.gz`. If you choose the online installation profile, Kubernetes will pull all the container images and deployment manifests directly from the container registry hosted in UiPath® servers.

`as-cmk.tar.gz` is required during installation and upgrade.

### 2.2510.1

```
https://download.uipath.com/automation-suite/2.2510.1/as-cmk-2.2510.1.tar.gz
```

For the checksum file, access this [link](https://download.uipath.com/automation-suite/2.2510.1/as-cmk-2.2510.1-sha256sum.txt).

* **Linux**:

To download `as-cmk.tar.gz` on a Linux machine, run the following command:

  ```
  wget -O ~/as-cmk.tar.gz https://download.uipath.com/automation-suite/2.2510.1/as-cmk-2.2510.1.tar.gz
  ```
* **Windows**:

To download `as-cmk.tar.gz`, access this [link](https://download.uipath.com/automation-suite/2.2510.1/as-cmk-2.2510.1.tar.gz) and rename the file to `as-cmk.tar.gz`.

### 2.2510.0

```
https://download.uipath.com/automation-suite/2.2510.0/as-cmk-2.2510.0.tar.gz
```

For the checksum file, access this [link](https://download.uipath.com/automation-suite/2.2510.0/as-cmk-2.2510.0-sha256sum.txt).

* **Linux**:

To download `as-cmk.tar.gz` on a Linux machine, run the following command:

  ```
  wget -O ~/as-cmk.tar.gz https://download.uipath.com/automation-suite/2.2510.0/as-cmk-2.2510.0.tar.gz
  ```
* **Windows**:

To download `as-cmk.tar.gz`, access this [link](https://download.uipath.com/automation-suite/2.2510.0/as-cmk-2.2510.0.tar.gz) and rename the file to `as-cmk.tar.gz`.

## mirror-registry.sh

`mirror-registry.sh` is required to configure an external Docker registry.

### 2.2510.1

```
https://download.uipath.com/automation-suite/2.2510.1/mirror-registry.sh
```

* **Linux**:

To download `mirror-registry.sh` on a Linux machine, run the following command:

  ```
  wget -O ~/mirror-registry.sh https://download.uipath.com/automation-suite/2.2510.1/mirror-registry.sh
  ```
* **Windows**:

To download `mirror-registry.sh` on a Windows machine, access this [link](https://download.uipath.com/automation-suite/2.2510.1/mirror-registry.sh).

### 2.2510.0

```
https://download.uipath.com/automation-suite/2.2510.0/mirror-registry.sh
```

* **Linux**:

To download `mirror-registry.sh` on a Linux machine, run the following command:

  ```
  wget -O ~/mirror-registry.sh https://download.uipath.com/automation-suite/2.2510.0/mirror-registry.sh
  ```
* **Windows**:

To download `mirror-registry.sh` on a Windows machine, access this [link](https://download.uipath.com/automation-suite/2.2510.0/mirror-registry.sh).

## hydrate-registry.sh

`hydrate-registry.sh` is required for configuring your external OCI-compliant registry for offline installations in the Automation Suite.

### 2.2510.1

* **Linux**:

To download `hydrate-registry.sh` on a Linux machine, run the following command:

  ```
  wget -O ~/hydrate-registry.sh https://download.uipath.com/automation-suite/2.2510.1/hydrate-registry.sh
  ```
* **Windows**:

To download `hydrate-registry.sh` on a Windows machine, access this [link](https://download.uipath.com/automation-suite/2.2510.1/hydrate-registry.sh).

### 2.2510.0

* **Linux**:

To download `hydrate-registry.sh` on a Linux machine, run the following command:

  ```
  wget -O ~/hydrate-registry.sh https://download.uipath.com/automation-suite/2.2510.0/hydrate-registry.sh
  ```
* **Windows**:

To download `hydrate-registry.sh` on a Windows machine, access this [link](https://download.uipath.com/automation-suite/2.2510.0/hydrate-registry.sh).

## as-images.txt

`as-images.txt` contains the name and version of the container images that must be pulled and uploaded into the external Docker registry.

### 2.2510.1

```
https://download.uipath.com/automation-suite/2.2510.1/air-images.txt
```

* **Linux**

To download `air-images.txt` on a Linux machine, run the following command:

  ```
  wget -O ~/as-images.txt https://download.uipath.com/automation-suite/2.2510.1/air-images.txt
  ```
* **Windows**:

To download `air-images.txt` on a Windows machine, access this [link](https://download.uipath.com/automation-suite/2.2510.1/air-images.txt) and rename the file to `as-images.txt`.

### 2.2510.0

```
https://download.uipath.com/automation-suite/2.2510.0/air-images.txt
```

* **Linux**

To download `air-images.txt` on a Linux machine, run the following command:

  ```
  wget -O ~/as-images.txt https://download.uipath.com/automation-suite/2.2510.0/air-images.txt
  ```
* **Windows**:

To download `air-images.txt` on a Windows machine, access this [link](https://download.uipath.com/automation-suite/2.2510.0/air-images.txt) and rename the file to `as-images.txt`.

## as-helm-charts.txt

`as-helm-charts.txt` contain the details for the UiPath® application helm chart that must be pulled and uploaded to an external Docker registry hosted on your environment.

### 2.2510.1

```
https://download.uipath.com/automation-suite/2.2510.1/embedded-helm-charts.txt
```

* **Linux**:

To download `embedded-helm-charts.txt` on a Linux machine, run the following command:

  ```
  wget -O ~/as-helm-charts.txt https://download.uipath.com/automation-suite/2.2510.1/embedded-helm-charts.txt
  ```
* **Windows**:

To download `embedded-helm-charts.txt` on a Windows machine, access this [link](https://download.uipath.com/automation-suite/2.2510.1/embedded-helm-charts.txt) and rename the file to `as-helm-charts.txt`.

### 2.2510.0

```
https://download.uipath.com/automation-suite/2.2510.0/embedded-helm-charts.txt
```

* **Linux**:

To download `embedded-helm-charts.txt` on a Linux machine, run the following command:

  ```
  wget -O ~/as-helm-charts.txt https://download.uipath.com/automation-suite/2.2510.0/embedded-helm-charts.txt
  ```
* **Windows**:

To download `embedded-helm-charts.txt` on a Windows machine, access this [link](https://download.uipath.com/automation-suite/2.2510.0/embedded-helm-charts.txt) and rename the file to `as-helm-charts.txt`.

## uipathtools

`uipathtools` is a CLI tool that contains a subset of `uipathctl` capabilities specific to health commands. The tool is backward compatible and works with any supported Automation Suite version. We recommend using `uipathtools` as the first step if you face any issue.

### 2.2510.1

To download `uipathtools`, run one of the following commands, depending on your OS:

* **Linux**
  ```
  wget -O uipathtools-linux-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.1/uipathtools-2.2510.1-linux-amd64.tar.gz
  ```
* **Windows**
  ```
  wget -O uipathtools-windows-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.1/uipathtools-2.2510.1-windows-amd64.tar.gz
  ```
* **MacOS**
  ```
  wget -O uipathtools-darwin-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.1/uipathtools-2.2510.1-darwin-amd64.tar.gz
  ```

### 2.2510.0

To download `uipathtools`, run one of the following commands, depending on your OS:

* **Linux**
  ```
  wget -O uipathtools-linux-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.0/uipathtools-2.2510.0-linux-amd64.tar.gz
  ```
* **Windows**
  ```
  wget -O uipathtools-windows-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.0/uipathtools-2.2510.0-windows-amd64.tar.gz
  ```
* **MacOS**
  ```
  wget -O uipathtools-darwin-amd64.tar.gz https://download.uipath.com/uipathctl/2.2510.0/uipathtools-2.2510.0-darwin-amd64.tar.gz
  ```