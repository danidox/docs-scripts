---
title: "Configuring input.json"
visible: true
slug: "configuring-inputjson"
---

The `input.json` file allows you to configure the UiPath® products you want to deploy, the parameters, settings, and preferences applied to the selected products, and the settings of your cloud infrastructure. You must update this file to change the defaults and use any advanced configuration for your cluster.

:::note
Some products may have dependencies. For details, see .
:::

To edit `input.json`, you can use your favorite text editor on your client machine.

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
   <td headers="d59234e38">
    <p>
     <code>
      kubernetes_distribution
     </code>
    </p>
   </td>
   <td headers="d59234e41">
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
   <td headers="d59234e38">
    <p>
     <code>
      install_type
     </code>
    </p>
   </td>
   <td headers="d59234e41">
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
   <td headers="d59234e38">
    <p>
     <code>
      registries
     </code>
    </p>
   </td>
   <td headers="d59234e41">
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
   <td headers="d59234e38">
    <p>
     <code>
      fqdn
     </code>
    </p>
   </td>
   <td headers="d59234e41">
    <p>
     The load balancer endpoint for Automation Suite
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e38">
    <p>
     <code>
      admin_username
     </code>
    </p>
   </td>
   <td headers="d59234e41">
    <p>
     The username that you would like to set as an admin for the host organization.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e38">
    <p>
     <code>
      admin_password
     </code>
    </p>
   </td>
   <td headers="d59234e41">
    <p>
     The host admin password to be set.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e38">
    <p>
     <code>
      profile
     </code>
    </p>
   </td>
   <td headers="d59234e41">
    <p>
     Default value, not changeable
    </p>
    <ul>
     <li>
      <code>
       ha
      </code>
      : multi-node HA-ready production profile.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d59234e38">
    <p>
     <code>
      telemetry_optout
     </code>
    </p>
   </td>
   <td headers="d59234e41">
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
   <td headers="d59234e38">
    <p>
     <code>
      fips_enabled_nodes
     </code>
    </p>
   </td>
   <td headers="d59234e41">
    Indicate whether you want to enable FIPS 140-2 on the nodes on which you plan to install Automation Suite on AKS. Possible
                                 values are
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
 </tbody>
</table>

```
"kubernetes_distribution": "aks",
  "registries": {
    "docker": {
      "url": "registry.uipath.com"
    },
    "helm": {
      "url": "registry.uipath.com"
    }
  },
  "fqdn": "replace with your fqdn",
  "admin_username": "replace with your UiPath® admin username",
  "admin_password": "replace with your UiPath® admin password",
  "profile": "ha",
  "telemetry_optout": false
  "fips_enabled_nodes": true
```

## UiPath® products

