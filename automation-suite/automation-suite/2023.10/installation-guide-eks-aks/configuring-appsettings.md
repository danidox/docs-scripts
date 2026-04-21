---
title: "Configuring appSettings"
visible: true
slug: "configuring-appsettings"
---

## Adding and changing appSettings

You can configure the Orchestrator settings in the `appsettings.json` file. If the file does not already exist, you can create it yourself. To modify the settings, take the following steps:

1. Place the new values inside an `appsettings.json` file. Make sure to use the format shown in the following example:
   ```
   {
       "EncryptionKeyPerTenant.Enabled": "true",
       "Triggers.DisableWhenFailedCount": "20",
       "Triggers.JobsCountStrategy": "NoLimit"
   }
   ```
2. Update the `appSettings` configuration using this command:
   ```
   uipathctl config orchestrator update-config --app-settings appsettings.json
   ```

## Removing appSettings

`appSettings` are stored under the `values.json` key of the `orchestrator-customconfig` config map in the uipath namespace. You can remove any unnecessary `appSettings` using `kubectl` or a similar tool.

Example of `values.json` in the `orchestrator-customconfig` config map:

```
{
  "AppSettings" : {
    "EncryptionKeyPerTenant.Enabled": "true",
    "Triggers.DisableWhenFailedCount": "20",
    "Triggers.JobsCountStrategy": "NoLimit"
  },
  "Kestrel" : {
     ...
  }
}
```