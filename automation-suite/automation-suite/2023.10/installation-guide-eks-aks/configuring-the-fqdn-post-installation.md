---
title: "Configuring the FQDN post-installation"
visible: true
slug: "configuring-the-fqdn-post-installation"
---

To update the FQDN of Automation Suite, you must update the `input.json` file and run the `uipathctl` installer.

:::note
Changing the FQDN requires new server certificates. If a new certificate is not available, you have two options: either continue with the new self-signed certificate configured by the installer automatically, or stop the installation and bring in a new CA-issued certificate. You can configure the certificate via the `server_certificate` field in the `input.json` file.
:::

## Updating the config file with the new FQDN value

You must update the following parameter in the `input.json` file:

* `fqdn` - update this field with new FQDN that you need to access the cluster.
  :::note
  We support only lowercase FQDNs. Do not use uppercase characters in your FQDN.
  :::

The following example shows the `input.json` configuration required to update the FQDN.

```
{
  "fqdn": "new-automationsuite.mycompany.com" //this is the fqdn for accessing the automation suite cluster
   
}
```

## Running the fabric and services installer to update the FQDN

To update the FQDN for the fabric and services, run the following command:

```
uipathctl manifest apply input.json --versions version.json
```

:::note
If you run the command with the `--force` flag, it will override the warning prompts and perform the FQDN changes directly.
:::
The installer warns you of the consequences of updating the FQDN. It asks for confirmation before proceeding.

```
[WARN]  You are about to change the FQDN of the Automation Suite Cluster.
        Changing the fqdn is a disruptive operation, and it will result in 
        disconnecting your robots, mobile orchestrator users, ML Activities, 
        and ML Skills and invalidating any pending user invites. 
        If you wish to continue type 'yes' and hit enter to continue.
```

The installer also warns you if there is no new valid certificate related to the FQDN. If the certificate validation fails, the installer requires you to provide the new CA-issued certificate or continue with the new self-signed certificate.

```
************************************************************************************
[ERROR] Validating certificate... Failed
[ERROR] Certificate doesn't have new-automationsuite.mycompany.com in the SAN
************************************************************************************

Certificate provided is invalid for the new fqdn, would you like us to configure the new self signed certificate?
If you wish to continue type `yes` and hit enter to continue.
```

:::note
Make sure to clear all the data from your Redis database. You can do this by running the FLUSHALL command.
:::