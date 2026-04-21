---
title: "Migrating between Automation Suite clusters"
visible: true
slug: "migrating-between-automation-suite-clusters"
---

## About the cluster migration

You can migrate from one Automation Suite cluster to another if you use the `uipath` namespace instead of a custom namespace and want to move from one Automation Suite flavor to another. We support the following scenarios:

* Migrate from Automation Suite on Linux to a new installation of Automation Suite on EKS/AKS;
* Migrate from Automation Suite on EKS/AKS to a new installation of Automation Suite on OpenShift;
* Migrate from Automation Suite on OpenShift to a new installation of Automation Suite on EKS/AKS;
* Migrate from Automation Suite on EKS to Automation Suite on AKS or from Automation Suite on AKS to Automation Suite on EKS.

Note that you can attempt to perform the migration operation multiple times with no impact on your existing cluster.

The following migration scenarios are not supported:

* Migrating from Automation Suite on Linux to an existing installation of Automation on EKS/AKS or Automation Suite on OpenShift;
* Migrating an Automation Suite on OpenShift cluster to Automation Suite on Linux cluster.

## Process overview

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Step
    </p>
   </th>
   <th>
    <p>
     Description
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d2739e66">
    <p>
     1.
    </p>
   </td>
   <td headers="d2739e69">
    <p>
     <strong>
      Mandatory
     </strong>
     . Make sure you meet the migration requirements.
    </p>
    <ul>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#requirements">
        Requirements
       </a>
      </p>
     </li>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#data-migration-and-responsibilities">
        Data migration and responsibilities
       </a>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d2739e66">
    <p>
     2.
    </p>
   </td>
   <td headers="d2739e69">
    <p>
     <strong>
      Mandatory.
     </strong>
     Prepare the target cluster and the docker images for both source and target cluster.
    </p>
    <ul>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#preparing-the-target-cluster">
        Preparing the target cluster
       </a>
      </p>
     </li>
    </ul>
    <p>
     <strong>
      Optional.
     </strong>
     If your deployment is offline or if you use a private OCI registry, make sure the required images are available.
    </p>
    <ul>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#hydrating-the-oci-compliant-registry-registry-without-internet-access">
        Hydrating the OCI-compliant registry in an offline setup
       </a>
      </p>
     </li>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#hydrating-the-oci-compliant-registry-with-internet-access">
        Hydrating the OCI-compliant registry in an online setup
       </a>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d2739e66">
    <p>
     3.
    </p>
   </td>
   <td headers="d2739e69">
    <p>
     <strong>
      Mandatory.
     </strong>
     Start the migration, move the data, and run the Automation Suite installation.
    </p>
    <ul>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#running-the-cluster-migration">
        Running the cluster migration
       </a>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d2739e66">
    <p>
     4.
    </p>
   </td>
   <td headers="d2739e69">
    <p>
     <strong>
      Optional
     </strong>
     . If AI Center is enabled on both the source and target clusters, migrate the skills.
    </p>
    <ul>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#migrating-the-ai-center-skills">
        Migrating the AI Center skills
       </a>
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

For detailed migration instructions, see the [Automation Suite on EKS/AKS Installation Guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters).

## Requirements

To migrate from an Automation Suite cluster to another, you must meet the following requirements:

* Download the following artifacts:
  + `uipathctl`
  + `versions.json`
* You must establish connectivity between the two environments.
* You must have an external objectstore configured in your source cluster. If you use in-cluster storage, see [Migrating in-cluster objectstore to external objectstore](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migrating-in-cluster-objectstore-to-external-objectstore).
* If you migrate from Automation Suite on Linux, the version of your source cluster must be 2022.10 or newer.
* If you migrate to Automation Suite on OpenShift, the version of your source cluster must be 2023.10 or newer.
* Offline-only requirements: You must hydrate the target cluster.

