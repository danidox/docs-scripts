---
title: "EKS input.json example"
visible: true
slug: "eks-inputjson-example"
---

The following example shows `input.json` with all products enabled, mandatory and optional configuration parameters for Automation Suite on EKS. You can use this as reference and **make changes as per your environment requirements**.

Note that the minimum UiPath® product selection requires `platform` to be enabled. Make sure to replace all the username and passwords, including SQL connection strings.

```
{
  "kubernetes_distribution": "eks",
  "install_type": "online",
  "profile": "ha",
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
  "admin_password": "password123",
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
  "pod_identity" : {
    "enabled": true,
    "aks_managed_identity_client_id": <client-id>
  },
  "external_object_storage": {
    "enabled": true,
    "create_bucket": true,
    "storage_type": "azure",
    "use_managed_identity": false,
    "azure_fqdn_suffix": "core.windows.net",
    "account_key": "secretkey",
    "account_name": "as-storage-account",
    // storage type s3 specific config:
    "fqdn": null,
    "port": null,
    "region": "us-east-1",
    "access_key": "",
    "secret_key": "",
    "use_instance_profile": true,
    "bucket_name_prefix": "",
    "bucket_name_suffix": ""
  },
  "ingress": {
    "service_annotations": {
      "service.beta.kubernetes.io/aws-load-balancer-backend-protocol": "ssl",
      "service.beta.kubernetes.io/aws-load-balancer-eip-allocations": "<elastic_ip_id_0>,<elastic_ip_id_1>",
      "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type": "ip",
      "service.beta.kubernetes.io/aws-load-balancer-scheme": "internet-facing",
      "service.beta.kubernetes.io/aws-load-balancer-type": "nlb"
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
  "infra": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    }
  },
  "dataservice": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-dataservice"
    },
    "enabled": true
  },
  "platform": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true
  },
  "integrationservices": {
    "queue_prefix": "<queuePrefix>",
    "account_id":""
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    }
  },
  "studioweb": {
    "enabled": true,
  },
  "orchestrator": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true,
    "testautomation": {
      "enabled": true
    },
    "updateserver": {
      "enabled": true
    }
  },
  "processmining": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-processmining"
    },
    "enabled": true
  },
  "insights": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true,
    "enable_realtime_monitoring": false,
  },
  "task_mining": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-taskmining"
    },
    "enabled": true
  },
  "automation_hub": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true
  },
  "automation_ops": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true
  },
  "aicenter": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common",
      "port": 443,
      "fqdn": "s3.eu-west-1.amazonaws.com"
    },
    "enabled": true
  },
  "documentunderstanding": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true
  },
  "test_manager": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true
  },
  "action_center": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true
  },
  "apps": {
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true
  },
  "asrobots": {
    "packagecaching": true,
    "packagecachefolder": "/uipath_asrobots_package_cache",
    "external_object_storage": {
      "bucket_name": "s3-sfd-ci-aseks3997852-common"
    },
    "enabled": true
  },
  "storage_class": "ebs-sc",
  "storage_class_single_replica": "efs-sc",
  "proxy": {
    "enabled": true,
    "http_proxy": "http://<PROXY-SERVER-IP:<PROXY-PORT>",
    "https_proxy": "http://<PROXY-SERVER-IP:<PROXY-PORT>",
    "no_proxy": "paste list from Configuring the cluster section"
  },
  "sql_connection_string_template": "Server=tcp:mssql.mycompany.com,1443;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=sqladmin;Password='sqlpassword';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
  "sql_connection_string_template_jdbc": "jdbc:sqlserver://mssql.mycompany.com:1443;database=DB_NAME_PLACEHOLDER;user=sqladmin;password={sqlpassword};encrypt=true;trustServerCertificate=true;loginTimeout=30;hostNameInCertificate=mssql.mycompany.com",
  "sql_connection_string_template_odbc": "SERVER=mssql.mycompany.com,1443;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};UID=sqladmin;PWD={sqlpassword};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;hostNameInCertificate=mssql.mycompany.com",
  "sql_connection_string_template_sqlalchemy_pyodbc": "mssql+pyodbc://sqladmin:sqlpassword@mssql.mycompany.com:1443/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server",
  "postgresql_connection_string_template_sqlalchemy_pyodbc": "postgresql+psycopg2://sa:&lt;password&gt;@135.235.240.165:5432/DB_NAME_PLACEHOLDER",
  "telemetry_optout": false
}
```