---
title: "Configuring preloaded execution"
visible: true
slug: "configuring-preloaded-execution"
---

You can manage the behavior of preloaded executors by setting specific environment variables on the robot machine, as follows:

| Environment variable | Value | Description |
| --- | --- | --- |
| `UIPATH_PRE_LOADED_EXECUTOR` | None | Overwrites the default behavior and starts the preloaded executor only when the first job starts. |
| `UIPATH_DISABLE_PRE_LOADED_EXECUTOR` | True | Disables the preloaded executor. |