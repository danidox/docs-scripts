---
title: "Kubernetes cluster and nodes"
visible: true
slug: "requirements"
---

## Dedicated cluster

You can bring your own Kubernetes cluster from Azure or AWS and follow your standard practices to provision and manage it. Automation Suite requires a **dedicated cluster with cluster admin privileges** because it deploys the entire UiPath® business platform, and it comprises many UiPath® products that include many micro-services.

## Supported EKS/AKS versions

Each Automation Suite Long-Term Support release comes with a compatibility matrix. For compatible EKS or AKS versions, see [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).

We tested Automation Suite compatibility with the following Linux OSes:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Cloud provider
   </th>
   <th>
    OS
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d33382e51">
    AKS
   </td>
   <td headers="d33382e53">
    <ul>
     <li>
      Ubuntu 22.04
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d33382e51">
    EKS
   </td>
   <td headers="d33382e53">
    <ul>
     <li>
      Amazon Linux 2 and Amazon Linux 2023 for all EKS versions
     </li>
     <li>
      RHEL 8.8 for EKS 1.27
     </li>
     <li>
      Bottlerocket 1.19.2
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

Automation Suite on EKS/AKS only supports the x86 EKS/AKS architecture, and does not support ARM64.

## Node capacity

To estimate node capacity based on your product and scale requirements, use the [UiPath Automation Suite Install Sizing Calculator](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/capacity-planning#capacity-planning).

The root volume requirement for agent (worker) nodes is 256 GB.

At a minimum, to start with the mandatory platform services (Identity, licensing, and routing) and Orchestrator, you must provision 8 vCPU and 16 GB RAM per node.

:::note
We do not recommend using spot instances in Automation Suite in production scenarios, due to stability and performance issues.
:::

## Swap memory

You must disable swap memory before installing Automation Suite. Swap memory is known to cause issues with container workloads. Additionally, Automation Suite workloads do not benefit from using swap memory, and Kubernetes already optimizes memory usage.

## Autoscaling

We recommend enabling autoscaling on your cluster to ensure high reliability and to avoid business interruptions.

## Additional Task Mining requirements

If you install Task Mining, you must provision additional worker node(s) with 20 vCPU and 60 GB RAM. This node must be tainted to ensure only Task Mining workloads run on it. For details, see the [Node scheduling](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/kubernetes-cluster-and-nodes#node-scheduling) section.

## Additional Automation Suite Robots requirements

Automation Suite Robots require additional worker node(s).

The hardware requirements for the Automation Suite Robots node depend on the way you plan to use your resources. In addition to the additional agent node requirements, you also need a minimum of **10 GB** of file storage to enable **[package caching](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#automation-suite-robots-specific-configuration)**.

For details, see [Storage](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/storage#file-storage) documentation.

The following sections describe the factors that impact the amount of hardware the Automation Suite Robots node requires.

### Robot size

The following table describes the required CPU, memory, and storage for all robot sizes.

| Size | CPU | Memory | Storage |
| --- | --- | --- | --- |
| Small | 0.5 | 1 GB | 1 GB |
| Standard | 1 | 2 GB | 2 GB |
| Medium | 2 | 4 GB | 4 GB |
| Large | 6 | 10 GB | 10 GB |

### Agent node size

The resources of the Automation Suite Robots agent node have an impact on the number of jobs that can be run concurrently. The reason is that the number of CPU cores and the amount of RAM capacity are divided by the CPU/memory requirements of the job.

For example, a node with 16 CPUs and 32 GB of RAM would be able to run any of the following:

* 32 Small jobs
* 16 Standard jobs
* 8 Medium jobs
* 2 Large jobs

Job sizes can be mixed, so at any given moment, the same node could run a combination of jobs, such as the following:

* 10 Small jobs (consuming 5 CPUs and 10 GB of memory)
* 4 Standard jobs (consuming 4 CPUs and 8 GB of memory)
* 3 Medium jobs (consuming 6 CPUs and 12 GB of memory)

### Kubernetes resource consumption

Given that the node is part of a Kubernetes cluster, the Kubernetes agent present on the server (kubelet) consumes a small amount of resources. Based on our measurements, the kubelet consumes the following resources:

* 0.6 CPU
* 0.4 GB RAM

A node similar to the one previously described would actually have approximately 15.4 CPUs and 31.6 GB of RAM.

### Automatic machine size selection

All your cross-platform processes have the **Automation Suite Robots** option set to **Automatic** by default. This setting selects the appropriate machine size for running the process using serverless robots.

When automatically choosing the size, the criteria listed in the below table are evaluated in order. As soon as one criterion is satisfied, the corresponding machine size is chosen and the remaining criteria are not evaluated.

| Order | Criterion | Machine size |
| --- | --- | --- |
| 1 | Remote debugging job | Medium |
| 2 | Process depends on [UI Automation](https://docs.uipath.com/studio/docs/ui-automation)  OR  Process depends on the [UiPath Document Understanding activities](https://docs.uipath.com/document-understanding/docs/activities-packages) | Standard |
| 3 | Other unattended process | Small |

## Additional Document Understanding recommendations

For increased performance, you can install Document Understanding on an additional agent node with GPU support. Note, however, that Document Understanding is fully functional without the GPU node. Actually, Document Understanding uses CPU VMs for all its extraction and classification tasks, while for OCR we strongly recommend the usage of a GPU VM.

For more details about the CPU/GPU usage within the Document Understanding framework, refer to [CPU and GPU Usage](https://docs.uipath.com/document-understanding/automation-suite/2023.10/classic-user-guide/hardware-requirements-ml#cpu-and-gpu-usage).

If you want to use an additional node with GPU support, you must meet the following requirements:

| Hardware | Minimum requirement |
| --- | --- |
| Processor | 8 (v-)CPU/cores |
| RAM | 52 GB |
| Cluster binaries and state disk | 256 GB SSD  Min IOPS: 1100 |
| Data disk | N/A |
| GPU RAM | 11 GB |

When adding the GPU node pool, it is important that you use `--node-taints nvidia.com/gpu=present:NoSchedule` instead of `--node-taints sku=gpu:NoSchedule`.

:::important
To ensure proper scheduling of GPU workloads, make sure your DaemonSet YAML configuration includes a matching `tolerations` block. You can use the following example: assignment
```
tolerations:
- key: "nvidia.com/gpu"
operator: "Equal"
value: "present"
effect: "NoSchedule"
```
:::

Automation Suite supports NVIDIA GPUs. To learn about how to configure NVDIA GPU (such as drivers), please refer to the respective docs from [Azure](https://learn.microsoft.com/en-us/azure/aks/gpu-cluster) or [AWS](https://aws.amazon.com/blogs/compute/running-gpu-accelerated-kubernetes-workloads-on-p3-and-p2-ec2-instances-with-amazon-eks/).

## Node scheduling

We recommend enabling node taints on dedicated worker nodes for Task Mining, Automation Suite Robots, and Document Understanding.

AI Center and DU example:

* For CPU:
  ```
  kubectl taint node <node_name> aic.ml/cpu=present:NoSchedule
  ```

* For GPU:
  ```
  kubectl taint node <node_name> nvidia.com/gpu=present:NoSchedule
  ```

Task Mining example:

```
kubectl taint node <node_name> task.mining/cpu=present:NoSchedule
```

Automation Suite Robots example:

* add a taint for serverless robots using the following command:
  ```
  kubectl taint node <node_name> serverless.robot=present:NoSchedule
  ```
* add the labels for serverless robots using the following command:
  ```
  kubectl label node <node_name> serverless.robot=true serverless.daemon=true
  ```

:::important
If you have custom node taints that are enforced by Gatekeeper Policy, such as specific roles for worker nodes or labels, they will not be passed to Automation Suite and may interrupt the installation process.
:::

To learn about taints and tolerations, see [Kubernetes documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).