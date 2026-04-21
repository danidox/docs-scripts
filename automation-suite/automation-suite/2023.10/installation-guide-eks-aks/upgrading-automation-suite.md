---
title: "Upgrading Automation Suite on EKS/AKS"
visible: true
slug: "upgrading-automation-suite"
---

Automation Suite on AKS/EKS consists of multiple components. Both you as a customer and UiPath® share responsibility of these components. For details, see [Responsibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-stack#responsibility-matrix).

You are responsible for upgrading:

* Kubernetes infrastructure where Automation Suite is deployed (AKS or EKS)
* Components that you choose to bring as part of Automation Suite (e.g., Gatekeeper, FluentD, etc.)

UiPath® is responsible for upgrading:

* UiPath® services (e.g., Orchestrator)
* Components deployed as part of Automation Suite (e.g., ArgoCD)

## Upgrading UiPath® services and components

### Preparation

:::note
There is a known issue with the backup logic in Automation Suite for AKS/EKS versions 2023.10.0 to 2023.10.7. Specifically, this issue excludes the backup of Insights dashboards. However, all historical data is successfully backed up. To include the Insights dashboards in backup, you must reconfigure the backup solution using the script available [here](https://raw.githubusercontent.com/UiPath/automation-suite-support-tools/refs/heads/main/Scripts/GeneralTools/veleroBackupASEA/dr.sh). This script allows you to reconfigure the backup solution and create the backup. For details on how to execute the command, see this [section](https://github.com/UiPath/automation-suite-support-tools/tree/main/Scripts/GeneralTools/veleroBackupASEA).
:::

To prepare for the upgrade, take the following steps:

1. Check the compatibility matrix to determine the supported versions for each available upgrade scenario. If you brought your own components, make sure the versions of your components are compatabile with the version you plan to upgrade to. For details, see [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).
2. Download `versions.json` and `uipathctl` for the version you want to upgrade to, on your management machine. For download instructions, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/downloading-the-installation-packages#downloading-the-installation-packages).
3. Generate the latest `input.json` file as follows:
   * **Option A:** To get the latest revision of your `input.json` file, run the following command:
     ```
     uipathctl manifest get-revision
     ```
   * **Option B:** To list all the past `input.json` files and determine the one you want to choose, run the following command:
     ```
     uipathctl manifest list-revisions
     ```
4. If you are using an offline setup with an external OCI-compliant registry, you must hydrate the registry with container images and Helm charts before upgrade. For details, refer to [Hydrating the registry with the offline bundle](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-oci-compliant-registry#option-b%3A-hydrating-the-registry-with-the-offline-bundle).
5. If Process Mining is installed, and you want to use latest version of Airflow which needs PostgreSQL, you must add or update the `sqlalchemy` connection string template applicable for PostgreSQL in the `cluster_config.json` file before the upgrade: `postgresql_connection_string_template_sqlalchemy_pyodbc`.
   ```
   postgresql+psycopg2://<user>:<password>@<postgresql host>:<postgresql port>/<airflow db name>
   ```
   :::note
   This only applies to Process Mining on Automation Suite 2023.10.9 or higher.
   :::

### Execution

To perform an upgrade of UiPath® services and component, take the following steps:

1. Confirm that your cluster is healthy:
   ```
   uipathctl health check
   ```
2. Put the cluster in maintenance mode to guarantee a consistent backup:
   ```
   uipathctl cluster maintenance enable
   ```
   :::important
   This operation causes downtime, and your business automation is suspended while maintenance mode is enabled.
   :::
3. Verify that the cluster is in maintenance mode:
   ```
   uipathctl cluster maintenance is-enabled
   ```
4. Back up the cluster and the SQL database, then check that the backup completed successfully.
   :::important
   It is strongly recommended to create a backup of the cluster and the SQL database before upgrading Automation Suite. This is to ensure you can restore the cluster if something goes wrong during the upgrade operation. This is applicable before upgrading your Kubernetes infrastructure as well. Make sure to copy the value of `global.userInputs.identity.krb5KeytabSecret` to `global.kerberosAuthConfig.userKeytab`, if you simultaneously meet the following requirements:
   * you configured the Active Directory integration using username and password
   * you have Windows authentication enabled
   * you do not use SQL integrated authentication
   :::
5. Disable the maintenance mode:
   ```
   uipathctl cluster maintenance disable
   ```
   :::note
   You must disable maintenance mode before upgrade. The Automation Suite upgrade process does not support having maintenance mode enabled.
   :::
6. Perform the upgrade of UiPath® services and components:
   ```
   uipathctl cluster upgrade input.json --versions versions.json
   ```
   :::important
   This operation causes downtime, and your business automation is suspended during the upgrade process. It is important that you perform the upgrade only during your maintenance window.
   :::
7. Check that the cluster is healthy after the upgrade:
   ```
   uipathctl health check
   ```
   :::note
   If you upgraded to Automation Suite 2024.10.3 or higher, you can uninstall Dapr and Cert Manager if you have not enabled Task Mining. For more details, refer to the and sections.
   :::

## Upgrading Kubernetes infrastructure

:::note
Automation Suite supports upstream N-1 to N-3 versions of Kubernetes irrespective of the cloud provider. For instance, if upstream is 1.27, we support versions 1.26, 1.25, and 1.24. For supported versions, see the [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).
:::

You are responsible for upgrading the Kubernetes infrastructure hosting Automation Suite. You should follow the standard practices of your company to upgrade Kubernetes infrastructure.