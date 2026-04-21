---
title: "Deployment scenarios"
visible: true
slug: "deployment-scenarios"
---

## Online deployment

An **online deployment** of Automation Suite is one that requires internet access during installation and runtime. All the UiPath® products and supporting libraries are hosted in the UiPath® registry or UiPath-trusted third-party store.

You can limit access to the internet with the help of a restricted firewall or a proxy server by blocking all the traffic over the internet other than what is required by Automation Suite. For more details on firewall or proxy rules, see [Configuring the proxy](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-proxy#proxy).

## Offline deployment

An **offline deployment** (air-gapped) is a completely isolated setup without access to the internet. This type of setup requires the installation of an additional registry to store all the UiPath® products' container images and binaries, which are shipped in the form of tarball.

:::note
You are not allowed to change the deployment method post-installation. This means that you cannot change to offline if the installation is done online and vice versa. It is recommended to choose your deployment strategy after careful consideration.
:::

## Automation Suite on EKS deployment

### Deployment architecture

You can reference the following architecture diagrams to deploy Automation Suite on EKS.

**Online deployment**
![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/279141)

**Offline deployment**
![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/330697)

### Overview

The previous architecture diagram depicts how Automation Suite can be set up on the AWS EKS cluster.

An EKS cluster is deployed in a single AWS region, where the EC2 worker nodes are in an autoscaling group distributed across three availability zones. The distribution of nodes across availability zones is what brings resiliency to complete zone failure.

Each zone has a private subnet and a public subnet. EC2 worker nodes are hosted in a private subnet, whereas the public subnet hosts an elastic IP address and NAT gateway. The NAT gateway is required to connect to the internet while accessing the EKS control plane from the worker nodes and connecting to the docker registry to get the container images for the Automation Suite deployment.

Elastic IP addresses hosted in each public subnet are passed to Automation Suite during installation to register that as an endpoint where Istio must listen for any incoming traffic. For the same reason, the Network Load Balancer (NLB) must use these endpoints to forward any request made to Automation Suite.

Datasources such as Amazon RDS for Microsoft SQL Server, S3 bucket, Elastic File System, and Elastic Cache should be set up to have enough redundancy in case of failure and must be accessed from the private subnet where the EC2 worker instances are hosted.

:::note
* Automation Suite has no affinity rules to ensure that the worker pods are distributed equally across the zone. If there is
any zone-level failure, there may be a momentary degradation of the service, which would be resolved when that service is automatically moved to a new zone by the EKS control plane.
* Insights requires the EBS volumes to store the dashboard and the other metadata. In AWS, EBS volumes are tied to the zone
in which they are present and do not move when the zone is down. Insights will not be available until the zone on which insights were scheduled is recovered.
* EKS does not enable autoscaling by default, as opposed to AKS. To activate this feature, you typically need to install and
configure additional software like [Metrics Server](https://github.com/kubernetes-sigs/metrics-server) and [Cluster-Autoscaler,](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html) or alternative solutions that provide similar autoscaling capabilities.
:::

## Automation Suite on AKS deployment

### Deployment architecture

You can reference the following architecture diagrams to deploy Automation Suite on AKS.

**Online deployment**
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/559285)

**Offline deployment**
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/330701)

### Overview

An AKS cluster is deployed in a single region where the worker nodes are distributed across the system and user node pools. The core AKS components (except the control plane)are hosted in the system node pool, such as CNI, CoreDNS, etc. Additionally, UiPath® core services are also hosted in the same Node Pool. Additional User Node Pools can host the worker nodes for Automation Suite Robots, Task Mining, and GPU.

Each Node Pool hosts the Virtual Machine Scale Set (VMSS), ensuring that worker nodes are distributed across multiple zones to provide resiliency to zone failure and scale when required.

The static IP address associated with the Load Balancer is passed to Automation Suite during installation to register that as an endpoint where Istio must listen for any incoming traffic. For the same reason, Azure Load Balancer (L4) must use these endpoints to forward any request to Automation Suite.

Datasources such as Microsoft SQL Server, Azure Storage Account, and Azure Redis Cache should be set up to have enough redundancy in case of failure and must be accessed from the subnet where the AKS worker nodes are hosted.

Additionally, there may be a need for an additional Jump Box / Bastion Server, which may have all the required privileges to operate the AKS cluster.

:::note
Automation Suite has no affinity rules to ensure that the worker pods are distributed equally across the zone. If there is any zone-level failure, there may be a momentary degradation of the service, which will be resolved when that service is automatically moved to a new zone by the AKS control plane.
:::