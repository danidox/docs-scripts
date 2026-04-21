---
title: "Installing Automation Suite"
visible: true
slug: "installing-automation-suite"
---

This page walks you through the high-level installation instructions for Automation Suite on AKS and EKS.

Before you begin, consider the following:

* Kubernetes, AWS, and Azure cloud resources management knowledge is required to deploy and manage Automation Suite on AKS/EKS. If you encounter issues installing and configuring Automation Suite on AKS/EKS, contact UiPath® Professional Services.
* Before choosing your deployment profile, see [Deployment scenarios](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/deployment-scenarios#deployment-scenarios).
* The installation process generates self-signed certificates on your behalf. You should replace them with certificates signed by a trusted Certificate Authority (CA) as soon as installation completes. For instructions, see [Managing the certificates](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-certificates#managing-the-certificates).
* Automation Suite supports enabling Federal Information Processing Standard 140-2 (FIPS 140-2) on AKS nodes. For details, see [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance#fips-140-2). You cannot enable FIPS 140-2 on EKS nodes.

## Step 1: Provisioning the infrastructure prerequisites

Before installing Automation Suite, you must configure the cloud resources in your environment. This includes the following:

* AKS or EKS cluster
* Mandatory for offline installations: external OCI-compliant registry
* Object Storage - Azure Blob or Amazon S3
* Block storage
* File storage
* Databases
* Caching
* Networking (e.g., VNETs / VPC, DNS, subnets, NSGs / security groups, NAT gateway, elastic IP and internet gateway)
* Networking policies
* Certificates

For instructions on prerequisites, see [Prerequisites at a glance.](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/requirements)

### Optional: Configuring the proxy

If you use a proxy server for internet-facing traffic, you must allow a list of URLs and use the `no_proxy` settings while configuring the proxy. For instructions on how to configure your proxy, see [Proxy](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-proxy#proxy).

## Step 2: Configuring the external OCI-compliant registry

In offline installations, you need a registry compliant with OCI (Open Container Initiative) to store the container images and deployment Helm charts.

There are two ways to upload the Automation Suite artifacts to the external OCI-compliant registry:

* **Option A**: By [mirroring your OCI-compliant registry with the UiPath® registry](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-oci-compliant-registry#option-a%3A-mirroring-the-uipath%C2%AE-registry-to-your-registry)
* **Option B**: By [hydrating your OCI-compliant registry with the offline bundle](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-oci-compliant-registry#option-b%3A-hydrating-the-registry-with-the-offline-bundle)

## Step 3: Downloading the software on your client machine

You must install the following software on your management machine. Management machine refers to the machine you use to operate your cluster and that can access your cluster via the `kubeconfig` file. Your management machine can run Linux, Windows, or MacOS.

The following tools are required to successfully run the prerequisite checks, installation, and post-installation steps on your cluster via the client machine.

| Tool | Description | Download |
| --- | --- | --- |
| `uipathctl` | **Required**. `uipathctl` is a UiPath® command-line tool that allows you to run commands against Automation Suite Kubernetes hosted on Azure Kubernetes Service (AKS) and Amazon Elastic Kubernetes Service (EKS).  You can use `uipathctl` to check prerequisites in your environment, install Automation Suite, configure and manage it from a single unified CLI. For more information, including a complete list of `uipathctl` operations, see the . | [Download uipathctl](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/downloading-the-installation-packages#uipathctl)  [Run uipathctl](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/uipathctl#uipathctl) |
| `versions.json` | **Required**. Needed to perform prerequisite checks and installation steps. | [Download versions.json](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/downloading-the-installation-packages#versionsjson) |
| `kubectl` | **Optional**. Ensure that `kubectl` matches the version of your cluster | [Download kubectl](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/downloading-the-installation-packages#kubectl) |

## Step 4: Configuring input.json

You must edit the `input.json` file to provide the required inputs for the `uipathctl` installer and perform operations such as configuring the SQL connection strings and the UiPath® services you would like to enable.

We provide different `input.json` template files for AKS and EKS. For instructions on how to configure `input.json`, see [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#configuring-inputjson).

Optionally, you can bring your own components that are part of the Automation Suite stack. For details on the components, see [Automation Suite on EKS/AKS stack](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-stack#automation-suite-stack). For details on how to configure the component you bring, see [Bring your own components](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#bring-your-own-components).

If you perform an offline installation, make sure to configure your [external OCI-compliant registry](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#external-oci-compliant-registry-configuration).

To install Automation Suite on EKS/AKS in offline mode, you must take the following additional steps:

* Explicitly set the value of the `install_type` parameter to `offline` in the `input.json` file;
* [Configure an external OCI-compliant registry](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-oci-compliant-registry#configuring-the-oci-compliant-registry).

## Step 5: Accessing your cluster with uipathctl

`uipathctl` requires access to the KubeAPI Server to perform cluster-level operations such as deployment, resource creation, etc. To access the KubeAPI server, `uipathctl` uses the `kubeconfig` file, which contains the admin-level credentials needed to access the cluster. This file must be present in the `~/.kube/config` folder (default location) of your local (management) machine.

Optionally, if you are concerned about storing the `kubeconfig` file in the default location, you can alternatively provide it with help of the `--kubeconfig` flag during every execution of `uipathctl`.

For example, you can use your preferred method to update your `~/.kube/config` file by using [AWS CLI](https://aws.amazon.com/cli/) or [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/).

## Step 6: Checking the infrastructure prerequisites

Prerequisite checks ensure that the needed cloud infrastructure is provisioned appropriately and is accessible by the client machine before starting the installation of Automation Suite.

The installer can automatically generate the following configurations on your behalf:

* The SQL databases required for the installation on the SQL server based if the `sql.create_db` key is set in your `input.json` file.
* The object storage buckets required in your cloud provider if the `external_object_storage.create_bucket` key is set in the configuration file.

To allow the installer to generate these configurations, run the following command:

```
uipathctl prereq create input.json --versions versions.json
```

:::important
The `uipathctl prereq create` command does not create the required SQL databases for Process Mining. You must manually create them by following the instructions in [Bring your own database](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/sql-database#bring-your-own-databases).
:::

To check the prerequisites based on the inputs you configured in the `input.json`, run the following command:

```
uipathctl prereq run input.json --versions versions.json
```

To check the prerequisites for installation, run . By default, the command checks all the prerequisites. However, it also allows you to run strictly the checks that are relevant to you:

* If you want to exclude components from the execution, use the `--excluded` flag. For example, if you do not want to check the database connection strings, run `uipathctl prereq --excluded SQL`. The command runs all the prerequisite checks except for the SQL-related one.
* If you want to include only certain components in the execution, use the `--included` flag. For example, if you only want to check the DNS and objectstore, run `uipathctl prereq --included DNS,OBJECTSTORAGE`.
  :::note
  You can find the names of the components you can include or exclude from the prerequisite checks [here](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/output-example-prerequisite-check#output-example%3A-prerequisite-check). In the example, the first word on each outdented line represents the component name. For example: SQL, OBJECTSTORE, DNS, etc.
  :::
:::important
You may receive a throttling message from AKS, such as *Waited for 1.0447523s due to client-side throttling, not priority and fairness.* In this case, allow a few minutes for the command to fully complete or try to re-run it.
:::

For an output result example, see [Output example: prerequisite check](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/output-example-prerequisite-check#output-example%3A-prerequisite-check).

### Prerequisite checks

It is recommended to run prerequisite checks to ensure that you properly configured the cloud infrastructure and to validate `input.json` before starting the Automation Suite installation.

You can run a prerequisite check using the command. By default, this command verifies all the prerequisites. You can use the following flags:

* `--excluded`, if you want to exclude components from the execution.
* `--verbose`, if you want to access the detailed prerequisites check output. You can skip this flag for a more concise and simplified output.

The prerequisite and health checks/tests run in the `uipath-check` namespace. You must either allow the creation of the `uipath-check` namespace or create it yourself before running the checks/tests. In addition to this, some checks/tests require that you allow the communication between the `uipath-check` and `uipath` namespaces, or that you enable the use of `hostNetwork`.

The checks in the following table are run on each node:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Check
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Description
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d2687e480">
    <p>
     SQL Connection
    </p>
   </td>
   <td headers="d2687e484">
    Validates that Automation Suite can successfully connect to SQL server for UiPath&reg; products and shared services (such as Identity,
                                       Portal, Org Mamagement, etc.) using the SQL connection strings provided in
    <code>
     input.json
    </code>
    . This is mandatory for a successful installation.
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     SQL DB roles
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates the necessary roles and permissions required by UiPath&reg; products. This is mandatory for a successful installation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     SQL DB compatibility
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates SQL DB compatibility requirements.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     FQDN resolution
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates that the FQDN and the sub-domains are successfully resolvable.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Object Storage API
    </p>
   </td>
   <td headers="d2687e484">
    Validates that Object store APIs are accessible based on access information provided in
    <code>
     input.json
    </code>
    . This is mandatory for a successful installation of UiPath&reg; Services.
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Cache / Redis
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates the connection to Cloud Redis or ElastiCache. This is mandatory for a successful installation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Capacity
    </p>
   </td>
   <td headers="d2687e484">
    Validates you have minimum worker nodes' CPU and RAM capacity based on products enabled in
    <code>
     input.json
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Storage Class
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates the storage classes for File Storage are configured as required for Automation Suite Robots.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Optional Components
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates that your cluster has components that you chose to exclude from the Automation Suite installation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Ingress
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates that the cluster ingress is configured correctly and the FQDN URL requests can reach UiPath&reg; products.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Network Policies
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Checks if network policies configured in Automation Suite are compatible with the cluster.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Registry
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates that Automation Suite can access the UiPath&reg; docker registry. This is mandatory for a successful installation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2687e480">
    <p>
     Cluster Connectivity
    </p>
   </td>
   <td headers="d2687e484">
    <p>
     Validates whether the cluster communication is configured properly:
    </p>
    <ul>
     <li>
      <p>
       Between two random pods completed
      </p>
     </li>
     <li>
      <p>
       Between pod to a multinode ClusterIP
      </p>
     </li>
     <li>
      <p>
       Between pod to a multinode ClusterIP without a clusterIP
      </p>
     </li>
     <li>
      <p>
       Between pod to a multinode ClusterIP using HostNetwork
      </p>
     </li>
     <li>
      <p>
       Between pod to a multinode ClusterIP without a clusterIP set using HostNetwork
      </p>
     </li>
     <li>
      <p>
       Between two pods colocated on the same node via ClusterIP
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Step 7: Installing Automation Suite

:::note
To see which deployment scenarios are available for Automation Suite on AKS/EKS, see [Deployment scenarios](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/deployment-scenarios#deployment-scenarios).
:::

1. After successfully validating the prerequisites, you can proceed to install Automation Suite by running the following command:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```

For an output example, see [Output example: Automation Suite installation](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/output-example-automation-suite-installation#output-example%3A-automation-suite-installation).
   :::note
   If you encounter issues while running the installation, rerun the command the installation commands with all the arguments and flags. For details on the issues you might encounter, refer to [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#troubleshooting).
   :::
2. To validate that your installation is successful, and services are healthy, run the following command:
   ```
   uipathctl health check
   ```