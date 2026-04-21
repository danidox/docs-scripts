---
title: "Configuring NGINX ingress controller"
visible: true
slug: "configuring-nginx-ingress-controller"
---

In standard configuration, Automation Suite provisions a Load Balancer Kubernetes service type configured with Istio Gateway as an ingress controller for the requests coming from the network load balancer.

If you already have an [NGINX ingress controller](https://github.com/kubernetes/ingress-nginx) in your cluster and want to continue to use it, you must configure the Kubernetes `service_type` as `cluster_IP` instead of Load Balancer. This document provides the necessary changes required for that configuration.

:::important
To manage large headers, adjust the `proxy-buffer-size` in the ingress annotation as follows: assignment
```
nginx.ingress.kubernetes.io/proxy-buffer-size: "8k"
```
:::

## NGINX to Istio via HTTP

### Updating your NGINX ingress configuration

You must update your NGINX specification with `istio-ingressgateway` as a backend service and specify the port number 80. Additionally, if you have your own Network Policies,make sure they are configured correctly to allow NGINX and Istio routing.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
  namespace: <istio-system>
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - "<FQDN>"
        - "*.<FQDN>"
      secretName: nginx-tls
  rules:
    - host: "<FQDN>"
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: istio-ingressgateway
              port:
                number: 80
    - host: "*.<FQDN>"
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: istio-ingressgateway
              port:
                number: 80
```

### input.json parameters

You must provide the following parameters in `input.json` to change `service_type` and `HTTPS`:

```
...
"ingress": {
  "service_type": "ClusterIP",
  "HTTPS": false
}
...
```

## NGINX to Istio via HTTPs

### Updating the NGINX ingress configuration

You must update your NGINX specification with `istio-ingressgateway` as a backend service and specify `https` as the port name.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
  namespace: <istio-system>
  annotations:
    nginx.ingress.kubernetes.io/backend-protocol: "https"
    nginx.ingress.kubernetes.io/proxy-ssl-name: "<FQDN>"
    nginx.ingress.kubernetes.io/proxy-ssl-server-name: "on"
    nginx.ingress.kubernetes.io/proxy-ssl-secret: "<istio-system>/istio-ingressgateway-certs"
    nginx.ingress.kubernetes.io/proxy-ssl-verify: "on"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - "<FQDN>"
        - "*.<FQDN>"
      secretName: nginx-tls
  rules:
    - host: "<FQDN>"
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: istio-ingressgateway
              port:
                name: https
    - host: "*.<FQDN>"
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: istio-ingressgateway
              port:
                name: https
```

### input.json parameters

You must provide the following parameters in `input.json` to change `service_type` and `HTTPS`:

```
...
"ingress": {
  "service_type": "ClusterIP",
  "HTTPS": true
}
...
```