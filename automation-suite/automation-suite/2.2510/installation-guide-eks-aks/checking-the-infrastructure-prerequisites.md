---
title: "Checking the infrastructure prerequisites"
visible: true
slug: "checking-the-infrastructure-prerequisites"
---

Prerequisite checks help you ensure that the required cloud infrastructure is provisioned appropriately and is accessible by the client machine before starting the Automation Suite installation.

For a list of prerequisite checks that the Automation Suite installer performs, see [Prerequisite checks](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/prerequisite-checks#prerequisite-checks).

## Generating configurations automatically

The Automation Suite installer can automatically generate the following configurations on your behalf:

* The SQL databases required for the installation on the SQL server based if the `sql.create_db` key is set in your `input.json` file.
* The object storage buckets required in your cloud provider if the `external_object_storage.create_bucket` key is set in the configuration file.

To allow the installer to generate these configurations, run the following command:

```
uipathctl prereq create input.json --versions versions.json
```

For details on the flags that you can use with the `uipathctl prereq create` command, see [uipathctl prereq create](https://docs.uipath.com/automation-suite/automation-suite/2.2510/reference-guide/uipathctl-prereq-create).
:::note
If you choose to enable a secretstore with Azure Key Vault, the External Secrets Operator and its corresponding CRDs will be deployed in the cluster as part of the `prereq create` command.
:::
:::important
The `uipathctl prereq create` command does not create the required SQL databases for Process Mining. You must manually create them by following the instructions in [Bring your own database](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#bring-your-own-databases).
:::

## Checking the prerequisites

To check the prerequisites based on the inputs you configured in the `input.json`, run the following command:

```
uipathctl prereq run input.json --versions versions.json
```

For details on the flags that you can use with the `uipathctl prereq run` command, see [uipathctl prereq run](https://docs.uipath.com/automation-suite/automation-suite/2.2510/reference-guide/uipathctl-prereq-run).

By default, the `uipathctl prereq` command checks all the prerequisites. Alternatively, the command also allows you to run strictly the checks that are relevant to you, as follows:

* If you want to exclude components from the execution, use the `--excluded` flag. For example, if you do not want to check the database connection strings, run `uipathctl prereq --excluded SQL`. The command runs all the prerequisite checks except for the SQL-related one.
* If you want to include only certain components in the execution, use the `--included` flag. For example, if you only want to check the DNS and objectstore, run `uipathctl prereq --included DNS,OBJECTSTORAGE`.
  :::note
  You can find the names of the components you can include or exclude from the prerequisite checks in the [prerequisite check output](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/output-example-prerequisite-check#output-example%3A-prerequisite-check). In the example, the first word on each outdented line represents the component name. For example: SQL, OBJECTSTORE, DNS, etc.
  :::
:::important
You may receive a throttling message from AKS, such as *Waited for 1.0447523s due to client-side throttling, not priority and fairness.* In this case, allow a few minutes for the command to fully complete or try to re-run it.
:::