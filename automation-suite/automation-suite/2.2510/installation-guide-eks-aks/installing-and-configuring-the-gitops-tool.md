---
title: "Installing and configuring the GitOps
            tool"
visible: true
slug: "installing-and-configuring-the-gitops-tool"
---

:::note
Before proceeding with the ArgoCD installation and configuration, you must install Istio and provide all the required permissions to the `uipathadmin` service account.
* For the service mesh installation and configuration instructions, see [Installing and configuring the service mesh](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-service-mesh#installing-and-configuring-the-service-mesh)
* For the installation permissions, see [Granting installation permissions](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions#granting-installation-permissions).
:::

If you cannot grant admin privileges to the Automation Suite installer, you must bring your own ArgoCD for the Automation Suite deployment. For more information, see [Provisioning ArgoCD](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-gitops-tool#provisioning-argocd).

## Provisioning ArgoCD

If you cannot grant admin privileges to the Automation Suite installer, you must bring your own ArgoCD and take the following configuration steps:

* Provide the correct value for the `application_namespace` parameter in the `argocd` section of your `input.json` file. This is the namespace where applications are created, and ideally should be the namespace where ArgoCD is installed.
* If you install Automation Suite on a shared cluster, we recommend creating a new ArgoCD project dedicated to Automation Suite rather than using the default project. For instructions on how to create a project in ArgoCD, see [Creating a project in ArgoCD](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-gitops-tool#creating-a-project-in-argocd).
* Configure the Helm repository in ArgoCD. For more information, see [Configuring the Helm repository in ArgoCD](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-gitops-tool#configuring-the-helm-repository-in-argocd).
* Grant the necessary permissions on the ArgoCD namespace. For more information, see [Granting the necessary permissions on the ArgoCD namespace](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-gitops-tool#granting-the-necessary-permissions-on-the-argocd-namespace).

### Creating a project in ArgoCD

To create a new project in the ArgoCD UI, take the following steps:

1. Log in to ArgoCD.
2. Navigate to **Settings &gt; Projects &gt; +NEW PROJECT**.
3. Provide a name and description for the project.
4. Add the following destinations:
   1. Enter `<uipath>` as the namespace and `https://kubernetes.default.svc` as the server.
   2. Enter `<istio-system>` as the namespace and `https://kubernetes.default.svc` as the server.
5. Add the `<argocd>` namespace to `sourceNamespaces`.
   :::note
   In older ArgoCD releases, `sourceNamespaces` is not visible in the UI.
   :::

You can also create an ArgoCD project declaratively:

```
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: <project-name>
  namespace: <argocd-namespace>
spec:
  description: App project to manage and deploy uipath applications
  clusterResourceWhitelist:
    - group: '*'
      kind: '*'
  destinations:
    - namespace: <uipath>
      server: https://kubernetes.default.svc
    - namespace: <istio-system>
      server: https://kubernetes.default.svc
  sourceNamespaces:
    - <argocd-namespace>
  sourceRepos:
    - '*'
```

### Configuring the Helm repository in ArgoCD

To configure the Helm repository in ArgoCD, take the following steps:

1. Log in to ArgoCD.
2. Navigate to **Settings &gt; Repositories &gt; +CONNECT REPO**.
3. Use **VIA HTTPS** for the connection method.
4. Select **Helm** as the type.
5. Provide a name.
6. Choose **uipath** as the project. **uipath** is the name of the ArgoCD project you created for the UiPath® application.
7. Provide the repository URL, username, password, and certificate info.
8. Enable the **OCI** checkbox.
9. Select **Connect**.
10. Make sure that the connection status is **Successful**.

### Granting the necessary permissions on the ArgoCD namespace

To grant the necessary permissions on the ArgoCD namespace, take the following steps:

1. Create a role to create and edit the secret in the `<argocd>` namespace:
   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: argo-secret-role
     namespace: <argocd>
   rules:
     - apiGroups: ["rbac.authorization.k8s.io"]
       resources: ["roles", "rolebindings"]
       verbs: ["*"]
     - apiGroups: ["*"]
       resources: ["secrets"]
       verbs: ["get", "watch", "list", "patch", "update", "create"]
   ```
2. Bind the `argo-secret-role` role to the `uipathadmin` service account:
   ```
   kubectl -n <argocd> create rolebinding secret-binding \
     --role=argo-secret-role --serviceaccount=<uipath>:uipathadmin
   ```
3. Create a role to manage the applications in the `<argocd>` namespace:
   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: uipath-application-manager
     namespace: <argocd>
   rules:
     - apiGroups:
         - argoproj.io
       resources:
         - applications
       verbs:
         - "*"
   ```
4. Bind the `uipath-application-manager` role to the `uipathadmin` service account:
   ```
   kubectl create rolebinding uipath-application-manager-rolebinding --role=uipath-application-manager --serviceaccount=<uipath>:uipathadmin -n <argocd>
   ```
5. Bind the namespace reader role in the `<argocd>` namespace to the `uipathadmin` service account:
   ```
   kubectl -n <argocd> create rolebinding namespace-reader-rolebinding \
     --clusterrole=namespace-reader-clusterrole --serviceaccount=<uipath>:uipathadmin
   ```