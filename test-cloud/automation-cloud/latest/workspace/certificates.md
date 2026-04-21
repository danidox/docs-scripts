---
title: "Certificates"
visible: true
slug: "certificates"
---

This page describes how certificate management is done at the platform level, a process that is critical for the correct functioning of the platform, and connected robots. Information on how our current Certificate Authority, Let's Encrypt, executes the certificate rotation process is also available on this page.

## Let's Encrypt Certificate Authority (CA)

Let’s Encrypt is a global CA that allows users and organizations to obtain, renew, and manage SSL/TLS certificates that are used by websites to enable secure HTTPS connections.
:::important
* The validity perios of Let's Encrypt certificates is 90 days.
* We strongly encourage you to always trust Let's Encrypt certificates, namely Root CAs and Intermediate CAs.
* If there are any planned rotations to your Root or Intermediate CAs, your access is not affected if you trust the Root and
Intermediate CAs.
* If your certificate expires or is involved in a certificate rotation process, an error occurs indicating that your certificate
is invalid. To learn how to fix errors related to certificates, refer to [Troubleshooting](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/general-troubleshooting#the-remote-certificate-is-invalid-because-of-errors-in-the-certificate-chain%3A-untrustedroot).
* We generally recommend trusting the Certificate Authority (CA). However, if your organization's IT policy does not allow trusting
the CA, consider installing your certificates at an organization level. This method is particularly helpful when dealing with a large number of machines, as it makes central management of certificates more feasible than setting them up individually. Keep in mind that if you choose this approach, you are responsible for periodically updating the certificates in line with our rotation schedule.
:::

## Resources

To learn more about all the current and relevant historical CAs operated by Let’s Encrypt, refer to [Chains of trust](https://letsencrypt.org/certificates/).

To learn more about CA features, limitations, and browser compatibility, refer to [Certificate authorities](https://developers.cloudflare.com/ssl/reference/certificate-authorities/).

## Certificate validity

To check your certificate validity, take the following steps:

1. In a browser window, navigate to your organization via the access URL.
   :::note
   Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
   :::
2. Select the **View site information** icon. Select **Connection is secure** from the dropdown menu.

   !['Connection is secure option' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/459660)
3. Select **Certificate is valid**.

   !['Certificate is valid option' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/459743)
4. In the **Certificate Viewer**, select the **Details** tab. Then select **Export** and save the certificate.
5. Open the certificate (`.crt` file) locally.
6. Select the **General** tab to check the validity of the certificate.