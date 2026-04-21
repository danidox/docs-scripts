---
title: "2023.10.2"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-2"
---

**Release date: February 28, 2024**

## Support for Microsoft SQL Server 2022

**Erratum - Added March 25, 2024:** We now support Microsoft SQL Server 2022.

## Updated URL proxy allowlist

**Erratum - Added March 18, 2024**: We have removed the following URLs from our URL proxy allowlist:
* `ftp.byfly.by`
* `ftp.gwdg.de`
* `mirror.firstyear.id.au`
* `ftp.lysator.liu.se`
* `mirror-jp.firstyear.id.au`

For more details on the proxy configuration, see [Proxy](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-proxy).

## Updated Kubernetes version support

We have added support for Kubernetes 1.28 and removed support for Kubernetes 1.25. We recommend that you check the [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix) and make sure you upgrade to a supported version, if needed.

## Security enhancements

We continue to provide security updates and patches to address Common Vulnerabilities and Exposures (CVEs).

## Known Issues

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-7#bug-fixes).

### Insights volumes created in two different zones following migration

When you migrate from Automation Suite on Linux to Automation Suite on EKS/AKS, Insights-related volumes are occasionally created in two different zones. As a result, you may encounter issues when bringing up the Insights service. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/insights-pvs-created-in-two-different-zones-following-migration).

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Test Automation SQL connection string is ignored

**Erratum - added October 17, 2024**: When you provide an SQL connection string under the `orchestrator.testautomation` section of the `input.json` file, the `uipathctl` binary ignores the connection string and uses the one under the `orchestrator` section instead. To address the problem, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#test-automation-sql-connection-string-is-ignored) section.

### Pods cannot communicate with FQDN in a proxy environment

**Erratum - added October 17, 2024**: In a proxy environment, if the proxy server uses the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods cannot communicate with the FQDN. The issue causes the following error:
```
System.Net.Http.HttpRequestException: The proxy tunnel request to proxy 'http://<proxyFQDN>:8080/' failed with status code '404'.
```

To fix the issue, see [Automation Suite on EKS/AKS troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pods-cannot-communicate-with-fqdn-via-proxy).

### Temporary network policies not getting cleaned up after health check

**Erratum - added August 14, 2024**: Running a health check creates temporary network policies that are not cleaned up when the check concludes. We fixed the issue in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-5#bug-fixes).

### Unnecessary ListBucket API prerequisite check fails for external objectstore

**Erratum - added August 14, 2024**: For AI Center and Task Mining, the `ListBucket API` prerequisite check fails when using an external objectstore. However, AI Center and Task Mining do not use the `ListBucket API` permission. We removed the unnecessary check in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-5#bug-fixes).

### Issue with saving custom configurations in email settings

**Erratum - added July 3, 2024**: When configuring the email settings, you cannot save any custom configurations due to an issue with form validation. The **Save** button incorrectly appears grayed out, despite filling in all the required fields correctly. As a workaround, you can make a PUT request to the `/identity_/api/setting` endpoint.

Use the appropriate access token and make sure the request body contains the necessary details. Also make sure that `Email.Smtp.UseDefaultCredentials` is set to `True`, like in the following example:

```
{
    "Settings": [
        {
            "Key": "Email.Smtp.Host",
            "Value": "SendGrid"
        },
        {
            "Key": "Email.Smtp.Port",
            "Value": "587"
        },
        {
            "Key": "Email.Smtp.UserName",
            "Value": ""
        },
        {
            "Key": "Email.Smtp.Domain",
            "Value": ""
        },
        {
            "Key": "Email.Smtp.FromEmail",
            "Value": "no-reply@uipath.com"
        },
        {
            "Key": "Email.Smtp.FromDisplayName",
            "Value": "UiPath Platform"
        },
        {
            "Key": "Email.Smtp.EnableSsl",
            "Value": "true"
        },
        {
            "Key": "Email.Smtp.UseDefaultCredentials",
            "Value": "true"
        },
        {
            "Key": "Email.Smtp.Password",
            "Value": ""
        },
        {
            "Key": "Email.Smtp.ConnectionTimeout",
            "Value": "180000"
        }
    ],
    "PartitionGlobalId": ""
}
```

### Installation fails when Velero is enabled

**Erratum - added June 25, 2024**: The Automation Suite installation might fail when Velero is enabled. To fix the issue, follow the steps in [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting).

