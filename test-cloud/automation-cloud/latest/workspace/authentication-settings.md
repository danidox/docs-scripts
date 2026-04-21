---
title: "Understanding authentication models"
visible: true
slug: "authentication-settings"
---

UiPath offerings support two authentication approaches: **local accounts** and **directory accounts**. Each approach defines how user identities are created, authenticated, and managed.

Depending on the cloud offering that you are using, refer to the following resources:

* [Authentication models for Test Cloud](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/authentication-models-for-test-cloud#authentication-models-for-test-cloud)
* [Authentication models for Test Cloud Public Sector](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/authentication-models-for-test-cloud-public-sector#authentication-models-for-test-cloud-public-sector)
* [Authentication models for Test Cloud Dedicated](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/authentication-models-for-test-cloud-dedicated#authentication-models-for-test-cloud-dedicated)

## Local accounts

Local accounts are user accounts that are created and managed directly within a UiPath organization. Organization administrators invite users to join, and each user signs in by using the credentials associated with their account.

Local accounts provide a self-contained authentication approach and allow organizations to manage users without integrating an external identity provider. Local accounts can coexist with directory-based authentication, depending on the offering and configuration.

## Directory accounts

Directory accounts rely on an external identity provider that integrates with the UiPath platform. User identities are created and maintained outside UiPath and are referenced by the platform only for authentication and authorization.

Directory-based authentication allows organizations to reuse existing identity systems, centralize account management, and apply corporate security policies consistently across applications. Supported directory integrations include Microsoft Entra ID and identity providers that support the SAML 2.0 standard.

## Authentication and authorization

Authentication verifies a user’s identity. Authorization determines which services, tenants, and features the user can access.

In UiPath offerings, authentication is handled either by the UiPath platform or by an integrated identity provider, depending on the selected authentication model. Authorization is always enforced within UiPath through roles, groups, and licenses.