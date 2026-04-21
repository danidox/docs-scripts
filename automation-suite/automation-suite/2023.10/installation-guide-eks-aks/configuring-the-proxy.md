---
title: "Proxy"
visible: true
slug: "configuring-the-proxy"
---

To deploy Automation Suite in a proxy configuration, you must configure your cluster and add all UiPath® required domains to an allowlist in your network proxy.

A proxy configuration is required only if you perform an online installation.

:::important
Automation Suite does not support the IPv6 internet protocol.
:::

## Configuring the cluster

For instructions on how to configure the cluster worker nodes in proxy mode, refer to the respective documentation from Microsoft and AWS:

* AWS example - [Automate HTTP proxy configuration for Amazon EKS containerd nodes](https://repost.aws/knowledge-center/eks-http-proxy-containerd-automation)
* Microsoft example - [Configuring Azure Kubernetes Service (AKS) nodes with an HTTP proxy - Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/http-proxy)

When configuring the cluster nodes in proxy mode, make sure to add the following domains to the `no_proxy` list:

* EKS
  ```
  "$VPC_CIDR,$SERVICE_CIDR, localhost,127.0.0.1,169.254.169.254,<clusterfqdn>,.<clusterfqdn>,.internal,.eks.amazonaws.com,.cloudfront.net,s3.CLOUD_REGION.amazonaws.com,.s3.CLOUD_REGION.amazonaws.com,.dkr.ecr.CLOUD_REGION.amazonaws.com,ec2.CLOUD_REGION.amazonaws.com,api.ecr.CLOUD_REGION.amazonaws.com,.elb.amazonaws.com,.gr7.CLOUD_REGION.eks.amazonaws.com,.s3.amazonaws.com,kubernetes,kubernetes.default,kubernetes.default.svc,kubernetes.default.svc.cluster,kubernetes.default.svc.cluster.local,.svc,.svc.cluster,.svc.cluster.local,.svc.cluster.local.,argocd-repo-server,istiod.istio-system.svc,logging-operator-logging-fluentd.logging.svc.cluster.local,argocd-repo-server,.local,.cluster,ai-helper-svc,ai-pkgmanager-svc,ai-deployer-svc,ai-appmanager-svc,ai-trainer-svc,get"
  ```
* AKS
  ```
  "<cluster-fqdn>,.<cluster-fqdn>,localhost,127.0.0.1,10.0.0.0/8,mcr.microsoft.com,kubernetes,kubernetes.default,kubernetes.default.svc,kubernetes.default.svc.cluster,kubernetes.default.svc.cluster.local,.svc,.svc.cluster,.svc.cluster.local,.svc.cluster.local.,argocd-repo-server,istiod.istio-system.svc,logging-operator-logging-fluentd.logging.svc.cluster.local,argocd-repo-server,.local,.cluster,ai-helper-svc,ai-pkgmanager-svc,ai-deployer-svc,ai-appmanager-svc,ai-trainer-svc,get\"
  ```

:::note
Make sure to replace `&lt;cluster-fqdn&gt;` with the actual FQDN URL.
:::

## Providing proxy setting in input.json

Configure the `input.json` file with the following parameters:

| Mandatory parameters | Description |
| --- | --- |
| `enabled` | Use `true` or `false` to enable or disable proxy settings. |
| `http_proxy` | Used to route HTTP outbound requests from the cluster. This should be the proxy server FQDN and port. |
| `https_proxy` | Used to route HTTPS outbound requests from the cluster. This should be the proxy server FQDN and port. |
| `no_proxy` | Comma-separated list of hosts, IP addresses, or IP ranges in CIDR format that you do not want to route via the proxy server.  The list must be the one provided in the [Configuring the cluster](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-proxy#configuring-the-cluster) section for EKS or AKS, respectively. |

Example `input.json` for proxy configuration:

```
"proxy": {
  "enabled": true,
  "http_proxy": "http://<PROXY-SERVER-IP:<PROXY-PORT>",>
  "https_proxy": "http://<PROXY-SERVER-IP:<PROXY-PORT>",>
  "no_proxy": <"paste list from Configuring the cluster section">
  }
```

## Adding URLs to an allowlist

### URLs for EKS and AKS

```
.microsoft.com
login.microsoftonline.com
login.windows.net
graph.microsoft.com
sfbrprddeploywe.azurecr.io
sfbrprddeploywe.westeurope.data.azurecr.io
registry-data.uipath.com
registry.uipath.com
dc.services.visualstudio.com
activate.uipath.com
download.uipath.com
du-metering.uipath.com
du.uipath.com
du-au.uipath.com
du-ca.uipath.com
du-jp.uipath.com
du-us.uipath.com
du-sg.uipath.com
raw.githubusercontent.com
objects.githubusercontent.com
pkg-containers.githubusercontent.com
raw.github.com
api.github.com
api.nuget.org
pkgs.dev.azure.com
gallery.uipath.com
github.com
pypi.org
pypi.python.org
pythonhosted.org
files.pythonhosted.org
opensuse.org
copr.fedorainfracloud.org
download.copr.fedorainfracloud.org
ping.looker.com
rt.services.visualstudio.com
uipath.pkgs.visualstudio.com
.blob.core.windows.net
pkgs.dev.azure.com
events.launchdarkly.com
app.launchdarkly.com
in.applicationinsights.azure.com
.pkg.dev
production.cloudflare.docker.com
.googleapis.com
```

### Additional URLs for EKS

```
.s3.dualstack.CLOUD_REGION.amazonaws.com
public.ecr.aws
.cloudfront.net
```

## Pods failing to communicate with FQDN in a proxy environment

In a proxy environment, if the proxy server uses the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods cannot communicate with the FQDN. For more information on the issue and how to address it, see [Pods cannot communicate with FQDN in a proxy environment](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pods-cannot-communicate-with-fqdn-via-proxy#pods-cannot-communicate-with-fqdn-in-a-proxy-environment).