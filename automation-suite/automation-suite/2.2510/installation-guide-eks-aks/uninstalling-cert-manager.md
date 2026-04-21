---
title: "How to uninstall Cert Manager"
visible: true
slug: "uninstalling-cert-manager"
---

## Prerequisites

* Kubectl CLI (`kubectl`) installed and configured.
* Appropriate permissions to delete resources in the target namespaces.

## Information required

Before proceeding, you must gather the following information:

* UiPath namespace where cert-manager resources are being used.

## Step-by-step uninstallation process

1. Delete the role bindings for cert-manager:
   ```
   # Verify if the role binding exists
   kubectl get rolebinding -n <uipath_namespace> | grep cert-manager

   # If it exists, delete it
   kubectl delete rolebinding <role-binding-name> -n <uipath_namespace>
   ```
2. Delete the cert-manager role:
   ```
   # Check if the role exists
   kubectl get role cert-manager -n <uipath_namespace> | grep cert-manager

   # If it exists, delete it
   kubectl delete role <cert-manamger-role> -n <uipath_namespace>
   ```
3. Clean up cert-manager resources in the namespace:
   ```
   # Delete all certificates
   kubectl delete certificates.cert-manager.io --all -n <uipath_namespace>

   # Delete all issuers
   kubectl delete issuers.cert-manager.io --all -n <uipath_namespace>

   # Delete all clusterissuers if you created any
   kubectl delete clusterissuers.cert-manager.io --all
   ```
4. Uninstall the cert-manager from cluster, delete the namespace or any residual certificate resources following steps 1, 2, and 3 for other namespaces. Also, cross verify if cert-manager is not used by any other component.
5. Verify remaining resources:
   ```
   # Check for any remaining cert-manager resources
   kubectl get all -n <uipath_namespace> | grep cert-manager
   kubectl get crd | grep cert-manager
   ```

## Troubleshooting

If certain resources cannot be deleted:

* Ensure you have the necessary permissions.
* Check if the resources are being used by other applications.
* For resources that are stuck in **Terminating** state, you may need to remove finalizers.

## Notes

* Only uninstall cert-manager if it is not being used by other applications in your cluster.
* If multiple applications depend on cert-manager, consider only removing the UiPath-specific resources.
* Replace `<uipath_namespace>` with your actual UiPath namespace.