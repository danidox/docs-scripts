---
title: "Granting installation permissions"
visible: true
slug: "granting-installation-permissions"
---

:::important
* Installation permissions are relevant only if you cannot provide admin privileges to the Automation Suite installer. If you
can provide the required admin privileges to the installer, you do not need to follow the instructions in this section.
:::

Automation Suite relies on specific permissions during installation. These permissions are assigned to the service account, which plays a pivotal role in installing the various Automation Suite components.

To configure all the permissions required for installation, take the following steps:

[Step 4.1: Creating a service account](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions#step-1%3A-creating-a-service-account)

[Step 4.2: Creating the required roles](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions#step-2%3A-creating-the-required-roles)

[Step 4.3: Binding the roles to the uipathadmin service account](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions#step-3%3A-binding-the-roles)

[Step 4.4: Generating the kubeconfig file](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions#step-4%3A-generating-the-kubeconfig-file)

## Step 1: Creating a service account

To create a service account, take the following steps:

1. Create the `<uipath>` namespace:
   ```
   kubectl create namespace <uipath>
   ```
2. Create a service account named `uipathadmin`:
   ```
    kubectl create serviceaccount uipathadmin -n <uipath>
   ```
3. Use the existing `admin` cluster role to grant admin permissions to the `uipathadmin` service account in the `<uipath>` namespace:
   ```
   kubectl create rolebinding uipathadmin --clusterrole=admin --serviceaccount=<uipath>:uipathadmin -n <uipath>
   ```

## Step 2: Creating the required roles

The `uipathadmin` service account requires certain permissions during the Automation Suite installation. You provide the necessary permissions by creating roles. To create each role, save its configuration as a YAML file and run the following command, replacing the `<file_name.yaml>` placeholder with the actual name of the YAML file:

```
kubectl apply -f <file_name.yaml>
```

You can create the YAML file for each role by copying its corresponding configuration from the following table:

Figure 1. Automation Suite installation permissions

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-3DD9D5BC-2805-4B25-9624-40C1651CA396__TABLE_N1S_PCF_XCC" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Permissions
    </p>
   </th>
   <th>
    <p>
     Purpose
    </p>
   </th>
   <th>
    <p>
     Configuration
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d19018e112">
    <p>
     Query the namespace [read-only]
    </p>
   </td>
   <td headers="d19018e115">
    Required to check whether the namespaces, such as the
    <code>
     &lt;istio-system&gt;
    </code>
    namespace, are available or not.
   </td>
   <td headers="d19018e118">
    <button>
     assignment
    </button>
    <pre>apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:  
  name: namespace-reader-clusterrole
rules:
  - apiGroups: [""]
    resources: ["namespaces"]
    verbs: ["get"]</pre>
   </td>
  </tr>
  <tr>
   <td headers="d19018e112">
    <p>
     List nodes and CRDs [read-only]
    </p>
   </td>
   <td headers="d19018e115">
    <p>
     The prerequisite check and diagnostic health check tool require this permission to perform the node validations, such as the
                                          capacity available on the node.
    </p>
   </td>
   <td headers="d19018e118">
    <button>
     assignment
    </button>
    <pre>apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: list-nodes-and-crd-clusterrole
rules:
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["list", "get"]
  - apiGroups: ["apiextensions.k8s.io"]
    resources: ["customresourcedefinitions"]
    verbs: ["list"]
  - apiGroups: ["metrics.k8s.io"]
    resources: ["nodes"]
    verbs: ["list", "get"]  
  - apiGroups: ["scheduling.k8s.io"]
    resources: ["priorityclasses"]
    verbs: ["get"]</pre>
   </td>
  </tr>
  <tr>
   <td headers="d19018e112">
    <p>
     Get storage classes
    </p>
    <p>
     [read-only]
    </p>
   </td>
   <td headers="d19018e115">
    <p>
     The prerequisite check and diagnostic health check tool require this permission to perform the validations.
    </p>
   </td>
   <td headers="d19018e118">
    <button>
     assignment
    </button>
    <pre>apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: storage-class-reader
rules:
  - apiGroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get"]</pre>
   </td>
  </tr>
  <tr>
   <td headers="d19018e112">
    <code>
     uipath
    </code>
    roles [write]
   </td>
   <td headers="d19018e115">
    <p>
     Most of the Automation Suite installation is performed via ArgoCD; however, the installation of some components is performed
                                          via Helm chart.
    </p>
    The
    <code>
     uipathctl
    </code>
    tool runs an installation job that executes the installation of the Helm chart. Connecting to the
    <code>
     kube-api-server
    </code>
    and installing the Helm chart in the
    <code>
     &lt;uipath&gt;
    </code>
    namespace require a namespace-level role-creator role.
   </td>
   <td headers="d19018e118">
    <button>
     assignment
    </button>
    <pre>apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: uipath-automationsuite-role
  namespace: &lt;uipath&gt;
rules:
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["roles", "rolebindings"]
    verbs: ["*"]
  - apiGroups: ["*"]
    resources: ["secrets", "configmaps"]
    verbs: ["get", "watch", "list", "patch", "update", "create"]
  - apiGroups: ["security.istio.io", "networking.istio.io"]
    resources: ["*"]
    verbs: ["*"]</pre>
   </td>
  </tr>
  <tr>
   <td headers="d19018e112">
    <code>
     &lt;istio-system&gt;
    </code>
    roles [write]
                                       
Note:
    <p>
     Provide these permissions only if you want the installer to configure the WASM plugin. Otherwise, do not provide the permissions.
    </p>
   </td>
   <td headers="d19018e115">
    The following operations are performed in the
    <code>
     &lt;istio-system&gt;
    </code>
    namespace:
    <ol>
     <li>
      The Automation Suite prerequisite check tool reads the pods and services in the
      <code>
       &lt;istio-system&gt;
      </code>
      namespace to validate that Istio is installed and configured properly.
     </li>
     <li>
      Automation Suite installs the WASM plugin in the
      <code>
       &lt;istio-system&gt;
      </code>
      namespace to configure the path-based routing rules. 
                                             
The installation requires the creation of an
      <code>
       imagepullsecret
      </code>
      that will be used in the WASM Helm chart to pull the image from the registry.
                                             
Additionally, a role creator is required for the
      <code>
       &lt;istio-system&gt;
      </code>
      namespace. Here,
      <code>
       uipathctl
      </code>
      executes a pod that uses the Helm chart to install the WASM plugin for routing.
     </li>
    </ol>
   </td>
   <td headers="d19018e118">
    <button>
     assignment
    </button>
    <pre>apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: istio-system-automationsuite-role
  namespace: &lt;istio-system&gt;
rules:
  - apiGroups: [""]
    resources: ["services", "pods"]
    verbs: ["list"]
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["roles", "rolebindings"]
    verbs: ["*"]
  - apiGroups: ["*"]
    resources: ["secrets", "configmaps"]
    verbs: ["get", "watch", "list", "patch", "update", "create"]
  - apiGroups: ["networking.istio.io", "extensions.istio.io"]
    resources: ["*"]
    verbs: ["*"]</pre>
   </td>
  </tr>
  <tr>
   <td headers="d19018e112">
    <code>
     &lt;istio-system&gt;
    </code>
    roles [read-only]
                                       
Note:
    <p>
     Provide these permissions if you have already configured Istio and installed the WASM plugin.
    </p>
   </td>
   <td headers="d19018e115">
    The following operations are performed in the
    <code>
     &lt;istio-system&gt;
    </code>
    namespace:
    <ol>
     <li>
      The Automation Suite prerequisite check tool reads the pods and services in the
      <code>
       &lt;istio-system&gt;
      </code>
      namespace to validate that Istio is installed and configured properly.
     </li>
     <li>
      The
      <code>
       get secrets
      </code>
      permission is required to copy the certificate file from the
      <code>
       &lt;istio-system&gt;
      </code>
      namespace to the
      <code>
       &lt;uipath&gt;
      </code>
      namespace.
     </li>
    </ol>
   </td>
   <td headers="d19018e118">
    <button>
     assignment
    </button>
    <pre>apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: istio-system-automationsuite-role
  namespace: &lt;istio-system&gt;
rules:
  - apiGroups: [""]
    resources: ["services", "pods"]
    verbs: ["list"]
  - apiGroups: ["*"]
    resources: ["secrets"]
    resourceNames: ["istio-ingressgateway-certs"]
    verbs: ["get"]</pre>
   </td>
  </tr>
 </tbody>
</table>

## Step 3: Binding the roles

You must bind the roles that you created in the previous step to the `uipathadmin` service account, by running the following commands:

```
kubectl -n <istio-system> create rolebinding istio-system-automationsuite-rolebinding \
  --role=istio-system-automationsuite-role --serviceaccount=<uipath>:uipathadmin
  
kubectl -n <istio-system> create rolebinding namespace-reader-rolebinding \
  --clusterrole=namespace-reader-clusterrole --serviceaccount=<uipath>:uipathadmin
  
kubectl -n <uipath> create clusterrolebinding list-nodes-and-crd-rolebinding \
  --clusterrole=list-nodes-and-crd-clusterrole --serviceaccount=<uipath>:uipathadmin
  
kubectl -n <uipath> create rolebinding uipath-automationsuite-rolebinding \
  --role=uipath-automationsuite-role --serviceaccount=<uipath>:uipathadmin
  
kubectl -n <uipath> create clusterrolebinding storage-class-reader-binding \
  --clusterrole=storage-class-reader --serviceaccount=<uipath>:uipathadmin

# This step is needed only if you want installer to configure the WASM Plugin. Otherwise skip it.
kubectl -n <istio-system> create rolebinding uipadmin-istio-system \
  --clusterrole=admin --serviceaccount=<uipath>:uipathadmin
```

## Step 4: Generating the kubeconfig file

After you assign all the permissions to the service account, you must create a `kubeconfig` file to pass to the `uipathctl` tool for the installation.

### Generating the kubeconfig file on Linux or Mac

To generate the `kubeconfig` file on Linux or Mac, run the following commands:

```
# Create a token
token="$(kubectl -n <uipath> create token uipathadmin --duration=8760h)"
# copy current kubeconfig to a temp file
mkdir temp
cp ~/.kube/config temp/kubeconfig.tmp
# Find the user name and unset it in the temp file
kube_user_name="$(kubectl config view -o jsonpath="{.users[0].name}")"
kubectl -n <uipath> config unset users."${kube_user_name}" --kubeconfig="temp/kubeconfig.tmp"
# Update the credentials in the temp file
kubectl -n <uipath> --kubeconfig="temp/kubeconfig.tmp" config set-credentials uipathadmin --token="$token"
# Set the context and the namespace
kubectl --kubeconfig="temp/kubeconfig.tmp" config set-context --current --namespace=<uipath> --user=uipathadmin
mv temp/kubeconfig.tmp temp/uipathadminkubeconfig
```

If the operation was successful, you should see a `kubeconfig` file named `uipathadminkubeconfig`.

### Generating the kubeconfig file on Windows

:::note
You must perform this step using Windows Powershell.
:::

To generate the kubeconfig file on Windows, run the following commands:

```
# Create a token
$token = kubectl -n <uipath> create token uipathadmin --duration=8760h
# copy current kubeconfig to a temp file
mkdir temp
cp ~/.kube/config temp/kubeconfig.tmp
# Find the user name and unset it in the temp file
$kube_user_name = kubectl config view -o jsonpath="{.users[0].name}"
kubectl -n <uipath> config unset users."${kube_user_name}" --kubeconfig="temp/kubeconfig.tmp"
# Update the credentials in the temp file
kubectl -n <uipath> --kubeconfig="temp/kubeconfig.tmp" config set-credentials uipathadmin --token="$token"
# Set the context and the namespace
kubectl --kubeconfig="temp/kubeconfig.tmp" config set-context --current --namespace=<uipath> --user=uipathadmin
mv temp/kubeconfig.tmp temp/uipathadminkubeconfig
```

If the operation was successful, you should see a `kubeconfig` file named `uipathadminkubeconfig` in the `temp` folder.