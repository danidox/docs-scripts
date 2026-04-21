---
title: "Managing the certificates"
visible: true
slug: "managing-the-certificates"
---

:::important
The installation process generates self-signed certificates on your behalf. You should replace them with certificates signed by a trusted Certificate Authority (CA) as soon as installation completes. You can use the `uipathctl` CLI tool to update certificates post-installation. For details, see [uipathctl documentation](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/uipathctl#uipathctl).
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
subjectAltName=DNS:$AS_FQDN,DNS:alm.$AS_FQDN,DNS:monitoring.$AS_FQDN,DNS:registry.$AS_FQDN,DNS:objectstore.$AS_FQDN,DNS:insights.$AS_FQDN
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

Certificates are stored as a secret at Istio level. You can find certificates under the `istio-ingressgateway-certs` name in the `istio-system` namespace.

See the certificate files in the following list:

* Server TLS certificate is stored as `tls.crt`
* Server TLS private key as `tls.key`
* CA bundle is stored as `ca.crt`

You can verify the secrets using the following command:

```
kubectl -n istio-system get secrets istio-ingressgateway-certs -o yaml
```

Certificates are also stored in the UiPath namespace. This is applicable to every UiPath® product that needs certificate information to trust incoming calls. For details, see [Understanding the container architecture related to certificates](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/certificates-overview#understanding-the-container-architecture-related-to-certificates).

### Updating the TLS certificates

:::important
You must decrypt the certificate key before updating the server certificate. Skipping the decryption step would result in an error.
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
* Private key - Private key for server certificate
```
uipathctl config tls-certificates update --cert server.crt --cacert ca.crt --key server.key
```

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
      --kubeconfig string   kubectl configuration file (default: ~/.kube/config)
      --log-format string   log format. one of [text,json] (default "text")
      --log-level string    set log level. one of [trace,debug,info,error] (default "error")
  -q, --quiet               suppress all output except for errors and warnings
      --timeout duration    timeout of the command (default 1h0m0s)

***************************************************************************************
```

### Updating the CA certificates

This command helps you update or replace the existing configured CA certificates.

```
uipathctl config additional-ca-certificates update --cacert additional_ca.crt
```

:::note
The command above adds a new certificate to the list of existing certificates. if you want to replace all the previously configured certificates, make sure to append `--replace` at the end. The CA Certificate bundle file should be a valid `.pem` format and can have more than one certificate present in it.
:::

### Accessing the CA certificates

To download the already configured CA certificates, run the following command:

```
 uipathctl config additional-ca-certificates get
```

## Managing identity token-signing certificates

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
  get         Get the current token signing certificate
  rotate      Rotate token signing certificates
  update      Update future token signing certificate

Flags:
  -h, --help   help for token-signing-certificates

Global Flags:
      --context string      name of the kubeconfig context to use
      --kubeconfig string   kubectl configuration file (default: ~/.kube/config)
      --log-format string   log format. one of [text,json] (default "text")
      --log-level string    set log level. one of [trace,debug,info,error] (default "error")
  -q, --quiet               suppress all output except for errors and warnings
      --timeout duration    timeout of the command (default 1h0m0s)

************************************************************************************
```

### Updating the certificate

To upload the new certificate to sign the token, run the following command:

:::note
The following command does not replace the existing token signing certificate. Make sure the certificate you provide is in `.pem` format.
:::

```
uipathctl config token-signing-certificates update --cert server.crt --key server.key
```

### Rotating the certificate

To rotate or replace the old certificate with the new one, run the following command:

```
uipathctl config token-signing-certificates rotate
```

After rotation, restart deployments and stateful sets by running the following commands:

```
kubectl -n uipath rollout restart deploy
kubectl -n uipath rollout restart sts
```

### Accessing the certificate

To download the current token signing certificate, run the following command:

```
uipathctl config token-signing-certificates get
```

:::note
There should be a lead time of approximately 24-48 hours between certificate update and rotate. We need this lead time to keep supporting the authentication for cached token signed by old certificate. Rotating the certificate too soon before the expiry of the cache token can result in downtime. In this case, you may have to restart all your robots.
:::

## Managing the external OCI-compliant registry certificate

To update the certificate for the external OCI-compliant registry post-installation, take the following steps:

1. Update the `registry_ca_cert` flag in the `input.json` file. For details, see [External OCI-compliant registry configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#external-oci-compliant-registry-configuration).
2. Update the ArgoCD trusted CA certificate for the external OCI-compliant registry:
   ```
   uipathctl config argocd ca-certificates update --cacert [PATH]
   ```

:::note
Registries signed by a private certificate authority do not work as expected by simply providing the CA file as `registry_ca_cert` for AKS and EKS. You need to follow additional steps, specific to the cloud provider. For example, see [Custom certificate authority (CA) in Azure Kubernetes Service (AKS) (preview)](https://learn.microsoft.com/en-us/azure/aks/custom-certificate-authority) or [Use private certificates to enable a container repository in Amazon EKS](https://aws.amazon.com/blogs/containers/use-private-certificates-to-enable-a-container-repository-in-amazon-eks/) as some of the possible solutions.
:::