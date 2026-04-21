---
title: "Managing UiPath signing certificate for SAML
            authentication requests"
visible: true
slug: "managing-uipath-signing-certificate-for-saml-authentication-requests"
---

In the SAML protocol, the service provider (SP) can sign authentication requests to confirm their origin and ensure they are not changed during transmission. The SP uses a private key (signing certificate) to sign the request. The identity provider (IdP) uses the matching public key (signing certificate) to validate the signature.

By default, UiPath signs SAML authentication requests using its own certificate. UiPath frequently changes this certificate. If your IdP cannot automatically retrieve the updated certificate from UiPath's SAML metadata URL, you must manually upload the new certificate in your IdP each time it changes. This manual process increases the risk of errors and service interruption.

To reduce this effort, you can use UiPath's [SAML certificate API endpoints](https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/saml-certificates) to upload your own signing certificate. This allows you to manage the signing certificate through automation. After you upload a new certificate, you must also update the matching public key in your IdP to maintain a valid connection and follow your organization's security policies.

When you upload a customer certificate, UiPath replaces the default certificate in the SAML metadata document. UiPath then uses your certificate for all signing actions. After you upload the certificate, update the matching public key in your IdP to follow your organization's IT security and compliance policies

## Considerations

Before you upload your own signing certificate for the SAML integration, make sure you take the following aspects into consideration:

* You are responsible for ensuring that you renew your uploaded self-signed certificates before they expire.
* Uploading a new certificate in UiPath will override the existing certificate in the UiPath SAML metadata document, and also the one uploaded in your IdP.

## Prerequisites

Before you upload your own signing certificate for the SAML integration, make sure you meet the following requirements:

* You must configure a SAML integration for your organization.
* You need access to your organization's `partitionGlobalId`.

`partitionGlobalId` is the organization ID.
* You must generate a certificate that includes a private key in PEM format.
* The PEM file must include both the certificate and the private key.
* You must upload the public certificate to your IdP (for example, PingOne) after you upload it to your UiPath organization.
* To upload a secondary certificate, you must first upload a primary certificate.

## Steps

To generate a custom signing certificate and uploading it to UiPath's Identity Server, for your existing SAML integrations, follow these steps:

1. Generate a self-signed certificate. For example, use the following OpenSSL powershell commands to generate a self-signed certificate valid for one year:
   ```
   openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365 -subj "/CN=example.com"
   Get-Content key.pem, cert.pem | Set-Content full-cert.pem
   ```

These commands create the following objects:
   * `key.pem` – private key
   * `cert.pem` – certificate
   * `full-cert.pm` – combined PEM with private key and certificate
2. Upload your primary certificate using the `PUT /<AccessURL>/{organizationName}/identity_/SamlCertificate/primary` API.
   :::note
   The certificate becomes the primary signing certificate for your organization.
   :::

Response example:

   ```
   {
     "partitionGlobalId": "GUID",
     "primaryCertificateId": int,
     "primaryCertificateThumbprint": "string",
     "secondaryCertificateId": null,
     "secondaryCertificateThumbprint": null
   }
   ```
3. (Optional) Upload a secondary certificate using the `PUT /<AccessURL>/{organizationName}/identity_/SamlCertificate/secondary` API: To minimize disruption during certificate rotation, the SAML protocol allows the IdP to validate the signature against any certificate published in the service provider's metadata. This enables you to:
   * Create a new signing certificate.
   * Upload it to your IdP as a verification certificate.
   * Switch the secondary certificate to primary.
   * Delete the old primary certificate.

Response example

   ```
   {
     "partitionGlobalId": "GUID",
     "primaryCertificateId": int,
     "primaryCertificateThumbprint": "string",
     "secondaryCertificateId": int,
     "secondaryCertificateThumbprint": "string"
   }
   ```
4. (Optional) Switch the secondary certificate to primary, using the `POST /<AccessURL>/{organizationName}/identity_/SamlCertificate/switch` API: Switching certificates ensures a seamless certificate replacement or renewal.

**Response example**
   ```
   {
     "partitionGlobalId": "<Id>",
     "primaryCertificateId": 74268,
     "primaryCertificateThumbprint": "<Id>",
     "secondaryCertificateId": <Id>,
     "secondaryCertificateThumbprint": "<Id>"
   }
   ```
5. (Optional) Verify which certificates are currently configured for your organization using the `GET /<AccessURL>/{organizationName}/identity_/SamlCertificate/{partitionGlobalId}/certificates` API. This returns the current primary and secondary certificate IDs and thumbprints. This step helps you verify your certificate setup to ensure the right certificate is currently active.
6. (Optional) Delete a certificate using the `DELETE /<AccessURL>/{organizationName}/identity_/SamlCertificate/{partitionGlobalId}/{certificateId}` API. Deleting old or unused certificates reduces potential security risks.
   :::note
   You cannot delete the primary certificate if a secondary certificate is still present.
   :::