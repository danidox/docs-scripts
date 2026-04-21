---
title: "Alert runbooks"
visible: true
slug: "alert-runbooks"
---

:::note
* For general
instructions on using the available tools for alerts, metrics, and visualizations, see [Using the monitoring stack](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/using-the-monitoring-stack#using-the-monitoring-stack).
* For more on how
to fix issues and how to create a support bundle for UiPath® Support engineers, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/troubleshooting#troubleshooting).
* When contacting UiPath® Support, please include any alerts that are currently firing.
:::

## Alert severity key

| Alert severity | Description |
| --- | --- |
| Info | Unexpected but harmless. Can be silenced but may be useful during diagnostics. |
| Warning | Indication of a targeted degradation of functionality or a likelihood of degradation in the near future, which may affect the entire cluster. Suggests prompt action (usually within days) to keep cluster healthy. |
| Critical | Known to cause serious degradation of functionality that is often widespread in the cluster. Requires immediate action (same day) to repair cluster. |

## general.rules

### TargetDown

Prometheus is not able to collect metrics from the target in the alert, which means Grafana dashboards and further alerts based on metrics from that target are not be available. Check other alerts pertaining to that target.

## Kubernetes-storage

### KubePersistentVolumeFillingUp

When **Warning**: The available space is less than 30% and is likely to fill up within four days.

When **Critical**: The available space is less than 10%.

For any services that run out of space, data may be difficult to recover, so volumes should be resized before hitting 0% available space.

For Prometheus-specific alerts, see [PrometheusStorageUsage](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/alert-runbooks#alert-runbooks) for more details and instructions.

## kubernetes-apps

### KubePodNotReady

A pod has started, but it is not responding to the health probe with success. This may mean that it is stuck and is not able to serve traffic. You can check pod logs with `kubectl logs` to see if there is any indication of progress. If the issue persists, contact UiPath® Support.

## kubernetes-system-kubelet

### , KubeNodeNotReady, KubeNodeUnreachable, KubeletDown

These alerts indicate a problem with a node. In multi-node HA-ready production clusters, pods would likely be rescheduled onto other nodes. If the issue persists, you should remove and drain the node to maintain the health of the cluster. In clusters without extra capacity, another node should be joined to the cluster first.

If the issues persist, contact UiPath® Support.

## kubernetes-system

### KubernetesMemoryPressure

This alert indicates that memory usage is very high on the Kubernetes node.

The Kubernetes nodes with `MemoryPressure` incident type occurs when a Kubernetes cluster node is running low on memory, which can be caused by a memory leak in an application. This incident type requires immediate attention to prevent any downtime and ensure the proper functioning of the Kubernetes cluster.

If this alert fires, try to identify the pod on the node that is consuming more memory, by taking these steps:

1. Retrieve the nodes CPU and memory stats:
   ```
   kubectl top node
   ```
2. Retrieve the pods running on the node:
   ```
   kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=${NODE_NAME}
   ```
3. Check the memory usage for pods in a namespace using:
   ```
   kubectl top pod --namespace <namespace>
   kubectl logs -f <pod-name> -n <ns>
   ```

If you are able to identify any pod with high memory usage, check the logs of the pod and look for memory leak errors.

To address the issue, increase the memory spec for the nodes if possible.

If the issue persists, generate the[support bundle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/running-the-support-bundle-tool#running-the-support-bundle-tool) and contact UiPath® Support.

### KubernetesDiskPressure

This alert indicates that disk usage is very high on the Kubernetes node.

If this alert fires, try to see which pod is consuming more disk:

* Confirm if the node is under `DiskPressure` using the following command:
  ```
  kubectl describe node <node-name>
  ```

Identify for the `DiskPressure` condition in the output.
* Check the disk space usage on the affected node:
  ```
  df -h
  ```

This shows disk usage on all mounted file systems. Identify where the high usage.
* If the disk is full and cleanup is insufficient, consider resizing the disk for the node (especially in cloud environments such as AWS or GCP). This process may involve expanding volumes, depending on your infrastructure.

## node-exporter

### NodeFilesystemSpaceFillingUp

The filesystem on a particular node is filling up.

If this alert fires, consider the following steps:

* Confirm if the node is under `DiskPressure` using the following command:
  ```
  kubectl describe node <node-name>
  ```

Identify for the `DiskPressure` condition in the output.

* Clear the logs and temporary files. Check for large log files in `/var/log/` and clean them, if possible.
* Check the disk space usage on the affected node:
  ```
  df -h
  ```

This shows disk usage on all mounted file systems. Identify where the high usage.

* If the disk is full and cleanup is insufficient, consider resizing the disk for the node (especially in cloud environments such as AWS or GCP). This process may involve expanding volumes, depending on your infrastructure.

### NodeNetworkReceiveErrs

These errors indicate that the network driver is reporting a high number of failures. This can be caused by physicall hardware failures, or misconfiguration in the physical network. This issue pertains to the OS and is not controlled by the UiPath® application.

The alert is triggered by monitoring the`/proc/net/dev` counter that the linux kernel provides.

Contact your network admin and the team that manages the physical infrastructure.

### NodeNetworkTransmitErrs

These errors indicate that the network driver is reporting a high number of failures. This can be caused by physicall hardware failures, or misconfiguration in the physical network. This issue pertains to the OS and is not controlled by the UiPath® application.

The alert is triggered by monitoring the`/proc/net/dev` counter that the linux kernel provides.

Contact your network admin and the team that manages the physical infrastructure.

## InternodeCommunicationBroken

The node has become unresponsive due to some issue causing broken communication between nodes in the cluster.

If the issue persists, reach out to UiPath® Support with the generated [support bundle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/running-the-support-bundle-tool#running-the-support-bundle-tool).

## uipath.prometheus.resource.provisioning.alerts

### PrometheusMemoryUsage, PrometheusStorageUsage

These alerts warn when the cluster is approaching the configured limits for memory and storage. This is likely to happen on clusters with a recent substantial increase in usage (usually from Robots rather than users), or when nodes are added to the cluster without adjusting Prometheus resources. This is due to an increase in the amount of metrics being collected. This could also be due to a large number of alerts that are being fired, it is important to check why the large amount of alerts are being fired.

If this issue persists, contact UiPath® Support with the generated [support bundle.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/running-the-support-bundle-tool#running-the-support-bundle-tool)

## alertmanager.rules

### AlertmanagerConfigInconsistent

This alert fires when `Alertmanager` instances within the same cluster have different configurations. This could indicate a problem with the configuration rollout which is not consistent across all the instances of `Alertmanager`.

To fix the issue, take the following steps:

1. Run a `diff` tool between all `alertmanager.yml` that are deployed to identify the problem.
2. Delete the incorrect secret and deploy the correct one.

If the issue persists, contact UiPath® Support.

### AlertmanagerFailedReload

AlertManager has failed to load or reload configuration. Please check any custom AlertManager configurations for input errors and otherwise contact UiPath® Support and provide the support bundle. For details, see [Using the Automation Suite support bundle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/running-the-support-bundle-tool#running-the-support-bundle-tool).

### AlertmanagerMembersInconsistent

This alert fires when `Alertmanager` has not found all other members of the cluster.

## UiPathAvailabilityHighTrafficBackend, UiPathAvailabilityMediumTrafficUserFacing, UiPathAvailabilityMediumTrafficBackend, UiPathAvailabilityLowTrafficUserFacing, UiPathAvailabilityLowTrafficBackend

The number of http 500 responses from UiPath® services exceeds a given threshold.

| Traffic level | Number of requests in 20 minutes | Error threshold (for http 500s) |
| --- | --- | --- |
| High | &gt;100,000 | 0.1% |
| Medium | Between 10,000 and 100,000 | 1% |
| Low | &lt; 10,000 | 5% |

Errors in user-facing services would likely result in degraded functionality that is directly observable in the Automation Suite UI, while errors in backend services would have less obvious consequences.

The alert indicates which service is experiencing a high error rate. To understand what cascading issues there may be from other services that the reporting service depends on, you can use the Istio Workload dashboard, which shows errors between services.

Please double check any recently reconfigured Automation Suite products. Detailed logs are also available with the **kubectl logs** command. If the error persists, please contact UiPath® Support.

## uipath.cronjob.alerts.rules

### IdentityKerberosTgtUpdateFailed

This job updates the latest Kerberos ticket to all the UiPath® services. Failures in this job would cause SQL server authentication to fail. Please contact UiPath® Support.

## ceph.rules, cluster-state-alert.rules

### CephMgrIsAbsent

This alert indicates that Ceph Manager has disappeared from Prometheus target discovery.

If this alert fires, check and ensure the the Ceph manager pod is up and running and healthy. If the pod is healthy please check the logs and check if the pod is enable to emit Prometheus metrics.

### CephNodeDown

This alert indicates thata node running Ceph pods is down. While storage operations continue to function as Ceph is designed to deal with a node failure, it is recommended to resolve the issue to minimize the risk of another node going down and affecting storage functions.

If this alert fires, in case of a multi-node cluster, the pod must to be scheduled on another node. Ensure that the new osd pods in `rook-ceph` namespace are running and in healthy state in the new node.

You can check the node failure by describing the node using the following command:

```
kubectl get nodes
```

Check the node to identify the root cause of the issue and contact UiPath® support.

## Ceph Alerts

### CephClusterCriticallyFull

This alert indicates that Ceph storage cluster utilization has crossed 80% and will become read-only at 85%.

If this alert fires, free up some space in Ceph by deleting some unused datasets in AI Center or expand the storage available for Ceph PVC.

Before resizing PVC, make sure you meet the storage requirements. For details, see.

### CephClusterReadOnly

This alert indicates that Ceph storage cluster utilization has crossed 85% and will become read-only now. Free up some space or expand the storage cluster immediately.

If this alert fires, free up some space in Ceph by deleting some unused datasets in AI Center or expand the storage available for Ceph PVC.

Before resizing PVC, make sure you meet the storage requirements. For details, see.

### CephPoolQuotaBytesCriticallyExhausted

This alert indicates that Ceph storage pool usage has crossed 90%.

If this alert fires, free up some space in CEPH by deleting some unused datasets in AI Center or expand the storage available for Ceph PVC.

Before resizing PVC, make sure you meet the storage requirements. For details, see.

### CephClusterErrorState

This alert indicates that the Ceph storage cluster has been in error state for more than 10m.

This alert reflects that the `rook-ceph-mgr` job has been in error state for an unacceptable amount of time. Check for other alerts that might have triggered prior to this one and troubleshoot those first.

### CephOSDCriticallyFull

When the alert severity is **Critical**, the available space is less than 20%.

For any services that run out of space, data may be difficult to recover, so you should resize volumes before hitting 10% available space. See the following instructions:.

## uipath.requestrouting.alerts

### UiPathRequestRouting

Errors in the request routing layer would result in degraded functionality that is directly observable in the Automation Suite UI. The requests will not be routed to backend services.

You can find detailed error log of request routing in `istio-ingressgateway` pods in `istio-system` namespace. Retrieve the pod name by running the following commands:

```
kubectl get pods -n istio-system
kubectl logs <istio-ingressgateway-pod-name> -n istio-system
```

If the error persists, contact UiPath® Support.

## osd-alert.rules

### CephOSDFlapping

This alert indicates that the storage daemon has restarted more than 5 times in last 5 minutes.

If this alert fires, take the following steps:

1. Check the Ceph cluster health. Yuo must run `ceph status` in the Ceph toolbox to identify the flapping OSDs:
   ```
   kubectl -n rook-ceph exec -it <ceph-tools-pod> -- ceph status
   ```

You can identify the Ceph tools pod by listing the pods in the namespace:

   ```
   kubectl -n rook-ceph get pod | grep tools
   ```
2. Check the OSD logs for the flapping OSD pod to identify issues:
   ```
   kubectl -n rook-ceph logs <osd-pod>
   ```
3. Identify node level issues:
   * Check the resource usage:
     ```
     kubectl top node <node-name>
     ```
   * Check the disk health. You need to SSH into the node and run`df -h` and `dmesg` to check disk errors.
4. Restart the OSD pod. If the issue is transient, you need to restart the flapping OSD pod:
   ```
   kubectl -n rook-ceph delete pod <osd-pod>
   ```
5. Ensure that there are no network connectivity issues between OSDs and Ceph monitors.
6. If needed, temporarily mark the flapping OSD as `out`:
   ```
   ceph osd out <osd-id>
   ```
7. Continue to monitor the cluster to ensure the problem does not recur.

### CephOSDDiskNotResponding

This alert indicates that the host disk device is not responding.

If this alert fires, take the following steps:

1. Check the status of the Ceph cluster. You need to confirm the overall health of the Ceph cluster and get more details about the OSD status:
   * Run the following command inside the Ceph toolbox pod:
     ```
     kubectl -n rook-ceph exec -it <ceph-tools-pod> -- ceph status
     ```
   * Identify the Ceph tools pod by listing the pods in the namespace:
     ```
     kubectl -n rook-ceph get pod | grep tools
     ```
2. Check the OSD pod status. You need to check whether the OSD pods are running. Run the following command to check all OSD pod statuses:
   ```
   kubectl -n rook-ceph get pods | grep osd
   ```

If any OSD pod is in a `CrashLoopBackOff` or `Pending` state, that could indicate an issue with the OSD disk or the underlying node.
3. Restart the affected OSD pod. If an OSD pod is in a bad state (`CrashLoopBackOff`, `Error`, etc.), you must restart the pod to see if the issue resolves itself. Kubernetes automatically attempts to reschedule the pod.
   ```
   kubectl -n rook-ceph delete pod <osd-pod>
   ```

The OSD pod will be restarted, and if it is a transient issue, this may resolve it.
4. Check the OSD logs. If the restart did not resolve the issue, check the OSD pod logs for more details on why the disk is not responding:
   ```
   kubectl -n rook-ceph logs <osd-pod>
   ```

Look for disk-related errors or other issues (e.g., I/O errors, failed mounts).
5. Identify node level issues. If the OSD disk is not mounted properly or has been disconnected, you can log in to the affected node and check the disk mount status:
   ```
   ssh <node> df -h
   ```

Look for missing or unmounted disks that Ceph is expecting. If necessary, remount the disk or replace it if it has failed.

## CephOSDDiskUnavailable

This alert indicates that the Ceph OSD disk not accessible on host.

If this alert fires, take the following steps:

1. Check the status of the Ceph cluster. You need to confirm the overall health of the Ceph cluster and get more details about the OSD status:
   * Run the following command inside the Ceph toolbox pod:
     ```
     kubectl -n rook-ceph exec -it <ceph-tools-pod> -- ceph status
     ```
   * Identify the Ceph tools pod by listing the pods in the namespace:
     ```
     kubectl -n rook-ceph get pod | grep tools
     ```
2. Check the OSD pod status. You need to check whether the OSD pods are running. Run the following command to check all OSD pod statuses:
   ```
   kubectl -n rook-ceph get pods | grep osd
   ```

If any OSD pod is in a `CrashLoopBackOff` or `Pending` state, that could indicate an issue with the OSD disk or the underlying node.
3. Restart the affected OSD pod. If an OSD pod is in a bad state (`CrashLoopBackOff`, `Error`, etc.), you must restart the pod to see if the issue resolves itself. Kubernetes automatically attempts to reschedule the pod.
   ```
   kubectl -n rook-ceph delete pod <osd-pod>
   ```

The OSD pod will be restarted, and if it is a transient issue, this may resolve it.
4. Check the OSD logs. If the restart did not resolve the issue, check the OSD pod logs for more details on why the disk is not responding:
   ```
   kubectl -n rook-ceph logs <osd-pod>
   ```

Look for disk-related errors or other issues (e.g., I/O errors, failed mounts).

## persistent-volume-alert.rules

### PersistentVolumeUsageCritical

If this alert fires, free up some space in Ceph by deleting some unused datasets in AI Center or expand the storage available for Ceph PVC.

Before resizing PVC, make sure you meet the storage requirements. For details, see.

## Server TLS Certificate Alerts

### SecretCertificateExpiry7Days

This alert indicates that the server TLS certificate will expire in the following 7 days.

To fix this issue, update the TLS certificate. For instructions, see [Managing server certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#managing-the-tls-certificate).

### RKE2CertificateExpiry7Days

This alert indicates that the server RKE2 certificate will expire in the following 7 days.

## Identity Token Signing Certificate Alerts

### IdentityCertificateExpiry30Days

This alert indicates that the Identity token signing certificate will expire in the following 30 days.

To fix this issue, update the Identity token signing certificate. For instructions, see [Managing server certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#managing-identity-token-signing-certificates).

### IdentityCertificateExpiry7Days

This alert indicates that the Identity token signing certificate will expire in the following 7 days.

To fix this issue, update the Identity token signing certificate. For instructions, see [Managing server certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#managing-identity-token-signing-certificates).

## etdc Alerts

### EtcdGrpcRequestsSlow

This alert indicates that etcd GRPC requests are slow. This is a warning.

If this alert persists, contact UiPath® support.

### EtcdHttpRequestsSlow

This alert indicates that HTTP requests are slowing down. This is a warning.

## Disk Size Alerts

### LowDiskForRancherPartition

This alert indicates that the free space for the `/var/lib/rancher` partition is less than:

* 35% – the severity of the alert is warning
* 25% – the severity of the alert is critical

If this alert fires, increase the size of the disk.

### LowDiskForKubeletPartition

This alert indicates that the free space for the `/var/lib/kubelet` partition is less than:

* 35% – the severity of the alert is warning
* 25% – the severity of the alert is critical If this alert fires, increase the size of the disk.

### LowDiskForVarPartition

This alert indicates that the free space for the `/var` partition is less than:

* 35% – the severity of the alert is warning
* 25% – the severity of the alert is critical
  :::note
  The storage requirements for ML skills can substantially increase disk usage.
  :::

If this alert fires, increase the size of the disk.

### LowDiskForVarLogPartition

This alert indicates that the free space for the `/var/lib/var` partition is less than:

* 25% – the severity of the alert is critical

If this alert fires, increase the size of the disk.

## Backup Alerts

### NFSServerDisconnected

This alert indicates that the NFS server connection is lost.

You need to check the NFS server connection and mount path.

### VolumeBackupFailed

This alert indicates that the backup failed for a PVC.

To address this issue, take the following steps:

1. Check the status of the PVC to ensure it is `Bound` to a Persistent Volume (PV).
   ```
   kubectl get pvc --namespace <namespace>
   ```

The command lists all PVCs and their current status. The PVC should have a status of `Bound` to indicate it has successfully claimed a PV.

If the status is `Pending`, it means the PVC is still waiting for a suitable PV, and further investigation is needed.
2. If the PVC is not in a `Bound` state or if you need more detailed information, use the `describe` command:
   ```
   kubectl describe pvc <pvc-name> --namespace <namespace>
   ```

Look for information on the status, events, and any error messages. For example, an issue could be related to storage class misconfigurations or quota limitations.
3. Check the health of the Persistent Volume (PV) that is bound to the PVC:
   ```
   kubectl get pv <pv-name>
   ```

The status should be `Bound`. If the PV is in a `Released` or `Failed` state, it may indicate issues with the underlying storage.
4. If the PVC is used by a pod, check whether the pod has successfully mounted the volume:
   ```
   kubectl get pod <pod-name> --namespace <namespace>
   ```

If the pod is in a `Running` state, it indicates that the PVC is mounted successfully. If the pod is in an error state (such as `InitBackOff`), it might indicate issues with volume mounting.
5. If there are issues with mounting the PVC, describe the pod to check for any mounting errors:
   ```
   kubectl describe pod <pod-name> --namespace <namespace>
   ```

### BackupDisabled

This alert indicates that the backup is disabled.

You need to enable backup.

### BackupPartiallyFailed

This alert indicates that the Velero backup has failed.

You need to contact UiPath® support.