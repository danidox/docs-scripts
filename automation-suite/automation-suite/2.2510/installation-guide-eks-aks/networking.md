---
title: "Networking"
visible: true
slug: "networking"
---

You must provision and configure Azure or AWS networking resources to ensure that Automation Suite on your cluster has connectivity and access to the cloud infrastructure prerequisites (e.g., storage, database, cache, and DNS). Depending on your networking architecture, this may include configuring VNETs / VPC, DNS, subnets, NSGs / security groups, NAT gateway, elastic IP, and internet gateway. For details, see [Deployment scenarios](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/deployment-scenarios#deployment-scenarios).

Note that, based on the workload scaling, more replicas might be needed. By default, the HA mode requires two replicas and can go up to ten or more replicas. Make sure your network supports this scaling level.

You can use any CNI as long as pods can communicate with one another.

There are special considerations for cloud CNIs such as Azure CNI and Amazon VPC CNI, which do not support internal or private pod networking subnets. The number of pods required for Automation Suite depends on your product selection and workload scaling. For instance, for a deployment with all the services enabled and at high utilization, you might need over 400 IPs to support the scaling requirements. Because of this, we recommend allocating a CIDR range of at least /23.

Automation Suite supports IPv6 and dual-stack configurations.

:::important
Migration from single-stack IPv4 to dual-stack or single-stack IPv6 is not supported. All external dependencies, such as SQL, Redis, object storage, and external DNS must support the enabled IP family.
:::

:::note
Changes to IP tables are not recommended or supported.
:::

## IPv6 or dual-stack configuration

To enable IPv6 or dual stack, you must configure the `network` parameter in the `input.json` file to specify whether Automation Suite uses IPv4, IPv6, or both.

You can configure it as follows:

* Dual-stack configuration: enables both IPv4 and IPv6 communication for Automation Suite services and ingress components. You can use the following example to configure dual-stack networking:
  ```
  "network": {
    "ipv4": { "enabled": true },
    "ipv6": { "enabled": true }
  }
  ```
* Single-stack IPv6 configuration: enables IPv6-only communication and disables IPv4. You can use the following example to configure single-stack IPv6 networking:
  ```
  "network": {
    "ipv4": { "enabled": false },
    "ipv6": { "enabled": true }
  }
  ```

:::note
Some Integration Service connectors may not support IPv6. Before enabling this feature, check the provider documentation and authentication requirements for the connectors you use to make sure IPv6 is supported.
:::

## Custom ingress controller

If you have a custom ingress controller (NGINX), refer to [Configuring NGINX ingress](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-nginx-ingress-controller#configuring-nginx-ingress-controller) and skip the rest of the page.

## Load balancer configuration

Automation Suite provisions a load balancer on your behalf during installation. The load balancer must be assigned with public or private IP addresses to route the incoming FQDN requests. You have two options to configure the load balancer:

* **Preallocated IPs**: Allocate public or private IPs for the load balancer, configure the DNS records to map the FQDNs to these IPs, and provide these IPs as part of the ingress section of `input.json`.
* **Dynamically allocated IPs:** If you do not provide an IP address, Automation Suite dynamically allocates IPs from the cluster subnet to the load balancer.

The network security groups on the load balancer must allow HTTPS traffic from end clients via port 443. By default, we configure the load balancer to conduct regular TCP health checks.

If using your own ingress like NGINX, make sure you meet the network requirements documented in [Configuring NGINX ingress controlle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-nginx-ingress-controller#configuring-nginx-ingress-controller)r. When using Istio that deploys an NLB, note that it typically creates three listeners, which include ports 80, 443, and 15021. However, this is a typical setup, and your actual requirements may differ based on your exact circumstances, so adjust as needed.

## Pre-allocated IPs

You must provide the following service annotations in the `ingress` section of `input.json`.

For a list of service annotations in EKS, see the [AWS Load Balancer documentation](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/guide/service/annotations/).

For a list of service annotations in AKS, see the [Azure Load Balancer documentation](https://cloud-provider-azure.sigs.k8s.io/topics/loadbalancer/#loadbalancer-annotations).

### EKS annotations examples

The following examples show how to create the `ingress.service_annotations` section in `input.json`. You must deploy an [AWS load balancer controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.7/deploy/installation/) on your EKS cluster prior to the installation for the examples to properly work.

The following example shows how to allocate Elastic IPs from AWS and provision a public load balancer. If you use this example as a starting point for your configuration, make sure to replace the IPs with actual values.

```
"ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/aws-load-balancer-backend-protocol": "ssl",
      "service.beta.kubernetes.io/aws-load-balancer-eip-allocations": "<elastic_ip_id_0>,<elastic_ip_id_1>",
      "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type": "ip",
      "service.beta.kubernetes.io/aws-load-balancer-scheme": "internet-facing",
      "service.beta.kubernetes.io/aws-load-balancer-type": "nlb"
    }
  }
```

The following example shows how to allocate private IPs to an internal load balancer from the EKS cluster subnets. If you use this example as a starting point for your configuration, make sure to update the IPs and subnets with actual values.

```
 "ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/aws-load-balancer-backend-protocol": "ssl",
      "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type": "ip",
      "service.beta.kubernetes.io/aws-load-balancer-private-ipv4-addresses":""<IP_0>,<IP_1>"",
      "service.beta.kubernetes.io/aws-load-balancer-subnets": "SUBNET_ID_0>,<SUBNET_ID_1>",
      "service.beta.kubernetes.io/aws-load-balancer-scheme": "internal",
      "service.beta.kubernetes.io/aws-load-balancer-type": "nlb"
      "service.beta.kubernetes.io/aws-load-balancer-target-group-attributes": "preserve_client_ip.enabled=false"
    }
  }
```

:::important
IPs and subnets must match. In the previous example, `&lt;IP_0&gt;` is in `&lt;SUBNET_0&gt;` and `&lt;IP_1&gt;` in `&lt;SUBNET_1&gt;`.
:::

### AKS annotations example

The following example shows how to allocate public IPs from Azure and provision a public load balancer. If you use this example as a starting point for your configuration, make sure to update the IPs with actual values.

```
...
"ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/azure-load-balancer-internal": "false",
      "service.beta.kubernetes.io/azure-load-balancer-ipv4": "<IP>"
    }
  }
...
```

The following example shows how to allocate private IPs to an internal load balancer from the AKS cluster subnets. If you use this example as a starting point for you configuration, make sure to update the IPs and subnets with actual values.

```
...
"ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/azure-load-balancer-internal": "true",
      "service.beta.kubernetes.io/azure-load-balancer-ipv4": "<IP>",
      "service.beta.kubernetes.io/azure-load-balancer-internal-subnet": "<SUBNET>",
    }
  }
...
```

### DNS configuration

Ensure that the DNS records are configured to map the following UiPath® FQDNs to the load balancer:

* `FQDN`
* `alm.FQDN`
* `monitoring.FQDN`
* `insights.FQDN` (if installing UiPath Insights)
* `apps.FQDN` (if installing UiPath Apps)
  :::note
  The FQDN is one of the prerequisite checks before installation. If you do not provide an IP address or have not yet done the FQDN mapping, the check will fail.
  :::

When using Route 53 for DNS, change the relevant DNS records to Alias records that directly point to the Elastic Load Balancer (ELB) created during the installation. This ensures proper routing and faster resolution, especially when multiple public IPs are involved during multi-AZ installations in AWS environments.

## Dynamically allocated IPs

If you do not provide any IPs in `input.json`, Automation Suite dynamically allocates the private IPs from the worker node subnets. In this scenario, run the Automation Suite installation in the following way.

### EKS example of input.json

```
...
  "ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/aws-load-balancer-backend-protocol": "ssl",
      "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type": "ip",
      "service.beta.kubernetes.io/aws-load-balancer-scheme": "internal",
      "service.beta.kubernetes.io/aws-load-balancer-type": "nlb",
      "service.beta.kubernetes.io/aws-load-balancer-internal": true
    }
  }
...
```

### AKS example of input.json

```
...
  "ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/azure-load-balancer-internal": "true"
    }
  }
...
```

### Installation steps

In this scenario, run the installer as follows:

1. Run the installer only until the provisioning of the Load Balancer:
   ```
   uipathctl manifest apply <INPUT_JSON> --versions <VERSIONS_JSON> --override=gateway
   ```
2. Retrieve the load balancer host name:
   ```
   kubectl get svc -n <istio-system> istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
   ```
3. Configure your DNS with FQDNs mapped to the load balancer endpoint or IPs.
4. Re-run the installer to complete the installation:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```

:::note
Note that without the DNS mapping, the FQDN prerequisite check will fail. Prerequisite checks are meant to give you confidence that you have provisioned all the prerequisites correctly before installing Automation Suite. The FQDN check does not prevent you from installing Automation Suite.
:::