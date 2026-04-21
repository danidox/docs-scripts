---
title: "Output example: prerequisite check"
visible: true
slug: "output-example-prerequisite-check"
---

The following example shows the output you may get after checking the infrastructure prerequisites when preparing an Automation Suite installation. For details, see [Checking the infrastructure prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/checking-the-infrastructure-prerequisites).

```
Checks run on nodes/aks-pool1-27380386-vmss000000
 ✔ [SQL(PRODUCT=TEST_MANAGER, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=ASROBOTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=ORCHESTRATOR, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=APPS)]
    ✔ [CHECK_API] Object storage test passed for apps
 ✔ [OBJECTSTORAGE(PRODUCT=TEST_MANAGER)]
    ✔ [CHECK_API] Object storage test passed for test_manager
 ✔ [OBJECTSTORAGE(PRODUCT=PLATFORM)]
    ✔ [CHECK_API] Object storage test passed for platform
 ✔ [REDIS(PORT=6380)]
    ✔ [CONNECTIVITY] Successfully made Redis connection on ci-asaks3955328.redis.cache.windows.net:6380
 ✔ [SQL(PRODUCT=AUTOMATION_OPS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=AUTOMATION_HUB, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
 ✔ [SQL(PRODUCT=INSIGHTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
    ✔ [COLUMNSTORE_INDEX] Columnstore index is supported for SQL DB
    ✔ [OPENJSON] OpenJSON is supported for SQL DB
 ✔ [OBJECTSTORAGE(PRODUCT=ORCHESTRATOR)]
    ✔ [CHECK_API] Object storage test passed for orchestrator
 ✔ [SQL(PRODUCT=DATASERVICE, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=APPS, TYPE=ODBC)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ODBC client
    ✔ [CONNECT] Successfully connected ODBC client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=PLATFORM, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=DATASERVICE)]
    ✔ [CHECK_API] Object storage test passed for dataservice
 ✔ [DNS(FQDN=MONITORING.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://monitoring.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [DNS(FQDN=ALM.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://alm.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
Checks run on nodes/aks-pool0-27380386-vmss000000
 ✔ [SQL(PRODUCT=INSIGHTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
    ✔ [COLUMNSTORE_INDEX] Columnstore index is supported for SQL DB
    ✔ [OPENJSON] OpenJSON is supported for SQL DB
 ✔ [SQL(PRODUCT=TEST_MANAGER, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=APPS, TYPE=ODBC)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ODBC client
    ✔ [CONNECT] Successfully connected ODBC client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=ORCHESTRATOR)]
    ✔ [CHECK_API] Object storage test passed for orchestrator
 ✔ [SQL(PRODUCT=AUTOMATION_OPS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=DATASERVICE, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=PLATFORM)]
    ✔ [CHECK_API] Object storage test passed for platform
 ✔ [SQL(PRODUCT=ASROBOTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=MONITORING.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://monitoring.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=ORCHESTRATOR, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=ALM.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://alm.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [OBJECTSTORAGE(PRODUCT=TEST_MANAGER)]
    ✔ [CHECK_API] Object storage test passed for test_manager
 ✔ [SQL(PRODUCT=PLATFORM, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=APPS)]
    ✔ [CHECK_API] Object storage test passed for apps
 ✔ [REDIS(PORT=6380)]
    ✔ [CONNECTIVITY] Successfully made Redis connection on ci-asaks3955328.redis.cache.windows.net:6380
 ✔ [OBJECTSTORAGE(PRODUCT=DATASERVICE)]
    ✔ [CHECK_API] Object storage test passed for dataservice
 ✔ [SQL(PRODUCT=AUTOMATION_HUB, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
Checks run on nodes/aks-pool0-27380386-vmss000003
 ✔ [SQL(PRODUCT=INSIGHTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
    ✔ [COLUMNSTORE_INDEX] Columnstore index is supported for SQL DB
    ✔ [OPENJSON] OpenJSON is supported for SQL DB
 ✔ [SQL(PRODUCT=AUTOMATION_HUB, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
 ✔ [OBJECTSTORAGE(PRODUCT=PLATFORM)]
    ✔ [CHECK_API] Object storage test passed for platform
 ✔ [OBJECTSTORAGE(PRODUCT=TEST_MANAGER)]
    ✔ [CHECK_API] Object storage test passed for test_manager
 ✔ [SQL(PRODUCT=TEST_MANAGER, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=PLATFORM, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=MONITORING.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://monitoring.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [OBJECTSTORAGE(PRODUCT=DATASERVICE)]
    ✔ [CHECK_API] Object storage test passed for dataservice
 ✔ [DNS(FQDN=ALM.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://alm.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [OBJECTSTORAGE(PRODUCT=ORCHESTRATOR)]
    ✔ [CHECK_API] Object storage test passed for orchestrator
 ✔ [OBJECTSTORAGE(PRODUCT=APPS)]
    ✔ [CHECK_API] Object storage test passed for apps
 ✔ [SQL(PRODUCT=ORCHESTRATOR, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=APPS, TYPE=ODBC)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ODBC client
    ✔ [CONNECT] Successfully connected ODBC client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=DATASERVICE, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [REDIS(PORT=6380)]
    ✔ [CONNECTIVITY] Successfully made Redis connection on ci-asaks3955328.redis.cache.windows.net:6380
 ✔ [SQL(PRODUCT=ASROBOTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=AUTOMATION_OPS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
Checks run on nodes/aks-pool0-27380386-vmss000004
 ✔ [SQL(PRODUCT=AUTOMATION_OPS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=ASROBOTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=ORCHESTRATOR)]
    ✔ [CHECK_API] Object storage test passed for orchestrator
 ✔ [OBJECTSTORAGE(PRODUCT=DATASERVICE)]
    ✔ [CHECK_API] Object storage test passed for dataservice
 ✔ [SQL(PRODUCT=AUTOMATION_HUB, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
 ✔ [SQL(PRODUCT=TEST_MANAGER, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=PLATFORM, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=ALM.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://alm.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [REDIS(PORT=6380)]
    ✔ [CONNECTIVITY] Successfully made Redis connection on ci-asaks3955328.redis.cache.windows.net:6380
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=INSIGHTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
    ✔ [COLUMNSTORE_INDEX] Columnstore index is supported for SQL DB
    ✔ [OPENJSON] OpenJSON is supported for SQL DB
 ✔ [SQL(PRODUCT=DATASERVICE, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=APPS)]
    ✔ [CHECK_API] Object storage test passed for apps
 ✔ [DNS(FQDN=MONITORING.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://monitoring.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=ORCHESTRATOR, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=PLATFORM)]
    ✔ [CHECK_API] Object storage test passed for platform
 ✔ [OBJECTSTORAGE(PRODUCT=TEST_MANAGER)]
    ✔ [CHECK_API] Object storage test passed for test_manager
 ✔ [SQL(PRODUCT=APPS, TYPE=ODBC)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ODBC client
    ✔ [CONNECT] Successfully connected ODBC client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
Checks run on nodes/aks-pool0-27380386-vmss000001
 ✔ [SQL(PRODUCT=AUTOMATION_OPS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=INSIGHTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
    ✔ [COLUMNSTORE_INDEX] Columnstore index is supported for SQL DB
    ✔ [OPENJSON] OpenJSON is supported for SQL DB
 ✔ [OBJECTSTORAGE(PRODUCT=PLATFORM)]
    ✔ [CHECK_API] Object storage test passed for platform
 ✔ [SQL(PRODUCT=ORCHESTRATOR, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=DATASERVICE, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=DATASERVICE)]
    ✔ [CHECK_API] Object storage test passed for dataservice
 ✔ [OBJECTSTORAGE(PRODUCT=TEST_MANAGER)]
    ✔ [CHECK_API] Object storage test passed for test_manager
 ✔ [SQL(PRODUCT=AUTOMATION_HUB, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
 ✔ [OBJECTSTORAGE(PRODUCT=ORCHESTRATOR)]
    ✔ [CHECK_API] Object storage test passed for orchestrator
 ✔ [DNS(FQDN=MONITORING.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://monitoring.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=APPS, TYPE=ODBC)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ODBC client
    ✔ [CONNECT] Successfully connected ODBC client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [REDIS(PORT=6380)]
    ✔ [CONNECTIVITY] Successfully made Redis connection on ci-asaks3955328.redis.cache.windows.net:6380
 ✔ [OBJECTSTORAGE(PRODUCT=APPS)]
    ✔ [CHECK_API] Object storage test passed for apps
 ✔ [DNS(FQDN=ALM.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://alm.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=TEST_MANAGER, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=ASROBOTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=PLATFORM, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
Checks run on nodes/aks-pool0-27380386-vmss000002
 ✔ [OBJECTSTORAGE(PRODUCT=TEST_MANAGER)]
    ✔ [CHECK_API] Object storage test passed for test_manager
 ✔ [SQL(PRODUCT=TEST_MANAGER, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=INSIGHTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
    ✔ [COLUMNSTORE_INDEX] Columnstore index is supported for SQL DB
    ✔ [OPENJSON] OpenJSON is supported for SQL DB
 ✔ [DNS(FQDN=ALM.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://alm.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [DNS(FQDN=MONITORING.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://monitoring.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [SQL(PRODUCT=AUTOMATION_HUB, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
    ✔ [COMPATIBILITY_LEVEL] SQL DB compatibility level meets requirement
 ✔ [SQL(PRODUCT=ASROBOTS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=AUTOMATION_OPS, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=DATASERVICE)]
    ✔ [CHECK_API] Object storage test passed for dataservice
 ✔ [OBJECTSTORAGE(PRODUCT=PLATFORM)]
    ✔ [CHECK_API] Object storage test passed for platform
 ✔ [SQL(PRODUCT=ORCHESTRATOR, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [OBJECTSTORAGE(PRODUCT=APPS)]
    ✔ [CHECK_API] Object storage test passed for apps
 ✔ [OBJECTSTORAGE(PRODUCT=ORCHESTRATOR)]
    ✔ [CHECK_API] Object storage test passed for orchestrator
 ✔ [REDIS(PORT=6380)]
    ✔ [CONNECTIVITY] Successfully made Redis connection on ci-asaks3955328.redis.cache.windows.net:6380
 ✔ [SQL(PRODUCT=DATASERVICE, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=APPS, TYPE=ODBC)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ODBC client
    ✔ [CONNECT] Successfully connected ODBC client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
 ✔ [SQL(PRODUCT=PLATFORM, TYPE=ADO)]
    ✔ [EXECUTE_NATIVE] Successfully executed command
    ✔ [BUILD_CLIENT] Successfully built ADO client
    ✔ [CONNECT] Successfully connected ADO client to DB
    ✔ [DB_ROLES] SQL user has the required roles to DB
Checks run on local/
 ✔ [STORAGECLASS(NAME=STORAGE_CLASS)]
    ✔ [STORAGE_CLASS_EXISTS] Storage class managed-premium exists
    ✔ [LIST_NODES] Listed 6 nodes
    ✔ [CREATE_NAMESPACE] Created namespace prereq6g5cg
    ✔ [CREATE_STATEFULSET] Created statefulset storage-class-check-wthrk
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000001
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000001
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000003
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000003
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000002
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000002
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000004
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000004
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool1-27380386-vmss000000
    ✔ [POD_RUNNING] Found one pod running on node aks-pool1-27380386-vmss000000
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000000
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000000
 ✔ [DNS(FQDN=ALM.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://alm.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [DNS(FQDN=INSIGHTS.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved insights.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [OSS(COMPONENT=MONITORING)]
    ✔ [OSS(component=monitoring)] Check for component monitoring passed
 ✔ [STORAGECLASS(NAME=STORAGE_CLASS_SINGLE_REPLICA)]
    ✔ [STORAGE_CLASS_EXISTS] Storage class azurefile-csi exists
    ✔ [LIST_NODES] Listed 6 nodes
    ✔ [CREATE_NAMESPACE] Created namespace prereqzb8mv
    ✔ [CREATE_STATEFULSET] Created statefulset storage-class-check-r9rzv
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000000
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000000
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000001
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000001
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000004
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000004
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000002
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000002
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool0-27380386-vmss000003
    ✔ [POD_RUNNING] Found one pod running on node aks-pool0-27380386-vmss000003
    ✔ [LIST_PODS] Listed 1 pods on node aks-pool1-27380386-vmss000000
    ✔ [POD_RUNNING] Found one pod running on node aks-pool1-27380386-vmss000000
 ✔ [INGRESS]
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000000] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:80 
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000000] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:443
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000001] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:80 
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000001] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:443
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000002] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:80 
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000002] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:443
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000003] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:80 
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000003] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:443
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000004] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:80 
    ✔ [INGRESS_FQDN_CHECK_TARGET_aks-pool0-27380386-vmss000004] Ingress check successful for url http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com:443
 ✔ [CONNECTIVITY]
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-5dqxb on aks-pool0-27380386-vmss000000 can reach echo-a-5dqxb's IP 10.240.0.216 on aks-pool0-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-5dqxb on aks-pool0-27380386-vmss000000 can reach echo-a-9tl9f's IP 10.240.1.137 on aks-pool0-27380386-vmss000002
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-5dqxb on aks-pool0-27380386-vmss000000 can reach echo-a-g9vp7's IP 10.240.1.230 on aks-pool0-27380386-vmss000003
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-5dqxb on aks-pool0-27380386-vmss000000 can reach echo-a-hsr5v's IP 10.240.1.247 on aks-pool0-27380386-vmss000004
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-5dqxb on aks-pool0-27380386-vmss000000 can reach echo-a-wg6dl's IP 10.240.0.176 on aks-pool0-27380386-vmss000001
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-5dqxb on aks-pool0-27380386-vmss000000 can reach echo-a-zzbt8's IP 10.240.0.15 on aks-pool1-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-9tl9f on aks-pool0-27380386-vmss000002 can reach echo-a-5dqxb's IP 10.240.0.216 on aks-pool0-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-9tl9f on aks-pool0-27380386-vmss000002 can reach echo-a-9tl9f's IP 10.240.1.137 on aks-pool0-27380386-vmss000002
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-9tl9f on aks-pool0-27380386-vmss000002 can reach echo-a-g9vp7's IP 10.240.1.230 on aks-pool0-27380386-vmss000003
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-9tl9f on aks-pool0-27380386-vmss000002 can reach echo-a-hsr5v's IP 10.240.1.247 on aks-pool0-27380386-vmss000004
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-9tl9f on aks-pool0-27380386-vmss000002 can reach echo-a-wg6dl's IP 10.240.0.176 on aks-pool0-27380386-vmss000001
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-9tl9f on aks-pool0-27380386-vmss000002 can reach echo-a-zzbt8's IP 10.240.0.15 on aks-pool1-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-g9vp7 on aks-pool0-27380386-vmss000003 can reach echo-a-5dqxb's IP 10.240.0.216 on aks-pool0-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-g9vp7 on aks-pool0-27380386-vmss000003 can reach echo-a-9tl9f's IP 10.240.1.137 on aks-pool0-27380386-vmss000002
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-g9vp7 on aks-pool0-27380386-vmss000003 can reach echo-a-g9vp7's IP 10.240.1.230 on aks-pool0-27380386-vmss000003
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-g9vp7 on aks-pool0-27380386-vmss000003 can reach echo-a-hsr5v's IP 10.240.1.247 on aks-pool0-27380386-vmss000004
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-g9vp7 on aks-pool0-27380386-vmss000003 can reach echo-a-wg6dl's IP 10.240.0.176 on aks-pool0-27380386-vmss000001
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-g9vp7 on aks-pool0-27380386-vmss000003 can reach echo-a-zzbt8's IP 10.240.0.15 on aks-pool1-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-hsr5v on aks-pool0-27380386-vmss000004 can reach echo-a-5dqxb's IP 10.240.0.216 on aks-pool0-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-hsr5v on aks-pool0-27380386-vmss000004 can reach echo-a-9tl9f's IP 10.240.1.137 on aks-pool0-27380386-vmss000002
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-hsr5v on aks-pool0-27380386-vmss000004 can reach echo-a-g9vp7's IP 10.240.1.230 on aks-pool0-27380386-vmss000003
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-hsr5v on aks-pool0-27380386-vmss000004 can reach echo-a-hsr5v's IP 10.240.1.247 on aks-pool0-27380386-vmss000004
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-hsr5v on aks-pool0-27380386-vmss000004 can reach echo-a-wg6dl's IP 10.240.0.176 on aks-pool0-27380386-vmss000001
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-hsr5v on aks-pool0-27380386-vmss000004 can reach echo-a-zzbt8's IP 10.240.0.15 on aks-pool1-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-wg6dl on aks-pool0-27380386-vmss000001 can reach echo-a-5dqxb's IP 10.240.0.216 on aks-pool0-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-wg6dl on aks-pool0-27380386-vmss000001 can reach echo-a-9tl9f's IP 10.240.1.137 on aks-pool0-27380386-vmss000002
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-wg6dl on aks-pool0-27380386-vmss000001 can reach echo-a-g9vp7's IP 10.240.1.230 on aks-pool0-27380386-vmss000003
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-wg6dl on aks-pool0-27380386-vmss000001 can reach echo-a-hsr5v's IP 10.240.1.247 on aks-pool0-27380386-vmss000004
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-wg6dl on aks-pool0-27380386-vmss000001 can reach echo-a-wg6dl's IP 10.240.0.176 on aks-pool0-27380386-vmss000001
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-wg6dl on aks-pool0-27380386-vmss000001 can reach echo-a-zzbt8's IP 10.240.0.15 on aks-pool1-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-zzbt8 on aks-pool1-27380386-vmss000000 can reach echo-a-5dqxb's IP 10.240.0.216 on aks-pool0-27380386-vmss000000
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-zzbt8 on aks-pool1-27380386-vmss000000 can reach echo-a-9tl9f's IP 10.240.1.137 on aks-pool0-27380386-vmss000002
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-zzbt8 on aks-pool1-27380386-vmss000000 can reach echo-a-g9vp7's IP 10.240.1.230 on aks-pool0-27380386-vmss000003
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-zzbt8 on aks-pool1-27380386-vmss000000 can reach echo-a-hsr5v's IP 10.240.1.247 on aks-pool0-27380386-vmss000004
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-zzbt8 on aks-pool1-27380386-vmss000000 can reach echo-a-wg6dl's IP 10.240.0.176 on aks-pool0-27380386-vmss000001
    ✔ [OVERLAY_CONNECTIVITY_TEST] echo-a-zzbt8 on aks-pool1-27380386-vmss000000 can reach echo-a-zzbt8's IP 10.240.0.15 on aks-pool1-27380386-vmss000000
    ✔ [POD_TO_A] Scenario: http check between two random pods completed successfully
    ✔ [POD_TO_B_MULTI_NODE_CLUSTERIP] Scenario: http check between from pod to a multinode ClusterIP completed successfully
    ✔ [POD_TO_B_MULTI_NODE_HEADLESS] Scenario: http check between from pod to a multinode ClusterIP without a clusterIP set completed successfully
    ✔ [HOST_TO_B_MULTI_NODE_CLUSTERIP] Scenario: http check between from pod to a multinode ClusterIP using HostNetwork completed successfully
    ✔ [HOST_TO_B_MULTI_NODE_HEADLESS] Scenario: http check between from pod to a multinode ClusterIP without a clusterIP set using HostNetwork completed successfully
    ✔ [POD_TO_B_INTRA_NODE_CLUSTERIP] Scenario: http check between from two pods colocated on the same node via ClusterIP completed successfully
 ✔ [OSS(COMPONENT=CERT-MANAGER)]
    ✔ [OSS(component=cert-manager)] Check for component cert-manager passed
 ✔ [DNS(FQDN=MONITORING.<FQDN>)]
    ✔ [VALIDATE_FQDN] FQDN is valid
    ✔ [RESOLVE_TOP_DOMAIN] Resolved http://ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [RESOLVE_SUBDOMAIN] Resolved http://monitoring.ci-asaks3955328.devtest-ascloudgen-ea.infra.uipath-dev.com  to [{20.9.49.161 }]
    ✔ [IPS_MATCH] Subdomain resolves to top domain
 ✔ [NODE(CPU >= 8, RAM >= 16GI)]
    ✔ [LIST_NODES] Listed 6 nodes
    ✔ [AT_LEAST_ONE_NODE] At least one node found
    ✔ [CPU_USAGE] Node aks-pool0-27380386-vmss000000 has 12.50% CPU usage
    ✔ [MEMORY_USAGE] Node aks-pool0-27380386-vmss000000 has 5.95% memory usage
    ✔ [POD_USAGE] Node aks-pool0-27380386-vmss000000 has 10.00% of pods in use. Number of pods: 10.00 max allowed: 100.00
    ✔ [CPU_CAPACITY(aks-pool0-27380386-vmss000000)] Node has enough CPU capacity. Has: 8, needs at least: 8
    ✔ [RAM_CAPACITY(aks-pool0-27380386-vmss000000)] Node has enough RAM capacity. Has: 32882800Ki, needs at least: 16Gi
    ✔ [CPU_USAGE] Node aks-pool0-27380386-vmss000001 has 12.50% CPU usage
    ✔ [MEMORY_USAGE] Node aks-pool0-27380386-vmss000001 has 6.04% memory usage
    ✔ [POD_USAGE] Node aks-pool0-27380386-vmss000001 has 23.00% of pods in use. Number of pods: 23.00 max allowed: 100.00
    ✔ [CPU_CAPACITY(aks-pool0-27380386-vmss000001)] Node has enough CPU capacity. Has: 8, needs at least: 8
    ✔ [RAM_CAPACITY(aks-pool0-27380386-vmss000001)] Node has enough RAM capacity. Has: 32882800Ki, needs at least: 16Gi
    ✔ [CPU_USAGE] Node aks-pool0-27380386-vmss000002 has 12.50% CPU usage
    ✔ [MEMORY_USAGE] Node aks-pool0-27380386-vmss000002 has 6.07% memory usage
    ✔ [POD_USAGE] Node aks-pool0-27380386-vmss000002 has 26.00% of pods in use. Number of pods: 26.00 max allowed: 100.00
    ✔ [CPU_CAPACITY(aks-pool0-27380386-vmss000002)] Node has enough CPU capacity. Has: 8, needs at least: 8
    ✔ [RAM_CAPACITY(aks-pool0-27380386-vmss000002)] Node has enough RAM capacity. Has: 32882800Ki, needs at least: 16Gi
    ✔ [CPU_USAGE] Node aks-pool0-27380386-vmss000003 has 12.50% CPU usage
    ✔ [MEMORY_USAGE] Node aks-pool0-27380386-vmss000003 has 6.41% memory usage
    ✔ [POD_USAGE] Node aks-pool0-27380386-vmss000003 has 23.00% of pods in use. Number of pods: 23.00 max allowed: 100.00
    ✔ [CPU_CAPACITY(aks-pool0-27380386-vmss000003)] Node has enough CPU capacity. Has: 8, needs at least: 8
    ✔ [RAM_CAPACITY(aks-pool0-27380386-vmss000003)] Node has enough RAM capacity. Has: 32882800Ki, needs at least: 16Gi
    ✔ [CPU_USAGE] Node aks-pool0-27380386-vmss000004 has 12.50% CPU usage
    ✔ [MEMORY_USAGE] Node aks-pool0-27380386-vmss000004 has 6.18% memory usage
    ✔ [POD_USAGE] Node aks-pool0-27380386-vmss000004 has 25.00% of pods in use. Number of pods: 25.00 max allowed: 100.00
    ✔ [CPU_CAPACITY(aks-pool0-27380386-vmss000004)] Node has enough CPU capacity. Has: 8, needs at least: 8
    ✔ [RAM_CAPACITY(aks-pool0-27380386-vmss000004)] Node has enough RAM capacity. Has: 32882796Ki, needs at least: 16Gi
    ✔ [CPU_USAGE] Node aks-pool1-27380386-vmss000000 has 12.50% CPU usage
    ✔ [MEMORY_USAGE] Node aks-pool1-27380386-vmss000000 has 6.01% memory usage
    ✔ [POD_USAGE] Node aks-pool1-27380386-vmss000000 has 11.00% of pods in use. Number of pods: 11.00 max allowed: 100.00
    ✔ [CPU_CAPACITY(aks-pool1-27380386-vmss000000)] Node has enough CPU capacity. Has: 8, needs at least: 8
    ✔ [RAM_CAPACITY(aks-pool1-27380386-vmss000000)] Node has enough RAM capacity. Has: 32882800Ki, needs at least: 16Gi
 ✔ [REGISTRY]
    ✔ [CONNECTIVITY] Successfully made Registry connection on Azure Container Registry | Microsoft Azure 
 ✔ [OSS(COMPONENT=GATEKEEPER)]
    ✔ [OSS(component=gatekeeper)] Check for component gatekeeper passed
 ✔ [OSS(COMPONENT=LOGGING)]
    ✔ [OSS(component=logging)] Check for component logging passed
 ✔ [RESOURCE]
    ✔ [Capacity] Cluster has enough resources to run the given requirements
 ✔ [NETWORK-POLICIES]
    ✔ [CREATE_NAMESPACE] Namespace prereqmnfk5 created
    ✔ [CREATE_EGRESS_NETWORK_POLICY] Created the egress network policies allow-coredns-egress and block-external-traffic
    ✔ [CREATE_INGRESS_NETWORK_POLICY] Created the ingress network policy: block-echo-server-ingress
    ✔ [CREATE_SERVICE] Service echo-server-svc created
    ✔ [CREATE_ECHO_SERVER_POD] Echo server pod echo-server created
    ✔ [ECHO_SERVER_ACCESS] Echo server is expectedly not accessible from curl pod
    ✔ [DELETE_CURL_POD] Curl pod curl-pod deleted
    ✔ [UPDATE_NETWORK_POLICY] Network policy block-echo-server-ingress updated to allow traffic
    ✔ [ECHO_SERVER_ACCESS] Echo server is expectedly not accessible from curl pod
    ✔ [DELETE_CURL_POD] Curl pod curl-pod deleted
    ✔ [UPDATE_NETWORK_POLICY] Network policy block-external-traffic updated to allow traffic
    ✔ [CURL_RESULT] Traffic to pod echo-server is allowed from pod curl-pod
```