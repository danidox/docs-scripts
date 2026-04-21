---
title: "Kubernetes cluster and nodes"
visible: true
slug: "kubernetes-cluster-and-nodes"
---

## Cluster and permissions

You can bring your own Kubernetes cluster and follow your standard practices to provision and manage it.

If you grant the Automation Suite installer admin privileges, UiPath® installs and manages all the necessary components for running Automation Suite. However, if you cannot grant the installer admin privileges on the cluster, the installation of some required components is impossible. Therefore, before installing Automation Suite on a cluster where you did not grant the installer admin privileges, an admin user must install specific required components separately, before the Automation Suite platform installation. Here are the main steps that you must perform if you cannot grant admin privileges to the Automation Suite installer:

* Install and configure the Istio service mesh. For details, see [Installing and configuring the service mesh](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-service-mesh).
* Bring your own ArgoCD. For details, see [Installing and configuring the GitOps tool](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-gitops-tool).
* Create and manage certificates yourself. For details, see [Certificates generated during installation](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/certificates-overview#certificates-generated-during-installation).
* Create a service account and grant the necessary permissions for the Automation Suite installation. For details, see [Granting installation permissions](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions).

After installing the required components, you can execute the installer with lower permissions. For the list of required permissions, see [Granting installation permissions](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions#granting-installation-permissions).

## Supported EKS/AKS versions

Each Automation Suite Long-Term Support release comes with a compatibility matrix. For compatible EKS or AKS versions, see [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).

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
   <td headers="d48842e85">
    AKS
   </td>
   <td headers="d48842e87">
    <ul>
     <li>
      Ubuntu 22.04
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d48842e85">
    EKS
   </td>
   <td headers="d48842e87">
    <ul>
     <li>
      Amazon Linux 2 up to EKS 1.32
     </li>
     <li>
      Amazon Linux 2023 for all EKS versions
     </li>
     <li>
      Bottlerocket 1.48.0
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

Automation Suite on EKS/AKS only supports the x86 EKS/AKS architecture, and does not support ARM64.

## Node capacity

To estimate node capacity based on your product and scale requirements, use the [UiPath Automation Suite Install Sizing Calculator](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/capacity-planning#capacity-planning).

The root volume requirement for agent (worker) nodes is 256 GB.

At a minimum, to start with the mandatory platform services (Identity, licensing, and routing) and Orchestrator, you must provision 8 vCPU and 16 GB RAM per node.

:::note
We do not recommend using spot instances in Automation Suite in production scenarios, due to stability and performance issues.
:::

## Swap memory

You must disable swap memory before installing Automation Suite. Swap memory is known to cause issues with container workloads. Additionally, Automation Suite workloads do not benefit from using swap memory, and Kubernetes already optimizes memory usage.

## Autoscaling

We recommend enabling autoscaling on your cluster to ensure high reliability and to avoid business interruptions.

## Additional Automation Suite Robots requirements

Automation Suite Robots require additional worker node(s).

The hardware requirements for the Automation Suite Robots node depend on the way you plan to use your resources. In addition to the additional agent node requirements, you also need a minimum of **10 GB** of file storage to enable **[package caching](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#automation-suite-robots-specific-configuration)**.

For details, see [Storage](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#file-storage) documentation.

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

For increased performance, you can install Document Understanding on an additional agent node with GPU support. Note, however, that AI Center-based projects in Document Understanding are fully functional without the GPU node. Actually, Document Understanding uses CPU VMs for all its extraction and classification tasks, while for OCR we strongly recommend the usage of a GPU VM.

For more details about the CPU/GPU usage within the Document Understanding framework, refer to [CPU and GPU Usage](https://docs.uipath.com/document-understanding/automation-suite/2.2510/classic-user-guide/hardware-requirements-ml#cpu-and-gpu-usage).

If you want to use an additional node with GPU support, you must meet the following requirements:

| Hardware | Minimum requirement |
| --- | --- |
| Processor | 8 (v-)CPU/cores |
| RAM | 52 GB |
| OS disk | 256 GB SSD  Min IOPS: 1100 |
| Data disk | N/A |
| GPU RAM | 11 GB |

When adding the GPU node pool, it is important that you use `--node-taints nvidia.com/gpu=present:NoSchedule` instead of `--node-taints sku=gpu:NoSchedule`.

:::important
To ensure proper scheduling of GPU workloads, make sure your DaemonSet (NFD or Nvidia GPU Operator) YAML configuration includes a matching `tolerations` block. You can use the following example: assignment
```
tolerations:
- key: "nvidia.com/gpu"
operator: "Equal"
value: "present"
effect: "NoSchedule"
```
:::

Automation Suite supports NVIDIA GPUs. To learn about how to configure NVDIA GPUs (such as drivers), please refer to the respective docs from [Azure](https://learn.microsoft.com/en-us/azure/aks/gpu-cluster) or [AWS](https://aws.amazon.com/blogs/compute/running-gpu-accelerated-kubernetes-workloads-on-p3-and-p2-ec2-instances-with-amazon-eks/).

### Additional Document Understanding modern projects requirements

With CPU inference activated, a minimum of 2 GPUs is required. To enable CPU inference, set the `enable_cpu_inference` property to `true`, as indicated in the [Enabling or disabling Document Understanding](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide/managing-products#enabling-or-disabling-document-understanding) section.

CAUTION:

:::note
* Inference may be up to 10 times slower.
* We recommend using it for documents with a maximum of 125 pages. No active limitation
is in place. However, inference might fail for documents larger than 125 pages.
:::

Without CPU inference, a minimum of **5 GPUs** is required for Document Understanding modern projects. The example scenario in the following table demonstrates how 5 GPUs is enough to process 300 pages.

:::note
For Document Understanding modern projects, the minimum recommended GPU is NVIDIA T4.
:::

| Function | Number |
| --- | --- |
| Custom model pages processed per hour | 300 |
| Out of the box model pages processed per hour | 0 |
| Models training in parallel | 1 |
| Number of pages in all projects - Design time | 200 |
| Number of document types per project version | 3 |

The 5 GPUs are distributed amongst different functions, as detailed in the following table:

| Service | Number of GPUs |
| --- | --- |
| OCR replicas | 1 |
| Custom model training replicas | 1 |
| Custom model replicas | 2 |
| Out of the box model replicas | 1 |
| **Total** | **5** |

For more information on how to allocate GPUs to each service, check the [Allocating GPU resources for Document Understanding modern projects](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/allocating-gpu-resources-for-document-understanding-modern-projects#allocating-gpu-resources-for-document-understanding-modern-projects) page.

In addition to the GPU demands, Document Understanding modern projects also require specific CPU resources for optimal performance. For optimal performance, a minimum of **18 vCPUs** is required.

With the modern Document Understanding project, an additional 4 TB of the `objectstore` is required to perform the activities from the provided examples continuously for one year. You can start with a smaller number, but the activity will fail once the storage is complete, unless you explicitly scale it.

If you are provisioning for one year of continuous processing, you will need 4 TB for Document Understanding modern projects and 512 GB for the other products. The total will be 4.5 TB of storage. Similarly, if you start with six months of processing, you will need 2 TB for Document Understanding modern projects and 512 GB for the other products. In this case the total will be 2.5 TB.

:::note
For more detailed calculations and the capacity required for your needs, check the [UiPath Automation Suite Install Sizing Calculator](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/capacity-planning#capacity-planning).
:::

### Provisioning MIG-enabled GPUs

Automation Suite Document Understanding workloads support running on Virtual GPUs (VGPUs) created with NVIDIA MIG (Multi-Instance GPU) technology.

To run Document Understanding in these conditions, keep in mind the following requirements:

* **GPU memory (VRAM):** at least **16 GB per VGPU**
  :::note
  UiPath only support the [single strategy](https://docs.nvidia.com/datacenter/cloud-native/kubernetes/latest/index.html#the-single-strategy), meaning that all VGPUs will be exactly the same.
  :::
* **Storage:** at least **80 GB per VGPU**

#### Enabling MIG-enabled GPUs in Kubernetes

After provisioning the MIG enabled GPUs in your cluster with profiles matching or exceeding the above minimum requirements, ensure that the GPUs are schedulable Kubernetes. The node must report a non-zero number of GPUs before workloads can be scheduled on it.

To make the GPUs schedulable, you have two options:

* **Option A:** Follow the official GPU setup documentation of your cloud provider:
  + [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu?tabs=add-ubuntu-gpu-node-pool)
  + [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/blogs/containers/maximizing-gpu-utilization-with-nvidias-multi-instance-gpu-mig-on-amazon-eks-running-more-pods-per-gpu-for-enhanced-performance/)
* **Option B (Alternative):** Deploy the NVIDIA device plugin directly:
  1. Create a new namespace:
     ```
     kubectl create namespace gpu-resources
     ```
  2. Apply the following configuration, replacing `migEnabledPoolName` with the label that matches your GPU node:
     ```
     apiVersion: v1
     kind: Pod
     metadata:
       name: nvidia-device-plugin-pod
       namespace: gpu-resources
     spec:
      affinity:
         nodeAffinity:
           requiredDuringSchedulingIgnoredDuringExecution:
             nodeSelectorTerms:
             - matchExpressions:
               - key: agentpool
                 operator: In
                 values:
                 # To be changed to a selector that matches the GPU nodes
                 - migEnabledPoolName
      containers:
      - args:
        - --fail-on-init-error=false
        env:
        - name: MPS_ROOT
          value: /run/nvidia/mps
        - name: MIG_STRATEGY
           # We only support the single strategy for now
          value: single
        - name: NVIDIA_MIG_MONITOR_DEVICES
          value: all
        - name: NVIDIA_VISIBLE_DEVICES
          value: all
        - name: NVIDIA_DRIVER_CAPABILITIES
          value: compute,utility
        image: nvcr.io/nvidia/k8s-device-plugin:v0.17.3
        imagePullPolicy: IfNotPresent
        name: nvidia-device-plugin-ctr
        securityContext:
          allowPrivilegeEscalation: true
          capabilities:
            add:
            - SYS_ADMIN
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /var/lib/kubelet/device-plugins
          name: device-plugin
      tolerations:
      - key: CriticalAddonsOnly
        operator: Exists
      - effect: NoSchedule
        key: nvidia.com/gpu
        operator: Exists
      terminationGracePeriodSeconds: 30
      volumes:
      - hostPath:
          path: /var/lib/kubelet/device-plugins
          type: ""
        name: device-plugin
     ```

After deploying the plugin, the node’s **Allocatable** section should show the correct number of VGPUs under `nvidia.com/gpu`, based on the MIG profile you configured. The node should now be schedulable and ready to run Document Understanding workloads.

## Node scheduling

We recommend enabling node taints on dedicated worker nodes for Automation Suite Robots and Document Understanding.

AI Center and DU example:

* For CPU:
  ```
  kubectl taint node <node_name> aic.ml/cpu=present:NoSchedule
  ```

* For GPU:
  ```
  kubectl taint node <node_name> nvidia.com/gpu=present:NoSchedule
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