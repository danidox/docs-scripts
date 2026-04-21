---
title: "Alert runbooks"
visible: true
slug: "alert-runbooks"
---

:::note
* For general
instructions on using the available tools for alerts, metrics, and visualizations, see [Using the monitoring stack](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/using-the-monitoring-stack#using-the-monitoring-stack).
* For more on how
to fix issues and how to create a support bundle for UiPath® Support engineers, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#troubleshooting).
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

### Watchdog

This is an alert meant to ensure that the entire alerting pipeline is functional. This alert is always firing. Therefore, it should always be firing in AlertManager and against a receiver. There are integrations with various notification mechanisms that notify you when this alert is not firing. For example, the **DeadMansSnitch** integration in PagerDuty.

## kubernetes-apps

### KubePodCrashLooping

A pod that keeps restarting unexpectedly. This can happen due to an out-of-memory (OOM) error, in which case the limits can be adjusted. Check the pod events with `kubectl describe`, and logs with `kubectl logs` to see details on possible crashes. If the issue persists, contact UiPath® Support.

### KubePodNotReady

A pod has started, but it is not responding to the health probe with success. This may mean that it is stuck and is not able to serve traffic. You can check pod logs with `kubectl logs` to see if there is any indication of progress. If the issue persists, contact UiPath® Support.

### KubeDeploymentGenerationMismatch, KubeStatefulSetGenerationMismatch

There has been an attempted update to a deployment or statefulset, but it has failed, and a rollback has not yet occurred. Contact UiPath® Support.

### KubeDeploymentReplicasMismatch, KubeStatefulSetReplicasMismatch

In high availability clusters with multiple replicas, this alert fires when the number of replicas is not optimal. This may occur when there are not enough resources in the cluster to schedule. Check resource utilization, and add capacity as necessary. Otherwise contact UiPath® Support.

### KubeStatefulSetUpdateNotRolledOut

An update to a statefulset has failed. Contact UiPath® Support.

See also: [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

### KubeDaemonSetRolloutStuck

Daemonset rollout has failed. Contact UiPath® Support.

See also: [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

### KubeContainerWaiting

A container is stuck in the waiting state. It has been scheduled to a worker node, but it cannot run on that machine. Check `kubectl describe` of the pod for more information. The most common cause of waiting containers is a failure to pull the image. For air-gapped clusters, this could mean that the local registry is not available. If the issue persists, contact UiPath® Support.

### KubeDaemonSetNotScheduled, KubeDaemonSetMisScheduled

This may indicate an issue with one of the nodes Check the health of each node, and remediate any known issues. Otherwise contact UiPath® Support.

### KubeJobCompletion

A job takes more than 12 hours to complete. This is not expected. Contact UiPath® Support.

### KubeJobFailed

A job has failed; however, most jobs are retried automatically. If the issue persists, contact UiPath® Support.

### KubeHpaReplicasMismatch

The autoscaler cannot scale the targeted resource as configured. If desired is higher than actual, then there may be a lack of resources. If desired is lower than actual, pods may be stuck while shutting down. If the issue persists, contact UiPath® Support.

See also: [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

### KubeHpaMaxedOut

The number of replicas for a given service has reached its maximum. This happens when the amount of requests being made to the cluster is very high. If high traffic is expected and temporary, you may silence this alert. However, this alert is a sign that the cluster is at capacity and cannot handle much more traffic. If more resource capacity is available on the cluster, you can increase the number of maximum replicas for the service by following these instructions:

```
# Find the horizontal autoscaler that controls the replicas of the desired resource
kubectl get hpa -A
# Increase the number of max replicas of the desired resource, replacing <namespace> <resource> and <maxReplicas>
kubectl -n <namespace> patch hpa <resource> --patch '{"spec":{"maxReplicas":<maxReplicas>}}'
```

See also: [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).

## kubernetes-resources

### KubeCPUOvercommit, KubeMemoryOvercommit

These warnings indicate that the cluster cannot tolerate node failure. For single-node evaluation clusters, this is known, and these alerts may be silenced. For multi-node HA-ready production setups, these alerts fire when too many nodes become unhealthy to support high availability, and they indicate that the nodes should be brought back to health or replaced.

### KubeCPUQuotaOvercommit, KubeMemoryQuotaOvercommit, KubeQuotaAlmostFull, KubeQuotaFullyUsed, KubeQuotaExceeded

These alerts pertain to namespace resource quotas that only exist in the cluster if added through customization. Namespace resource quotas are not added as part of Automation Suite installation.

See also: [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/).

### CPUThrottlingHigh

A container’s CPU utilization has been throttled according to the configured limits. This is part of normal Kubernetes operation and may provide useful information when other alerts are firing. You may silence this alert.

## Kubernetes-storage

### KubePersistentVolumeFillingUp

When **Warning**: The available space is less than 30% and is likely to fill up within four days.

When **Critical**: The available space is less than 10%.

For any services that run out of space, data may be difficult to recover, so volumes should be resized before hitting 0% available space.

For Prometheus-specific alerts, see [PrometheusStorageUsage](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/alert-runbooks#alert-runbooks) for more details and instructions.

## kube-state-metrics

### KubeStateMetricsListErrors, KubeStateMetricsWatchErrors

The Kube State Metrics collector is not able to collect metrics from the cluster without errors. This means important alerts may not fire. Contact UiPath® Support.

See also: [Kube state metrics at release](https://github.com/kubernetes/kube-state-metrics/tree/release-2.0).

## kubernetes-system-apiserver

### KubeClientCertificateExpiration

When **Warning**: A client certificate used to authenticate to the Kubernetes API server expires in less than seven days.

When **Critical**: A client certificate used to authenticate to the Kubernetes API server expires in less than one day.

You must renew the certificate.

### AggregatedAPIErrors, AggregatedAPIDown, KubeAPIDown, KubeAPITerminatedRequests

Indicates problems with the Kubernetes control plane. Check the health of master nodes, resolve any outstanding issues, and contact UiPath® Support if the issues persist.

See also:

[The Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)

[Kubernetes API Aggregation Layer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)

### KubernetesApiServerErrors

This alert indicates that the Kubernetes API server is experiencing a high error rate. This issue could lead to other failures, so it is recommended that you investigate the problem proactively.

Check logs for the `api-server` pod to find out the root cause of the issue using the `kubectl logs <pod-name> -n kube-system` command.

## kubernetes-system-kubelet

### KubeNodeNotReady, KubeNodeUnreachable, KubeNodeReadinessFlapping, KubeletPlegDurationHigh, KubeletPodStartUpLatencyHigh, KubeletDown

These alerts indicate a problem with a node. In multi-node HA-ready production clusters, pods would likely be rescheduled onto other nodes. If the issue persists, you should remove and drain the node to maintain the health of the cluster. In clusters without extra capacity, another node should be joined to the cluster first.

If the issues persist, contact UiPath® Support.

### KubeletTooManyPods

There are too many pods running on the specified node.

### KubeletClientCertificateExpiration, KubeletServerCertificateExpiration

When **Warning**: A client or server certificate for Kubelet expires in less than seven days.

When **Critical**: A client or server certificate for Kubelet expires in less than one day.

You must renew the certificate.

### KubeletClientCertificateRenewalErrors, KubeletServerCertificateRenewalErrors

Kubelet has failed to renew its client or server certificate. Contact UiPath® support.

## kubernetes-system

### KubeVersionMismatch

There are different semantic versions of Kubernetes components running. This can happen as a result of an unsuccessful Kubernetes upgrade.

### KubeClientErrors

Kubernetes API server client is experiencing greater than 1% errors. There may be an issue with the node this client is running on, or the Kubernetes API server itself.

### KubernetesMemoryPressure

This alert indicates that memory usage is very high on the Kubernetes node.

If this alert fires, try to see which pod is consuming more memory.

### KubernetesDiskPressure

This alert indicates that disk usage is very high on the Kubernetes node.

If this alert fires, try to see which pod is consuming more disk.

## Kube-apiserver-slos

### KubeAPIErrorBudgetBurn

The Kubernetes API server is burning too much error budget.

## node-exporter

### NodeFilesystemSpaceFillingUp, NodeFilesystemAlmostOutOfSpace, NodeFilesystemFilesFillingUp

The filesystem on a particular node is filling up. Provision more space by adding a disk or mounting unused disks.

### NodeRAIDDegraded

RAID array is in a degraded state due to one or more disk failures. The number of spare drives

is insufficient to fix the issue automatically.

### NodeRAIDDiskFailure

RAID array needs attention and possibly a disk swap.

### NodeNetworkReceiveErrs, NodeNetworkTransmitErrs, NodeHighNumberConntrackEntriesUsed

There is a problem with the physical network interface on the node. If the issues persist, it may need to be replaced.

### NodeClockSkewDetected, NodeClockNotSynchronising

There is a problem with the clock on the node. Make sure NTP is configured correctly.

## node-network

### NodeNetworkInterfaceFlapping

There is a problem with the physical network interface on the node. If the issues persist, it may need to be replaced.

## InternodeCommunicationBroken

The node has become unresponsive due to some issue causing broken communication between nodes in the cluster.

To fix this problem, restart the affected node. If the issue persists, reach out to UiPath® Support with the Support Bundle Tool.

## alertmanager.rules

### AlertmanagerConfigInconsistent

These are internal Alertmanager errors for HA clusters with multiple AlertManager replicas. Alerts may appear and disappear intermittently. Temporarily scaling down, then scaling up Alertmanager replicas may fix the issue.

To fix the issue, take the following steps:

1. Scale to zero. Note that it takes a moment for the pods to shut down:
   ```
   kubectl scale statefulset -n cattle-monitoring-system alertmanager-rancher-monitoring-alertmanager --replicas=0
   ```
2. Scale back to two:
   ```
   kubectl scale statefulset -n cattle-monitoring-system alertmanager-rancher-monitoring-alertmanager --replicas=2
   ```
3. Check if the Alertmanager pods started and are in the running state:
   ```
   kubectl get po -n cattle-monitoring-system
   ```

If the issue persists, contact UiPath® Support.

### AlertmanagerFailedReload

AlertManager has failed to load or reload configuration. Please check any custom AlertManager configurations for input errors and otherwise contact UiPath® Support.

## prometheus-operator

### PrometheusOperatorListErrors, PrometheusOperatorWatchErrors, PrometheusOperatorSyncFailed, PrometheusOperatorReconcileErrors, PrometheusOperatorNodeLookupErrors, PrometheusOperatorNotReady, PrometheusOperatorRejectedResources

Internal errors of the Prometheus operator, which controls Prometheus resources. Prometheus itself may still be healthy while these errors are present; however, this error indicates there is degraded monitoring configurability. Contact UiPath® Support.

## prometheus

### PrometheusBadConfig

Prometheus has failed to load or reload configuration. Please check any custom Prometheus configurations for input errors. Otherwise contact UiPath® Support.

### PrometheusErrorSendingAlertsToSomeAlertmanagers, PrometheusErrorSendingAlertsToAnyAlertmanager, PrometheusNotConnectedToAlertmanagers

The connection from Prometheus to AlertManager is not healthy. Metrics may still be queryable, and Grafana dashboards may still show them, but alerts will not fire. Check any custom configuration of AlertManager for input errors and and otherwise contact UiPath® Support.

### PrometheusNotificationQueueRunningFull, PrometheusTSDBReloadsFailing, PrometheusTSDBCompactionsFailing, PrometheusNotIngestingSamples, PrometheusDuplicateTimestamps, PrometheusOutOfOrderTimestamps, PrometheusRemoteStorageFailures, PrometheusRemoteWriteBehind, PrometheusRemoteWriteDesiredShards

Internal Prometheus errors indicating metrics may not be collected as expected. Please contact UiPath® Support.

### PrometheusRuleFailures

This may happen if there are malformed alerts based on non-existent metrics or incorrect PromQL syntax. Contact UiPath® Support if no custom alerts have been added.

### PrometheusMissingRuleEvaluations

Prometheus is not able to evaluate whether alerts should be firing. This may happen if there are too many alerts. Please remove expensive custom alert evaluations and/or see documentation on increasing CPU limit for Prometheus. Contact UiPath® Support if no custom alerts have been added.

### PrometheusTargetLimitHit

There are too many targets for Prometheus to collect from. If extra ServiceMonitors have been added (see Monitoring console), you can remove them.

## uipath.availability.alerts

### UiPathAvailabilityHighTrafficUserFacing, UiPathAvailabilityHighTrafficBackend, UiPathAvailabilityMediumTrafficUserFacing, UiPathAvailabilityMediumTrafficBackend, UiPathAvailabilityLowTrafficUserFacing, UiPathAvailabilityLowTrafficBackend

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

### CronJobSuspended

The `uipath-infra/istio-configure-script-cronjob` cronjob is in suspended state.

To fix this issue, enable the cronjob by taking the following steps:

```
export KUBECONFIG="/etc/rancher/rke2/rke2.yaml" && export PATH="$PATH:/usr/local/bin:/var/lib/rancher/rke2/bin"
kubectl -n uipath-infra patch cronjob istio-configure-script-cronjob -p '{"spec":{"suspend":false}}'
epoch=$(date +"%s")
kubectl -n uipath-infra create job istio-configure-script-cronjob-manual-$epoch --from=cronjob/istio-configure-script-cronjob
kubectl -n uipath-infra wait --for=condition=complete --timeout=300s job/istio-configure-script-cronjob-manual-$epoch
kubectl get node -o wide
#Verif if all the IP's listed by the previous command are part of output of the following command
kubectl -n istio-system get svc istio-ingressgateway -o json | jq '.spec.externalIPs'
```

### UiPath CronJob "kerberos-tgt-refresh" Failed

This job obtains the latest Kerberos ticket from the AD server for SQL-integrated authentication. Failures in this job would cause SQL server authentication to fail. Please contact UiPath® Support.

### IdentityKerberosTgtUpdateFailed

This job updates the latest Kerberos ticket to all the UiPath® services. Failures in this job would cause SQL server authentication to fail. Please contact UiPath® Support.

## uipath.requestrouting.alerts

### UiPathRequestRouting

Errors in the request routing layer would result in degraded functionality that is directly observable in the Automation Suite UI. The requests will not be routed to backend services.

You can find detailed error log of request routing by running the `kubectl logs` command in the Istio ingress gateway pod. If the error persists, contact UiPath® Support.

## Server TLS Certificate Alerts

### SecretCertificateExpiry30Days

This alert indicates that the server TLS certificate will expire in the following 30 days.

To fix this issue, update the server TLS certificate. For instructions, see [Managing server certificates](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-certificates#managing-the-tls-certificate).

### SecretCertificateExpiry7Days

This alert indicates that the server TLS certificate will expire in the following 7 days.

To fix this issue, update the TLS certificate. For instructions, see [Managing server certificates](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-certificates#managing-the-tls-certificate).

## Identity Token Signing Certificate Alerts

### IdentityCertificateExpiry30Days

This alert indicates that the Identity token signing certificate will expire in the following 30 days.

To fix this issue, update the Identity token signing certificate. For instructions, see [Managing server certificates](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-certificates#managing-identity-token-signing-certificates).

### IdentityCertificateExpiry7Days

This alert indicates that the Identity token signing certificate will expire in the following 7 days.

To fix this issue, update the Identity token signing certificate. For instructions, see [Managing server certificates](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-certificates#managing-identity-token-signing-certificates).

## etdc Alerts

### EtcdInsufficientMembers

This alert indicates that the etcd cluster has an insufficient number of members. Note that the cluster must have an odd number of members. The severity of this alert is critical.

Make sure that there is an odd number of server nodes in the cluster, and all of them are up and healthy.

### EtcdNoLeader

This alert shows that the etcd cluster has no leader. The severity of this alert is critical.

### EtcdHighNumberOfLeaderChanges

This alert indicates that the etcd leader changes more than twice in 10 minutes. This is a warning.

### EtcdHighNumberOfFailedGrpcRequests

This alert indicates that a certain percentage of GRPC request failures was detected in etcd.

### EtcdGrpcRequestsSlow

This alert indicates that etcd GRPC requests are slow. This is a warning.

### EtcdHighNumberOfFailedHttpRequests

This alert indicates that a certain percentage of HTTP failures was detected in etcd.

### EtcdHttpRequestsSlow

This alert indicates that HTTP requests are slowing down. This is a warning.

### EtcdMemberCommunicationSlow

This alert indicates that etcd member communication is slowing down. This is a warning.

### EtcdHighNumberOfFailedProposals

This alert indicates that the etcd server received more than 5 failed proposals in the last hour. This is a warning.

### EtcdHighFsyncDurations

This alert indicates that etcd WAL fsync duration is increasing. This is a warning.

### EtcdHighCommitDurations

This alert indicates that etcd commit duration is increasing. This is a warning.

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