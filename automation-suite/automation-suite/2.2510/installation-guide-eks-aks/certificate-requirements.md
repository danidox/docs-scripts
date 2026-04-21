---
title: "Certificate requirements"
visible: true
slug: "certificate-requirements"
---

:::important
For details on how to manage certificates post-installation, see [Managing certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#managing-the-certificates).
:::

Automation Suite requires two certificates at the time of installation.

* **TLS certificate** – required for TLS communication between the client and the cluster;
* **Identity token-signing certificate** – required to sign the authentication token.
  :::important
  The installation process generates self-signed certificates on your behalf. We recommend that you replace them with certificates signed by a trusted Certificate Authority (CA). Note that the certificates can be generated at the time of installation only if you grant the Automation Suite installer admin privileges during the installation. If you cannot grant the installer admin privileges, then you must create and manage the certificates yourself. Aside from the previous certificates, you may need to provide additional trusted CA certificates if you want the cluster to trust external software. Example: SQL Server CA Certificate, SMTP Server CA Certificate, external S3 compatible objectstore CA certificate, etc. At the time of installation, you must provide CA certificates for any external software that requires a secure TLS communication. However, if you have not enabled the TLS communication, you can configure it post-installation. For instructions, see [Managing](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#managing-the-certificates) certificates.
  :::

## TLS certificate requirements

The TLS certificate must meet the following requirements:

* File format should be `.pem`, i.e., Base64 encoded DER certificate;
* Private key length should be at least 2048;
* Extended Key Usage: TLS Web Server Authentication; required for accessing Automation Suite on iOS devices;
* Certificate key must be decrypted. If the key is encrypted, run the following command to decrypt it:
  ```
  # replace /path/to/encrypted/cert/key to absolute file path of key
  # replace /path/to/decrypt/cert/key to store decrypt key
  # Once prompted, please entry the passphrase or password to decrypt the key

  openssl rsa -in /path/to/encrypted/cert/key -out /path/to/decrypt/cert/key
  ```
* Should have Subject Alternative Name for all the DNS entries required for installing Automation Suite. If the FQDN for the cluster is `automationsuite.mycompany.com`, the certificate SAN should have the following DNS:
  + `automationsuite.mycompany.com`
  + `*.automationsuite.mycompany.com`
  :::note
  Alternatively, if the `*` wildcard is too generic, make sure you have SAN entries for the following DNS:
    * `automationsuite.mycompany.com`
    * `alm.automationsuite.mycompany.com`
    * `monitoring.automationsuite.mycompany.com`
    * `insights.automationsuite.mycompany.com`
    * `apps.automationsuite.mycompany.com`
    :::

## TLS certificate file

Automation Suite requires three files at the time of installation, as follows:

* **TLS certificate file** — the server’s public certificate file. This file must contain only the leaf server certificate.
* **TLS key file** — private key file for the server certificate.
* **Certificate Authority Bundle** — this is the Public Certificate of CA which is used to sign or issue the TLS certificate. This file must contain both root and all intermediate certificates if present.

To verify the CA and TLS certificate, run the following command on the Linux machine:

```
# Please replace /path/to/ca-certificate-bundle and /path/to/server-certificate with actual file path.

openssl verify -CAfile /path/to/ca-certificate-bundle /path/to/server-certificate
```

If you choose to bring your own Cert Manager, and your TLS certificate is issued by a private or non-public CA, you must manually include both the leaf certificate and intermediate CA certificates in the TLS certificate file. In case of public CAs, they are automatically trusted by client systems, and no further action is required on your part.

## Identity token-signing certificate

Automation Suite has the following requirements in terms of token-signing certificates at the time of installation:

* File format should be `pkcs12` to sign the authentication token;
* Password for signing the certificate is required.

If an identity token signing certificate is not provided, Automation Suite uses the server certificates to generate the one at the time of installation.