### The backup setup does not work due to a failure to connect to Azure Government

**Erratum - added June 25, 2024**: Following an Automation Suite on AKS installation or upgrade, the backup setup does not work because of a failure to connect to Azure Government. You can fix the issue by taking the steps described in [Automation Suite on EKS/AKS troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#the-backup-setup-does-not-work-due-to-a-failure-to-connect-to-azure-government).

### Issues affecting Grafana dasboards

**Erratum - added April 19, 2024**: An issue is causing a 404 error when trying to create or import a dashboard in Grafana.

To solve the problem, you need to manually edit the dashboard URL by adding an extra `/dashboard` between the existing `/dashboard` and `/new` or `/import`.

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance).

### Velero backup fails with FailedValidation error

**Erratum - added September 24, 2025:** An issue prevents Velero scheduled backups from running successfully. A `FailedValidation` error message is displayed, indicating that no default backup location can be found. This issue occurs because the `default-bs1` backup storage location is not marked as the default. As a result, Velero cannot identify a valid backup target, and scheduled backups fail.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/velero-backup-fails-with-failedvalidation-error) section.

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-11#bug-fixes).

### Log streaming does not work in proxy setups

**Erratum - added June 26, 2025:** Log forwarding does not work in proxy setups because the proxy environment variables were not set in the logging pods. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/log-streaming-does-not-work-in-proxy-setups) section.

We fixed the issue in [Automation Suite 2023.10.10](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-10#bug-fixes).

### Licensing SQL connection error

**Erratum - added June 26, 2025:** Licensing SQL connection errors occur when the Data Source property specified both a named instance and a port.

We fixed the issue in [Automation Suite 2023.10.10](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-10#bug-fixes).

### Insights dashboards excluded from backups

**Erratum - added April 2, 2025:** An issue is preventing the inclusion of Insights dashboards in backups. To address this issue, refer to the [Backing up the cluster](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/backing-up-the-cluster#prerequisites) page. The issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-8#bug-fixes).

### Fluentd logs transmission failure

**Erratum - added February 13, 2025**: An issue prevents Fluentd from sending logs to remote locations due to a lack of memory buffer. To address this issue, you must add a memory limit for Fluentd to prevent disruptions or delays when transmitting logs to a remote location.

This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-8#bug-fixes).

### Microsoft Entra ID limitations

**Erratum - added January 20, 2025**: Insights and Task Mining do not currently support Microsoft Entra ID (formerly Azure Active Directory) authentication configuration for access to SQL, storage, and other resources that support Microsoft Entra.

### Insights dashboards backup issue

**Erratum - added December 18, 2024** We have identified an issue with the backup logic in Automation Suite for AKS/EKS. Specifically, this defect excludes the backup of Insights dashboards. However, all historical data is successfully backed up.

We are working diligently to resolve this issue. We aim to develop and implement a mitigation approach as early as possible.

If you are using Automation Suite on AKS/EKS along with UiPath Insights, this defect may affect your operations. While we address this issue, we suggest [manually exporting your dashboards](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/dashboards#exporting-and-importing-dashboards) as a preventive measure.

Note that backups are mainly used as a recovery method in the event of a disaster-level incident or in preparation for an Automation Suite upgrade. This is particularly useful if an upgrade fails and stored data needs to be restored to its previous state.

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2023.10.2](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [Automation Ops 2023.10.2](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [AI Center 2023.10.2](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [Action Center 2023.10.2](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-2) |
| [Task Mining 2023.10.2](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [AI Computer Vision 2023.10.2](https://docs.uipath.com/ai-computer-vision/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [Insights 2023.10.2](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [Apps 2023.10.2](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/release-notes-2023-10-2) |
| [Process Mining 2023.10.2](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-2) | [Document Understanding 2023.10.2](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10) | [Orchestrator 2023.10.3](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-3) |  |
|  |  | [Test Manager 2023.10.2](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-2) |  |
|  |  | [Data Service 2023.10.2](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/release-notes-2023-10-2) |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.20.0 |
| ArgoCD | v2.7.7 |
| Prometheus | v2.42.0 |
| Grafana | 10.2.3 |
| Fluentd & Fluent-bit | logging-operator: 4.2.1  logging-operator-logging: 4.2.1 |
| Gatekeeper | 3.12.0 |
| Cert-Manager | v1.12.3 |
| Velero | 3.1.6 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration).