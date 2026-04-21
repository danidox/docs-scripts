---
title: "Managing the cluster in ArgoCD"
visible: true
slug: "managing-the-cluster-in-argocd"
---

## Overview

ArgoCD is a declarative, GitOps continuous delivery tool for Kubernetes. It is designed as a Kubernetes controller that continuously monitors UiPath® running applications and checks the current state against the desired target state as specified in the docker registry. For more details, see [ArgoCD documentation](https://argo-cd.readthedocs.io/en/stable/#what-is-argo-cd).

Administrators can have an overview of the cluster, configurations, applications status, and health, all via a simple UI or CLI. ArgoCD comes with its own open-source bundled Redis, which supports both HA and non-HA configurations.

Automation Suite uses ArgoCD in the following scenarios:

* Installing and upgrading the Fabric components and core UiPath® services.
* Automating the deployment of the desired application states in the specified target environments. ArgoCD follows the GitOps pattern of using Git/helm repositories as the source of truth for defining the desired application state.
* Keeping track of the installation state. If the installation failed at a specific point and you resume it after a while, ArgoCD skips all the steps that are already synced and resumes from the point where it failed.
* Self-healing the applications. If you mistakenly delete any of the objects, the manifests will automatically get synced.

## ArgoCD read-only scenarios

You can use the ArgoCD account in the following **read only scenarios**:

* Visualizing all your apps, pods, and services in a simple interface
* Monitoring the health of all your apps, pods, and services
* Quickly identifying issues in your deployment
* Resyncing your application in your cluster

## ArgoCD advanced scenarios

:::important
You must not modify any other settings or parameters except for the ones listed in this section.
:::

You can use the ArgoCD admin account in the following **advanced scenarios**:

* Changing parameters for debugging purposes only; for instance, disabling self-healing;
* Deleting pods;
* Troubleshooting;
* Managing Orchestrator custom configuration; for instance, setting up encryption key per tenant;
* Updating the database connection strings;
* Syncing applications.
  :::note
  Make sure to refer to the proper UiPath® documentation before deleting or changing the advanced configuration on the UI.
  :::

## Accessing ArgoCD

ArgoCD supports two authentication methods:

* **username and password** – default authentication method;
* **SSO** – recommended authentication method. You can enable SSO authentication post-installation. For instructions, see [Enabling SSO for ArgoCD](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-cluster-in-argocd#enabling-sso-for-argocd).

### Username and password authentication

#### Accessing the ArgoCD admin account

To access the ArgoCD admin account using username and password, take the following steps:

1. Access the following URL: `https://alm.${CONFIG_CLUSTER_FQDN}`.
2. Enter the following username: **admin**.
3. Access the password:
   ```
   kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath='{.data.password}'  | base64 -d
   ```
4. Enter your password.
   :::important
   You must use the ArgoCD admin account only for advanced scenarios. It can cause disruptive action on the cluster if not used with caution.
   :::

### SSO authentication

To access ArgoCD using SSO, take the following steps:

1. Select the SSO button on the ArgoCD login page.
2. Enter your company domain credentials.

## Enabling SSO for ArgoCD

### Overview

To enable SSO authentication, you must use the `uipathctl` command-line tool.

### Preparing the configuration files

You must generate the RBAC file before enabling SSO for ArgoCD.

#### The RBAC file

The RBAC file contains access rules.

For details on the built-in role definitions, see the [ArgoCD documentation](https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/).

For details on the ArgoCD account types and their permissions, see [Managing the cluster in ArgoCD](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-cluster-in-argocd#managing-the-cluster-in-argocd).

We recommend using these roles when defining your groups, but you can create your own set of permissions.

#### Configuring the RBAC file

1. Create a file named `policy.csv` by running the following command:
   ```
   uipathctl config argocd generate-rbac
   ```
2. Add the following content to the `policy.csv` file and save it:
   ```
   p, role:uipath-sync, applications, get, */*, allow
   p, role:uipath-sync, applications, sync, */*, allow
   g, argocdro, role:uipath-sync
   ```
3. Associate your RBAC groups with the built-in **admin** role and the UiPath® **argocdro** read-only role, by appending the following lines to the `policy.csv` RBAC file:
   ```
   g, <your_ldap_readonly_group_name>, role:uipath-sync
   g, <your_ldap_admin_group_name>, role:admin
   ```
4. Save the updated `policy.csv` RBAC file.
5. Create a new section named `policy.default` in the `argo-cd-rbac-cm` configuration map, after the `policy.csv` section, as shown in the following example:
   ```
   policy.csv: |
       p, role:org-admin, applications, *, /, allow
       p, role:org-admin, clusters, get, *, allow
       p, role:org-admin, repositories, get, *, allow
       p, role:org-admin, repositories, create, *, allow
       p, role:org-admin, repositories, update, *, allow
       p, role:org-admin, repositories, delete, *, allow
       g, "694afc07-6767-8998-bf84-ab80b53379df", role:org-admin # (azure group assigned to role)
     policy.default: role:readonly
   ```
6. Follow the instructions in the ArgoCD documentation for [configuring SSO with OIDC](https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/microsoft/#entra-id-app-registration-auth-using-oidc).

**Example:**

If your LDAP group for ArgoCD administrators is **Administrators** and the LDAP group for ArgoCD read-only users is **Readers**, the RBAC file should be similar to the one in the following example:

```
p, role:uipath-sync, applications, get, */*, allow
p, role:uipath-sync, applications, sync, */*, allow
g, argocdro, role:uipath-sync
g, Readers, role:uipath-sync
g, Administrators, role:admin
```

For more advanced use cases, the following example shows the default RBAC file:

```
# Built-in policy which defines two roles: role:readonly and role:admin,
# and additionally assigns the admin user to the role:admin role.
# There are two policy formats:
# 1. Applications, logs, and exec (which belong to a project):
# p, <user/group>, <resource>, <action>, <project>/<object>
# 2. All other resources:
# p, <user/group>, <resource>, <action>, <object>

p, role:readonly, applications, get, */*, allow
p, role:readonly, certificates, get, *, allow
p, role:readonly, clusters, get, *, allow
p, role:readonly, repositories, get, *, allow
p, role:readonly, projects, get, *, allow
p, role:readonly, accounts, get, *, allow
p, role:readonly, gpgkeys, get, *, allow
p, role:readonly, logs, get, */*, allow

p, role:admin, applications, create, */*, allow
p, role:admin, applications, update, */*, allow
p, role:admin, applications, delete, */*, allow
p, role:admin, applications, sync, */*, allow
p, role:admin, applications, override, */*, allow
p, role:admin, applications, action/*, */*, allow
p, role:admin, applicationsets, get, */*, allow
p, role:admin, applicationsets, create, */*, allow
p, role:admin, applicationsets, update, */*, allow
p, role:admin, applicationsets, delete, */*, allow
p, role:admin, certificates, create, *, allow
p, role:admin, certificates, update, *, allow
p, role:admin, certificates, delete, *, allow
p, role:admin, clusters, create, *, allow
p, role:admin, clusters, update, *, allow
p, role:admin, clusters, delete, *, allow
p, role:admin, repositories, create, *, allow
p, role:admin, repositories, update, *, allow
p, role:admin, repositories, delete, *, allow
p, role:admin, projects, create, *, allow
p, role:admin, projects, update, *, allow
p, role:admin, projects, delete, *, allow
p, role:admin, accounts, update, *, allow
p, role:admin, gpgkeys, create, *, allow
p, role:admin, gpgkeys, delete, *, allow
p, role:admin, exec, create, */*, allow

g, role:admin, role:readonly
g, admin, role:admin
```

### Enabling SSO for ArgoCD

After preparing the RBAC file, you can enable SSO for ArgoCD:

1. Add the following lines to the `input.json` file:
   ```
   {
   "fabric": {
   "argocd_rbac_config_file": "/path/to/policy.csv"
     }
   }
   ```
2. Apply the configuration by running the following command:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```