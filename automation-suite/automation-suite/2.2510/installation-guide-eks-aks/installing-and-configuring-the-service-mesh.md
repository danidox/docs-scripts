---
title: "Installing and configuring the service mesh"
visible: true
slug: "installing-and-configuring-the-service-mesh"
---

:::important
Installation permissions are relevant only if you cannot provide admin privileges to the Automation Suite installer. If you can provide the required admin privileges to the installer, you do not need to follow the instructions in this section.
:::

Automation Suite requires the Istio service mesh for ingress and networking.

The service mesh installation and configuration is a multi-step process. Which of the steps you must perform depends on whether or not you can grant the Automation Suite installer admin privileges over your cluster. For details, see the following table:

| Step | Admin privileges | No admin privileges |
| --- | --- | --- |
| [Step 1: Installing the service mesh](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-service-mesh#step-1%3A-installing-the-service-mesh) | Step not required | Required step |
| [Step 2: Configuring Istio and installing the WASM plugin for routing](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-service-mesh#step-2%3A-configuring-istio-and-installing-the-wasm-plugin-for-routing) | Step not required | Required step |

## Step 1: Installing the service mesh

To install Istio, follow the instructions in the [Istio documentation](https://istio.io/latest/docs/setup/install).

:::note
Automation Suite does not require applications such as Kiali and Jaeger. However, you can use them at your discretion.
:::

### Providing the Istio configuration

To provide the Istio configuration, you must set the following parameters in the `input.json` file:

```
"ingress": {
  "gateway_selector": {
    "istio": "ingressgateway"
  },
  "ingress_gateway_secret": "istio-ingressgateway-certs",
  "namespace": "<istio-system>"
},
```

For more information on the Istio configuration parameters, see the following table:

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-9715D15C-E978-4DAD-B0A6-C6BB78F9BFCB__TABLE_CGB_ZVC_5CC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Parameter
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Value
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d51172e103">
    <code>
     ingress.gateway_selector.istio
    </code>
   </td>
   <td headers="d51172e107">
    Default value:
    <code>
     ingressgateway
    </code>
    Note: This is the default label used internally by Automation Suite. However, your environment may use a different label for the
                                       Istio ingress gateway depending on how the cluster was configured.
                                    
                                    If you have changed the value, then use the following command to get the right value:
    <button>
     assignment
    </button>
    <pre>kubectl -n &lt;istio-system&gt; get deploy istio-ingressgateway -o jsonpath="{.metadata.labels.istio}"; echo</pre>
   </td>
  </tr>
  <tr>
   <td headers="d51172e103">
    <code>
     ingress.ingress_gateway_secret
    </code>
   </td>
   <td headers="d51172e107">
    The name of the secret that contains the certificate files. The default value is
    <code>
     istio-ingressgateway-certs
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d51172e103">
    <code>
     ingress.namespace
    </code>
   </td>
   <td headers="d51172e107">
    The namespace where you have installed the service mesh.
   </td>
  </tr>
 </tbody>
</table>

## Step 2: Configuring Istio and installing the WASM plugin for routing

### Overview

:::important
This step requires admin privileges for installation in the Istio namespace.
:::

There are two ways to perform the installation:

* Option A: If you cannot provide the permissions that the Automation Suite installer requires, then you must perform this step before the Automation Suite installation.
* Option B: During the Automation Suite installation. This method requires the Kubeconfig file that you use during the Automation Suite installation to have the necessary permissions. To review the permissions, refer to the [Granting installation permissions](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions#granting-installation-permissions) section. If you can provide all the necessary permissions, then skip this step.

### Configuration and installation

To configure Istio and install the WASM plugin for routing, take the following steps:

1. Create an `imagepullsecret` in the namespace where you installed the service mesh. To create the `imagepullsecret`, use your typical workflow or take the following steps:
   ```
   registry= <registry_url> #provide the registry where the UiPath images are hosted
   username= <user_name> #provide the username which will be used for the authentication
   password= <password> #provide the password which will be used for the authentication
   namespace= <namespace> #namespace where you want to create a secret

   kubectl create secret docker-registry uipathpullsecret --namespace=${namespace} \
     --docker-server=${registry} --docker-username=${username} \
     --docker-password=${password} --dry-run=client -o yaml \
     | kubectl apply -f -
   ```
2. Pull the helm chart to a local directory, `<uipath-istio-configure>`:
   ```
   helm pull oci://<docker-registry>/helm/istio-configure --version <istio-configure-version> \
   --untar --untardir <uipath-istio-configure>
   ```

The following example shows the command after you replace the placeholders with actual values:

   ```
   helm pull oci://registry.mycompany.com/helm/istio-configure --version 2.2510.0 \
   --untar --untardir uipath-istio-configure
   ```
3. Create a parameter values file to apply during the Helm installation of `istio-configure`. Use the following sample as a template for the file and the replace the `<fqdn>`, `<cluster_type>`, `<pullsecret>`, `<registry>`, and `<uipath_namespace>` placeholders with appropriate values:
   ```
   fqdn: <fqdn>    #the FQDN of the Automation Suite
   gateway:
     selector:
       istio: ingressgateway
   global:
     cluster_type: <cluster_type>    # REQUIRED. Example: eks, aks, openshift
     kubernetesDistribution: <cluster_type>  # REQUIRED. Example: eks, aks, openshift
     imagePullSecret:
       name: <pullsecret>    #name of pull secret which you had create earlier
   minProtocolVersion: TLSV1_2   #TLS versions
   uipath:
     registry: <registry>    #registry url without the protocol 
   uipathServiceNamespace: <uipath_namespace>   #namespace where the uipath application is deployed
   patchIstioService: false
   wasm:
     image:
       pullSecret: <pullsecret>    #name of pull secret which you had create earlier
       registry: oci://<registry>   #registry url without the protocol
   ```
4. Install `istio-configure` in the Istio namespace, using Helm. In the following command, replace the `<istio_namespace>` placeholder with the namespace where Istio is installed, and the `<path_to_the_values_yaml>` with the location of the YAML file containing the parameter values:
   ```
   helm upgrade --debug --install --wait custom-istio-configure \
     uipath-istio-configure/istio-configure --version 2.2510.0 \
     --namespace <istio_namespace> -f <path_to_the_values.yaml>
   ```
5. If you use a registry that is not signed by a known authority, you must add the `WASM_INSECURE_REGISTRIES` environment variable to the `istio-ingressgateway` deployment, so that Istio can pull the image that the WASM plugin uses. To add the environment variable, run the following command:
   ```
   kubectl -n <istio-system> patch deployment istio-ingressgateway --type json -p='[{"op": "add", "path": "/spec/template/spec/containers/0/env", "value": [{"name": "WASM_INSECURE_REGISTRIES", "value": "registry.mycompany.com"}]}]'
   ```
6. Add `istio-configure` to the `exclude_components` section in your `input.json` file. For details, refer to [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#configuring-inputjson).
7. Create certificate secrets using the name provided in `ingress.ingress_gateway_secret` within the `<istio-system>` namespace.
   :::note
   If you update the FQDN after installation, you must reconfigure Istio and the WASM plugin, unless the Automation Suite installer has administrative privileges. To reconfigure, you must take the following steps:
   1. Update the parameter values file mentioned in [Step 3](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-and-configuring-the-service-mesh) with the new FQDN.
   2. Repeat all the steps for configuring Istio and installing the WASM plugin for routing.
   :::