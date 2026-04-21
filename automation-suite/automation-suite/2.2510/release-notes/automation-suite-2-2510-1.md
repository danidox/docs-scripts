---
title: "2.2510.1"
visible: true
slug: "automation-suite-2-2510-1"
---

**Release date: December 19, 2025**

## Support bundle command no longer requires configuration files

You can generate the support bundle using a simplified command. The paths to the configuration file (`cluster_config.json`) and the versions file (`helm-charts.json`) parameters are now optional.

For details, refer to [Generating the support bundle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide/using-support-bundle-tool#generating-the-support-bundle).

## Bug fixes

* An issue was causing the Automation Suite upgrade to fail during image seeding due to an invalid reference to the `hashicorp/http-echo:1.0` image. We have fixed the issue.
* We have fixed an issue that prevented the `uipathctl rke2 gpu --enable` command from deploying the `nvidia-gpu-plugin` DaemonSet pods on GPU nodes. This issue occurred in offline clusters with an in-cluster registry.
* We have fixed an issue that caused the prerequisite checks to fail when Process Mining was enabled. The issue occurred due to the checks incorrectly treating `cert-manager` as a required component, even though it is no longer needed for Process Mining.
* An issue was causing upgrade operations to fail when the Kubernetes node hostname contained uppercase characters. The issue was due to the upgrade process relying on the system hostname, while Kubernetes automatically normalized the `kubernetes.io/hostname` label to lowercase. We have fixed the issue.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights and Integration Service are not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable these services.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide/security-and-compliance).

### Kerberos authentication limitations

Kerberos-based authentication is currently not supported for Integration Service.

We are working on bringing Kerberos support to upcoming Automation Suite releases.

Meanwhile, you can use alternative authentication mechanisms such as basic authentication or workload identity–based authentication.

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2.2510.1.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | 2.2510.1 | ✅ | [Action Center release notes](https://docs.uipath.com/action-center/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| AI Center | 2.2510.1 | ✅ | [AI Center release notes](https://docs.uipath.com/ai-center/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| AI Computer Vision | 2.2510.1 | ✅ | [AI Computer Vision release notes](https://docs.uipath.com/ai-computer-vision/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| Apps | 2.2510.1 | ✅ | [Apps release notes](https://docs.uipath.com/apps/automation-suite/2.2510/release-notes/2-2510-1) |
| Automation Hub | 2.2510.1 | ✅ | [Automation Hub release notes](https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| Automation Ops | 2.2510.1 | ✅ | [Automation Ops release notes](https://docs.uipath.com/automation-ops/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| Data Service | 2.2510.1 | ✅ | [Data Service release notes](https://docs.uipath.com/data-service/automation-suite/2.2510/release-notes/2-2510-1) |
| Document Understanding | 2.2510.1 | ✅ | [Document Understanding AI Center-based projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2.2510/release-notes/release-notes-22510#225101)  [Document Understanding modern projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2.2510/release-notes/release-notes-22510#225101) |
| Insights | 2.2510.1 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| Integration Service | 2.2510.1 | ✅ | [Integration Service release notes](https://docs.uipath.com/integration-service/automation-suite/2.2510/release-notes/2-2510-1) |
| Solutions | 2.2510.1 | ✅ | [Solutions release notes](https://docs.uipath.com/solutions-management/automation-suite/2.2510/release-notes/2-2510-1) |
| Orchestrator | 2.2510.1 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2.2510/release-notes/2-2510-1) |
| Process Mining | 2.2510.1 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2.2510/user-guide/process-mining-2-2510-1) |
| Test Manager | 2.2510.0 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2.2510/release-notes/test-manager-2-2510-1) |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.34.1+rke2r1 |
| ArgoCD | 3.2.0 |
| gatekeeper | 3.20.1 |
| rook | 1.17.6 |
| ceph | 19.2.3 |
| prometheus-pushgateway | v3.4.2 |
| cert-manager | v1.19.1 |
| kube-logging/logging-operator | 6.0.3 |
| kube-logging/config-reloader | 6.0.3 |
| istio | 1.28.0 |
| velero | 1.16.2 |
| reloader | 2.2.5 |
| Prometheus | 3.7.3 |
| Grafana | 12.2.1 |
| redis-operator | 8.0.2-2 |
| redis-cluster | 8.0.2-17 |
| oauth2-proxy | 7.13.0 |