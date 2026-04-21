---
title: "Applying a patch"
visible: true
slug: "applying-a-patch"
---

An Automation Suite patch is an update to an existing version, which addresses bugs or security vulnerabilities. For instance, patch 2.2510.0+patch1 addresses issues impacting version 2.2510.0.

:::important
Instead of applying the patch, we recommend upgrading to the Cumulative Update (CU) that contains the same fix. All fixes provided in patches will also be available in the CU mentioned in the release notes for the patch.
:::

To apply a patch to an existing Automation Suite version, take the following steps:

1. **Offline only**. Update the registry with the latest images.
   1. Download the following patch artifacts from [Patch artifact download links](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/patch-artifact-download-links#patch-artifact-download-links). Choose the set of artifacts applicable to your patch and registry configuration type.
      * To mirror the OCI-compliant registry with the UiPath® registry, download the following artifacts:
        + `as-images.txt`
        + `as-helm-charts.txt`
        + `mirror-registry.sh`
      * To hydrate the OCI-compliant registry with the offline bundle, download the following artifacts:
        + `hydrate-registry.sh`
        + `as-cmk.tar.gz`
   2. [Configure the OCI-compliant registry.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-oci-compliant-registry#configuring-the-oci-compliant-registry)
      :::important
      Do not download the artifacts from the links referenced in the instructions on configuring the OCI-compliant registry. Instead, use the download links provided on the [Patch artifact download links](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/patch-artifact-download-links#patch-artifact-download-links) page.
      :::
2. Download the corresponding `uipathctl` patch version from [Patch artifact download links](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/patch-artifact-download-links#patch-artifact-download-links). Replace the current `uipathctl` version with the patched `uipathctl` version.
   :::note
   For details on how to set up `uipathctl` CLI, refer to [Running uipathctl](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/running-uipathctl#running-uipathctl).
   :::
3. Download `versions.json`. For instructions, refer to[Patch artifact download links](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/patch-artifact-download-links#patch-artifact-download-links).
4. Apply the patch by running the following commands:
   ```
   uipathctl cluster patch <path_to_input.json> --versions <path_to_base_versions.json> --skip-oss-prereq --skip-upgrade-readiness --only <PRODUCTS(comma separated)> --patch-dir-path <path to patch version.json files directory>
   ```
   :::note
   `&lt;current versions.json&gt;` refers to the `versions.json` file for the current installation. You can find the file in the following location: `&lt;installer_directory&gt;/versions/helm-charts.json`. You must download the patch `versions.json` into a directory, and pass the directory path to the `--patch-dir-path` parameter.
   :::

The following configuration sample shows how to apply a patch to Orchestrator and Action Center:

   ```
   uipathctl cluster patch <path_to_input.json> --versions <path_to_base_versions.json> --skip-oss-prereq --skip-upgrade-readiness --only orchestrator,action_center --patch-dir-path <path to patch versions.json files directory>
   ```
5. Check if the patch operation was successful by taking the following steps:
   1. Run the following command to list the versions of all services:
      ```
      kubectl -n argocd get application -o wide || helm list -A
      ```
   2. Verify that the versions of the patched services are updated.