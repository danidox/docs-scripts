---
title: "Pods cannot communicate with FQDN in a proxy environment"
visible: true
slug: "pods-cannot-communicate-with-fqdn-via-proxy"
---

## Description

In a proxy environment, if the proxy server uses the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods cannot communicate with the FQDN. The issue causes the following error:

```
System.Net.Http.HttpRequestException: The proxy tunnel request to proxy 'http://<proxyFQDN>:8080/' failed with status code '404'.
```

## Solution

To fix the issue, you must create a `ServiceEntry`, as shown in the following example:

```
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: proxy
  namespace: uipath
spec:
  hosts:
  - <proxy-host>
  addresses:
  - <proxy-ip>/32
  ports:
  - number: <proxy-port>
    name: tcp
    protocol: TCP
  location: MESH_EXTERNAL
```

:::note
We fixed the issue in Automation Suite 2023.10.6. If you have already created the service entry, we recommend that you delete it after upgrading to Automation Suite 2023.10.6 or later. To delete the service entry, use the following command: assignment
```
kubectl delete serviceentry proxy -n uipath
```
:::