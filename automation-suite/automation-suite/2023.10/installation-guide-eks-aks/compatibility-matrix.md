---
title: "Compatibility matrix"
visible: true
slug: "compatibility-matrix"
---

## Azure third-party component compatibility

The following table lists the third-party software compatible with the latest version of Automation Suite on AKS.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-F35D7A6A-B265-4513-9FA9-B899227CD7D0__TABLE_R2Y_CTY_5CC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Prerequisites for Azure
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
   <td headers="d77753e25">
    Azure Kubernetes Service (AKS)
    <p>
     Architecture
    </p>
   </td>
   <td headers="d77753e29">
    <p>
     x86
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     Ubuntu
    </p>
   </td>
   <td headers="d77753e29">
    <p>
     22.04
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     Cloud Redis
    </p>
   </td>
   <td headers="d77753e29">
    <p>
     Version 6
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     Microsoft SQL Server
    </p>
   </td>
   <td headers="d77753e29">
    <p>
     Microsoft SQL Server 2016, 2017, 2019 and 2022, Standard and Enterprise editions. For product-specific version dependency,
                                 see
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/sql-database#sql-database">
      SQL database
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     PostgreSQL (for Process Mining Airflow database)
    </p>
    Note:
    <p>
     Process Mining on Automation Suite 2023.10.9 or higher.
    </p>
   </td>
   <td headers="d77753e29">
    PostgreSQL 12.x to 16.x are supported. It is recommended to use the most recent version of PostgreSQL within this range for
                              optimal compatibility and performance.
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     Prometheus (if you bring your own)
    </p>
   </td>
   <td headers="d77753e29">
    <p>
     3.5.0
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     Grafana (if you bring your own)
    </p>
   </td>
   <td headers="d77753e29">
    12.0.2
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     Alert Manager (if you bring your own)
    </p>
   </td>
   <td headers="d77753e29">
    <p>
     0.28.1
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     FluentD/Fluent-bit (if you bring your own)
    </p>
    <p>
     helm-charts: logging-operator, logging-operator-logging
    </p>
   </td>
   <td headers="d77753e29">
    <p>
     6.0.1
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
    <p>
     Gatekeeper (if you bring your own)
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
   <td headers="d77753e29">
    <p>
     3.20.0
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
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
   <td headers="d77753e29">
    <p>
     10.0.10
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
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
   <td headers="d77753e29">
    <p>
     1.18.2
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d77753e25">
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
   <td headers="d77753e29">
    1.26.3
   </td>
  </tr>
 </tbody>
</table>

## AWS third-party component compatibility

The following table lists the third-party software compatible with the latest version of Automation Suite on EKS.

| **Prerequisites for AWS** | **Compatible versions** |
| --- | --- |
| Elastic Kubernetes Service (EKS) Architecture | x86 |
| RHEL | 8.8 for EKS 1.33 |
| Amazon Linux | AL2 and AL2023 for all EKS versions except EKS 1.33 where only AL2023 is supported |
| Bottlerocket | 1.19.2 |
| Elasticache | version 6.2.6 |
| Database - RDS | 15.00.4236.7.v1 |
| Prometheus (if you bring your own) | 3.5.0 |
| Grafana (if you bring your own) | 12.0.2 |
| Alert Manager (if you bring your own) | 0.28.1 |
| FluentD/Fluent-bit (if you bring your own)  *helm-charts*: logging-operator, logging-operator-logging | 6.0.1 |
| *Gatekeeper* (if you bring your own)  *helm-charts*: *gatekeeper* | 3.20.0 |
| Velero (if you bring your own)  *helm-charts*: velero | 10.0.10 |
| Cert Manager (if you bring your own)  *helm-charts*: cert-manager | 1.18.2 |
| Istio (if you bring your own)  *helm-charts*: istio-base | 1.26.3 |

## Kubernetes compatibility

:::note
To receive UiPath® support for a particular Automation Suite Cumulative Update (CU), you must use both an Automation Suite version and a Kubernetes version that are currently supported. The support calendar for Automation Suite is available in the **Product lifecycle** section of the [Overview guide](https://docs.uipath.com/overview/other/latest/overview/product-lifecycle#installer-bundle). For the Kubernetes support calendar, see the [Kubernetes documentation](https://kubernetes.io/releases/). Updating your Kubernetes cluster to a supported version may require updating Automation Suite to a newer CU. For example, if you are on Automation Suite 2023.10.0, the last supported version for your cluster is Kubernetes 1.27. As this version reached its end of life, you must update your cluster to a newer Kubernetes version. This also requires updating to a newer Automation Suite CU.
:::

The following table lists the Kubernetes versions compatible with each Automation Suite 2023.10.x CU.

| Automation Suite version | Compatible Kubernetes versions |
| --- | --- |
| 2023.10.12 | 1.31, 1.32, 1.33 |
| 2023.10.11 | 1.31, 1.32, 1.33 |
| 2023.10.10 | 1.30, 1.31, 1.32 |
| 2023.10.9 | 1.30, 1.31, 1.32 |
| 2023.10.8 | 1.29 , 1.30, 1.31 |
| 2023.10.7 | 1.29, 1.30, 1.31 |
| 2023.10.6 | 1.28, 1.29, 1.30 |
| 2023.10.5 | 1.28, 1.29, 1.30 |
| 2023.10.4 | 1.28, 1.29, 1.30 |
| 2023.10.3 | 1.27, 1.28, 1.29 |
| 2023.10.2<sup>*</sup> | 1.26, 1.27, 1.28 |
| 2023.10.1<sup>*</sup> | 1.25, 1.26, 1.27 |
| 2023.10.0<sup>*</sup> | 1.25, 1.26, 1.27 |

*The Automation Suite versions marked with an asterisk (*) are out of support due to all the compatible Kubernetes versions also being out of support.