---
title: "Prerequisites at a glance"
visible: true
slug: "prerequisites-at-a-glance"
---

The following table lists the main hardware and software requirements for deploying Automation Suite on EKS/AKS .

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-C4097BCC-A6C1-47E7-8EDC-476DAE9102F0__TABLE_AHS_552_QCC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Component
   </th>
   <th>
    Prerequisites
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d71239e25">
    <p>
     <strong>
      Cluster
     </strong>
    </p>
   </td>
   <td headers="d71239e27">
    <p>
     AKS or EKS cluster
    </p>
    <p>
     See
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/compatibility-matrix">
      Kubernetes version
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     Minimum node capacity
    </strong>
   </td>
   <td headers="d71239e27">
    8 vCPU and 16 GB RAM
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     Total cluster capacity
    </strong>
   </td>
   <td headers="d71239e27">
    See
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/capacity-planning#capacity-planning">
     Capacity planning
    </a>
    .
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     Cache
    </strong>
   </td>
   <td headers="d71239e27">
    <p>
     Redis
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     Registry
    </strong>
   </td>
   <td headers="d71239e27">
    <p>
     OCI-compliant registry required in offline installations
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     SQL Server
    </strong>
   </td>
   <td headers="d71239e27">
    <ul>
     <li>
      Microsoft SQL Server 2017, 2019, and 2022; Standard and Enterprise editions
     </li>
     <li>
      8 (v-)CPU
     </li>
     <li>
      32 GB RAM
     </li>
     <li>
      256 GB SSD
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     Storage
    </strong>
   </td>
   <td headers="d71239e27">
    <ul>
     <li>
      Objectstore - Azure Blob, AWS S3, S3-compaMBle Objectstore
     </li>
     <li>
      Block storage (StorageClass with replication for the Persistent Volume)
     </li>
     <li>
      File system (StorageClass for workloads that do not require replication)
     </li>
     <li>
      Secretstore (optional) - Kubernetes Secret, Azure Key Vault
     </li>
     <li>
      Azure Queue Storage/SQS (required for Integration
                                    Service)
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     Networking
    </strong>
   </td>
   <td headers="d71239e27">
    Network policies, VNETs / VPCs, DNS, subnets, NSGs / security groups, NAT gateway, elastic IP and internet gateway
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <p>
     <strong>
      TLS
     </strong>
    </p>
   </td>
   <td headers="d71239e27">
    <p>
     1.2 or 1.3
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     Certificates
    </strong>
   </td>
   <td headers="d71239e27">
    The certificate for the FQDN to access Automation Suite
   </td>
  </tr>
  <tr>
   <td headers="d71239e25">
    <strong>
     Proxy
    </strong>
   </td>
   <td headers="d71239e27">
    Only required for proxy configurations
   </td>
  </tr>
 </tbody>
</table>