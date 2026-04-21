---
title: "AKS input.json example"
visible: true
slug: "aks-inputjson-example"
---

The following an example shows an `input.json` file with all the products enabled, as well as the mandatory and optional configuration parameters for Automation Suite on AKS. You can use the example as reference and make changes according to your environment requirements.

Note that the minimum UiPath® product selection requires the platform services to be enabled. Make sure to replace FQDNs, hostnames, usernames and passwords, and SQL connection strings with your own configurations.

```
{
  "kubernetes_distribution": "aks",
  "install_type": "online",
  "profile": "ha",
  "network": {
    "ipv4": { "enabled": true },
    "ipv6": { "enabled": true }
  },
  "registries": {
    "docker": {
      "url": "registry.uipath.com",
      "username": "",
      "password": ""
    },
    "helm": {
      "url": "registry.uipath.com",
      "username": "",
      "password": ""
    }
  },
  "fqdn": "automationsuite.mycompany.com",
  "admin_username": "admin",
  "admin_password": "password",
  "fips_enabled_nodes": false,
  "fabric": {
    "redis": {
      "license": "", // fabric.redis.license must not be specified when fabric.redis.{hostname, password, port} are specified
      "ha":false,
      "hostname": "redis-cache.mycompany.com",
      "password": "redispassword",
      "port": 6380,
      "tls": true
    }
  },
  "external_object_storage": {
    "enabled": true,
    "create_bucket": true,
    "storage_type": "azure",
    "use_managed_identity": false,
    "azure_fqdn_suffix": "core.windows.net",
    "account_key": "secretkey",
    "use_workload_identity" : "",
    "account_name": "as-storage-account",
    // storage type s3 specific config:
    "fqdn": "",
    "port": "",
    "region": "us-east-1",
    "access_key": "",
    "secret_key": "",
    "use_instance_profile": true,
    "bucket_name_prefix": "",
    "bucket_name_suffix": ""
  },
  "infra": {
    "docker_registry": {}
  },
  "ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/azure-load-balancer-internal": "false",
      "service.beta.kubernetes.io/azure-load-balancer-ipv4": "<ip>"
    },
    "gateway_selector": {
      "istio": "ingressgateway"
    }
  },
  "istioMinProtocolVersion": "TLSV1_3",
  "disable_presigned_url": false,
  "tolerations": [],
  "exclude_components": [],
  "server_certificate": {
    "tls_cert_file": "",
    "tls_key_file": "",
    "ca_cert_file": ""
  },
  "additional_ca_certs": "",
  "registry_ca_cert": "",
  "identity_certificate": {
    "saml_current_service_cert_file": "",
    "saml_current_service_cert_pass": "",
    "saml_future_service_cert_file": "",
    "saml_future_service_cert_pass": "",
    "ldap_cert_authority_file": ""
  },
  "sql": {
    "create_db": false,
    "server_url": "",
    "port": "",
    "username": "",
    "password": ""
  },
 "orchestrator": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-orchestrator"
    },
    "testautomation": {
      "enabled": true
    },
    "updateserver": {
      "enabled": true
    }
  },
  "processmining": {
    "external_object_storage": {
      "bucket_name": "uipath-as-processmining"
    },
    "enabled": true
  },

 "integrationservices": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "insights": {
    "enabled": true,
    "enable_realtime_monitoring": false,
     "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "automation_hub": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "automation_ops": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "aicenter": {
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    },
    "enabled": true
  },
  "documentunderstanding": {
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    },
    "enabled": true
  },
   "test_manager": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "action_center": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "apps": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "asrobots": {
    "packagecaching": true,
    "packagecachefolder": "/uipath_asrobots_package_cache",
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    },
    "enabled": true
  },
  "studioweb": {
    "enabled": false
  },
  "dataservice": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-dataservice"
    }
  },
  "ecs": {
    "enabled": true,
    "sql_connection_str": "",
    "sql_vector_connection_str": "",
    "external_object_storage": null,
  },
  "llmobservability": {
    "enabled": true,
    "trace_retention_in_days": 30,
    "llmaudit_retention_in_months": 24,
  },
  "llmgateway": {
    "enabled": true,
    "sql_connection_str": "",
  },
  "automationsolutions": {
    "enabled": true,
  },
  "autopiloteveryone": {
    "enabled": true,
  },
  "storage_class": "managed-premium",
  "storage_class_single_replica": "azurefile-csi",
  "storage_class_name_with_rwx_support": "azurefile-csi",
  "platform": {
    "enabled": true
  },
 "telemetry_optout": false,
 "pod_identity" : {     
   "enabled": true,     
   "aks_managed_identity_client_id": <client-id>
  },
  "proxy": {
    "enabled": true,
    "http_proxy": "<http://<PROXY-SERVER-IP>:<PROXY-PORT>",
    "https_proxy": "<http://<PROXY-SERVER-IP>:<PROXY-PORT>",
    "no_proxy": "paste list from Configuring the cluster section"
  },
  "snapshot": {
    "enabled": true,
    "aks_infra_resource_group": "MC_ci-asaks4002399_ci-asaks4002399_eastus",
    "external_object_storage": {
      "storage_type": "azure",
      "cloud_name": "AzurePublicCloud",
      "resource_group": "ci-asaks4002399",
      "auth_mode": "ServicePrincipal",
      "subscription_id": "b65b0225-ce9b-4a79-9dd9-c00071d40d64",
      "tenant_id": "d8353d2a-b153-4d17-8827-902c51f72357",
      "account_name": "storaccid2547865",
      "bucket_name": "uipath-backup",
      "client_id": "1fbd7d95-5f8c-4f70-90a6-fdf20310d10e",
      "client_secret": "----"
    }
  },
  "sql_connection_string_template": "Server=tcp:mssql.mycompany.com,1443;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=sqladmin;Password='sqlpassword';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
  "sql_connection_string_template_jdbc": "jdbc:sqlserver://mssql.mycompany.com:1443;database=DB_NAME_PLACEHOLDER;user=sqladmin;password={sqlpassword};encrypt=true;trustServerCertificate=true;loginTimeout=30;hostNameInCertificate=mssql.mycompany.com",
  "sql_connection_string_template_odbc": "SERVER=mssql.mycompany.com,1443;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};UID=sqladmin;PWD={sqlpassword};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;hostNameInCertificate=mssql.mycompany.com",
  "sql_connection_string_template_sqlalchemy_pyodbc": "mssql+pyodbc://sqladmin:sqlpassword@mssql.mycompany.com:1443/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server",
  "postgresql_connection_string_template_sqlalchemy_pyodbc": "postgresql+psycopg2://sa:&lt;password&gt;@135.235.240.165:5432/DB_NAME_PLACEHOLDER"
}
```