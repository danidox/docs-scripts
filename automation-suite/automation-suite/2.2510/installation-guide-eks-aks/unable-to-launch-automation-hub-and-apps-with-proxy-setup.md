---
title: "Unable to launch Automation Hub and Apps with proxy setup"
visible: true
slug: "unable-to-launch-automation-hub-and-apps-with-proxy-setup"
---

## Description

If you use a proxy setup, you may run into issues when trying to launch Automation Hub and Apps.

## Solution

You can fix the issue by taking the following steps:

1. Capture the existing `coredns` configmap from the running cluster:
   ```
   kubectl get configmap -n kube-system coredns -o yaml > coredns-config.yaml
   ```
2. Edit the `coredns-config.yaml` file to append the FQDN rewrite to the config.
   1. Rename the configmap to `coredns-custom`.
   2. Apply the correct configuration depending on your platform:
      * For AKS, define a new CoreDNS zone for the FQDN, as shown in the following example:
        ```
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: coredns-custom
          namespace: kube-system
        data:
          <FQDN>.server: |
            <FQDN>:53 {
                errors
                log
                health
                rewrite stop {
                    name exact <FQDN> istio-ingressgateway.istio-system.svc.cluster.local
                }
                kubernetes cluster.local in-addr.arpa ip6.arpa {
                  pods insecure
                  fallthrough in-addr.arpa ip6.arpa
                }
                prometheus :9153
                forward . /etc/resolv.conf
                cache 30
                loop
                reload
                loadbalance
            }
        ```
      * For EKS, it is enough to add only the rewrite block to the existing CoreDNS Corefile:
        ```
        rewrite stop {
            name exact <FQDN> istio-ingressgateway.istio-system.svc.cluster.local
        }
        ```Replace &lt;FQDN&gt; with the actual cluster FQDN.
3. Create the `coredns-custom` configmap:
   ```
   kubectl apply -f coredns-config.yaml
   ```
4. Replace the volume reference from `coredns` to `coredns-custom` in the `coredns` deployment in `kube-system` namespace:
   ```
   volumes:
     - emptyDir: {}
       name: tmp
     - configMap:
         defaultMode: 420
         items:
         - key: Corefile
           path: Corefile
         name: coredns-custom
       name: config-volume
   ```
5. Restart the `coredns` deployment and ensure the `coredns` pods are up and running without any issues:
   ```
   kubectl rollout restart deployment -n kube-system coredns
   ```
6. You should now be able to launch Automation Hub and Apps.