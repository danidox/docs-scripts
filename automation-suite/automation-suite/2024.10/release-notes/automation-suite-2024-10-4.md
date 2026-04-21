---
title: "2024.10.4"
visible: true
slug: "automation-suite-2024-10-4"
---

**Release date: June 26, 2025**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## Changes to the patching procedure

The procedure for applying patches now includes an additional step that requires you to download and use the corresponding `uipathctl` patch version before proceeding with the patch.

For more details, refer to [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/applying-a-patch).

## Deprecation of UiPath Backup based on NFS server

Starting with Automation Suite 2025.10, NFS server-based backups will not be supported if you are using an external objectstore. Your backups will be stored directly in the external objectstore. If you are upgrading to 2025.10, you are encouraged to switch to the external objectstore for backups.

Learn more about [Configuring the external objectstore](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/configuring-the-external-objectstore) or reach out to support.

## Bug fixes

* **Erratum - added July 17, 2025**: We have fixed an issue where uploading large Document Understanding bundles caused nodes to go out of memory due to parallel loading of large-sized image layers into memory.
* An issue was causing the Task Mining service to fail to initialize in certain Kerberos environments. This occurred due to missing configuration or parameters related to keytab secrets and app settings. We have fixed the issue.
* An issue was causing the addition process of agent nodes to fail in offline environments. We have fixed the issue.
* We have fixed an issue causing frequent restarts of deployments in the `uipath` namespace during offline installations due to inconsistent `istio-ingressgateway-certs` secrets across namespaces.
* We have fixed an issue causing Automation Suite installations to fail due to Certificate Authority (CA) certificates not being recognized. The issue occurred when the `CertificatePolicies` section included policy OID values exceeding 4 bytes.
* We have fixed an issue causing the custom changes made to the RKE2 configuration file (`/etc/rancher/rke2/config.yaml`) to be overwritten during upgrades. Now, the custom configurations are preserved.
* We have fixed an issue where the Process Mining portal failed to load the process apps.
* Log forwarding did not work in proxy setups because the proxy environment variables were not set in the logging pods. We have fixed the issue.
* Licensing SQL connection errors occurred when the Data Source property specified both a named instance and a port. We have fixed the issue.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/security-and-compliance).

### AI Center in-cluster proxy connectivity issue

**Erratum - added December 19, 2025:** An issue prevents AI Center pods from connecting to the in-cluster object store in proxy-enabled environments. This occurs due to unsupported CIDR notations and FQDN regex patterns in the `no_proxy` configuration.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/ai-center-in-cluster-proxy-issue) section.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Prerequisite checks fail when Process Mining is enabled

**Erratum - added December 19, 2025:** An issue causes the prerequisite checks to fail when Process Mining is enabled. The issue occurs due to the checks still requiring `cert-manager`, although `cert-manager` is no longer needed for Process Mining starting with Automation Suite 2024.10.3.

The failure message is a false positive and can be safely ignored.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Pre-upgrade command fails with proxy and external objectstore

**Erratum - added December 19, 2025:** An issue prevents the `uipathctl cluster pre-upgrade` command from completing successfully in environments configured with a proxy and external objectstore. The issue occurs due to an error during the Insights volume migration process.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Upgrade failure during posthook import in chained upgrades

**Erratum - added December 19, 2025:** An issue causes the upgrade to fail during the execution of the `uipathctl rke2 upgrade` command in chained upgrade scenarios. This issue occurs due to the posthook secret and configmap import operation not being idempotent, which leads to conflicts with existing Kubernetes objects.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/upgrade-failure-during-posthook-import) section.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Kerberos keytab rotation does not trigger token regeneration

**Erratum - added September 24, 2025:** An issue causes Kerberos keytab rotation to not immediately regenerate authentication tokens, which may lead to temporary connectivity disruptions between services and the database.

To address the issue, you must manually trigger the Kerberos ticket renewal cronjob by running the following command:

```
kubectl delete job tgt-rotate-manual -n uipath --ignore-not-found ; kubectl create job tgt-rotate-manual --from=cronjob/kerberos-tgt-update -n uipath
```

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Registry certificates not fully updated in offline scenarios

**Erratum - added September 24, 2025:** An issue causes the `uipathctl config tls-certificates` command to update only the internal certificate, while missing the certificate required by Argo CD to trust the in-cluster registry in offline scenarios.

