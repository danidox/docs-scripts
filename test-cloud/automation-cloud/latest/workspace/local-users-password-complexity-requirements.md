---
title: "Local users password complexity requirements"
visible: true
slug: "local-users-password-complexity-requirements"
---

Test Cloud enforces specific password policies for local users to ensure account security. The following table summarizes these policies:

| Policy | Description |
| --- | --- |
| **Minimum password length** | Passwords must be at least 8 characters long. |
| **Password expiration** | No expiration policy. Passwords do not need to be periodically changed. |
| **Password reuse** | No reuse policy. Previous passwords can be reused.  **Note**: It is better to use a unique password each time for improved security. |
| **Failed login attempts before lockout** | After 10 consecutive failed login attempts, the account is locked to prevent potential unauthorized access.  The lockout period lasts 30 days, after which you can login again. |