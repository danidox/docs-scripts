---
title: "2023.10.10"
visible: true
slug: "automation-suite-2023-10-10"
---

**Release date: June 26, 2025**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## What's new

This Automation Suite version brings various small bug fixes and improvements.

## Bug fixes

* An issue was causing the Task Mining service to fail to initialize in certain Kerberos environments. This occurred due to missing configuration or parameters related to keytab secrets and app settings. We have fixed the issue.
* An issue was causing the addition process of agent nodes to fail in offline environments. We have fixed the issue.
* We have fixed an issue causing Automation Suite installations to fail due to Certificate Authority (CA) certificates not being recognized. The issue occurred when the `CertificatePolicies` section included policy OID values exceeding 4 bytes.
* We have fixed an issue causing the custom changes made to the RKE2 configuration file (`/etc/rancher/rke2/config.yaml`) to be overwritten during upgrades. Now, the custom configurations are preserved.
* Licensing SQL connection errors occurred when the Data Source property specified both a named instance and a port. We have fixed the issue.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/security-and-compliance).

### Kerberos keytab rotation does not trigger token regeneration

**Erratum - added September 24, 2025:** An issue causes Kerberos keytab rotation to not immediately regenerate authentication tokens, which may lead to temporary connectivity disruptions between services and the database.

To address the issue, you must manually trigger the Kerberos ticket renewal cronjob by running the following command:

```
kubectl delete job tgt-rotate-manual -n uipath --ignore-not-found ; kubectl create job tgt-rotate-manual --from=cronjob/kerberos-tgt-update -n uipath
```

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-11#bug-fixes).

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

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-11#bug-fixes).

### Orchestrator does not start when using user-assigned managed identity

**Erratum - added September 24, 2025:** An issue prevents the `storage.useClientID` parameter from being set when you select a user-assigned managed identity for object storage. As a result, tOrchestrator cannot start in environments where access is restricted to user-assigned managed identities.

To address the issue, you must manually set the parameter in ArgoCD, as follows:

1. In the ArgoCD Orchestrator application, go to **Details** &gt; **Parameters**.
2. In the **values** text box, set `storage.isExternal : true` and save.

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-11#bug-fixes).

### Thanos compactor stops on corrupted blocks

**Erratum - added September 24, 2025:** An issue causes the Thanos compactor to stop compacting metrics when it encounters corrupted blocks in the object store. This prevents compaction and leads to increased storage usage.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/failure-to-compact-metrics-due-to-corrupted-blocks-in-thanos) section.

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-11#bug-fixes).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2023.10.10](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-10) | [Automation Ops 2023.10.10](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/release-notes-2023-10-10) | [AI Center 2023.10.10](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-10) | [Action Center 2023.10.10](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-10) |
| [Task Mining 2023.10.10](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-10) | [AI Computer Vision 2023.10.10](https://docs.uipath.com/ai-computer-vision/automation-suite/2023.10/user-guide/release-notes-2023-10-10) | [Insights 2023.10.10](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-10) | [Apps 2023.10.10](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-10) |
| [Process Mining 2023.10.10](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-10) | [Document Understanding 2023.10.10](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10) | [Orchestrator 2023.10.11](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-11) |  |
|  |  | [Test Manager 2023.10.10](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-10) |  |
|  |  | [Data Service 2023.10.10](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-10) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.32.3+rke2r1 |
| ArgoCD | v3.0.0 |
| Grafana | 11.6.1 |
| ceph | 19.2.2 |
| rook-ceph | 1.17.1 |
| prometheus-pushgateway | v3.1.3 |
| cert-manager | v1.17.2 |
| rancher-istio | 105.4.0-up1.23.2 |
| rancher-monitoring-crd | 106.0.1-up66.7.1-rancher.10 |
| rancher-gatekeeper | 104.0.1-up3.13.0 |
| rancher-monitoring | 106.0.1-up66.7.1-rancher.10 |
| longhorn | 1.8.1 |
| longhorn-crd | 1.1.100 |
| reloader | v2.1.3 |
| kube-logging/logging-operator | 5.3.0 |
| kube-logging/config-reloader | 5.3.0 |
| velero | 1.16.0 |
| csi-driver-smb | v1.16.0 |
| redis-operator | v7.22.0-7 |
| redis-cluster | v7.22.0-28.focal |
| oauth2-proxy | v7.9.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).