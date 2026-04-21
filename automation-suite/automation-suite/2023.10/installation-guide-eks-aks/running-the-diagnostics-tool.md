---
title: "Running the diagnostics tool"
visible: true
slug: "running-the-diagnostics-tool"
---

The Automation Suite diagnostics tool runs a set of checks to generate a report on the cluster health, which you can analyze to identify issues and their potential root causes. The tool helps you find common issues, such as lost database connectivity or invalid or expired credentials.

The Automation Suite diagnostics tool is available in both `uipathctl` and `uipathtools`, which you can download on your management machine.

For download instructions, see [uipathctl](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/downloading-the-installation-packages#uipathctl) and [uipathtools](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/downloading-the-installation-packages#uipathtools).

`uipathtools` is a CLI tool that contains a subset of `uipathctl` capabilities specific to health commands. The tool is backwards compatible and works with any of the supported Automation Suite versions. We recommend using `uipathtools` as the first step if you face any issue.

The prerequisite and health checks/tests run in the `uipath-check` namespace. You must either allow the creation of the `uipath-check` namespace or create it yourself before running the checks/tests. In addition to this, some checks/tests require that you allow the communication between the `uipath-check` and `uipath` namespaces, or that you enable the use of `hostNetwork`.

## Quick validation

### Quick validation

The `check` and `test` commands provide quick insights into the state of the cluster without running a deep analysis.

* `check` relies on the ArgoCD health and sync status and does not modify any state in the cluster
* `test` looks into the applications, deployment, or pods and temporarily mutates the state of the cluster to provide you with those insights.

### Health check

To run a health check, use one of the following commands, depending on the CLI tool you use:

* If you use `uipathctl`, run:
  ```
  ./uipathctl health check
  ```
* If you use `uipathtools`, run:
  ```
  ./uipathtools health check
  ```

:::note
Use the `--namespace` flag (optional) if you do not provide `input.json` . You need to use the flag only if the installation is not in the `uipath` namespace. Without the flag, the health check retrieves diagnostic data from all namespaces.
:::

Sample output of the generated report:

```
Checks run on cluster/
 ✔ [NOTIFICATIONSERVICE]
    ✔ [NOTIFICATIONSERVICE_HEALTH] Application is healthy and in sync
 ✔ [ACTION_CENTER]
    ✔ [ACTIONCENTER_HEALTH] Application is healthy and in sync
 ❌ [SYNC]
    ❌ [namespace:"argocd" | kind:"Application" | name:"dataservice"] Application health check failed: health status is Progressing and sync status is Synced
 ✔ [RELOADER]
    ✔ [RELOADER_HEALTH] Application is healthy and in sync
 ❌ [POD]
    ✔ [LIST_NAMESPACES] Retrieved 25 namespaces to check pod health
    ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-runtime-8f5bb7d56-v5krg cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
    ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-runtime-8f5bb7d56-xs9t5 cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
    ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-taskrunner-787df76c74-98h5l cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
 ✔ [ISTIO]
    ✔ [LIST_PODS] Found 2 pods for Istio
    ✔ [ISTIOD_EXISTS] The Istio pods are present and running version - 
    ✔ [ISTIOD_READY] Istio pods are healthy
 ✔ [AIEVENTS]
    ✔ [AIEVENTS_HEALTH] Application is healthy and in sync
 ❌ [DATASERVICE]
    ❌ [DATASERVICE_HEALTH] Application health check failed: health status is Progressing and sync status is Synced
 ✔ [PLATFORM]
    ✔ [PLATFORM_HEALTH] Application is healthy and in sync
 ✔ [TASK_MINING]
    ✔ [TASKMINING_HEALTH] Application is healthy and in sync
 ✔ [LOGGING]
    ✔ [LOGGING_HEALTH] Application is healthy and in sync
 ✔ [WEBHOOK]
    ✔ [WEBHOOK_HEALTH] Application is healthy and in sync
```

By default, the `uipathctl health check` command checks the health of all the components. However, it also allows you to check strictly the components that you are interested in:

* If you want to exclude components from the execution, use the `--excluded` flag. For example, if you do not want to check the health of SQL, run `uipathctl health check --excluded SQL`. The command checks the health of all components except for SQL.
* If you want to include only certain components in the execution, use the `--included` flag. For example, if you only want to check the health of DNS and objectstore, run `uipathctl health check --included DNS,OBJECTSTORAGE`.
  :::note
  You can find the names of the components you can include or exclude from the health checks [here](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/output-example-prerequisite-check#output-example%3A-prerequisite-check). In the example, the first word on each outdented line represents the component name. For example: SQL, OBJECTSTORE, DNS, etc.
  :::

Analyzing the logs

1. After running a check health check, the logs show that health check for the Data Service application failed.
   ```
   ❌ [DATASERVICE]
       ❌ [DATASERVICE_HEALTH] Application health check failed: health status is Progressing and sync status is Synced
   ```
2. After further investigation, it becomes clear that the Data Service application failed because the `dataservice-runtime-8f5bb7d56-v5krg` and `dataservice-taskrunner-787df76c74-98h5l` pods are in a failed state. If you analyze further, you can find that the missing `dataservice-external-storage-secret` is missing.
   ```
   ❌ [POD]
       ✔ [LIST_NAMESPACES] Retrieved 25 namespaces to check pod health
       ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-runtime-8f5bb7d56-v5krg cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
       ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-runtime-8f5bb7d56-xs9t5 cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
       ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-taskrunner-787df76c74-98h5l cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
   ```
3. To fix this issue, ensure that you provided the correct credentials for the objectstore in the `input.json`. For details, see [Updating credentials](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/updating-credentials#updating-credentials).

### Health test

To run a health test, use one of the following commands, depending on the CLI tool you use:

* If you use `uipathctl`, run:
  ```
  ./uipathctl health test
  ```
* If you use `uipathtools`, run:
  ```
  ./uipathtools health test
  ```

:::note
Use the `--namespace` flag (optional) if you do not provide `input.json` . You need to use the flag only if the installation is not in the `uipath` namespace.
:::

Sample output of the generated report:

```
Checks run on cluster/
 ✔ [GATEKEEPER]
    ✔ [CREATE_CONSTRAINT] Created test constraint
    ✔ [VERIFY] Constraint verified
    ✔ [CLEANUP] Cleaned up the test constraint
 ✔ [ACTION_CENTER]
    ✔ [CREATE_NAMESPACE] Created namespace prereqk6b72
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqk6b72
    ✔ [CREATE_NAMESPACE] Created namespace prereqbxjx8
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqbxjx8
    ✔ [CREATE_NAMESPACE] Created namespace prereq8zvw4
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq8zvw4
 ✔ [DATASERVICE]
    ✔ [CREATE_NAMESPACE] Created namespace prereqxwlsb
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqxwlsb
    ✔ [CREATE_NAMESPACE] Created namespace prereq5szsn
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq5szsn
 ✔ [APPS]
    ✔ [CREATE_NAMESPACE] Created namespace prereq9z6nb
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq9z6nb
    ✔ [CREATE_NAMESPACE] Created namespace prereq6v7lm
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq6v7lm
    ✔ [CREATE_NAMESPACE] Created namespace prereqxxn5v
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqxxn5v
 ✔ [AUTOMATION_HUB]
    ✔ [CREATE_NAMESPACE] Created namespace prereq4jkbt
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq4jkbt
 ✔ [TEST_MANAGER]
    ✔ [CREATE_NAMESPACE] Created namespace prereqnvvpc
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqnvvpc
 ✔ [ORCHESTRATOR]
    ✔ [CREATE_NAMESPACE] Created namespace prereq8pf2f
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq8pf2f
    ✔ [CREATE_NAMESPACE] Created namespace prereq4w4v4
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq4w4v4
    ✔ [CREATE_NAMESPACE] Created namespace prereqkzwqg
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqkzwqg
 ✔ [INSIGHTS]
    ✔ [CREATE_NAMESPACE] Created namespace prereqqmgjc
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqqmgjc
    ✔ [CREATE_NAMESPACE] Created namespace prereq4vnjx
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq4vnjx
    ✔ [CREATE_NAMESPACE] Created namespace prereqgtg9g
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqgtg9g
 ✔ [AUTOMATION_OPS]
    ✔ [CREATE_NAMESPACE] Created namespace prereqgkkrz
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqgkkrz
 ✔ [AICENTER]
    ✔ [CREATE_NAMESPACE] Created namespace prereqdls88
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqdls88
    ✔ [CREATE_NAMESPACE] Created namespace prereq6m7x9
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereq6m7x9
```

By default, the `uipathctl health test` command executes health tests on all the components. However, it also allows you to check strictly the components that you are interested in:

* If you want to exclude components from the execution, use the `--excluded` flag. For example, if you do not want to check the health of SQL, run `uipathctl health test --excluded SQL`. The command checks the health of all components except for SQL.
* If you want to include only certain components in the execution, use the `--included` flag. For example, if you only want to check the health of DNS and objectstore, run `uipathctl health test --included DNS,OBJECTSTORAGE`.
  :::note
  You can find the names of the components you can include or exclude from the health tests [here](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/output-example-prerequisite-check#output-example%3A-prerequisite-check). In the example, the first word on each outdented line represents the component name. For example: SQL, OBJECTSTORE, DNS, etc.
  :::
:::note
If you compare the output of the `check` and `test` commands for the Data Service application, you can see that the former validates the health of the application, whereas the latter checks the routing.
:::

Known issue

You might get an error message similar to the following sample. You can ignore it as no action is required from your side.

```
E0621 23:32:56.426321   24470 reflector.go:138] external/io_k8s_client_go/tools/cache/reflector.go:167: Failed to watch *v1.Pod: context deadline exceeded
E0621 23:32:56.426392   24470 reflector.go:138] external/io_k8s_client_go/tools/cache/reflector.go:167: Failed to watch *v1.Pod: context deadline exceeded
E0621 23:32:56.444420   24470 reflector.go:138] external/io_k8s_client_go/tools/cache/reflector.go:167: Failed to watch *v1.Pod: context deadline exceeded
E0621 23:32:56.446150   24470 reflector.go:138] external/io_k8s_client_go/tools/cache/reflector.go:167: Failed to watch *v1.Pod: context deadline exceeded
E0621 23:32:56.513357   24470 reflector.go:138] external/io_k8s_client_go/tools/cache/reflector.go:167: Failed to watch *v1.Pod: context deadline exceeded
```

## Deep validation

### Deep validation

The `diagnose` command provides deep insights into the state of the cluster. It helps you identify issues at all levels, such as SQL, objectstore, node, secret, Istio, networking etc.

* It covers both the `check` and `test` commands.
* It runs the prerequisites checks performed before the Automation suite installation, to validate changes to the environment configuration that were made post-installation and that can be the potential cause of the issue.
* It runs on the all the nodes to gather any node-specific issues, such as resource unavailability, any network interference, etc.

To run a diagnostic check, use one of the following commands, depending on the CLI tool you use:

* If you use `uipathctl`, run:
  ```
  ./uipathctl health diagnose input.json --versions version.json
  ```
* If you use `uipathtools`, run:
  ```
  ./uipathtools health diagnose input.json --versions version.json
  ```

:::note
Use the `--namespace` flag (optional) if you do not provide `input.json` . You need to use the flag only if the installation is not in the `uipath` namespace. Without the flag, diagnostics data will be fetched from all namespaces.
:::

Sample output of the generated report:

```
Checks run on nodes/aks-pool0-27031798-vmss000001
 ✔ [REDIS(PORT=6380)]
    ✔ [CONNECTIVITY] Successfully made Redis connection on ci-asaks4011056.redis.cache.windows.net:6380
 ✔ [OBJECTSTORAGE(PRODUCT=ORCHESTRATOR)]
    ✔ [CHECK_API] Object storage test passed for orchestrator
 ✔ [SQL(PRODUCT=PROCESSMINING, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks4011056.infra-sf-ea.infra.uipath-dev.com to [{20.71.155.129 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [DNS(FQDN=ALM.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_SUBDOMAIN] Resolved alm.ci-asaks4011056.infra-sf-ea.infra.uipath-dev.com to [{20.71.155.129 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 Checks run on cluster/
 ✔ [NODE]
    ✔ [NODE_EXISTS] 12 Nodes present in the cluster
    ✔ [NODE_READY] All the nodes are in ready state
 ✔ [GATEKEEPER]
    ✔ [GATEKEEPER_HEALTH] Application is healthy and in sync
    ✔ [CREATE_CONSTRAINT] Created test constraint
    ✔ [VERIFY] Constraint verified
    ✔ [CLEANUP] Cleaned up the test constraint
 ✔ [LOGGING]
    ✔ [LOGGING_HEALTH] Application is healthy and in sync
 ✔ [DATASERVICE]
    ✔ [CREATE_NAMESPACE] Created namespace prereqctzhp
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqctzhp
 ✔ [ROBOTUBE]
    ✔ [ROBOTUBE_HEALTH] Application is healthy and in sync
 ✔ [AIRFLOW]
    ✔ [AIRFLOW_HEALTH] Application is healthy and in sync
 ✔ [ARGOCD]
    ✔ [ARGOCD_SERVER_PODS] Component argocd-server has ready Pods
    ✔ [ARGOCD_REPO_SERVER_PODS] Component argocd-repo-server has ready Pods
    ✔ [ARGOCD_APP_CONTROLLER_PODS] Component argocd-application-controller has ready Pods
    ✔ [ARGOCD_REDIS_PODS] Component redis-ha has ready Pods
 ✔ [ISTIO]
    ✔ [LIST_PODS] Found 2 pods for Istio
    ✔ [ISTIOD_EXISTS] The Istio pods are present and running version - 
    ✔ [ISTIOD_READY] Istio pods are healthy
 ✔ [AICENTER]
    ✔ [AICENTER_HEALTH] Application is healthy and in sync
    ✔ [CREATE_NAMESPACE] Created namespace prereqn6sqn
    ✔ [CREATE_POD] Created test pod curl-pod in namespace prereqn6sqn
Checks run on local/
 ✔ [CONNECTIVITY]
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-4rffj on aks-pool0-27031798-vmss000002 can reach echo-a-4rffj's IP 10.240.1.86 on aks-pool0-27031798-vmss000002
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-4rffj on aks-pool0-27031798-vmss000002 can reach echo-a-8c6t5's IP 10.240.3.57 on aks-pool3-27031798-vmss000000
    ✔ [POD_TO_A] Scenario: http check between two random pods completed successfully
    ✔ [POD_TO_B_MULTI_NODE_CLUSTERIP] Scenario: http check between from pod to a multinode ClusterIP completed successfully
    ✔ [POD_TO_B_MULTI_NODE_HEADLESS] Scenario: http check between from pod to a multinode ClusterIP without a clusterIP set completed successfully
    ✔ [POD_TO_B_INTRA_NODE_CLUSTERIP] Scenario: http check between from two pods colocated on the same node via ClusterIP completed successfully
 ✔ [INGRESS]
    ✔ [INGRESS_GATEWAY_FOUND] Found service istio-ingressgateway in the cluster
    ✔ [INGRESS_GATEWAY_PORT_CHECK] Service istio-ingressgateway is configured to allow traffic on http://ci-asaks4011056.infra-sf-ea.infra.uipath-dev.com
    ✔ [INGRESS_GATEWAY_PORT_CHECK] Service istio-ingressgateway is configured to allow traffic on https://ci-asaks4011056.infra-sf-ea.infra.uipath-dev.com:443
 ✔ [OSS(COMPONENT=MONITORING)]
    ✔ [OSS(component=monitoring)] Check for component monitoring passed
 ✔ [OSS(COMPONENT=GATEKEEPER)]
    ✔ [OSS(component=gatekeeper)] Check for component gatekeeper passed
 ✔ [STORAGECLASS(NAME=STORAGE_CLASS_SINGLE_REPLICA)]
    ✔ [STORAGE_CLASS_EXISTS] Storage class azurefile-csi exists
    ✔ [LIST_NODES] Listed 12 nodes
    ✔ [CREATE_NAMESPACE] Created namespace prereqhcpkc
    ✔ [CREATE_STATEFULSET] Created statefulset storage-class-check-5n272
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool3-27031798-vmss000001
    ✔ [POD_RUNNING] Found one pod running on node aks-pool3-27031798-vmss000001
 ✔ [REGISTRY]
    ✔ [CONNECTIVITY] Successfully made Registry connection on sfbrdevhelmweacr.azurecr.io
 ✔ [NETWORK-POLICIES]
    ✔ [CREATE_NAMESPACE] Namespace prereqw4t9b created
    ✔ [CREATE_EGRESS_NETWORK_POLICY] Created the egress network policies allow-coredns-egress and block-external-traffic
    ✔ [CREATE_INGRESS_NETWORK_POLICY] Created the ingress network policy: block-echo-server-ingress
    ✔ [CREATE_SERVICE] Service echo-server-svc created
 ✔ [STORAGECLASS(NAME=STORAGE_CLASS)]
    ✔ [STORAGE_CLASS_EXISTS] Storage class managed-premium exists
    ✔ [LIST_NODES] Listed 12 nodes
    ✔ [CREATE_NAMESPACE] Created namespace prereqgjhcb
    ✔ [CREATE_STATEFULSET] Created statefulset storage-class-check-nm9th
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27031798-vmss000003
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27031798-vmss000003
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27031798-vmss000001
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27031798-vmss000001
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved ci-asaks4011056.infra-sf-ea.infra.uipath-dev.com to [{20.71.155.129 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks4011056.infra-sf-ea.infra.uipath-dev.com to [{20.71.155.129 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [NODE(CPU >= 8, RAM >= 16GI)]
    ✔ [LIST_NODES] Listed 12 nodes
    ✔ [AT_LEAST_ONE_NODE] At least one node found
    ✔ [CPU_USAGE] Node aks-pool0-27031798-vmss000000 has 12.50% CPU usage
    ✔ [MEMORY_USAGE] Node aks-pool0-27031798-vmss000000 has 38.27% memory usage
    ✔ [POD_USAGE] Node aks-pool0-27031798-vmss000000 has 40.00% of pods in use. Number of pods: 40.00 max allowed: 100.00
 ✔ [OSS(COMPONENT=CERT-MANAGER)]
    ✔ [OSS(component=cert-manager)] Check for component cert-manager passed
 ✔ [RESOURCE]
    ✔ [Capacity] Automation suite already installed on cluster
 ✔ [OSS(COMPONENT=LOGGING)]
    ✔ [OSS(component=logging)] Check for component logging passed
 ✔ [GPU(PRODUCT=DOCUMENTUNDERSTANDING)]
    ✔ [BASIC_GPU_SUCCESS] Was able to start a CUDA job on a GPU node
Checks run on cluster/
 ❌ [DATASERVICE]
    ❌ [DATASERVICE_HEALTH] Application health check failed: health status is Progressing and sync status is Synced
 ❌ [ISTIO]
    ✔ [ISTIO_SYNC_STATUS] Istio sync is up-to-date
    ❌ [ISTIO_ENVOY_CONFIG_STATUS] Istio Envoy configs are not healthy: Error [IST0101] (VirtualService uipath/du-platform-vs) Referenced host:port not found: "aistorage:5000"
    ✔ [ISTIO_SERVICEMESH_VALIDATION_GET_REGISTRY_FQDN] Successfully retrieved registry url
    ✔ [ISTIO_SERVICEMESH_VALIDATION_GET_CLUSTER_FQDN] Successfully retrieved cluster fqdn
    ✔ [ISTIO_SERVICEMESH_VALIDATION_CREATE_TEST_DEPLOYMENT] Successfully created the test deployment istio-validation-deployment
    ✔ [ISTIO_SERVICEMESH_VALIDATION_CREATE_TEST_SERVICE] Successfully created the test service istio-validation-service
    ✔ [ISTIO_SERVICEMESH_VALIDATION_CREATE_TEST_GATEWAY] Successfully created the test gateway istio-validation-gateway
    ✔ [ISTIO_SERVICEMESH_VALIDATION_CREATE_TEST_VIRTUALSERVICE] Successfully created the test virtual service istio-validation-vs
    ✔ [ISTIO_SERVICEMESH_VALIDATION_URL_ACCESS] Success exposing the service via servicemesh
 ❌ [POD]
    ✔ [LIST_NAMESPACES] Retrieved 25 namespaces to check pod health
    ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/ah-tenant-service-sync-insights-data-job-28122960-p6rzg cannot mount volume: MountVolume.SetUp failed for volume "ah-insights-secrets" : failed to sync secret cache: timed out waiting for the condition
    ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-runtime-8f5bb7d56-v5krg cannot mount volume: (combined from similar events): Unable to attach or mount volumes: unmounted volumes=[external-storage-creds], unattached volumes=[workload-socket is-secrets openssl istio-podinfo temp-location cert-location istio-data external-storage-creds workload-certs istio-envoy java domain-cert-config edk2 credential-socket tmp additional-ca-cert-config pem istiod-ca-cert istio-token app-secrets ceph-storage-creds]: timed out waiting for the condition
    ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-runtime-8f5bb7d56-xs9t5 cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
    ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-taskrunner-787df76c74-98h5l cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
    ❌ [POD_UNHEALTHY] Latest event for pod uipath/du-documentmanager-dm-maintenance-cron-28122960-4sm5z: Error: failed to sync configmap cache: timed out waiting for the condition
 ❌ [SYNC]
    ❌ [namespace:"argocd" | kind:"Application" | name:"dataservice"] Application health check failed: health status is Progressing and sync status is Synced
```

:::note
The aforementioned sample is trimmed down. Actual logs have more information. You can notice that the `diagnose` command runs at multiple levels, such as infrastructure, networking, storage, pods, DNS etc.
:::

Analyzing the logs

There are two potential issues that you can notice in the previous logs:

* Istio has a bad configuration, which can cause issues accessing the Document Understanding platform:
  ```
  ❌ [ISTIO]
      ✔ [ISTIO_SYNC_STATUS] Istio sync is up-to-date
      ❌ [ISTIO_ENVOY_CONFIG_STATUS] Istio Envoy configs are not healthy: Error [IST0101] (VirtualService uipath/du-platform-vs) Referenced host:port not found: "aistorage:5000"
  ```
* Data Service is unavailable. See Ceph in the code example.
  ```
  ❌ [DATASERVICE]
      ❌ [DATASERVICE_HEALTH] Application health check failed: health status is Progressing and sync status is Synced
  ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-runtime-8f5bb7d56-v5krg cannot mount volume: (combined from similar events): Unable to attach or mount volumes: unmounted volumes=[external-storage-creds], unattached volumes=[workload-socket is-secrets openssl istio-podinfo temp-location cert-location istio-data external-storage-creds workload-certs istio-envoy java domain-cert-config edk2 credential-socket tmp additional-ca-cert-config pem istiod-ca-cert istio-token app-secrets ceph-storage-creds]: timed out waiting for the condition
      ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-runtime-8f5bb7d56-xs9t5 cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
      ❌ [CANNOT_MOUNT_VOLUME] Pod uipath/dataservice-taskrunner-787df76c74-98h5l cannot mount volume: MountVolume.SetUp failed for volume "external-storage-creds" : secret "dataservice-external-storage-secret" not found
  ```

Known issues

You might get an error message similar to the following sample. You can ignore it as no action is required from your side.

```
I0622 01:31:28.917107   28815 request.go:601] Waited for 1.017599292s due to client-side throttling, not priority and fairness, request: GET:https://ci-asaks4011056-fwwpyxm7.hcp.westeurope.azmk8s.io:443/apis/networking.istio.io/v1alpha3
```

## Additional utilities

### Additional uitilities

All the Automation Suite diagnostics tool commands (`check`, `test`, and `diagnose`) support additional filtering and output format.

Filtering

Expand Table

| **Filters** | **Description** | **Usages** |
| --- | --- | --- |
| `--included` | Comma-separated list of the services to include in the validation | `/uipathctl health diagnose input.json --versions.json --included ISTIO,INSIGHTS`  This command runs the diagnose only against Istio and Insights. |
| `--excluded` | Comma-separated list of the services to exclude from the validation | `/uipathctl health test --excluded ISTIO,INSIGHTS`  This command runs the test in the entire cluster, except Istio and Insights. |

Output format

The Automation Suite diagnostics tool can generate reports in multiple formats: `json`, `yaml`, `text`, and `junit`. You can pass these values to any of the command via the `--output` flag. These output formats are handy when you want to leverage these tools to build your own troubleshooting framework on top of them.

Example usages

| **Usage** | **Example Output** |
| --- | --- |
| ``` ./uipathctl health check --included DATASERVICE --output json ./uipathtools health check --included DATASERVICE --output json ``` | ``` { "cluster/": { "DATASERVICE": [ { "name": "DATASERVICE_HEALTH", "description": "Application health check failed: health status is Progressing and sync status is Synced", "status": "failed" } ] } } ``` |
| ``` ./uipathctl health check --included DATASERVICE --output yaml ./uipathtools health check --included DATASERVICE --output yaml ``` | ``` ? locationType: cluster : DATASERVICE: - name: DATASERVICE_HEALTH description: 'Application health check failed: health status is Progressing and sync status is Synced' status: failed ``` |
| ``` ./uipathctl health check --included DATASERVICE --output text ./uipathtools health check --included DATASERVICE --output text ``` | ``` Checks run on cluster/ ❌ [DATASERVICE] ❌ [DATASERVICE_HEALTH] Application health check failed: health status is Progressing and sync status is Synced ``` |
| ``` ./uipathctl health check --included DATASERVICE --output junit ./uipathtools health check --included DATASERVICE --output junit ``` | ``` <testsuite name="Health" tests="1" errors="0" failures="1" time="0" timestamp="2023-06-22T01:59:08.313362+05:30" hostname=""> <testcase name="DATASERVICE_HEALTH" classname="" time="0"> <failure message="Application health check failed: health status is Progressing and sync status is Synced" type=""> </failure> </testcase> </testsuite> ``` |