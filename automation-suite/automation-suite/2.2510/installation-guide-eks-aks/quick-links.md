---
title: "Quick links"
visible: true
slug: "quick-links"
---

## Before you begin

| Step | Details |
| --- | --- |
| Find out the essentials on Disaster Recovery - Active/Passive deployments | [Overview](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/overview-active-passive-active-active-deployments#overview) |
| Learn more on the architecture of Disaster Recovery - Active/Passive deployments | [Basic architecture considerations](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/basic-architecture-considerations#basic-architecture-considerations) |
| Frequently asked questions | [Q&A: Disaster Recovery](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/qa-multi-site-deployments#q%26amp%3Ba%3A-disaster-recovery) |

## Installing a new Automation Suite setup

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2">
    <p>
     Step
    </p>
   </th>
   <th>
    <p>
     Details
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d37568e68" rowspan="3">
    <p>
     Install the primary server
    </p>
   </td>
   <td headers="d37568e68">
    Generate the
    <code>
     input.json
    </code>
    file using the interactive installer.
   </td>
   <td headers="d37568e71">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#configuring-inputjson">
      Configuring input.json
     </a>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37568e68">
    Update the
    <code>
     input.json
    </code>
    file.
   </td>
   <td headers="d37568e71">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery-installation#disaster-recovery%3A-active%2Fpassive-configurations">
      Advanced installation experience
     </a>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37568e68">
    <p>
     Resume the installation.
    </p>
   </td>
   <td headers="d37568e71">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-automation-suite#installing-automation-suite">
      Installing Automation Suite
     </a>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37568e68" rowspan="3">
    <p>
     Install the secondary server
    </p>
   </td>
   <td headers="d37568e68">
    <p>
     Copy or generate the
     <code>
      input.json
     </code>
     from the primary server.
    </p>
   </td>
   <td headers="d37568e71">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-the-secondary-cluster#generating-or-copying-the-configuration-file-of-the-primary-cluster">
      Generating or copying the configuration file of the primary cluster
     </a>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37568e68">
    <p>
     Update the
     <code>
      input.json
     </code>
     file.
    </p>
   </td>
   <td headers="d37568e71">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery-installation#disaster-recovery%3A-active%2Fpassive-configurations">
      Advanced installation experience
     </a>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37568e68">
    <p>
     Resume the installation.
    </p>
   </td>
   <td headers="d37568e71">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-automation-suite#installing-automation-suite">
      Installing Automation Suite
     </a>
    </p>
    Note:
    <p>
     For Active/Passive configurations, make sure to switch off the products in the passive cluster. For details, see
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-the-secondary-cluster#switching-off-inactive-products">
      Switching off inactive products
     </a>
     .
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Converting an existing setup

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2">
    <p>
     Step
    </p>
   </th>
   <th>
    <p>
     Details
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d37568e167" rowspan="2">
    <p>
     Converting an existing installation to a Disaster Recovery - Active/Passive setup
    </p>
   </td>
   <td headers="d37568e167">
    <p>
     Convert the standalone Automation Suite cluster into the primary cluster
    </p>
   </td>
   <td headers="d37568e170">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/converting-an-existing-installation-to-multi-site-setup#converting-a-standalone-cluster-into-a-primary-cluster">
      Converting a standalone cluster into a primary cluster
     </a>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37568e167">
    <p>
     Install secondary Automation Suite cluster.
    </p>
   </td>
   <td headers="d37568e170">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-the-secondary-cluster#disaster-recovery---installing-the-secondary-cluster">
      Disaster recovery - Installing the secondary cluster
     </a>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37568e167">
    Switching to the secondary cluster
   </td>
   <td headers="d37568e167">
    <p>
     N/A
    </p>
   </td>
   <td headers="d37568e170">
    <p>
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/switching-to-the-secondary-cluster#switching-to-the-secondary-cluster-manually-in-an-active%2Fpassive-setup" title="This section provides high-level instructions on how to manually switch the traffic to the secondary cluster in an Active/Passive setup.">
      Switching to the secondary cluster
     </a>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37568e167">
    <p>
     Upgrading an Active/Passive deployment
    </p>
   </td>
   <td headers="d37568e167">
    <p>
     N/A
    </p>
   </td>
   <td headers="d37568e170">
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/upgrading-an-active-passive-or-active-active-deployment#guidelines-on-upgrading-an-active%2Fpassive-deployment">
     Upgrading an Active/Passive deployment
    </a>
   </td>
  </tr>
  <tr>
   <td headers="d37568e167">
    <p>
     Backing up and restoring an Active/Passive deployment
    </p>
   </td>
   <td headers="d37568e167">
    <p>
     N/A
    </p>
   </td>
   <td headers="d37568e170">
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/backing-up-and-restoring-an-active-passive-or-active-active-deployment#guidelines-on-backing-up-and-restoring-an-active%2Fpassive-deployment">
     Backing up and restoring an Active/Passive deployment
    </a>
   </td>
  </tr>
 </tbody>
</table>