To address the issue, you must run the following command to explicitly update the ArgoCD registry certificate in internal–external registry scenarios:

```
./bin/uipathctl config argocd ca-certificates update --cacert [PATH]
```

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### GPU enablement fails with external registries containing project names

**Erratum - added September 24, 2025:** An issue prevents GPU enablement after adding a GPU node when using external registries with project names (such as Harbor). The required pods do not start and display an `ImagePullBackoff` error.

If you are using an external registry with a project name, update the NVIDIA device plugin daemonset with the following command:

```
# Replace REGISTRY_WITH_PROJECT_NAME with the correct value (Eg. my.registry.io:443/myproject)
# Replcae TAG with the correct value. You can get this from the <installer_directory>/versions/docker-images.json file (Eg. v0.17.1)
kubectl set image daemonset/nvidia-device-plugin-daemonset \
  -n kube-system \
  nvidia-device-plugin-ctr=<REGISTRY_WITH_PROJECT_NAME>/k8s-device-plugin:<TAG>
```

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Orchestrator does not start when using user-assigned managed identity

**Erratum - added September 24, 2025:** An issue prevents the `storage.useClientID` parameter from being set when you select a user-assigned managed identity for object storage. As a result, Orchestrator cannot start in environments where access is restricted to user-assigned managed identities.

To address the issue, you must manually set the parameter in ArgoCD, as follows:

1. In the ArgoCD Orchestrator application, go to **Details** &gt; **Parameters**.
2. In the **values** text box, set `storage.isExternal : true` and save.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Temporary registry installation timeout

**Erratum - added September 24, 2025:** An issue causes the temporary registry installation to fail with a timeout error when connecting to `registry-1.docker.io`. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/unable-to-install-temporary-registry) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Thanos compactor stops on corrupted blocks

**Erratum - added September 24, 2025:** An issue causes the Thanos compactor to stop compacting metrics when it encounters corrupted blocks in the object store. This prevents compaction and leads to increased storage usage.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/failure-to-compact-metrics-due-to-corrupted-blocks-in-thanos) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Upgrade fails during rook-ceph app deletion

**Erratum - added September 24, 2025:** An issue causes the upgrade to fail at the pre-upgrade stage and get stuck while deleting the rook-ceph ArgoCD application. This issue occurs when upgrading from Automation Suite 2023.10.10 to version 2024.10.4.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/upgrade-stuck-on-rook-ceph-application-deletion) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Garbage collection fails during registry cleanup

**Erratum - added September 24, 2025:** An issue prevents garbage collection from executing correctly during in-cluster registry cleanup. This may result in unused images not being cleaned up as expected.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/how-to-clean-up-unused-docker-images-from-registry-pods) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2024.10.4](https://docs.uipath.com/automation-hub/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [Automation Ops 2024.10.4](https://docs.uipath.com/automation-ops/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [AI Center 2024.10.4](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [Action Center 2024.10.4](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-4) |
| [Task Mining 2024.10.4](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [AI Computer Vision 2024.10.4](https://docs-dev.uipath.com/ai-computer-vision/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [Insights 2024.10.4](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [Apps 2024.10.4](https://docs.uipath.com/apps/automation-suite/2024.10/release-notes/2024-10-4) |
| [Process Mining 2024.10.4](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-4) | [Document Understanding AI Center-based projects 2024.10.4](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10)  [Document Understanding modern projects 2024.10.4](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10) | [Orchestrator 2024.10.6](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-6) |  |
|  |  | [Test Manager 2024.10.4](https://docs.uipath.com/test-suite/automation-suite/2024.10/release-notes/test-manager-2024-10-4) |  |
|  |  | [Data Service 2024.10.4](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-4) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.32.3+rke2r1 |
| ArgoCD | v3.0.0 |
| gatekeeper | 3.19.1 |
| rook | 1.17.1 |
| ceph | 19.2.2 |
| prometheus-pushgateway | v3.1.3 |
| cert-manager | v1.17.2 |
| kube-logging/logging-operator | 5.3.0 |
| kube-logging/config-reloader | 5.3.0 |
| istio | 1.25.2 |
| velero | 1.16.0 |
| reloader | v2.1.3 |
| Prometheus | v3.3.0 |
| Grafana | 11.6.1 |
| redis-operator | v7.22.0-7 |
| redis-cluster | v7.22.0-28.focal |
| oauth2-proxy | v7.9.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).