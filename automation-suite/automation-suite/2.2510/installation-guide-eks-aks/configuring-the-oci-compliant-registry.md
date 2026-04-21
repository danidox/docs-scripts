---
title: "Configuring the OCI-compliant registry"
visible: true
slug: "configuring-the-oci-compliant-registry"
---

In offline installations, you need a registry compliant with OCI (Open Container Initiative) to store the container images and deployment Helm charts.

## Uploading the Automation Suite artifacts to the external OCI-compliant registry

There are two ways to upload the Automation Suite artifacts to the external OCI-compliant registry:

* **Option A**: By [mirroring your OCI-compliant registry with the UiPath® registry](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-oci-compliant-registry#option-a%3A-mirroring-the-uipath%C2%AE-registry-to-your-registry)
* **Option B**: By [hydrating your OCI-compliant registry with the offline bundle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-oci-compliant-registry#option-b%3A-hydrating-the-registry-with-the-offline-bundle)

The following table compares the two options to upload the artifacts to the registry so that you can choose the one that suits your needs:

| Option A: Mirroring the registry | Option B: Hydrating the registry |
| --- | --- |
| Copies the artifacts from the UiPath® registry to any target registry. | Uses the offline tarball to untar and upload the artifacts to the target registry. |
| Requires Docker and Helm tools. | Requires Podman and Helm tools. |
| Requires internet access to copy the artifacts from the UiPath® registry to the target registry. | Requires internet access only to download the offline tarball to the jump server. Uploading the tarball does not require internet access. |
| Requires a temporary space to cache the images during the copying method. This space is usually configured during the Docker installation. The default location is `/var/lib/docker`. | Requires a temporary space to extract the tarball and a temporary space for Podman to load the images.  The location of the tarball extraction must be provided during the hydration step. The Podman location can be `/var/tmp`, which must have adequate storage available. |
| The required storage capacity for the `/var/lib/docker` directory is around 128 GB. | The required storage capacity for the extraction is around 200 GB, and `/var/tmp` must be 256 GB. |

:::note
It is recommended to perform the mirroring or hydration operation from the management machine or jump box, instead of using the server nodes.
:::

### Option A: Mirroring the UiPath® registry to your registry

This method requires internet access on the jump machine from which you upload the Automation Suite artifacts onto your OCI-compliant registry.

#### Prerequisites for mirroring the UiPath® registry

To mirror the UiPath® registry, you need the following:

* a VM running a Linux distribution (recommended) or a laptop (not recommended)
* a Docker client authenticated with the private registry
* Helm 3.8 or newer authenticated with the private registry
* `as-images.txt`
* `as-helm-charts.txt`
* `mirror-registry.sh`
* outbound connectivity to `registry.uipath.com`
* 128 GB of free disk space for Docker under the `/var/lib/docker` partition on the machine from which you upload the container images and charts

#### Installing Docker and Helm

You must have Docker and Helm installed and authenticated on the machine from which you plan to upload the Automation Suite container images and charts to your registry.

* To download the Docker binaries, see the [official documentation](https://docs.docker.com/engine/install/).
* To authenticate the Docker registry, see the [official documentation](https://docs.docker.com/engine/reference/commandline/login/). Alternatively, you can use the following command by replacing the sample credentials with your actual registry credentials:
  ```
  docker login my.registry.io:443 --username "admin" --password "secret"
  ```
* To download the Helm binaries, see the [official documentation](https://helm.sh/docs/intro/install/).
* To authenticate the Helm registry, see the [official documentation](https://helm.sh/docs/helm/helm_registry_login/). Alternatively, you can use the following command by replacing the sample credentials with your actual registry credentials:
  ```
  helm registry login my.registry.io:443 --username "admin" --password "secret"
  ```

#### Downloading as-images.txt

To download `as-images.txt`, see [Downloading installation bundles](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#as-imagestxt).

#### Downloading as-helm-charts.txt

To download `as-helm-charts.txt`, see [Downloading installation bundles](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#as-helm-chartstxt).

#### Downloading the optional Document Understanding bundles

To download the optional Document Understanding bundles, see [Document Understanding documentation](https://docs.uipath.com/document-understanding/automation-suite/2.2510/classic-user-guide/ml-packages-offline-installation).

#### Downloading mirror-registry.sh

To download the `mirror-registry.sh` script, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#mirror-registrysh).

#### Uploading the Automation Suite images to your registry

The `mirror-registry.sh` script requires outbound connectivity to the source (default `registry.uipath.com`) and target registries.

:::note
The `mirror-registry.sh` script does not perform authentication to the registry. It is assumed that you have already authenticated to the registry.
:::

| Flag | Environment variable | Description |
| --- | --- | --- |
| `--images-manifest` | `IMAGES_MANIFEST` | Mandatory. Path to the image manifest file. |
| `--helm-charts-manifest` | `HELM_CHARTS_MANIFEST` | Mandatory. Path to the Helm chart manifest file. |
| `--target-registry-url` | `TARGET_REGISTRY_URL` | Mandatory. Pass the URL for the target registry. |
| `--source-registry-url` | `SOURCE_REGISTRY_URL` | Optional. Pass the URL for the source registry. The default is `registry.uipath.com`. |

To upload the Automation Suite images to your registry:

1. Ensure that you have the necessary permissions to execute the shell script, by running the following command:
   ```
   chmod +x mirror-registry.sh
   ```
2. Upload the Automation Suite images to your registry, by running the following command:
   ```
   ./mirror-registry.sh --target-registry-url my.registry.io:443 --source-registry-url registry.uipath.com --images-manifest /home/myuser/as-images.txt --helm-charts-manifest /home/myuser/as-helm-charts.txt
   ```
   :::note
   For registries, such as Harbor, which require using a project, make sure you append the project name to the target registry URL you include in the command, as shown in the following example: assignment
   ```
   ./mirror-registry.sh --target-registry-url my.registry.io:443/myproject --source-registry-url registry.uipath.com --images-manifest /home/myuser/as-images.txt --helm-charts-manifest /home/myuser/as-helm-charts.txt
   ```
   :::

### Option B: Hydrating the registry with the offline bundle

This method only requires internet access on the jump machine to download the offline bundle. Once the bundle is available, you can upload to your OCI-compliant registry without an internet connection.

:::note
This method may also require additional space on the machine to un-tar and upload to your registry. In addition, this method may take longer than the mirroring approach.
:::

#### Prerequisites for hydrating the registry

To hydrate the registry, you need the following:

* a VM running a Linux distribution is preferred over running the script on a laptop
* ability to download and copy or somehow propagate the offline bundle to the VM
* Helm 3.8 or newer authenticated with the private registry
* Podman installed, configured, and authenticated with the private registry
* 150 GB of free disk space for Podman under `/var/lib/containers` for loading the containers locally before pushing them to the remote registry. If you need to change the default path, update the `graphRoot` variable in the `/etc/containers/storage.conf` file.

For example, you can edit `storage.conf` using `sudo nano /etc/containers/storage.conf`, change `graphRoot` to your new path, and then verify that the path is updated using the `podman info` command.
* Set the `TMP_DIR` environment variable as described in the [official Podman documentation](https://docs.podman.io/en/stable/markdown/podman.1.html). This variable specifies the temporary storage for downloaded container images during pull and build operations, crucial for avoiding out-of-space errors if `/var/tmp` is limited.
* `as-cmk.tar.gz`

#### Installing Podman and Helm

You must ensure you have Podman and Helm installed and authenticated on the machine from which you plan to upload the Automation Suite container images and charts to your registry.

* To download the Podman binaries, see the [official documentation](https://podman.io/docs/installation).
* To authenticate to the Podman registry, see the [official documentation](https://docs.podman.io/en/latest/markdown/podman-login.1.html). Alternatively, you can use the following command by replacing the sample credentials with your actual registry credentials:
  ```
  podman login my.registry.io:443 --username "admin" --password "secret"
  ```
* To download the Helm binaries, see the [official documentation](https://helm.sh/docs/intro/install/).
* To authenticate the Helm registry, see the [official documentation](https://helm.sh/docs/helm/helm_registry_login/). Alternatively, you can use the following command by replacing the sample credentials with your actual registry credentials:
  ```
  helm registry login my.registry.io:443 --username "admin" --password "secret"
  ```

#### Downloading as-cmk.tar.gz

To download `as-cmk.tar.gz`, see [Downloading installation bundles](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#as-cmktargz).

#### Downloading the optional Document Understanding bundles

To download optional Document Understanding bundles, see [Document Understanding documentation](https://docs.uipath.com/document-understanding/automation-suite/2.2510/user-guide/ml-packages-offline-installation).

#### Downloading hydrate-registry.sh

To download the `hydrate-registry.sh` script, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#hydrate-registrysh).

#### Uploading the Automation Suite images to the registry

To upload the Automation Suite images to the registry, use the `hydrate-registry.sh` script.

The `hydrate-registry.sh` script does not require outbound connectivity except with the target registries.

:::note
The `hydrate-registry.sh` script does not perform authentication to the registry. It is assumed that you have already authenticated to the registry.
:::

| Flag | Description |
| --- | --- |
| `--offline-bundle-path` | Mandatory. Path to the offline bundle. |
| `--target-registry-url` | Mandatory. Pass the URL for the target registry. |
| `--extract-path` | The location to be used to untar the offline bundle. It can be either `/var/lib/containers` or a [custom location](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-oci-compliant-registry#prerequisites-for-hydrating-the-registry). Ensure you have a minimum of 100 GB of storage. It is recommended to have 256 GB of storage. |

To upload the Automation Suite images to the registry:

1. Ensure that we have the necessary permissions to execute the shell script, by running the following command:
   ```
   chmod +x hydrate-registry.sh
   ```
2. Upload the Automation Suite images to your registry by running the following command:
   ```
   ./hydrate-registry.sh --target-registry-url my.registry.io:443 --offline-bundle-path /path/to/as-cmk.tar.gz --extract-path /tmp
   ```

:::note
For registries, such as Harbor, which require using a project, make sure you append the project name to the target registry URL you include in the command, as shown in the following example: assignment
```
./hydrate-registry.sh --target-registry-url my.registry.io:443/myproject --offline-bundle-path /path/to/as-cmk.tar.gz
```
For Document Understanding offline bundles, make sure to include `--extract-path` in the command, as shown in the following example: assignment
```
./hydrate-registry.sh --target-registry-url my.registry.io:443 --optional-bundle-path ./dusemistructured-2023.10.0.tar.gz --extract-path /tmp
```
:::

## Configuring the certificate for the external OCI-compliant registry

To properly configure your external OCI-compliant registry, you must update the trust store of all the machines on which you plan to install Automation Suite. For instructions on how to perform this step post-installation, see.