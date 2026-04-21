---
title: "Compatibility matrix"
visible: true
slug: "compatibility-matrix"
---

## Azure third-party component compatibility

The following table lists the third-party software compatible with the latest version of Automation Suite on AKS.

| **Prerequisites for Azure** | **Compatible versions** |
| --- | --- |
| Azure Kubernetes Service (AKS) Architecture | x86 |
| Ubuntu | 22.04 |
| Cloud Redis | Version 6 |
| Microsoft SQL Server | Microsoft SQL Server 2016, 2017, 2019, and 2022, Standard and Enterprise editions. For product-specific version dependency, see [SQL database](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#sql-database). |
| PostgreSQL | PostgreSQL 12.x to 16.x are supported. It is recommended to use the most recent version of PostgreSQL within this range for optimal compatibility and performance. |
| Prometheus (if you bring your own) | 3.7.3 |
| Grafana (if you bring your own) | 12.2.1 |
| Alert Manager (if you bring your own) | 0.29.0 |
| FluentD/Fluent-bit (if you bring your own)  helm-charts: logging-operator, logging-operator-logging | 6.0.3 |
| Gatekeeper (if you bring your own)  *helm-charts*: *gatekeeper* | 3.20.1 |
| Velero (if you bring your own)  *helm-charts*: velero | 10.1.3 |
| Cert Manager (if you bring your own)  *helm-charts*: cert-manager | 1.19.1 |
| Istio (if you bring your own)  *helm-charts*: istio-base | 1.28.0 |

## AWS third-party component compatibility

The following table lists the third-party software compatible with the latest version of Automation Suite on EKS.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-F35D7A6A-B265-4513-9FA9-B899227CD7D0__TABLE_QM1_WBX_FCC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Prerequisites for AWS
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Compatible versions
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d80409e160">
    Elastic Kubernetes Service (EKS)
    <p>
     Architecture
    </p>
   </td>
   <td headers="d80409e164">
    <p>
     x86
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Amazon Linux
    </p>
   </td>
   <td headers="d80409e164">
    <ul>
     <li>
      Amazon Linux 2 up to EKS 1.32
     </li>
     <li>
      Amazon Linux 2023 for all EKS versions
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Bottlerocket
    </p>
   </td>
   <td headers="d80409e164">
    <p>
     1.48.0
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Elasticache
    </p>
   </td>
   <td headers="d80409e164">
    <p>
     version 6.2.6
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Database - RDS
    </p>
   </td>
   <td headers="d80409e164">
    <p>
     15.00.4236.7.v1
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Prometheus (if you bring your own)
    </p>
   </td>
   <td headers="d80409e164">
    3.7.3
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Grafana (if you bring your own)
    </p>
   </td>
   <td headers="d80409e164">
    12.2.1
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Alert Manager (if you bring your own)
    </p>
   </td>
   <td headers="d80409e164">
    <p>
     0.29.0
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     FluentD/Fluent-bit (if you bring your own)
    </p>
    <p>
     <em>
      helm-charts
     </em>
     : logging-operator, logging-operator-logging
    </p>
   </td>
   <td headers="d80409e164">
    <p>
     6.0.3
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     <em>
      Gatekeeper
     </em>
     (if you bring your own)
    </p>
    <p>
     <em>
      helm-charts
     </em>
     :
     <em>
      gatekeeper
     </em>
    </p>
   </td>
   <td headers="d80409e164">
    <p>
     3.20.1
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Velero (if you bring your own)
    </p>
    <p>
     <em>
      helm-charts
     </em>
     : velero
    </p>
   </td>
   <td headers="d80409e164">
    <p>
     10.1.3
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Cert Manager (if you bring your own)
    </p>
    <p>
     <em>
      helm-charts
     </em>
     : cert-manager
    </p>
   </td>
   <td headers="d80409e164">
    1.19.1
   </td>
  </tr>
  <tr>
   <td headers="d80409e160">
    <p>
     Istio (if you bring your own)
    </p>
    <p>
     <em>
      helm-charts
     </em>
     : istio-base
    </p>
   </td>
   <td headers="d80409e164">
    1.28.0
   </td>
  </tr>
 </tbody>
</table>

## Kubernetes compatibility

:::note
To receive UiPath® support for a particular Automation Suite Cumulative Update (CU), you must use both an Automation Suite version and a Kubernetes version that are currently supported. The support calendar for Automation Suite is available in the **Product lifecycle** section of the [Overview guide](https://docs.uipath.com/overview/other/latest/overview/product-lifecycle#installer-bundle). For the Kubernetes support calendar, see the [Kubernetes documentation](https://kubernetes.io/releases/). Updating your Kubernetes cluster to a supported version may require updating Automation Suite to a newer CU. For example, if you are on Automation Suite 2.2510.0, the last supported version for your cluster is Kubernetes 1.33. When this version reaches its end of life, you must update your cluster to a newer Kubernetes version. This also requires updating to a newer Automation Suite CU.
:::

The following table lists the Kubernetes versions validated and supported with each Automation Suite 2.2510.x CU.

| Automation Suite version | Compatible Kubernetes versions |
| --- | --- |
| 2.2510.1 | 1.32 , 1.33, 1.34 |
| 2.2510.0 | 1.31, 1.32 , 1.33 |