You can enable and disable products in Automation Suite at the time of installation and at any point post-installation. For more details on each product configuration, see [Managing products](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-products#managing-products).

:::note
Depending on your product selection, some configurations might not be available. For example, Insights and Task Mining do not currently support Microsoft Entra ID (formerly Azure Active Directory) authentication configuration for access to SQL, storage, and other resources that support Microsoft Entra.
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

* For the list of optional components and responsibility matrix, see [Automation Suite on EKS/AKS Stack](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-stack#automation-suite-stack).
* Make sure to review the [compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix) for versions that are validated with Automation Suite.

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
        "sfcore"
  ]
```

### Excluding sfcore

If you exclude the `sfcore` component, make sure you have public CA-issued certificates in `input.json`. For details, see [Certificate configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#certificate-configuration).

### Excluding Istio

If you bring your own Istio component, make sure to include the `gateway_selector` labels from your Istio gateway in the `input.json` file. For more details, refer to [AKS input.json example](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/aks-inputjson-example#aks-inputjson-example) or [EKS input.json example](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/eks-inputjson-example#eks-inputjson-example).

To find your gateway selector label, take the following steps:

1. List all the pods in the `istio-system` namespace by running the `kubectl get pods -n istio-system` command.
2. Find the one for your Istio gateway deployment.

### Excluding Cert Manager

If you choose to bring your own Cert Manager, and your TLS certificate is issued by a private or non-public CA, you must manually include both the leaf certificate and intermediate CA certificates in the TLS certificate file. In case of public CAs, they are automatically trusted by client systems, and no further action is required on your part.

## Certificate configuration

If no certificate is provided at the time of installation, the installer creates self-issued certificates and configures them in the cluster.

:::note
Make sure to specify the absolute path for the certificate files. Run `pwd` to get the path of the directory where files are placed and append the certificate file name to the `input.json`.
:::

| Parameter | Description |
| --- | --- |
| `server_certificate.ca_cert_file` | Absolute path to the Certificate Authority (CA) certificate. This CA is the authority that signs the TLS certificate. A CA bundle must contain only the chain certificates used to sign the TLS certificate. The chain limit is nine certificates.  If you use a self-signed certificate, you must specify the path to `rootCA.crt`, which you previously created. Leave blank if you want the installer to generate ir. |
| `server_certificate.tls_cert_file` | Absolute path to the TLS certificate (`server.crt` is the self-signed certificate). Leave blank if you want the installer to generate it. |
| `server_certificate.tls_key_file` | Absolute path to the certificate key (`server.key` is the self-signed certificate). Leave blank if you want the installer to generate it. |
| `identity_certificate.token_signing_cert_file` | Absolute path to the identity token signing certificate used to sign tokens (`identity.pfx` is the self-signed certificate). Leave blank if you want the installer to generate an identity certificate using the server certificate. |
| `identity_certificate.token_signing_cert_pass` | Plain text password set when exporting the identity token signing certificate. |
| `additional_ca_certs` | Absolute path to the file containing the additional CA certificates that you want to be trusted by all the services running as part of Automation Suite. All certificates in the file must be in valid `PEM` format.  For example, you need to provide the file containing the SQL server CA certificate if the certificate is not issued by a public certificate authority. |

## Infrastructure prerequisites

You must provide configurations details of the prerequisites that you configured on Azure or AWS. For `input.json` parameter requirements, see the following prerequisite sections:

* [SQL database](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/sql-database#sql-database) (mandatory)
* [Caching](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/caching#caching) (mandatory)
* [Storage](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/storage#storage) (mandatory)
* [Networking](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/networking#networking) (mandatory)
* [NGINX ingress configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-nginx-ingress-controller#configuring-nginx-ingress-controller) (optional)
* [Proxy configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-proxy#proxy) (optional)

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
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.enabled
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
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
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.create_bucket
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
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
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.storage_type
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
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
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.fqdn
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify the FQDN of the S3 server. Required in the case of AWS instance and non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.port
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify the S3 port. Required in the case of AWS instance and non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.region
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify the AWS region where buckets are hosted. Required in the case of AWS instance and non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.access_key
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify the access key for the S3 account. Only required in the case of the AWS non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.secret_key
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify the secret key for the S3 account. Only required in the case of the AWS non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.use_instance_profile
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify whether you want to use an instance profile. An AWS Identity and Access Management (IAM) instance profile grants secure
                                    access to AWS resources for applications or services running on Amazon Elastic Compute Cloud (EC2) instances. If you opt for
                                    AWS S3, an instance profile allows an EC2 instance to interact with S3 buckets without the need for explicit AWS credentials
                                    (such as access keys) to be stored on the instance.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <code>
     external_object_storage.bucket_name_prefix
    </code>
    <sup>
     1
    </sup>
   </td>
   <td headers="d59234e508">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Indicate the prefix for the bucket names. Optional in the case of the AWS non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <code>
     external_object_storage.bucket_name_suffix
    </code>
    <sup>
     2
    </sup>
   </td>
   <td headers="d59234e508">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Indicate the suffix for the bucket names. Optional in the case of the AWS non-instance profile.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.account_key
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify the Azure account key.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.account_name
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify the Azure account name.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e505">
    <p>
     <code>
      external_object_storage.azure_fqdn_suffix
     </code>
    </p>
   </td>
   <td headers="d59234e508">
    <p>
     ✅
    </p>
   </td>
   <td headers="d59234e511">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e514">
    <p>
     ❌
    </p>
   </td>
   <td headers="d59234e517">
    <p>
     Specify the Azure FQDN suffix. Optional parameter.
    </p>
   </td>
  </tr>
 </tbody>
</table>

<sup>1</sup> If you plan on disabling pre-signed URL access, note that this configuration is not supported by Task Mining and the following activities that upload or retrieve data from the objectstore:

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

You can use the parameters described in the [General configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#general-configuration) section to update the general Automation Suite configuration. This means that all installed products would share the same configuration. If you want to configure one or more products differently, you can override the general configuration. You just need to specify the product(s) you want to set up external object storage for differently, and use the same parameters to define your configuration. Note that all the other installed products would continue to inherit the general configuration.

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

To rotate the blob storage credentials for Process Mining in Automation Suite the stored secrets must be updated with the new credentials. See [Rotating blob storage credentials](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/rotating-blob-storage-credentials#rotating-blob-storage-credentials).

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
| `registries.docker.pull_secret_value` | The registry pull secret. |
| `registries.helm.url` | Default value: `registry.uipath.com`  The URL or FQDN of the registry to be used by Automation Suite to host the Helm chart of the service. |
| `registries.helm.username`  `registries.helm.password` | Authentication information to be used for pulling Helm charts from the registry.  If one of the values is found in the input file, you must provide both of them when configuring the external registry. |
| `registry_ca_cert` | The location of the CA file corresponding to the certificate configured for the registry.  If the registry is signed by a private certificate authority hosted on your premises, you must provide it to establish the trust. |

:::note
You can use different methods to generate the encoded version of the `pull_secret_value`, including the one using Docker. For details, see .
:::

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

### Internal load balancer configuration

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

You can use the `uipathctl` command-line tool to apply configuration changes. For more information, check the [uipathctl reference guide](https://docs.uipath.com/automation-suite/automation-suite/2023.10/reference-guide/uipathctl-reference).

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
   <td headers="d59234e1501">
    <p>
     <code>
      sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d59234e1504">
    DotNet formatted connection string with database set as a placeholder:
    <code>
     Initial Catalog=DB_NAME_PLACEHOLDER
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d59234e1501">
    <p>
     <code>
      sqlalchemy_pyodbc_sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d59234e1504">
    Sqlalchemy PYODBC formatted connection string for custom airflow metadata database location:
    <code>
     sqlServer:1433/DB_NAME_PLACEHOLDER
    </code>
    .
    <p>
     Example:
    </p>
    <p>
     <code>
      mssql+pyodbc://testadmin%40myhost:mypassword@myhost:1433/AutomationSuite_Airflow?driver=ODBC+Driver+17+for+SQL+Server&amp;TrustServerCertificate=YES&amp;Encrypt=YES
     </code>
    </p>
    <p>
     where
    </p>
    user:
    <code>
     testadmin%40myhost
    </code>
    Note:
    <p>
     If there is '@' in user name it has to be urlencoded to %40
    </p>
    <p>
     Example: (SQL Server setup with Kerberos authentication)
    </p>
    <p>
     <code>
      mssql+pyodbc://:@assql2019.autosuitead.local:1433/AutomationSuite_ProcessMining_Warehouse?driver=ODBC+Driver+17+for+SQL+Server&amp;TrustServerCertificate=YES&amp;Encrypt=YES&amp;Trusted_Connection=yes
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d59234e1501">
    <p>
     <code>
      warehouse.sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d59234e1504">
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
   <td headers="d59234e1501">
    <p>
     <code>
      warehouse.sqlalchemy_pyodbc_sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d59234e1504">
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
   <td headers="d59234e1501">
    <p>
     <code>
      warehouse.master_sql_connection_str
     </code>
    </p>
   </td>
   <td headers="d59234e1504">
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

Sample Process Mining connection string

```
"processmining": {
    "enabled": true,
    "app_security_mode": "system_managed",
    "warehouse": {
        "sql_connection_str": "Server=tcp:sfdev4515230-sql.database.windows.net,1433;Initial Catalog=AutomationSuite_ProcessMining_Warehouse;User Id=testadmin@sfdev4515230-sql.database.windows.net;Password='password';Persist Security Info=False;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
        "sqlalchemy_pyodbc_sql_connection_str": "mssql+pyodbc://testadmin%40sfdev4515230-sql.database.windows.net:<password>:@sfdev4515230-sql.database.windows.net:1433/AutomationSuite_ProcessMining_Warehouse?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=YES&Encrypt=YES",
        "master_sql_connection_str": "Server=tcp:sfdev4515230-sql.database.windows.net,1433;Initial Catalog=master;Persist Security Info=False;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
    },
    "sqlalchemy_pyodbc_sql_connection_str": "mssql+pyodbc://testadmin%40sfdev4515230-sql.database.windows.net:<password>@sfdev4515230-sql.database.windows.net:1433/AutomationSuite_Airflow?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=YES&Encrypt=YES"
    "sql_connection_str": "Server=tcp:sfdev4515230-sql.database.windows.net,1433;Initial Catalog=AutomationSuite_ProcessMining_Metadata;User Id=testadmin@sfdev4515230-sql.database.windows.net;Password='password';Persist Security Info=False;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",  
},
```

:::note
When using Kerberos authentication, utilize the `Integrated Security` and `Trusted_Connection` parameters. By setting `Integrated Security` to `true` and setting `Trusted_Connection` to `yes`, the credentials of the currently logged in user are used for the connection. In this case, you do not need to specify a separate username and password.
:::
:::note
When setting up Microsoft SQL Server make sure that the timezone of the SQL Server machine where the Airflow database is installed, is set to UTC.
:::
:::important
You must use the default server port `1433` for Airflow database connections. Non-standard SQL server ports are not supported.
:::
:::note
When configuring the connection strings for the processmining data warehouse SQL Server, the named instance of the SQL Server should be omitted. Named instances of SQL Server cannot operate on the same TCP port. Therefore, the port number alone is sufficient to distinguish between instances. For example, use `tcp:server,1445` instead of `tcp:server\namedinstance,1445`.
:::
:::important
Note that the names for *template* PYODBC connection string `sql_connection_string_template_sqlalchemy_pyodbc` and the PYODBC connection string `sqlalchemy_pyodbc_sql_connection_str` used when you *bring your own database* are different. Also connection string names are different for the template SQL `sql_connection_string_template` and `sql_connection_str` used when you *bring your own database*.
:::
:::important
If you bring your own database and you configured this using the `sql_connection_str` and `sqlalchemy_pyodbc_sql_connection_str` connection strings in the `processmining` section of the `input.json`file, the *template* connection strings `sql_connection_string_template` and `sql_connection_string_template_sqlalchemy_pyodbc` are ignored if specified.
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