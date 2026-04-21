---
title: "2.2510.1"
visible: true
slug: "automation-suite-on-eks-aks-2-2510-1"
---

**Release date: December 19, 2025**

## Support bundle command no longer requires configuration files

**Erratum - added January 20, 2026:** You can generate the support bundle using a simplified command. The paths to the configuration file (`input.json`) and the versions file (`versions.json`) parameters are now optional.

For details, refer to [Generating the support bundle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/running-the-support-bundle-tool).

## Support for disabling priority class creation

You can now disable priority class creation during deployment. This capability is intended for shared cluster environments where priority classes are not required. To enable it, you must edit the `input.json` configuration file.

For details, refer to [Creating a priority class](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/applying-miscellaneous-configurations#creating-a-priority-class).

## Bug fixes

* We have fixed an issue that caused the prerequisite checks to fail when Process Mining was enabled. The issue occurred due to the checks incorrectly treating `cert-manager` as a required component, even though it is no longer needed for Process Mining.
* The Context Grounding service is now available in EKS environments with IPv6 enabled. This fix restores full functionality to Autopilot for Everyone and the GenAI activities that use Context Grounding.
* This release includes the fixes delivered in [Automation Suite 2.2510.0+patch1](https://docs.uipath.com/automation-suite/automation-suite/2.2510/release-notes/automation-suite-on-eks-aks-2-2510-0-patch-1#225100%2Bpatch1).

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights and Integration Service are not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable these services.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/security-and-compliance).

### Kerberos authentication limitations

Kerberos-based authentication is currently not supported for the following products:

* Integration Service
* Autopilot for Everyone
* AI Trust Layer (LLM Gateway, LLM Observability, Context Grounding)

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
| AI Center | 2.2510.1 | ✅ | [AI Center release notes](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-7) |
| AI Computer Vision | 2.2510.1 | ✅ | [AI Computer Vision reelase notes](https://docs.uipath.com/ai-computer-vision/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| Apps | 2.2510.1 | ✅ | [Apps release notes](https://docs.uipath.com/apps/automation-suite/2.2510/release-notes/2-2510-1) |
| Automation Hub | 2.2510.1 | ✅ | [Automation Hub release notes](https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| Automation Ops | 2.2510.1 | ✅ | [Automation Ops release notes](https://docs.uipath.com/automation-ops/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| Autopilot for Everyone | 2025.9.4 | ✅ | [Autopilot for Everyone release notes](https://docs.uipath.com/autopilot/other/latest/release-notes/2025-9-4) |
| Data Service | 2.2510.1 | ✅ | [Data Service release notes](https://docs.uipath.com/data-service/automation-suite/2.2510/release-notes/2-2510-1) |
| Document Understanding | 2.2510.1 | ✅ | [Document Understanding AI Center-based projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2.2510/release-notes/release-notes-22510#225101)  [Document Understanding modern projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2.2510/release-notes/release-notes-22510#225101) |
| Insights | 2.2510.1 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2.2510/user-guide/release-notes-2-2510-1) |
| Integration Service | 2.2510.1 | ✅ | [Integration Service release notes](https://docs.uipath.com/integration-service/automation-suite/2.2510/release-notes/2-2510-1) |
| Solutions | 2.2510.1 | ✅ | [Solutions release notes](https://docs.uipath.com/solutions-management/automation-suite/2.2510/release-notes/2-2510-1) |
| Orchestrator | 2.2510.1 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2.2510/release-notes/2-2510-1) |
| Process Mining | 2.2510.1 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2.2510/user-guide/process-mining-2-2510-1) |
| Studio Web | 2.2510.1 | ✅ | [Studio Web release notes](https://docs.uipath.com/studio-web/automation-suite/2.2510/release-notes/2-2510-1) |
| Test Manager | 2.2510.1 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2.2510/release-notes/test-manager-2-2510-1) |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.28.0 |
| ArgoCD | 3.2.0 |
| Prometheus | 3.7.3 |
| Grafana | 12.2.1 |
| Fluentd and Fluent-bit | logging-operator: 6.0.3  fluent/fluent-bit: 4.0.3 |
| Gatekeeper | 3.20.1 |
| Cert-Manager | 1.19.1 |
| Velero | 10.1.3 |