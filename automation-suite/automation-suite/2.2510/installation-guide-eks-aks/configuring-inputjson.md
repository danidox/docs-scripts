---
title: "Configuring input.json"
visible: true
slug: "configuring-inputjson"
---

The `input.json` file allows you to configure the UiPath® products you want to deploy, the parameters, settings, and preferences applied to the selected products, and the settings of your cloud infrastructure. You must update this file to change the defaults and use any advanced configuration for your cluster.

:::note
Some products might have dependencies. For details, see [Automation Suite products](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/automation-suite-products#automation-suite-products).
:::

To edit `input.json`, you can use your favorite text editor on your client machine.

The following table describes the main `input.json` parameters you must update to properly configure Automation Suite. For a configuration example, refer to [AKS input.json example](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/aks-inputjson-example#aks-inputjson-example) or [EKS input.json example](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/eks-inputjson-example#eks-inputjson-example).

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     General parameters
    </p>
   </th>
   <th>
    <p>
     Description
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      kubernetes_distribution
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    Specificy which Kubernetes distribution you use. Can be
    <code>
     aks
    </code>
    or
    <code>
     eks
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      install_type
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    Determines whether the cluster is deployed in online or offline mode. If not specified, the cluster is deployed in online
                                 mode. To deploy the cluster in offline mode, you must explicitly set the value of the
    <code>
     install_type
    </code>
    parameter to
    <code>
     offline
    </code>
    .
                              
Possible values:
    <code>
     online
    </code>
    or
    <code>
     offline
    </code>
    Default value:
    <code>
     online
    </code>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      registries
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    <p>
     URLs to pull the docker images and helm charts for UiPath&reg; products and Automation Suite.
    </p>
    <p>
     <code>
      registry.uipath.com
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      istioMinProtocolVersion
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    The minimum version of the TLS protocol accepted by Istio for secure communications. It can be set to either
    <code>
     TLSV1_2
    </code>
    or
    <code>
     TLSV1_3
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      fqdn
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    <p>
     The load balancer endpoint for Automation Suite
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      admin_username
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    <p>
     The username that you would like to set as an admin for the host organization.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      admin_password
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    <p>
     The host admin password to be set.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <code>
     profile
    </code>
   </td>
   <td headers="d62703e54">
    <p>
     Sets the profile of the installation. The available profiles are:
    </p>
    <ul>
     <li>
      <code>
       lite
      </code>
      : lite mode profile.
     </li>
     <li>
      <code>
       ha
      </code>
      : multi-node HA-ready production profile.
     </li>
    </ul>
    <p>
     For more details about managing profiles, see
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#profile-configuration">
      Profile configuration
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <code>
     network
    </code>
   </td>
   <td headers="d62703e54">
    Enables IPv4/IPv6 operation for the cluster networking stack used by Automation Suite. For details, refer to
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/networking#networking">
     Networking
    </a>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      telemetry_optout
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    <code>
     true
    </code>
    or
    <code>
     false
    </code>
    - used to opt out of sending telemetry back to UiPath&reg;. It is set to
    <code>
     false
    </code>
    by default.
                              
If you want to opt out, then set to
    <code>
     true
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      fips_enabled_nodes
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    Indicate whether you want to enable FIPS 140-2 on the nodes on which you plan to install Automation Suite. Possible values
                                 are
    <code>
     true
    </code>
    and
    <code>
     false
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <code>
     storage_class
    </code>
   </td>
   <td headers="d62703e54">
    <p>
     Specify the storage class to be used for PV provisioning. This storage class must support multiple replicas for optimum High
                                 Availability and possess backup capabilities.
    </p>
    <p>
     For more information, refer to
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#block-storage">
      Block storage
     </a>
     section.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      storage_class_single_replica
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    <p>
     Provide the storage class to be used for PV provisioning. This storage class can have a single replica for the components
                                 that do not require High Availability. The storage class can have no backup capabilities.
    </p>
    <p>
     For more information, refer to
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#file-storage">
      File storage
     </a>
     section.
    </p>
    The
    <code>
     storage_class_single_replica
    </code>
    value can be the same as the
    <code>
     storage_class
    </code>
    value.
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <code>
     storage_class_name_with_rwx_support
    </code>
   </td>
   <td headers="d62703e54">
    Specifies the StorageClass that supports ReadWriteMany (RWX) access mode. This field ensures that components requiring shared
                              persistent volumes use the correct RWX-enabled storage.
                              Important: This field cannot be empty if Studio Web or ECS is enabled. If left empty, an error is thrown during validation.
    <p>
     For fresh installations, provide a StorageClass name with RWX (ReadWriteMany) support.
    </p>
    For upgrades from versions prior to 2.2510.0 using Studio Web, use the same storage class name as specified in
    <code>
     storage_class_single_replica
    </code>
    , ensuring it supports RWX access mode.
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <code>
     exclude_components
    </code>
   </td>
   <td headers="d62703e54">
    <p>
     Use this parameter to prevent non-essential components from being installed.
    </p>
    <p>
     For details, see
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#bring-your-own-components">
      Bring your own components
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <code>
     namespace
    </code>
   </td>
   <td headers="d62703e54">
    <p>
     Specify the namespace where you want to install Automation Suite.
    </p>
    <p>
     For details, see
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#custom-namespace-configuration">
      Custom namespace configuration
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <code>
     argocd.application_namespace
    </code>
   </td>
   <td headers="d62703e54">
    <p>
     The namespace of the application you plan to install. This should ideally be the same as the namespace where you plan to install
                                 Automation Suite.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e51">
    <p>
     <code>
      argocd.project
     </code>
    </p>
   </td>
   <td headers="d62703e54">
    <p>
     The ArgoCD project required to deploy Automation Suite. This is only required if you want to use the shared or the global
                                 ArgoCD instance instead of a dedicated ArgoCD instance.
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Profile configuration

You can choose from the following profile modes when installing Automation Suite:

* Configurable high availability profile (lite mode)
* Standard high availability profile (HA mode)

Only in lite mode you can switch specific products to high availability (HA). This flexibility allows you to start with non-critical workload, and have the freedom to easily switch to HA mode when onboarding critical ones.

To enable high availability (HA) for a product, you must modify the `input.json` file. Specifically, you must change the `profile` parameter to `ha` for the products you want to make highly available:

```
  ....
  "automation_ops": {
    "enabled": true,
    "profile": "ha" // flag for turning on high availability
  },
  "action_center": {
    "enabled": true,
    "profile": "lite"
  },
  ...
```

To switch from lite mode to HA mode, take the following steps:

1. Make sure you have enough infrastructure capabilities to switch to standard HA at platform level. By default, lite mode sets each product to have one replica with horizontal pod scaling enabled.
2. Edit the `input.json` configuration file, and make change the `profile` parameter for the targeted products.
3. To apply the changes, run the following command:
   ```
    uipathctl manifest apply
   ```

## UiPath® products

You can enable and disable products in Automation Suite at the time of installation and at any point post-installation. For more details on each product configuration, see [Managing products](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-products#managing-products).

:::note
Depending on your product selection, some configurations might not be available. For example, Insights does not currently support Microsoft Entra ID (formerly Azure Active Directory) authentication configuration for access to SQL, storage, and other resources that support Microsoft Entra.
:::

Orchestrator example:

```
"orchestrator": {
  "enabled": true,
  "external_object_storage": {
    "bucket_name": "uipath-as-orchestrator"
  },
  "testautomation": {
    "enabled": true
  },
  "updateserver": {
    "enabled": true
  }
```

## Bring your own components

Automation Suite allows you to bring your own Gatekeeper and OPA Policies, Cert Manager, Istio, monitoring, logging components, and more. If you choose to exclude these components, ensure that they are available in your cluster before installing Automation Suite.

* For the list of optional components and responsibility matrix, see [Automation Suite stack](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/automation-suite-stack#automation-suite-stack).
* Make sure to review the [compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix) for versions that are validated with Automation Suite.

The following sample shows a list of excluded components. You can remove the components you would like Automation Suite to provision.

```
   "exclude_components": [
        "alerts",
        "auth",
        "istio",
        "cert-manager",
        "logging",
        "monitoring",
        "gatekeeper",
        "network-policies",
        "velero",
    "external-secrets"
  ]
```

### Excluding Istio

If you bring your own Istio component, make sure to include the `gateway_selector` labels from your Istio gateway in the `input.json` file. For more details, refer to [AKS input.json example](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/aks-inputjson-example#aks-inputjson-example) or [EKS input.json example](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/eks-inputjson-example#eks-inputjson-example).

To find your gateway selector label, take the following steps:

1. List all the pods in the `<istio-system>` namespace by running the `kubectl get pods -n <istio-system>` command.
2. Find the one for your Istio gateway deployment.
   :::note
   If you plan to install the WASM plugin yourself and want to avoid providing the Automation Suite installer with write access to the `&lt;istio-system&gt;` namespace, you must add the `istio-configure` component to the `exclude_components` list.
   :::

### Excluding Cert Manager

If you choose to bring your own Cert Manager, and your TLS certificate is issued by a private or non-public CA, you must manually include both the leaf certificate and intermediate CA certificates in the TLS certificate file. In case of public CAs, they are automatically trusted by client systems, and no further action is required on your part.

## Certificate configuration

If no certificate is provided at the time of installation, the installer creates self-issued certificates and configures them in the cluster.

:::note
The certificates can be created at the time of installation only if you grant the Automation Suite installer admin privileges during the installation. If you cannot grant the installer admin privileges, then you must create and manage the certificates yourself.
:::

For details on how to obtain a certificate, see [Managing the certificates.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#managing-the-certificates)

:::note
Make sure to specify the absolute path for the certificate files. Run `pwd` to get the path of the directory where files are placed and append the certificate file name to the `input.json`.
:::

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Parameter
    </p>
   </th>
   <th>
    <p>
     Description
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d62703e510">
    <p>
     <code>
      server_certificate.ca_cert_file
     </code>
    </p>
   </td>
   <td headers="d62703e513">
    <p>
     Absolute path to the Certificate Authority (CA) certificate. This CA is the authority that signs the TLS certificate. A CA
                                    bundle must contain only the chain certificates used to sign the TLS certificate. The chain limit is nine certificates.
    </p>
    If you use a self-signed certificate, you must specify the path to
    <code>
     rootCA.crt
    </code>
    , which you previously created. Leave blank if you want the installer to generate ir.
   </td>
  </tr>
  <tr>
   <td headers="d62703e510">
    <p>
     <code>
      server_certificate.tls_cert_file
     </code>
    </p>
   </td>
   <td headers="d62703e513">
    Absolute path to the TLS certificate (
    <code>
     server.crt
    </code>
    is the self-signed certificate). Leave blank if you want the installer to generate it.
                                 
Note: If you provide the certificate yourself,
                                    the
    <code>
     server.crt
    </code>
    file must contain the entire
                                    chain, as shown in the following
                                    example:
    <button>
     assignment
    </button>
    <pre>-----server cert-----
-----root ca chain-----</pre>
   </td>
  </tr>
  <tr>
   <td headers="d62703e510">
    <p>
     <code>
      server_certificate.tls_key_file
     </code>
    </p>
   </td>
   <td headers="d62703e513">
    Absolute path to the certificate key (
    <code>
     server.key
    </code>
    is the self-signed certificate). Leave blank if you want the installer to generate it.
   </td>
  </tr>
  <tr>
   <td headers="d62703e510">
    <p>
     <code>
      identity_certificate.token_signing_cert_file
     </code>
    </p>
   </td>
   <td headers="d62703e513">
    Absolute path to the identity token signing certificate used to sign tokens (
    <code>
     identity.pfx
    </code>
    is the self-signed certificate). Leave blank if you want the installer to generate an identity certificate using the server
                                    certificate.
   </td>
  </tr>
  <tr>
   <td headers="d62703e510">
    <p>
     <code>
      identity_certificate.token_signing_cert_pass
     </code>
    </p>
   </td>
   <td headers="d62703e513">
    <p>
     Plain text password set when exporting the identity token signing certificate.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e510">
    <p>
     <code>
      additional_ca_certs
     </code>
    </p>
   </td>
   <td headers="d62703e513">
    Absolute path to the file containing the additional CA certificates that you want to be trusted by all the services running
                                    as part of Automation Suite. All certificates in the file must be in valid
    <code>
     PEM
    </code>
    format.
    <p>
     For example, you need to provide the file containing the SQL server CA certificate if the certificate is not issued by a public
                                    certificate authority.
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Infrastructure prerequisites

You must provide configurations details of the prerequisites that you configured on Azure or AWS. For `input.json` parameter requirements, see the following prerequisite sections:

* [SQL database](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#sql-database) (mandatory)
* [Caching](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/caching#caching) (mandatory)
* [Storage](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#storage) (mandatory)
* [Networking](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/networking#networking) (mandatory)
* [NGINX ingress configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-nginx-ingress-controller#configuring-nginx-ingress-controller) (optional)
* [Proxy configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-proxy#proxy) (optional)

## External Objectstore configuration

### General configuration

Automation Suite allows you to bring your own external storage provider. You can choose from the following storage providers:

* **Azure**
* **AWS**
* **S3-compatible**

You can configure the external object storage in one of the following ways:

* during installation;
* post-installation, using the `input.json` file.
  :::note
  * For Automation Suite to function properly when using pre-signed URLs, you must make sure that your external objectstore is
  accessible from the Automation Suite cluster, browsers, and all your machines, including workstations and robot machines.
  * The Server Side Encryption with Key Management Service (SSE-KMS) can only be enabled on the Automation Suite buckets deployed
  in any region created after January 30, 2014. SSE-KMS functionality requires pure SignV4 APIs. Regions created before January 30, 2014 do not use pure SignV4 APIs due to backward compatibility with SignV2. Therefore, SSE-KMS is only functional in regions that use SignV4 for communication. To find out when the various regions were provisioned, refer to the [AWS documentation](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).
  :::

If you use a Private Endpoint to access the container, you must add the `fqdn` parameter in the `input.json` file and specify the Private Endpoint as value.

The following table lists out the `input.json` parameters you can use to configure each provider of external object storage:

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Parameter
    </p>
   </th>
   <th>
    <p>
     Azure
    </p>
   </th>
   <th>
    <p>
     AWS
    </p>
   </th>
   <th>
    <p>
     S3-compatible
    </p>
   </th>
   <th>
    <p>
     Description
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.enabled
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    Specify whether you would like to bring your own object store. Possible values:
    <code>
     true
    </code>
    and
    <code>
     false
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.create_bucket
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    Specify whether you would like to provision the bucket. Possible values:
    <code>
     true
    </code>
    and
    <code>
     false
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.storage_type
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    Specify the storage provider you would like to configure. The value is case-sensitive. Possible values:
    <code>
     azure
    </code>
    and
    <code>
     s3
    </code>
    .
                                 
Note: Many S3 objectstores require the CORS set to all the traffic from the Automation Suite cluster. You must configure the CORS
                                    policy at the objectstore level to allow the FQDN of the cluster.
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.fqdn
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify the FQDN of the S3 server. Required in the case of AWS instance and non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.port
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify the S3 port. Required in the case of AWS instance and non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.region
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify the AWS region where buckets are hosted. Required in the case of AWS instance and non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.access_key
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify the access key for the S3 account. Only required in the case of the AWS non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.secret_key
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify the secret key for the S3 account. Only required in the case of the AWS non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.use_instance_profile
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify whether you want to use an instance profile. An AWS Identity and Access Management (IAM) instance profile grants secure
                                    access to AWS resources for applications or services running on Amazon Elastic Compute Cloud (EC2) instances. If you opt for
                                    AWS S3, an instance profile allows an EC2 instance to interact with S3 buckets without the need for explicit AWS credentials
                                    (such as access keys) to be stored on the instance.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <code>
     external_object_storage.bucket_name_prefix
    </code>
    <sup>
     1
    </sup>
   </td>
   <td headers="d62703e729">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Indicate the prefix for the bucket names. Optional in the case of the AWS non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <code>
     external_object_storage.bucket_name_suffix
    </code>
    <sup>
     2
    </sup>
   </td>
   <td headers="d62703e729">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Indicate the suffix for the bucket names. Optional in the case of the AWS non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.account_key
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify the Azure account key.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.account_name
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify the Azure account name.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d62703e726">
    <p>
     <code>
      external_object_storage.azure_fqdn_suffix
     </code>
    </p>
   </td>
   <td headers="d62703e729">
    <p>
     ✅
    </p>
   </td>
   <td headers="d62703e732">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e735">
    <p>
     ❌
    </p>
   </td>
   <td headers="d62703e738">
    <p>
     Specify the Azure FQDN suffix. Optional parameter.
    </p>
   </td>
  </tr>
 </tbody>
</table>

<sup>1</sup> If you plan on disabling pre-signed URL access, note that this configuration is not supported by the following activities that upload or retrieve data from the objectstore:

* [Write Storage Text](https://docs.uipath.com/activities/other/latest/workflow/write-storage-text)
* [Upload Storage File](https://docs.uipath.com/activities/other/latest/workflow/upload-storage-file)
* [List Storage Files](https://docs.uipath.com/activities/other/latest/workflow/list-storage-files)
* [Read Storage Text](https://docs.uipath.com/activities/other/latest/workflow/read-storage-text)
* [Download Storage File](https://docs.uipath.com/activities/other/latest/workflow/download-storage-file)
* [Delete Storage File](https://docs.uipath.com/activities/other/latest/workflow/delete-storage-file)

<sup>2, 3</sup> When configuring the external object storage, you must follow the naming rules and conventions from your provider for both `bucket_name_prefix` and `bucket_name_suffix`. In addition to that, the suffix and prefix must have a combined length of no more than 25 characters, and you must not end the prefix or start the suffix with a hyphen (`-`) as we already add the character for you automatically.

To ensure secure and compatible communication with Automation Suite, your S3-compatible objectstore must support one or more of the following secure TLS cipher suites:

* TLS 1.3:
  + `TLS_AES_128_GCM_SHA256`
  + `TLS_AES_256_GCM_SHA384`
  + `TLS_CHACHA20_POLY1305_SHA256`
* TLS 1.2:
  + `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`
  + `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`
  + `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`
  + `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`
  + `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
  + `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
  + `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
  + `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
  + `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`
  + `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`

:::note
The list of supported cipher suites may evolve over time to align with security best practices and updates in the Go cryptographic library. Refer to the [latest Go documentation](https://go.dev/doc/) for the current list.
:::

### Product-specific configuration

You can use the parameters described in the [General configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#general-configuration) section to update the general Automation Suite configuration. This means that all installed products would share the same configuration. If you want to configure one or more products differently, you can override the general configuration. You just need to specify the product(s) you want to set up external object storage for differently, and use the same parameters to define your configuration. Note that all the other installed products would continue to inherit the general configuration.

The following example shows how you can override the general configuration for Orchestrator:

```
"external_object_storage": {
  "enabled": false, // <true/false>
  "create_bucket": true, // <true/false>
  "storage_type": "s3", // <s3,azure,aws>
  "fqdn": "",  // <needed in the case of aws instance and non-instance profile>
  "port": 443, // <needed in the case of aws instance and non-instance profile>
  "region": "", 
  "access_key": "", // <needed in the case of aws non instance profile>
  "secret_key": "", // <needed in the case of aws non instance profile>
  "bucket_name_prefix": "",
  "bucket_name_suffix": "",
  "account_key": "",
  "account_name": "",
  "azure_fqdn_suffix": "core.windows.net",
},

"orchestrator": {
  "external_object_storage": {
    "enabled": false, // <true/false>
    "create_bucket": true, // <true/false>
    "storage_type": "s3", // <s3,azure>
    "fqdn": "",  // <needed in the case of aws instance and non-instance profile>
    "port": 443, // <needed in the case of aws instance and non-instance profile>
    "region": "", 
    "access_key": "", // <needed in case of aws non instance profile>
    "secret_key": "", // <needed in case of aws non instance profile>
    "bucket_name_prefix": "",
    "bucket_name_suffix": "",
    "account_key": "",
    "account_name": "",
    "azure_fqdn_suffix": "core.windows.net",
  }
}
```

### Rotating the blob storage credentials for Process Mining

To rotate the blob storage credentials for Process Mining in Automation Suite the stored secrets must be updated with the new credentials. See [Rotating blob storage credentials](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/rotating-blob-storage-credentials#rotating-blob-storage-credentials).

## Pre-signed URL configuration

You can use the `disable_presigned_url` flag to specify whether you would like to disable pre-signed URL access at global level. By default, pre-signed URLs are enabled for the entire platform. The possible values are: `true` and `false`.

```
{
  "disable_presigned_url" : true
}
```

:::note
* You can only change the default value of this parameter only for new installations. The operation is irreversible and does
not apply to an existing cluster.
* You can apply this configuration only to the entire platform. You cannot override the global configuration at product level.
:::

## External OCI-compliant registry configuration

To configure an external OCI-compliant registry, update the following parameters in the `input.json` file:

| Keys | Value |
| --- | --- |
| `registries.docker.url` | Default value: `registry.uipath.com`  The URL or FQDN of the registry to be used by Automation Suite to host the container images. |
| `registries.docker.username`  `registries.docker.password` | Authentication information to be used for pulling the Docker images from the registry.  If one of the values is found in the input file, you must provide both of them when configuring the external registry. |
| `registries.docker.pull_secret_value` | The registry pull secret.  This field is optional. |
| `registries.helm.url` | Default value: `registry.uipath.com`  The URL or FQDN of the registry to be used by Automation Suite to host the Helm chart of the service. |
| `registries.helm.username`  `registries.helm.password` | Authentication information to be used for pulling Helm charts from the registry.  If one of the values is found in the input file, you must provide both of them when configuring the external registry. |
| `registry_ca_cert` | The location of the CA file corresponding to the certificate configured for the registry.  If the registry is signed by a private certificate authority hosted on your premises, you must provide it to establish the trust. |
| `registry.pull_secret_name` | The name of the Kubernetes Secret that stores the registry credentials.  Use this parameter to reference an existing Secret that contains the authentication information for the registry. |

:::note
You can use different methods to generate the encoded version of the `pull_secret_value`, including the one using Docker. For details, see .
:::

The following configuration sample shows a Kubernetes Secret definition used to store registry credentials:

```
apiVersion: v1
kind: Secret
metadata:
  name: registry-credentials
data:
  url: base64Encode(sfbrdevhelmweacr.azurecr.io)
  username: base64Encode(registry-username)
  password: base64Encode(registry-password)
```

The following configuration sample shows a typical OCI-compliant registry setup:

```
{
    "registries": {
        "docker": {
            "url": "registry.domain.io",
            "username": "username",
            "password": "password", 
            "pull_secret_value": "pull-secret-value"
        },
        "helm": {
            "url": "registry.domain.io",
            "username": "username",
            "password": "password"
        },
        "trust": {
            "enabled": true,
            "public_key": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUZrd0V3WUhLb1pJemowQ0FRWUlLb1pJemowREFRY0RRZ0FFNE4vSzNzK2VXUTJHU3NnTTJNcUhsdEplVHlqRQp1UC9sd0dNTnNNUjhUZTI2Ui9TTlVqSVpIdnJKcEx3YmpDc0ZlZUI3L0xZaFFsQzlRdUU1WFhITDZ3PT0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==",
            "detection_mode": false
        }
    },
    "registry_ca_cert": "/etc/pki/ca-trust/extracted/ca-bundle.trust.crt"
}
```

:::note
For registries such as Harbor, which require using a project, you must append the project name to the registry URL. The requirement applies to the `registries.docker.url` and `registries.helm.url` parameters in the `input.json` file, as shown in the following example: assignment
```
{
"registries": {
"docker": {
"url": "registry.domain.io/myproject",
"username": "username",
"password": "password"
"pull_secret_value": "pull-secret-value"
},
"helm": {
"url": "registry.domain.io/myproject",
"username": "username",
"password": "password"
}
"trust": {
"enabled": true,
"public_key": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUZrd0V3WUhLb1pJemowQ0FRWUlLb1pJemowREFRY0RRZ0FFNE4vSzNzK2VXUTJHU3NnTTJNcUhsdEplVHlqRQp1UC9sd0dNTnNNUjhUZTI2Ui9TTlVqSVpIdnJKcEx3YmpDc0ZlZUI3L0xZaFFsQzlRdUU1WFhITDZ3PT0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==",
"detection_mode": false
}
},
"registry_ca_cert": "/etc/pki/ca-trust/extracted/ca-bundle.trust.crt"
}
```
:::

## Custom namespace configuration

You can specify a single custom namespace that replaces the default `uipath`, `uipath-check`, and `uipath-installer` namespaces. To define a custom namespace, provide a value for the optional `namespace` parameter. If you do not provide a value for the `namespace` parameter, the default namespaces are used instead.

## Custom namespace label configuration

If you want the UiPath namespaces to contain custom namespace labels, add the following section to the `input.json` file. Make sure to add your own labels.

```
 "namespace_labels": {
        "install-type": "aksoffline",
        "uipathctlversion": "rc-10_0.1",
        "updatedLabel": "rerun"
    },
```

## Custom node toleration configuration

If you need custom taints and tolerations on the nodes on which you plan to install Automation Suite, update `input.json` with the following flags. Make sure to provide the appropriate values to the `spec` field.

```
"tolerations": [
  {
    "spec": {
      "key": "example-key", 
      "operator": "Exists",
      "value": "optional-value",
      "effect": "NoSchedule"
    }
  },
  {
    "spec": {
      "key": "example-key2", 
      "operator": "Exists",
      "value": "optional-value2",
      "effect": "NoSchedule"
    }
  }
]
```

## Internal load balancer configuration

You can use an internal load balancer for your deployment in both AKS and EKS installation types. To do this, you must specify this in the `ingress` section of the `input.json` file.

The `AKS internal load balancer configuration field details` field details:

| Parameter | Description |
| --- | --- |
| azure-load-balancer-internal | Specifies if the load balancer is internal. |

The `EKS internal load balancer configuration field details` field details:

|  |  |
| --- | --- |
| aws-load-balancer-backend-protocol | Specifies the backend protocol. |
| aws-load-balancer-nlb-target-type | Specifies the target type to configure for NLB. You can choose between `instance` and `ip`. |
| aws-load-balancer-scheme | Specifies whether the NLB will be internet-facing or internal. Valid values are `internal` or `internet-facing`. If not specified, default is `internal`. |
| aws-load-balancer-type | Specifies the load balancer type. This controller reconciles those service resources with this annotation set to either `nlb` or `external`. |
| aws-load-balancer-internal | Specifies whether the NLB will be internet-facing or internal. |

AKS Example

```
 "ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/azure-load-balancer-internal": "true"
    }
  },
```

EKS Example

```
  "ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/aws-load-balancer-backend-protocol": "ssl",
      "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type": "ip",
      "service.beta.kubernetes.io/aws-load-balancer-scheme": "internal",
      "service.beta.kubernetes.io/aws-load-balancer-type": "nlb",
      "service.beta.kubernetes.io/aws-load-balancer-internal": "true"
    }
  },
```

For more information on creating internal load balancers in AKS and EKS, access the following links:

* [Internal load balancer for AKS](https://learn.microsoft.com/en-us/azure/aks/internal-lb?tabs=set-service-annotations).
* [Internal load balancer for EKS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/guide/service/annotations/)

## Workload identity configuration

Workload identity is a variant of managed identity available if you use Automation Suite on AKS. Workload identity helps you avoid managing credentials by enabling pods to use a Kubernetes identity, such as a service account. Workload identity also allows Kubernetes applications to access Azure resources securely with Microsoft Entra ID, based on annotated service accounts.

To learn more about workload identity, see [Use a Microsoft Entra Workload ID on AKS - Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview?tabs=dotnet).

:::note
Insights currently does not support workload identity.
:::

To use workload identity, take the following steps:

1. Enable workload identity and the OIDC issuer for the cluster, retrieve the OIDC issuer URL, and create a user-assigned managed identity, which will be used in the workload identity. To perform these operations, follow the instructions in [Deploy and configure an AKS cluster with workload identity - Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster).
2. Save the client ID of the user-assigned managed identity and provide it in your `input.json` file.
   ```
   {
     ...
     "pod_identity" : {
       "enabled": true,
       "aks_managed_identity_client_id":<client-id>,
     }
     ...
   }
   ```
3. Run the following script that creates the federated credentials for all the service accounts we create for Automation Suite:
   ```
   #!/bin/bash

   # Variables
   RESOURCE_GROUP="<resource-group-name>"
   USER_ASSIGNED_IDENTITY_NAME="<user-assigned-identity-name>"
   AKS_OIDC_ISSUER="<aks-oidc-issuer>"
   AUDIENCE="api://AzureADTokenExchange"

   # Helper function to create federated credentials
   create_federated_credentials() {
     local NAMESPACE=$1
     shift
     local SERVICE_ACCOUNTS=("$@")

     for SERVICE_ACCOUNT_NAME in "${SERVICE_ACCOUNTS[@]}"; do
       # Generate a unique federated identity credential name
       FEDERATED_IDENTITY_CREDENTIAL_NAME="${NAMESPACE}-${SERVICE_ACCOUNT_NAME}"

       echo "Creating federated credential for namespace: ${NAMESPACE}, service account: ${SERVICE_ACCOUNT_NAME}"

       # Run the Azure CLI command
       az identity federated-credential create \
         --name "${FEDERATED_IDENTITY_CREDENTIAL_NAME}" \
         --identity-name "${USER_ASSIGNED_IDENTITY_NAME}" \
         --resource-group "${RESOURCE_GROUP}" \
         --issuer "${AKS_OIDC_ISSUER}" \
         --subject "system:serviceaccount:${NAMESPACE}:${SERVICE_ACCOUNT_NAME}" \
         --audience "${AUDIENCE}"

       if [ $? -eq 0 ]; then
         echo "Federated credential created successfully for ${NAMESPACE}:${SERVICE_ACCOUNT_NAME}"
       else
         echo "Failed to create federated credential for ${NAMESPACE}:${SERVICE_ACCOUNT_NAME}"
       fi
     done
   }


   # Call the function for each namespace and its service accounts
   create_federated_credentials "uipath" "default" "asrobots-sa" "dataservice-be-service-account" "dataservice-fe-service-account" "insights-adf" "du-documentmanager-service-account" "services-configure-uipath-ba" "aicenter-jobs" "aicenter-deploy" "ailoadbalancer-service-account" "airflow"
   create_federated_credentials "uipath-check" "default"
   create_federated_credentials "velero" "velero-server"
   ```

To use workload identity with SQL, refer to[Workload identity-based access to SQL from AKS](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#workload-identity-based-access-to-sql-from-aks).

To use workload identity with your storage account, refer to [Workload identity-based access to your storage account from AKS](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#workload-identity-based-access-to-your-storage-account-from-aks).

To use workload identity with Azure Key Vault, refer to [Using Workload Identity authentication](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-azure-key-vault-as-a-secretstore#using-workload-identity-authentication).

:::note
If SQL Server is not configured to support workload identity–based authentication, set `enable_sql_wi` to `false` for each component that connects to SQL. The following example shows the configuration for Document Understanding: assignment
```
"documentunderstanding": {
"enabled": true,
"enable_sql_wi": false
}
```
:::

## Orchestrator-specific configuration

Orchestrator can save robot logs to an Elasticsearch server. You can configure this functionality in the `orchestrator.orchestrator_robot_logs_elastic` section. If not provided, robot logs are saved to Orchestrator's database.

The following table lists out the `orchestrator.orchestrator_robot_logs_elastic` parameters:

| Parameter | Description |
| --- | --- |
| `orchestrator_robot_logs_elastic` | Elasticsearch configuration. |
| `elastic_uri` | The address of the Elasticsearch instance that should be used. It should be provided in the form of a URI. If provided, then username and password are also required. |
| `elastic_auth_username` | The Elasticsearch username, used for authentication. |
| `elastic_auth_password` | The Elasticsearch password, used for authentication. |

## Insights-specific configuration

If enabling Insights, users can include SMTP server configuration that will be used to send scheduled emails/alert emails. If not provided, scheduled emails and alert emails will not function.

You can use the `uipathctl` command-line tool to apply configuration changes. For more information, check the [uipathctl reference guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/reference-guide/uipathctl-reference).

The `insights.smtp_configuration` fields details:

| Parameter | Description |
| --- | --- |
| `tls_version` | Valid values are `TLSv1_2`, `TLSv1_1`, `SSLv23`. **Omit key altogether if not using TLS**. |
| `from_email` | Address that alert/scheduled emails will be sent from. |
| `host` | Hostname of the SMTP server. |
| `port` | Port of the SMTP server. |
| `username` | Username for SMTP server authentication. |
| `password` | Password for SMTP server authentication. |
| `enable_realtime_monitoring` | Flag to enable Insights Real-time monitoring. Valid values are `true`, `false`. Default value is `false`. |

Example

```
"insights": {
    "enabled": true,
    "enable_realtime_monitoring": true,
    "smtp_configuration": {
      "tls_version": "TLSv1_2",
      "from_email": "test@test.com",
      "host": "smtp.sendgrid.com",
      "port": 587,
      "username": "login",
      "password": "password123"
    }
  }
```

## Process Mining-specific configuration

If enabling **Process Mining**, we recommend users to specify a SECONDARY SQL server to act as a data warehouse that is separate from the primary Automation Suite SQL Server. The data warehouse SQL Server will be under heavy load and can be configured in the `processmining` section:

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Parameter
    </p>
   </th>
   <th>
    <p>
     Description
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d62703e1838">
    <p>
     <code>
      sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d62703e1841">
    DotNet formatted connection string with database set as a placeholder:
    <code>
     Initial Catalog=DB_NAME_PLACEHOLDER
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e1838">
    <p>
     <code>
      airflow.metadata_db_connection_str
     </code>
    </p>
   </td>
   <td headers="d62703e1841">
    Note: This applies to PostgreSQL
    <code>
     AutomationSuite Airflow
    </code>
    database.
                              
Sqlalchemy PSYCOPG2 formatted connection string for custom airflow metadata database location:
    <code>
     PostgreSQL:5432/DB_NAME_PLACEHOLDER
    </code>
    .
    <p>
     Example:
    </p>
    <p>
     <code>
      postgresql+psycopg2://testadmin:&lt;password&gt;@postgres.company.com:5432/DB_NAME_PLACEHOLDER
     </code>
    </p>
    Note:
You can also use the
    <code>
     metadata_db_connection_str
    </code>
    in the
    <strong>
     processmining
    </strong>
    section at the global level in the
    <code>
     cluster_config.json
    </code>
    to provide the value for the Airflow metadatabase. In this case, the
    <code>
     airflow.metadata_db_connection_str
    </code>
    is optional.
    <button>
     assignment
    </button>
    <pre>"processmining": {
  "enabled": true,
  "app_security_mode": "system_managed",
  "airflow": {
    "metadata_db_connection_str": "postgresql+psycopg2://testadmin:&lt;password&gt;@sfdev8454496-postgresql.postgres.database.azure.com:5432/AutomationSuite_Airflow"
  }
}
</pre>
   </td>
  </tr>
  <tr>
   <td headers="d62703e1838">
    <p>
     <code>
      warehouse.sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d62703e1841">
    <p>
     DotNet formatted SQL connection string to the processmining data warehouse SQL Server with placeholder for dbname:
    </p>
    <code>
     Initial Catalog=DB_NAME_PLACEHOLDER
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e1838">
    <p>
     <code>
      warehouse.sqlalchemy_pyodbc_sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d62703e1841">
    <p>
     Sqlalchemy PYODBC formatted SQL connection string to the processmining data warehouse SQL Server with placeholder for dbname:
    </p>
    <code>
     sqlServer:1433/DB_NAME_PLACEHOLDER
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d62703e1838">
    <p>
     <code>
      warehouse.master_sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d62703e1841">
    If the installer is creating databases through
    <code>
     sql.create_db: true
    </code>
    setting, a DotNet formatted master SQL connection string must be provided for the processmining data warehouse SQL Server.
                                 Database in the connection string
    <strong>
     must
    </strong>
    be set as
    <code>
     master
    </code>
    .
   </td>
  </tr>
 </tbody>
</table>

Sample Process Mining connection string with PostgreSQL for `AutomationSuite_Airflow`

```
"processmining": {
    "enabled": true,
    "app_security_mode": "system_managed",
    "airflow": {
      "metadata_db_connection_str": "postgresql+psycopg2://testadmin:<password>@sfdev8454496-postgresql.postgres.database.azure.com:5432/AutomationSuite_Airflow"
    },
    "warehouse": {
      "sql_connection_str": "Server=tcp:kerberossql.autosuitead.local,1433;Initial Catalog=AutomationSuite_Warehouse;Persist Security Info=False;User Id=testadmin;Password='<password>';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
      "sqlalchemy_pyodbc_sql_connection_str": "mssql+pyodbc://testadmin:<password>@kerberossql.autosuitead.local:1433/AutomationSuite_Warehouse?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=YES&Encrypt=YES",
      "master_sql_connection_str": "Server=tcp:kerberossql.autosuitead.local,1433;Initial Catalog=master;Persist Security Info=False;User Id=testadmin;Password='<password>';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
```

:::note
When using Kerberos authentication, utilize the `Integrated Security` and `Trusted_Connection` parameters. By setting `Integrated Security` to `true` and setting `Trusted_Connection` to `yes`, the credentials of the currently logged in user are used for the connection. In this case, you do not need to specify a separate username and password.
:::
:::note
When configuring the connection strings for the Process Mining data warehouse SQL Server, the named instance of the SQL Server should be omitted. Named instances of SQL Server cannot operate on the same TCP port. Therefore, the port number alone is sufficient to distinguish between instances. For example, use `tcp:server,1445` instead of `tcp:server\namedinstance,1445`.
:::
:::important
Note that the names for *template* PYODBC connection string `postgresql_connection_string_template_sqlalchemy_pyodbc` (for PostgreSQL) and the PYODBC connection string `sqlalchemy_pyodbc_sql_connection_str` used when you *bring your own database* are different. Also connection string names are different for the template SQL `sql_connection_string_template` and `sql_connection_str` used when you *bring your own database*.
:::
:::important
If you bring your own database and you configured this using the `sql_connection_str` and `sqlalchemy_pyodbc_sql_connection_str` or `airflow.metadata_db_connection_str` connection strings in the `processmining` section of the `input.json`file, the *template* connection strings `sql_connection_string_template` and `postgresql_connection_string_template_sqlalchemy_pyodbc` (for PostgreSQL) are ignored if specified.
:::

## Automation Suite Robots-specific configuration

Automation Suite Robots can use package caching to optimize your process runs and allow them to run faster. NuGet packages are fetched from the filesystem instead of being downloaded from the Internet/network. This requires an additional space of minimum 10GB and should be allocated to a folder on the host machine filesystem of the dedicated nodes.

To enable package caching, you need to update the following `input.json` parameters:

| Parameter | Default value | Description |
| --- | --- | --- |
| `packagecaching` | `true` | When set to `true`, robots use a local cache for package resolution. |
| `packagecachefolder` | `/uipath_asrobots_package_cache` | The disk location on the serverless agent node where the packages are stored. |

## AI Center-specific configuration

This section only applies to S3 endpoints (not needed for Azure Storage).

For AI Center to function properly, you must configure the `aicenter.external_object_storage.port` and `aicenter.external_object_storage.fqdn` parameters in the `input.json` file.

:::note
You must configure the parameters in the `aicenter` section of the `input.json` file even if you have configured the `external_object_storage` section of the file.
:::

The following sample shows a valid `input.json` configuration for AI Center:

```
"aicenter": {
  "external_object_storage" {
    "port": 443,
    "fqdn": "s3.us-west-2.amazonaws.com"
  }
},
"external_object_storage": {
  "enabled": true,
  "create_bucket": false,
  "storage_type": "s3", 
  "region": "us-west-2", 
  "use_instance_profile": true
}
...
```