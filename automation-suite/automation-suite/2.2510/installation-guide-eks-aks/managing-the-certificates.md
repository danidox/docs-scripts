---
title: "Managing the certificates"
visible: true
slug: "managing-the-certificates"
---

:::important
The installation process generates self-signed certificates on your behalf. These certificates will expire in 90 days. You must replace them with certificates signed by a trusted Certificate Authority (CA) as soon as installation completes. If you do not update the certificates, the installation will stop working in 90 days. You can use the `uipathctl` CLI tool to update certificates post-installation. For details, see [uipathctl documentation](https://docs.uipath.com/automation-suite/automation-suite/2.2510/reference-guide/about-uipathctl).
:::

## Generating a Certificate Signing Request (CSR) and a private key

To generate the CSR and the private key, run the following command:

```
# copy the machine openssl configuration locally
cp /etc/pki/tls/openssl.cnf ./openssl.tmp.cnf

# Replace the [AUTOMATION_SUITE_FQDN] value. For example, "automationsuite.corp.com"
AS_FQDN=[AUTOMATION_SUITE_FQDN]
cat >> ./openssl.tmp.cnf <<EOF
[SAN]
subjectAltName=DNS:$AS_FQDN,DNS:alm.$AS_FQDN,DNS:monitoring.$AS_FQDN,DNS:registry.$AS_FQDN,DNS:objectstore.$AS_FQDN,DNS:insights.$AS_FQDN,DNS:apps.$AS_FQDN
EOF

# create the certificate request
openssl req -new -sha256 -newkey rsa:2048 -nodes -keyout server.key -subj "/C=xx/ST=xx/O=xx/OU=xx/CN=$AS_FQDN" -reqexts SAN -config openssl.tmp.cnf -out ${AS_FQDN}.csr
```

Your IT team uses the obtained values to generate a signed certificate. The generated private key remains local.

## Managing the TLS certificate

To view more information about updating the TLS certificates, run the following command:

```
uipathctl config update-tls-certificates --help
```

Output:

```
************************************************************************************
Manage tls certificates

Usage:
  uipathctl config tls-certificates [flags]
  uipathctl config tls-certificates [command]

Available Commands:
  get         Get the current tls certificates
  update      Update tls certificates

Flags:
  -h, --help   help for tls-certificates

Global Flags:
      --context string      name of the kubeconfig context to use
      --kubeconfig string   kubectl configuration file (default: ~/.kube/config)
      --log-format string   log format. one of [text,json] (default "text")
      --log-level string    set log level. one of [trace,debug,info,error] (default "error")
  -q, --quiet               suppress all output except for errors and warnings
      --timeout duration    timeout of the command (default 1h0m0s)

************************************************************************************
```

### Finding the TLS certificates

Certificates are stored as a secret at Istio level. You can find certificates under the `istio-ingressgateway-certs` name in the `<istio-system>` namespace.

See the certificate files in the following list:

* Server TLS certificate is stored as `tls.crt`
* Server TLS private key as `tls.key`
* CA bundle is stored as `ca.crt`

You can verify the secrets using the following command:

```
kubectl -n <istio-system> get secrets istio-ingressgateway-certs -o yaml
```

Certificates are also stored in the `<uipath>` namespace. This is applicable to every UiPath® product that needs certificate information to trust incoming calls. For details, see [Understanding the container architecture related to certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/certificates-overview#understanding-the-container-architecture-related-to-certificates).

### Updating the TLS certificates

:::important
Before updating the server certificate, you must decrypt the private key that was generated in the [Generating a Certificate Signing Request (CSR) and a private key](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#generating-a-certificate-signing-request-(csr)-and-a-private-key) section. Skipping this decryption step will result in an error.
:::

To decrypt the certificate key, run the following command:

```
# replace /path/to/encrypted/cert/key to absolute file path of key
# replace /path/to/decrypt/cert/key to store decrypt key
# Once prompted, please entry the passphrase or password to decrypt the key

openssl rsa -in /path/to/encrypted/cert/key -out /path/to/decrypt/cert/key
```

To update the certificate, run the following `uipathctl` command. You need the path to each of the three certificate files. All the certificate file should be in `pem` format.

* Certificate Authority Bundle - This bundle should contain only the chain certificates used to sign the TLS server certificate. The certificate provided in the `--cacert` option should not include the leaf certificates. The chain limit is up to nine certificates.
* Server Certificate - Public server certificate
  :::note
  The `server.crt` file must contain the entire chain, as shown in the following example: assignment
  ```
  -----server cert-----
  -----root ca chain-----
  ```
  :::
* Private key - Private key for server certificate
```
uipathctl config tls-certificates update --cert server.crt --cacert ca.crt --key server.key
```

If you choose to manage the certificates yourself, you must use the `--use-istio-cert` flag with the certificates update command. This flag allows for the exisiting secrets to be copied to the `uipath` namespace. Be aware that, when using the `--use-istio-cert` flag, you must not use any other certificate flags, otherwise the command fails. If you use other namespace instead of `uipath`, you must specify it by passing it to the`--namespace <uipath>` flag, where `<uipath>` represents the namespace where Automation Suite is deployed.

### Accessing the TLS certificate

To print out the certificate files, run the following command:

```
uipathctl config tls-certificates get
```

## Managing additional CA certificates

To view more information about additional CA certificates, run the following command:

```
 uipathctl config additional-ca-certificates --help
```

Output:

```
***************************************************************************************

Manage additional ca certificates

Usage:
  uipathctl config additional-ca-certificates [flags]
  uipathctl config additional-ca-certificates [command]

Available Commands:
  get         Get the current additional ca certificates
  update      Update additional ca certificates

Flags:
  -h, --help   help for additional-ca-certificates

Global Flags:
      --context string      name of the kubeconfig context to use
  -f, --force               override all user prompts to true
      --kubeconfig string   kubectl configuration file (default: ~/.kube/config)
      --log-format string   log format. one of [text,json] (default "text")
      --log-level string    set log level. one of [trace,debug,info,error] (default "info")
  -q, --quiet               suppress all output except for errors and warnings
      --timeout duration    timeout of the command (default: 90 minutes) (default 1h30m0s)
      --versions string     optional path to versions file

Use "uipathctl config additional-ca-certificates [command] --help" for more information about a command.

***************************************************************************************
```

The following sections describe the operations you can perform using the `uipathctl config additional-ca-certificates` command.

### Updating the CA certificates

To update the CA certificates, take the following steps:

1. Update the `input.json` file to point to the file with `additional_ca_certs`. For more details about this parameter, refer to [Certificate configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#certificate-configuration).
2. Apply the manifest:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```
   :::important
   This command may fail with errors such as: assignment
   ```
   Error: [failed to wait for application argocd/&lt;app-name1&gt;: timed out waiting for the condition,
   failed to wait for application argocd/&lt;app-name2&gt;: timed out waiting for the condition]]
   ```
   :::
Irrespective of the failure, proceed to step 3 to restart deployments and stabilize the environment.
3. Manually restart all deployments and stateful sets in the `uipath` namespace:
   ```
   kubectl rollout restart deployment -n <uipath>
   kubectl rollout restart sts -n <uipath>
   ```

:::note
To append the old certificates, you must use the `get` command from the [Accessing the CA certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#accessing-the-ca-certificates) section and append them in the CA certificate `.pem` file that you must provide in the `additional_ca_certs` field. The CA Certificate bundle file should be a valid `.pem` format and can have more than one certificate present in it.
:::

### Accessing the CA certificates

To download the already configured CA certificates, run the following command:

```
 uipathctl config additional-ca-certificates get
```

## Managing identity token-signing certificates

Automation Suite offers two methods to manage the rotation of identity token-signing certificates: automatic and manual.

To view more information about identity token-signing certificates, run the following command:

```
 uipathctl config token-signing-certificates --help
```

Output:

```
************************************************************************************

Manage token signing certificates

Usage:
  uipathctl config token-signing-certificates [flags]
  uipathctl config token-signing-certificates [command]

Available Commands:
  automatic-key-management Manage key management
  get                      Get the current token signing certificate
  rotate                   Rotate token signing certificates
  update                   Update future token signing certificate

Flags:
  -h, --help   help for token-signing-certificates

Global Flags:
      --context string      name of the kubeconfig context to use
  -f, --force               override all user prompts to true
      --kubeconfig string   kubectl configuration file (default: ~/.kube/config)
      --log-format string   log format. one of [text,json] (default "text")
      --log-level string    set log level. one of [trace,debug,info,error] (default "info")
  -q, --quiet               suppress all output except for errors and warnings
      --timeout duration    timeout of the command (default: 90 minutes) (default 1h30m0s)
      --versions string     optional path to versions file

Use "uipathctl config token-signing-certificates [command] --help" for more information about a command.

************************************************************************************
```

:::important
You can use a maximum key length of 4096 bits for signing certificates. We highly recommend you to use a key length of at least 512 bits (64 bytes) as a best practice.
:::

The following section provide details on the operations you can perform using the `uipathctl config token-signing-certificates` command.

### Automatic certificate rotation

Automatic certificate rotation means Automation Suite manages the lifecycle of signing keys. This includes rotating keys every 90 days, announcing new keys 14 days prior to rotation, retaining old keys for 14 days post-rotation, and then deleting them when the 14-day period ends.

If you're upgrading from an older version to 2.2510, automatic certificate rotation is disabled by default. To enable automatic key management, use the following command:

```
uipathctl config token-signing-certificates automatic-key-management enable
```

:::important
Enabling automatic certificate rotation may result in a downtime of up to one hour.
:::

Automatic certificate rotation is enabled by default for clean Automation Suite installations. To disable automatic key management, use the following command:

```
uipathctl config token-signing-certificates automatic-key-management disable
```

If the automatic management feature is disabled, signing certificates need to be updated and rotated manually. For details on manual key management, see the documentation on manually updating and rotating the certificate.

### Manually updating the certificate

To upload the new certificate to sign the token, run the following command:

:::note
The following command does not replace the existing token signing certificate. Make sure the certificate you provide is in `.pem` format. The `server.crt` file must contain the entire chain, as shown in the following example: assignment
```
-----server cert-----
-----root ca chain-----
```
:::

```
uipathctl config token-signing-certificates update --cert server.crt --key server.key
```

After running the update command, restart the Identity deployment and wait 48 hours before running the rotate command.

### Manually rotating the certificate

To rotate or replace the old certificate with the new one, run the following command:

```
uipathctl config token-signing-certificates rotate
```

After rotation, restart deployments and stateful sets by running the following commands:

```
kubectl -n <uipath> rollout restart deploy
kubectl -n <uipath> rollout restart sts
```

### Accessing the certificate

To download the current token signing certificate, run the following command:

```
uipathctl config token-signing-certificates get
```

:::note
There should be a lead time of approximately 24-48 hours between certificate update and rotate. We need this lead time to keep supporting the authentication for cached token signed by old certificate. Rotating the certificate too soon before the expiry of the cache token can result in downtime. In this case, you may have to restart all your robots.
:::