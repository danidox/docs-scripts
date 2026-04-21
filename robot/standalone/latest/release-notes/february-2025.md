---
title: "February 2025"
visible: true
slug: "february-2025"
---

## February 26, 2025

**Build number: 2025.0.161**

### HTTPS for all NuGet feeds

Starting with the Robot releases in February 2025 (Latest) and October 2025 (LTS), calls to [HTTP-unsecure feeds from NuGet-supported packages are no longer allowed](https://docs.uipath.com/overview/other/latest/overview/deprecation-timeline#robot). When a non-HTTPS feed is used, an error is thrown, and opting out of this behavior is not possible.

Transition to secure HTTPS feeds to prevent disruptions.

### New options for user sessions

Two new options for the `UIPATH_SESSION_BEHAVIOR` system environment variable, `LeaveSessionActive` and `LeaveSessionDisconnected`, allow you to control what happens to the user session after a job completes.

* `UIPATH_SESSION_BEHAVIOR=LeaveSessionActive`—Prevents restoration of the initial session state.
* `UIPATH_SESSION_BEHAVIOR=LeaveSessionDisconnected`—Always disconnects the session on restore.

### New UiPath repository certificate SHA-256 fingerprint

If you are using package signature verification, a new UiPath repository certificate SHA-256 fingerprint must be added to your NuGet configuration. Ensure it is added under both trusted authors and trusted repositories, as [shown in our documentation](https://docs.uipath.com/robot/standalone/latest/admin-guide/package-signature-verification#adding-trusted-sources).

```
<certificate fingerprint="A96ADDC7455443CF702A887BC153CF7844038E2E88081D676C57DDD90EC90245" hashAlgorithm="SHA256" allowUntrustedRoot="false" />
```

### Support for Windows Server 2025

Starting with release, UiPath Robot can also run on Windows Server 2025 operating systems.

### .NET Framework requirement update

The minimum.NET Framework requirement has been updated from 4.6.1 to 4.7.2.

### Bug fixes

* Using special character quotes `"` (0x201C) in strings caused a JIT compilation error at runtime in Windows projects.