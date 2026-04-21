---
title: "Applying miscellaneous configurations"
visible: true
slug: "applying-miscellaneous-configurations"
---

:::note
Only apply the configurations in this section if you cannot provide admin privileges to the Automation Suite installer. If you can provide the required permissions to the installer, you do not need to apply the configurations in this section.
:::

## Creating a priority class

To create a priority class for UiPath® applications, take the following steps:

1. Save the following configuration as a YAML file:
   ```
   ---
   apiVersion: scheduling.k8s.io/v1
   kind: PriorityClass
   metadata:
     name: uipath-high-priority
   value: 1000000
   preemptionPolicy: PreemptLowerPriority
   globalDefault: false
   description: "Priority class for uipath applications"
   ```
2. Run the following command, replacing the `<file_name.yaml>` placeholder with the actual name of your YAML file:
   ```
   kubectl apply -f <file_name.yaml>
   ```

To disable priority class creation, set `ignore_priority_class` to `true` in the `input.json` file.

## Labeling the namespaces

To create namespace labels, run the following commands:

```
kubectl label namespace <uipath> uipath-injection=enabled
kubectl label namespace <uipath> istio-injection=enabled
```

## Configuring CoreDNS

If you are using a proxy setup, specific CoreDNS configuration changes are required to ensure successful installation and operation of Automation Hub and Apps.

We recommend adding this to the CoreDNS settings as it allows any Service to Service requests, that use the FQDN of the cluster, to bypass the load balancer and route internally through Istio.

Follow these steps to configure your cluster during installation:

1. Capture the existing `coredns` configmap from the running cluster:
   ```
   kubectl get configmap -n kube-system coredns -o yaml > coredns-config.yaml
   ```
2. Edit the `coredns-config.yaml` file to append the `fqdn` rewrite to the config.
   1. Rename the configmap to `coredns-custom`.
   2. Add the following code block to your `coredns-config.yaml` file. Make sure the code block comes before the `kubernetes cluster.local in-addr.arpa ip6.arp` line.
      ```
      rewrite stop {
                              name exact <cluster-fqdn> istio-ingressgateway.istio-system.svc.cluster.local
                              }
      ```
   3. Replace `<cluster-fqdn>` with the actual value.Once you have completed these steps, your file should resemble the following sample:
   ```
   apiVersion: v1
                   data:
                   Corefile: |
                   .:53 {
                   errors
                   log
                   health
                   rewrite stop {
                   name exact mycluster.autosuite.com istio-ingressgateway.istio-system.svc.cluster.local
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
                   kind: ConfigMap
                   metadata:
                   name: coredns-custom
                   namespace: kube-system
   ```
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

Once these steps are complete, Automation Hub and Apps should launch successfully in the proxy-enabled environment.