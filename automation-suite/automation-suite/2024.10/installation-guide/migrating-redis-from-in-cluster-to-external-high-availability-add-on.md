---
title: "Migrating Redis from in-cluster to external High Availability Add-on"
visible: true
slug: "migrating-redis-from-in-cluster-to-external-high-availability-add-on"
---

To migrate Redis from in-cluster to external High Availability Add-on, take the following steps. Note that this operation might cause downtime.

1. Update the `cluster_config.json` file. For more details, see [External High Availability Add-on configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/high-availability-add-on-configuration#external-high-availability-add-on-configuration).
2. Rerun the installer to update the `cluster_config.json` configuration.
   ```
   ./install-uipath.sh -i cluster_config.json -o output.json -f -s --accept-license-agreement
   ```

At this point, the services should be connected to the external Redis, and the in-cluster High Availability Add-on should be uninstalled.