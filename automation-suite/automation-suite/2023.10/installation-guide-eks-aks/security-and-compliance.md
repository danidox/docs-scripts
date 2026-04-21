---
title: "Security and compliance"
visible: true
slug: "security-and-compliance"
---

## Security context for UiPath® services

This section provides details on the security context of the UiPath® services.

All UiPath® services are configured with a security context defined in the `spec` section. The following sample shows the configuration for all services, with the exception of `du-cjk-ocr`:

```
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 1000
    fsGroup: 1000
  containers:
    - securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
  hostPID: false
  hostNetwork: false
```

In the case of the `du-cjk-ocr` service, the value of the `readOnlyRootFilesystem` parameter is `false`. For further information on `du-cjk-ocr`, see the [Document Understanding documentation](https://docs.uipath.com/document-understanding/automation-suite/2023.10/user-guide/document-understanding-deployed-in-automation-suite-install-and-use).

In some instances, the user IDs and group IDs can be greater than or equal to 1000. Such values are permissible based on your environment. It is important to configure the user and group IDs according to your security principles and your organization's security guidelines.

## Gatekeeper and OPA policies

Automation Suite is pre-configured with Gatekeeper and OPA policies. If you bring your own Gatekeeper component and OPA policies, you can skip these components from the Automation Suite installation. For details, see [Automation Suite stack](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-stack#automation-suite-stack). In this case, review the OPA policies and the exceptions needed for installing and running Automation Suite.

By default, these policies only run in the following UiPath® namespaces: `-uipath`, `uipath-installer`, `uipath-infra`, `airflow`, and `argocd`**.**

### OPA policies

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Policy
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Enforcement action
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Namespaces/Images to be excluded
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/allow-privilege-escalation">
      Allow Privilege Escalation in Container
     </a>
    </p>
    Controls restricting escalation to root privileges. Corresponds to the
    <code>
     allowPrivilegeEscalation
    </code>
    field in a PodSecurityPolicy
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/apparmor">
      App Armor
     </a>
    </p>
    <p>
     Configures an allowlist of AppArmor profiles for use by containers. This corresponds to specific annotations applied to a
                                       PodSecurityPolicy.
    </p>
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/capabilities">
      Capabilities
     </a>
    </p>
    Controls Linux capabilities on containers. Corresponds to the
    <code>
     allowedCapabilities
    </code>
    and
    <code>
     requiredDropCapabilities
    </code>
    fields in a PodSecurityPolicy.
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/flexvolume-drivers">
      FlexVolumes
     </a>
    </p>
    Controls the allowlist of FlexVolume drivers. Corresponds to the
    <code>
     allowedFlexVolumes
    </code>
    field in PodSecurityPolicy.
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/forbidden-sysctls">
      Forbidden Sysctls
     </a>
    </p>
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/fsgroup">
      FS Group
     </a>
    </p>
    Controls allocating an FSGroup that owns the pod's volumes. Corresponds to the
    <code>
     fsGroup
    </code>
    field in a PodSecurityPolicy.
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/host-filesystem">
      Host Filesystem
     </a>
    </p>
    Controls usage of the host filesystem. Corresponds to the
    <code>
     allowedHostPaths
    </code>
    field in a PodSecurityPolicy.
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/host-namespaces">
      Host Namespace
     </a>
    </p>
    Disallows sharing of host PID and IPC namespaces by pod containers. Corresponds to the
    <code>
     hostPID
    </code>
    and
    <code>
     hostIPC
    </code>
    fields in a PodSecurityPolicy.
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/host-network-ports">
      Host Networking Ports
     </a>
    </p>
    <p>
     Controls usage of host network namespace by pod containers.
    </p>
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/privileged-containers">
      Privileged Container
     </a>
    </p>
    Controls the ability of any container to enable privileged mode. Corresponds to the
    <code>
     privileged
    </code>
    field in a PodSecurityPolicy.
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/proc-mount">
      Proc Mount
     </a>
    </p>
    Controls the allowed
    <code>
     procMount
    </code>
    types for the container. Corresponds to the
    <code>
     allowedProcMountTypes
    </code>
    field in a PodSecurityPolicy.
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/read-only-root-filesystem">
      Read Only Root Filesystem
     </a>
    </p>
    <p>
     Requires the use of a read-only root file system by pod containers.
    </p>
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/seccomp">
      Seccomp
     </a>
    </p>
    Controls the seccomp profile used by containers. Corresponds to the
    <code>
     seccomp.security.alpha.kubernetes.io/allowedProfileNames
    </code>
    annotation on a PodSecurityPolicy.
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/selinux">
      SELinux V2
     </a>
    </p>
    <p>
     Defines an allowlist of seLinuxOptions configurations for pod containers.
    </p>
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/users">
      Allowed Users
     </a>
    </p>
    <p>
     Controls the user and group IDs of the container and some volumes.
    </p>
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       velero
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e98">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/volumes">
      Volume Types
     </a>
    </p>
    <p>
     Restricts mountable volume types to those specified by the user.
    </p>
   </td>
   <td headers="d27733e102">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e106">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       velero
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

:::note
* The `dapr-system`
namespace is only needed if you install Process Mining and Task Mining.
* The `airflow` namespace is only needed if you install Process Mining.
:::

### Other OPA policies

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Policy
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Enforcement action
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Namespaces/Images to be excluded
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/automount-serviceaccount-token">
      Automount Service Account Token for Pod
     </a>
    </p>
    Controls the ability of any pod to enable
    <code>
     automountServiceAccountToken
    </code>
    .
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/allowedrepos">
      Allowed Repositories
     </a>
    </p>
    <p>
     Requires container images to begin with a string from the specified list.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       <u>
        registry.uipath.com
       </u>
      </p>
     </li>
     <li>
      <p>
       <u>
        registry-data.uipath.com
       </u>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/block-endpoint-edit-default-role">
      Block Endpoint Edit Default Role
     </a>
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/block-loadbalancer-services">
      Block Services with type LoadBalancer
     </a>
    </p>
    <p>
     Disallows all services of type LoadBalancer.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       kube-system
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/block-nodeport-services">
      Block NodePort
     </a>
    </p>
    <p>
     Disallows all Services of type NodePort.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       network-prereq-checks
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/block-wildcard-ingress">
      Block Wildcard Ingress
     </a>
    </p>
    <p>
     Users must not able to create Ingresses with a blank or wildcard (*) hostname since that would enable them to intercept traffic
                                       for other services in the cluster, even if they do nto have access to those services.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/containerlimits">
      Container Limits
     </a>
    </p>
    <p>
     Requires containers to have memory and CPU limits set. Constrains limits to be within the specified maximum values.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/containerrequests">
      Container Requests
     </a>
    </p>
    <p>
     Requires containers to have memory and CPU requests set. Constrains requests to be within the specified maximum values.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/containerresourceratios">
      Container Ratios
     </a>
    </p>
    <p>
     Sets a maximum ratio for container resource limits to requests.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       prereq**
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/containerresources">
      Required Resources
     </a>
    </p>
    <p>
     Requires containers to have defined resources set.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/disallowanonymous">
      Disallow Anonymous Access
     </a>
    </p>
    Disallows associating ClusterRole and Role resources to the
    <code>
     system:anonymous
    </code>
    user and
    <code>
     system:unauthenticated
    </code>
    group.
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/disallowedtags">
      Disallow tags
     </a>
    </p>
    <p>
     Requires container images to have an image tag different from the ones in the specified list.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/ephemeralstoragelimit">
      Container ephemeral storage limit
     </a>
    </p>
    <p>
     Requires containers to have an ephemeral storage limit set and constrains the limit to be within the specified maximum values.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       gatekeeper
      </p>
     </li>
     <li>
      <p>
       logging
      </p>
     </li>
     <li>
      <p>
       dapr-system
      </p>
     </li>
     <li>
      <p>
       uipath-installer
      </p>
     </li>
     <li>
      <p>
       kube-system
      </p>
     </li>
     <li>
      <p>
       uipath
      </p>
     </li>
     <li>
      <p>
       argocd
      </p>
     </li>
     <li>
      <p>
       default
      </p>
     </li>
     <li>
      <p>
       istio-system
      </p>
     </li>
     <li>
      <p>
       cert-manager
      </p>
     </li>
     <li>
      <p>
       monitoring
      </p>
     </li>
     <li>
      <p>
       airflow
      </p>
     </li>
     <li>
      <p>
       uipath-check
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/horizontalpodautoscaler">
      Horizontal Pod Autoscaler
     </a>
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/httpsonly">
      HTTPS Only
     </a>
    </p>
    Requires Ingress resources to be HTTPS only. Ingress resources must include the
    <code>
     kubernetes.io/ingress.allow-http
    </code>
    annotation, set to
    <code>
     false
    </code>
    . By default a valid TLS {} configuration is required, this can be made optional by setting the
    <code>
     tlsOptional
    </code>
    parameter to
    <code>
     true
    </code>
    .
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       monitoring
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/imagedigests">
      Image Digests
     </a>
    </p>
    <p>
     Requires container images to contain a digest.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       uipath
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/noupdateserviceaccount">
      Block updating Service Account
     </a>
    </p>
    <p>
     Blocks updating the service account on resources that abstract over Pods. This policy is ignored in audit mode.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/poddisruptionbudget">
      Pod Disruption Budget
     </a>
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      deny
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       airflow
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/requiredprobes">
      Required Probes
     </a>
    </p>
    <p>
     Requires Pods to have readiness and/or liveness probes.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <ul>
     <li>
      <p>
       uipath
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/storageclass">
      Storage Class
     </a>
    </p>
    <p>
     Requires storage classes to be specified when used.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/uniqueingresshost">
      Unique Ingress Host
     </a>
    </p>
    <p>
     Requires all Ingress rule hosts to be unique.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27733e881">
    <p>
     <a href="https://open-policy-agent.github.io/gatekeeper-library/website/validation/uniqueserviceselector">
      Unique Service Selector
     </a>
    </p>
    <p>
     Requires Services to have unique selectors within a namespace. Selectors are considered the same if they have identical keys
                                       and values. Selectors may share a key/value pair as long as there is at least one distinct key/value pair between them.
    </p>
   </td>
   <td headers="d27733e885">
    <p>
     <code>
      dryrun
     </code>
    </p>
   </td>
   <td headers="d27733e889">
    <p>
     N/A
    </p>
   </td>
  </tr>
 </tbody>
</table>

:::note
* The `dapr-system`
namespace is only needed if you install Process Mining and Task Mining.
* The `airflow` namespace is only needed if you install Process Mining.
* `prereq**` are temporary namespaces created while running a prerequisite or health check. The namespaces self-delete upon completion.
:::

## Networking policies

Automation Suite is pre-configured with standard Kubernetes Network Policies to follow the principle of least privilege network access. You can choose to skip installing UiPath-provided network policies by adding `network-policies` under the `exclude components` list in `input.json`. To learn more about optional components, see the [Automation Suite stack](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-stack#automation-suite-stack).

Automation Suite enforces the network from, to, and within the `uipath` namespace. If you bring your own network policies or if you have a custom CNI (e.g., Cilium Enterprise or Calico Tigera Enterprise), make sure to update your policies to mirror the `network-policies` Helm chart.

You can find the Automation Suite `network-policies` Helm chart by running the following command.

:::note
* You must replace `&lt;automation-suite-version&gt;` with your current Automation Suite version in the following command.
* You must unzip the file to extract the Helm chart.
:::

```
helm pull oci://registry.uipath.com/helm/network-policies --version <automation-suite-version>
```

## Cluster privilege requirements

Cluster admin access is required for `uipathctl` on your management node to install and manage Automation Suite on a dedicated cluster. This level of access is needed for system-level components in Automation Suite, such as Istio (routing / service mesh) and ArgoCD (deployment and application lifecycle management), and to create Automation Suite-related namespaces. For shared clusters, admin privileges are not required.

## FIPS 140-2

Federal Information Processing Standards 140-2 (FIPS 140-2) is a security standard that validates the effectiveness of cryptographic modules.

Automation Suite on AKS can run on FIPS 140-2-enabled nodes.

You can enable FIPS 140-2 on the AKS nodes on which you install Automation Suite in the following scenarios:

1. **Scenario 1: new installations**​​ - Enable FIPS 140-2 before performing a clean installation of Automation Suite 2023.4 or later.
2. **Scenario 2: existing installations**​​ - Enable FIPS 140-2 after performing an Automation Suite installation on a machine with FIPS-140-2 disabled.

### Scenario 1: new installations

To enable FIPS 140-2 on the machines where you plan to perform a fresh installation of Automation Suite, take the following steps:

1. Before starting the Automation Suite installation, enable FIPS 140-2 on your machines.
2. Perform the Automation Suite installation by following the installation instructions in this guide.
   * If you install AI Center on a FIPS 140-2-enabled machine and also use Microsoft SQL Server, some additional configuration is required. For details, see [SQL requirements for AI Center](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/sql-database#sql-requirements-for-ai-center).
   * Make sure Insights is disabled as it is not supported on FIPS 140-2.
3. Set the `fips_enabled_nodes` flag to `true` in the `input.json` file.
4. Make sure your certificates are FIPS 140-2-compatible.
   :::note
   By default, Automation Suite generates self-signed FIPS 140-2-compatible certificates whose expiry date depends on the type of Automation Suite installation you choose. You are strongly recommended to replace these self-signed certificates with CA-issues certificates at installation time. To use Automation Suite on FIPS 140-2-enabled machines, the newly provided certificates must be FIPS 140-2-compatible. For a list of eligible ciphers supported by RHEL, see [RHEL documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening#doc-wrapper). For details on how to add your own FIPS 140-2-compliant token-signing and TLS certificates, see [Certificate configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#certificate-configuration).
   :::

### Scenario 2: existing installations

You can install Automation Suite on machines with FIPS 140-2 disabled, and then enable the security standard on the same machines. This is also possible when you upgrade to a new Automation Suite version.

To enable FIPS 140-2 on the machines where you already performed an Automation Suite installation, take the following steps:

1. Perform a regular Automation Suite installation or upgrade operation on machines with FIPS 140-2 disabled.
2. Enable FIPS 140-2 on all your machines.
3. Make sure your certificates are FIPS 140-2-compatible.
   :::note
   To use Automation Suite on FIPS 140-2-enabled machines, you must replace your certificates with new FIPS 140-2-compatible certificates signed by a CA. For a list of eligible ciphers supported by RHEL, see [RHEL documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening#doc-wrapper). For details on how to add your own FIPS 140-2-compliant token-signing and TLS certificates, see [Certificate configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#certificate-configuration). For more on certificates, see .
   :::
4. Make sure your product selection is in line with the FIPS-140-2 requirements:
   * If you install AI Center on a FIPS 140-2-enabled machine and also use Microsoft SQL Server, some additional configuration is required. For details, see [SQL requirements for AI Center](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/sql-database#sql-requirements-for-ai-center).
   * If you previously enabled Insights, you must disable it as it is not supported on FIPS 140-2. For details on how to disable products post-installation, see [Managing products](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-products#managing-products).
5. Reboot your machines and check if you successfully enabled FIPS 140-2.
6. Rerun the `uipathctl` installer.