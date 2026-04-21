---
title: "Pods in the uipath namespace stuck when enabling custom node taints"
visible: true
slug: "pods-in-the-uipath-namespace-not-running-when-enabling-custom-node-taints"
---

## Description

Pods in the `<uipath>` namespace are not running when custom node taints are enabled. The pods cannot talk to the adminctl webhook that injects pod tolerations in an EKS env.

## Solution

To fix the issue, create a network policy to allow traffic into the `admctl` webhook from the cluster CIDR or `0.0.0.0/0`.

```
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-all-ingress-to-admctl
  namespace: <uipath>
spec:
  podSelector:
    matchLabels:
      app: admctl-webhook
  ingress:
    - from:
        - ipBlock:
            cidr: <cluster-pod-cdr> or "0.0.0.0/0"
```