---
title: "December 2025"
visible: true
slug: "december-2025"
---

## December 3, 2025

**Build number: 2026.0.181**

### Bug fixes

* Resolved an issue where Chrome window was not visible in the PiP preview. This was applicable for Chrome v139+ on Windows 11 22H2 or newer.
* Fixed an issue that causes the LiteDB backup files to persist, using unnecessary disk space.
* Fixed an issue where the **RobotJS listener** occasionally failed to start, causing the following error:
  ```
  System.TimeoutException: RegisterListenerPort timed out.
  ```