## Data migration and responsibilities

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th rowspan="2">
    <p>
     Data
    </p>
   </th>
   <th colspan="2">
    <p>
     Migration mechanism
    </p>
   </th>
  </tr>
  <tr>
   <th>
    Status
   </th>
   <th>
    Responsibility
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d2739e237">
    <p>
     SQL
    </p>
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Retained
     </strong>
    </p>
    <p>
     You have two options:
    </p>
    <ol>
     <li>
      <p>
       Reuse the same databases for the new installation. Point the cluster configuration's SQL connection strings to the existing
                                       database server.
      </p>
     </li>
     <li>
      <p>
       Clone your databases and use the clones instead.
      </p>
     </li>
    </ol>
   </td>
   <td headers="d2739e240 d2739e246">
    <p>
     <strong>
      Customer
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    Docker registry
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Not migrated
     </strong>
    </p>
    If you use a private registry, you must hydrate the target registry. If you use
    <code>
     registry.uipath.com
    </code>
    for the target cluster, no further steps are needed.)
   </td>
   <td headers="d2739e240 d2739e246">
    <p>
     <strong>
      Customer
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    FQDN
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Required
     </strong>
    </p>
    <p>
     You must choose a new FQDN for the new cluster. Optionally, you can revert to the previous FQDN if needed.
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <strong>
     Customer
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    Certificates
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Not migrated
     </strong>
    </p>
    <p>
     You must bring certificates as part of the new cluster installation.
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <strong>
     Customer
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    Cluster configuration
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Not migrated
     </strong>
    </p>
    You must generate the new
    <code>
     input.json
    </code>
    applicable to the target cluster type (AKS or EKS).
   </td>
   <td headers="d2739e240 d2739e246">
    <strong>
     Customer
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    Custom alerts and dashboards created by users
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Not migrated
     </strong>
    </p>
    <p>
     Post-migration, you must reconfigure any custom alerts in Alert Manager and Grafana dashboards.
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <strong>
     Customer
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    Application logs / Prometheus streaming configuration created by users
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Not migrated
     </strong>
    </p>
    <p>
     You must reconfigure application log and Prometheus streaming.
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <strong>
     Customer
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    Dynamic workloads
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Depends on application
     </strong>
    </p>
    <p>
     AI Center training jobs are lost; Skills are retained.
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <p>
     Skills (script needed to be executed after upgrade):
     <strong>
      UiPath&reg;
     </strong>
    </p>
    <p>
     Training jobs:
     <strong>
      Customer
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    <p>
     Objectstore
    </p>
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     External objectstore:
     <strong>
      Retained
     </strong>
    </p>
    <p>
     For external objectstore, you have two options:
    </p>
    <ol>
     <li>
      <p>
       Reuse the existing external object store and connect it to the new environment.
      </p>
     </li>
     <li>
      <p>
       Create a replica of your current object store and use this for the new setup.
      </p>
     </li>
    </ol>
    <p>
     <strong>
      Important
     </strong>
     : If you're using an in-cluster object store, you must perform a ceph-to-external migration before the upgrade.
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <p>
     Migrating from in-cluster to external objectstore:
     <strong>
      Customer
     </strong>
    </p>
    <p>
     External objectstore:
     <strong>
      UiPath&reg;
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    <p>
     Insights
    </p>
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Retained
     </strong>
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <p>
     <strong>
      UiPath&reg;
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    <p>
     MongoDB data
    </p>
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Retained
     </strong>
    </p>
    <p>
     MongoDB data is moved to the target SQL.
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <p>
     <strong>
      UiPath&reg;
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    <p>
     RabbitMQ
    </p>
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Not needed
     </strong>
    </p>
   </td>
   <td headers="d2739e240 d2739e246">
    <p>
     <strong>
      UiPath&reg;
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d2739e237">
    Monitoring (data)
   </td>
   <td headers="d2739e240 d2739e244">
    <p>
     <strong>
      Not needed
     </strong>
    </p>
    <p>
     Monitoring data does not apply to the new cluster.
    </p>
    Important: If you do not use the built-in monitoring components, you must set up external monitoring components after the migration
                                 upgrade.
   </td>
   <td headers="d2739e240 d2739e246">
    N/A
   </td>
  </tr>
 </tbody>
</table>

## Preparing the cluster migration

### Preparing the target cluster

:::important
Do not run `uipathctl manifest apply` until you have completed Step 1 in the [Running the cluster migration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#running-the-cluster-migration) section. Running this command too early can result in configuration inconsistencies in the target cluster.
:::
:::note
Do not modify the source cluster after starting the migration process.
:::
To prepare the target cluster, take the following steps:

1. Download the targeted version of `input.json` on the source cluster and generate the `input.json` file by running the following command:
   ```
   uipathctl manifest get-revision
   ```

For details, refer to the following diagram:

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/397183)
2. Based on the previously generated `input.json` file, modify the `input.json` file of the target cluster.

You must transfer the Orchestrator-specific configuration that includes the and settings.

Additionally, you must update the following components so that they reference the correct infrastructure in the target cluster:

   * External objectstore
   * SQL Server or PostgreSQL connection details
   * Redis cluster configuration
   :::note
   Dedicated Microsoft SQL Server and PostgreSQL for Process Mining Airflow database is the required for Process Mining on Automation Suite 2.2510 or higher. If you migrate from a version prior to 2024.10.3, the generated `input.json` file for the target cluster does not contain the connection string for the Airflow PostgreSQL database. To use the latest version of Airflow, which requires PostgreSQL, you will need to manually add the `sqlalchemy` connection string template for PostgreSQL to the `input.json` file for the target cluster before migration. `Postgresql_connection_string_template_sqlalchemy_pyodbc` assignment
   ```
   postgresql+psycopg2://&lt;user&gt;:&lt;password&gt;@&lt;postgresql host&gt;:&lt;postgresql port&gt;/DB_NAME_PLACEHOLDER
   ```
   :::
