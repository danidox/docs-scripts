---
title: "Functional security"
visible: true
slug: "functional-security"
---

This page outlines the key functionalities we implemented to ensure that your interactions with the platform occur securely.

## Audit logging

The UiPath platform includes audit logging capabilities. This allows you to maintain a detailed record of activities, user actions, and system events. [Audit logs](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-logs#about-logs) are essential for monitoring and compliance purposes, helping you track and investigate security incidents.

## Authentication and authorization

The platform supports multiple authentication and authorization models to accommodate different security and identity requirements. We leverage Auth0 for robust and secure user authentication and authorization. Auth0 is a trusted identity management platform, providing strong authentication and authorization capabilities.

Depending on the cloud offering and configuration, the following authentication models may be available: TOPLEVELNOTEMARKER
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

* **Local accounts**: Users authenticate using basic authentication with a user-owned email address and password. In some environments, users can also authenticate using an existing Microsoft or Google account linked to their email address.
* **Enterprise authentication (SSO)**: Organizations can configure Single Sign-On (SSO) using Microsoft Entra ID or other SAML-based identity providers, allowing users to sign in through their enterprise authentication systems.
* **Directory-managed accounts**: Users authenticate using company-managed accounts when a third-party identity provider is connected to the platform.

These authentication models allow organizations to align platform access with their identity and access management policies.

## Access control features

* **Restricting access by IP**: You can restrict access to the platform based on IP addresses, allowing only traffic from authorized locations. This adds an additional layer of protection against unauthorized access. In some environments, IP restrictions can also be applied at the infrastructure level with assistance from [Support](https://www.uipath.com/company/contact-us/contact-technical-support).
* **Session policy:** You can define and enforce rules for concurrent user sessions. This helps prevent unauthorized access and enhances security.
* **Restricting access to users:** You can define access controls that restrict specific users or user groups from accessing the platform.

## Data encryption

* **Custom data encryption:** You can encrypt your data stored across the platform using custom encryption keys. This ensures that sensitive data is protected and only accessible to authorized users.
* **UiPath® keys:** You can use UiPath keys for data encryption. This provides a secure and standardized approach to data protection.