---
title: "Upgrading Automation Suite"
visible: true
slug: "upgrading-automation-suite"
---

Automation Suite consists of multiple components. Both you as a customer and UiPath® share responsibility of these components. For details, see [Responsibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/automation-suite-stack#responsibility-matrix).

You are responsible for upgrading:

* Kubernetes infrastructure where Automation Suite is deployed (AKS or EKS)
* Components that you choose to bring as part of Automation Suite (e.g., Gatekeeper, FluentD, etc.)

UiPath® is responsible for upgrading:

* UiPath® services (e.g., Orchestrator)
* Components deployed as part of Automation Suite (e.g., ArgoCD)

## Upgrading UiPath® services and components

### Preparation

:::note
* If you upgrade to Automation Suite 2.2510 or higher, you need to bring a PostgreSQL database for `AutomationSuite_Airflow` and configure the connection string for it in `input.json`.
Refer to [Process Mining-specific configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#process-mining-specific-configuration) for details.
* If you upgarde from versions prior to 2.2510.0 using Studio Web, make sure to use the same storage class name as specified
in `storage_class_single_replica`, to support RWX access mode. Refer to [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#configuring-inputjson) for details.
:::
To prepare for the upgrade, take the following steps:

1. Check the compatibility matrix to determine the supported versions for each available upgrade scenario. If you brought your own components, make sure the versions of your components are compatible with the version you plan to upgrade to. For details, see [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).
2. Download `versions.json` and `uipathctl` for the version you want to upgrade to, on your management machine. For download instructions, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/downloading-the-installation-packages#downloading-the-installation-packages).
3. Generate the latest `input.json` file as follows:
   * **Option A:** To get the latest revision of your `input.json` file, run the following command:
     ```
     uipathctl manifest get-revision
     ```
   * **Option B:** To list all the past `input.json` files and determine the one you want to choose, run the following command:
     ```
     uipathctl manifest list-revisions
     ```
4. If you are using an offline setup with an external OCI-compliant registry, you must hydrate the registry with container images and Helm charts before upgrade. For details, refer to [Hydrating the registry with the offline bundle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-oci-compliant-registry#option-b%3A-hydrating-the-registry-with-the-offline-bundle).
5. If Process Mining is installed, and you want to use latest version of Airflow which needs PostgreSQL, you must add or update the `sqlalchemy` connection string template applicable for PostgreSQL in the `cluster_config.json` file before the upgrade: `postgresql_connection_string_template_sqlalchemy_pyodbc`.
   ```
   postgresql+psycopg2://<user>:<password>@<postgresql host>:<postgresql port>/<airflow db name>
   ```
6. If Integration Service is installed, make sure your external cloud queues (SQS) are synced and cross-region replication is enabled. For example:
   * In Azure Queue Storage, configure the GRS/RA-GRS or GZRS/RA-GZRS redundancy options. For more details, see:
     + [Data redundancy in Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)
     + [Reliability in Azure Queue Storage](https://learn.microsoft.com/en-us/azure/reliability/reliability-storage-queue)
     + [Geo-redundant design guidance](https://learn.microsoft.com/en-us/azure/storage/common/geo-redundant-design)
   * In Amazon SQS, create SQS queues in each region and replicate messages using SNS fan-out or custom logic. For more details, see:
     + [Amazon SQS – Active/Active Disaster Recovery](https://disaster-recovery.workshop.aws/en/services/app_integration/sqs/active-active.html)
     + [SNS Cross-region message delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-cross-region-delivery.html)

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
   :::note
   In Automation Suite 2.2510.0, the `uipathctl cluster upgrade` command fails with the following error when maintenance mode is disabled. assignment
   ```
   Please enable maintenance mode prior to attempting an upgrade. Use 'uipathctl cluster maintenance enable'.
   ```
   To avoid the error message, use the following command to perform the upgrade. Make sure you have created all required backups before proceeding. assignment
   ```
   uipathctl cluster upgrade input.json --versions versions.json --skip-upgrade-readiness
   ```
   :::
   :::important
   This operation causes downtime, and your business automation is suspended during the upgrade process. It is important that you perform the upgrade only during your maintenance window.
   :::
7. Check that the cluster is healthy after the upgrade:
   ```
   uipathctl health check
   ```
   :::note
   If you upgraded to Automation Suite 2.2510 or higher, you can uninstall Dapr and Cert Manager, if you previously installed these add-ons for Process Mining or Task Mining. For details, refer to the [Uninstall Dapr](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/uninstalling-dapr#how-to-uninstall-dapr) and [Uninstall Cert Manager](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/uninstalling-cert-manager#how-to-uninstall-cert-manager) sections.
   :::

## Upgrading Kubernetes infrastructure

:::note
Automation Suite supports upstream N-1 to N-3 versions of Kubernetes irrespective of the cloud provider. For instance, if upstream is 1.27, we support versions 1.26, 1.25, and 1.24. For supported versions, see the [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).
:::

You are responsible for upgrading the Kubernetes infrastructure hosting Automation Suite. You should follow the standard practices of your company to upgrade Kubernetes infrastructure.

## Performing post-upgrade operations

The following table describes the possible scenarios where you must perform to perform post-upgrade operations:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Condition
    </p>
   </th>
   <th>
    <p>
     Action
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d10567e321">
    <p>
     1. You upgrade to Automation Suite 2.2510.0 or higher.
    </p>
    <p>
     <strong>
      AND
     </strong>
    </p>
    <p>
     2. Process Mining or Task Mining was enabled on the previous version.
    </p>
   </td>
   <td headers="d10567e324">
    <ul>
     <li>
      Uninstall Dapr. Check out
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/uninstalling-dapr#how-to-uninstall-dapr">
       How to uninstall Dapr
      </a>
      .
     </li>
     <li>
      Uninstall Cert Manager. Check out
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/uninstalling-cert-manager#how-to-uninstall-cert-manager">
       How to uninstall Cert Manager
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d10567e321">
    1. You upgraded to Automation Suite 2.2510.0 or newer.
   </td>
   <td headers="d10567e324">
    You must immediately reactivate your existing licenses for each organization and host.
    <ul>
     <li>
      Online activation: Reactivate directly after upgrade.
     </li>
     <li>
      Offline activation: Generate a new activation payload file from the Automation Suite instance, then upload it in
      <a href="https://activate.uipath.com/">
       Activation
      </a>
      .
     </li>
    </ul>
    Reusing old activation files is not allowed and will result in an invalid license. License reactivation must be performed
                                 using the
    <strong>
     Update License
    </strong>
    button. Do not manually deactivate and then reactivate the license, as this action disables services.
   </td>
  </tr>
 </tbody>
</table>