3. Validate the prerequisites in the target cluster by running the following command:
   ```
   uipathctl prereq run input-target.json --kubeconfig kubeconfig.target --versions versions.json
   ```
   :::note
   `input-target.json` is the `input.json` file corresponding to the target cluster.
   :::
To generate the `kubeconfig` file, refer to [Generating the kubeconfig file](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/granting-installation-permissions#step-4%3A-generating-the-kubeconfig-file).
4. If you are migrating from Automation Suite on Linux to a EKS/AKS deployment, you must put the source cluster in maintenance mode. For details, refer to [Putting the cluster in maintenance mode](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide/executing-the-upgrade#putting-the-cluster-in-maintenance-mode).
5. Clone the SQL databases from the source deployment to the target deployment.

### Hydrating the OCI-compliant registry registry without internet access

The migration process requires the latest `uipathcore` Docker image tag to be available for both the source and target clusters. If your source cluster is offline, make the image available by taking the following steps:

1. Follow the steps to hydrate the registry used by the target cluster with the offline bundle in [Option B: Hydrating the registry with the offline bundle](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-oci-compliant-registry#option-b%3A-hydrating-the-registry-with-the-offline-bundle).
2. Copy the `uipathctl` binary and `versions.json` file on a VM with access to the source cluster.
3. Run the following command:
   ```
   jq -r '.[][] | select(.name=="uipath/uipathcore") | .ref + ":" + .version' "/path/to/versions.json" > images.txt
   ```
4. Seed the `uipathcore` image from the registry of the target cluster to the registry of source cluster:
   ```
   ./uipathctl registry seed --tag-file ./images.txt \
               --source-registry "target.registry.fqdn.com" \
               --source-password "target-registry-username" \
               --source-username "target-registry-password" \
               --dest-registry "source.registry.fqdn.com" \
               --dest-username "source-registry-username" \
               --dest-password "source-registry-password"
   ```
   :::note
   Make sure to update the command as follows:
   * Replace `target.registry.fqdn.com`,
   `target.registry.fqdn.com`, and `target-registry-password` with the proper values that correspond to the registry associated with the target cluster;
   * Replace `source.registry.fqdn.com`,
   `source.registry.fqdn.com`, and `source-registry-password` with the proper values that correspond to the registry associated with the source cluster.
   :::

### Hydrating the OCI-compliant registry with internet access

If you use a private registry, you must seed it. For instructions, see [Configuring the OCI-compliant registry](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-oci-compliant-registry#configuring-the-oci-compliant-registry).

## Running the cluster migration

To migrate to the target Automation Suite cluster, take the following steps:

1. Execute the migration by running the following command:
   ```
   uipathctl cluster migration run input-target.json --kubeconfig kubeconfig.source --target-kubeconfig kubeconfig.target --versions versions-target.json
   ```
2. Complete the Automation Suite installation on the target cluster by running the following command:
   ```
   uipathctl manifest apply input-target.json --kubeconfig kubeconfig.target --versions versions-target.json
   ```

## Migrating the AI Center skills

The steps in this section are applicable only if you enabled AI Center on both the source and target clusters. Note that the instructions assume that AI Center on the target cluster points to the database containing the skill data for running the skills.

After completing the migration, you must sync the AI Center skills so that you can use them again.

### Checking the skill migration status

You can use the following script to sync the AI Center ML Skill to the target cluster. The script triggers the sync in the background if no active sync is in progress.

The script syncs the skills in the background (async) and returns. The job ensures that the skills are deployed and updates the DB entry to reflect the current status.

```
uipathctl service aicenter sync-skills [skill_ids]
```

| Parameter | Description |
| --- | --- |
| `[skill_ids]` | The optional array of the skill IDs separated by space. If you provide the skill ID, then only those skills are updated; otherwise, all deployed skills are re-synced. |

```
uipathctl service aicenter sync-skills 783273-3232-3232-323 32-32-323-3232

//this will only sync the skills with ID 783273-3232-3232-323 and 32-32-323-3232
```

To view the status of the AI Center ML Skill, run the following command:

```
uipathctl service aicenter sync-skill-status [skill_ids]
```

The command can return any of the following statuses:

* `InProgess` - skill deployment is in progress.
* `Failed` - skill deployment is failed.
* `OutOfSync` - skill is available in the database; however, it has yet to be deployed.
* `Available` - when the skills are deployed and available to consume.