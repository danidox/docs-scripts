---
title: "2023.10.5"
visible: true
slug: "release-notes-2023-10-5"
---

**Release date: April 3, 2024**

## Preserving credentials casing

By default, login credentials (domain\username) are converted to UPPERCASE, which may cause automations to fail. To preserve the original casing, we've created a new system variable: `UIPATH_PRESERVE_CREDENTIALS_CASE`. Add it to your environment, and set its value to `True`**.**

## Bug fixes

* We've fixed the issue where users were unable to log into their Virtual Desktop Infrastructure (VDI) accounts. This primarily occurred when a previous user did not log off after manually stopping an unattended automation via Orchestrator.
* When authenticating through client certificates, a bug prevented the robot from reading private keys from card readers. This mainly occurred when multiple card readers were present and at least one had unexpected issues.
* Previously, sessions might have remained in use after a job was completed due to an incorrect status of the executor’s exit. The system now automatically terminates the executor 30 seconds after a job is completed.
* An issue causing Assistant to throw the `Format string contains an unescaped latin alphabet character` error when running a job has been resolved.