---
title: "How to uninstall Dapr"
visible: true
slug: "uninstalling-dapr"
---

## Prerequisites

* Kubectl CLI (`kubectl`) installed and configured.
* Appropriate permissions to delete resources in the target namespaces.

## Information required

Before proceeding, you must gather the following information:

* UiPath namespace where Dapr is installed.
* ArgoCD namespace (typically `argocd` or `openshift-gitops`).

## Step-by-step uninstallation process

1. Delete the Dapr application from ArgoCD:
   ```
   # Verify the application exists first
   kubectl get application.argoproj.io dapr -n <argocd_namespace>

   # If it exists, delete it
   kubectl delete application.argoproj.io dapr -n <argocd_namespace>
   ```

Wait for resources to be deleted.
2. Delete Dapr custom resources:
   ```
   # Delete all Dapr components in the UiPath namespace
   kubectl delete components.dapr.io --all -n <uipath_namespace>

   # Delete all Dapr configurations in the UiPath namespace
   kubectl delete configurations.dapr.io --all -n <uipath_namespace>

   # Delete all Dapr resiliencies in the UiPath namespace
   kubectl delete resiliencies.dapr.io --all -n <uipath_namespace>

   # Delete all Dapr subscriptions in the UiPath namespace
   kubectl delete subscriptions.dapr.io --all -n <uipath_namespace>
   ```
3. Delete Dapr custom resource definitions (CRDs):
   ```
   # Delete Dapr CRDs
   kubectl delete crd components.dapr.io
   kubectl delete crd configurations.dapr.io
   kubectl delete crd resiliencies.dapr.io
   kubectl delete crd subscriptions.dapr.io
   ```
4. Remove Dapr webhook configurations:
   ```
   # Delete the Dapr sidecar injector webhook
   kubectl delete mutatingwebhookconfigurations dapr-sidecar-injector
   ```
5. Remove Dapr-specific role bindings
   ```
   # Verify if the role binding exists
   kubectl get rolebinding -n <uipath_namespace> | grep dapr

   # If it exists, delete dapr specific role binding
   kubectl delete rolebinding <dapr-role-binding> -n <uipath_namespace>
   ```
6. Remove Dapr-specific roles:
   ```
   # Check if the dapr-creator role exists
   kubectl get role -n <uipath_namespace> | grep dapr

   # If it exists, delete dapr specific rolekubectl delete role <dapr-role> -n <uipath_namespace>
   ```
7. Clean up remaining Dapr resources
   * Pods:
     ```
     # List all Dapr-related pods
     kubectl get pods -n <uipath_namespace> | grep dapr

     # Delete each Dapr pod if any
     kubectl delete pod <pod_name> -n <uipath_namespace>
     ```
   * Services:
     ```
     # List all Dapr-related services
     kubectl get svc -n <uipath_namespace> | grep dapr

     # Delete each Dapr service if any
     kubectl delete svc <service_name> -n <uipath_namespace>
     ```
   * Deployments:
     ```
     # List all Dapr-related deployments
     kubectl get deployments -n <uipath_namespace> | grep dapr

     # Delete each Dapr deployment
     kubectl delete deployment <deployment_name> -n <uipath_namespace>
     ```

## Verification

After completing all the uninstallation steps, verify that all Dapr components have been removed:

```
# Check for any remaining Dapr resources
kubectl get pods -n <uipath_namespace> | grep dapr
kubectl get svc -n <uipath_namespace> | grep dapr
kubectl get deployments -n <uipath_namespace> | grep dapr
kubectl get crd | grep dapr
```

## Troubleshooting

If certain resources cannot be deleted:

* Ensure you have the necessary permissions.
* Check if the resources are being managed by another controller.
* Investigate any dependencies that might be preventing deletion.

## Notes

* Replace `<uipath_namespace>` with your actual UiPath namespace.
* Replace `<argocd_namespace>` with your actual ArgoCD namespace.
* Be cautious when deleting shared resources that might affect other applications.