---
title: "Using EntraID users with multifactor authentication (MFA) for unattended robots"
visible: true
slug: "using-entraid-users-with-multifactor-authentication-mfa-with-robots"
---

Multifactor authentication (MFA) adds an extra layer of security by requiring users to verify their identity using two or more factors, such as:

* Something you know: a password
* Something you have: a mobile device or smart card
* Something you are: a fingerprint or face scan

MFA helps protect against unauthorized access, even if a password is compromised. However, it introduces additional complexity when setting up unattended automations.

Passwords count as a single authentication factor. Because MFA requires at least two factors, Robots cannot create user sessions using password credentials alone.

To enable MFA users to authenticate, you can use smart card credentials instead.

## Step 1: Create virtual smart cards

Virtual smart cards are easier to deploy and manage across multiple machines.

You must create virtual smart cards on all virtual machines (VMs) where robots run. Do this for each Entra ID user that executes automations.

A virtual smart card functions as a physical one, but instead of using a physical container, it relies on the machine [Trusted Platform Module (TPM)](https://learn.microsoft.com/en-us/windows/security/identity-protection/virtual-smart-cards/virtual-smart-card-get-started) chip to securely store cryptographic keys.

## Step 2: Configure Entra certificate-based authentication

After creating the virtual smart cards, configure [Entra certificate-based authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-certificate-based-authentication) to allow Entra ID users to authenticate using certificates.

The certificates used for authentication must be configured as [multi-factor](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-certificate-based-authentication#step-3-configure-an-authentication-binding-policy) to meet MFA requirements.