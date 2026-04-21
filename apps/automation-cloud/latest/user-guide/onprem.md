---
title: "Connecting Apps to an on-premises Orchestrator instance"
visible: true
slug: "onprem"
---

UiPath Apps cloud does provide means to connect to an on-premise deployed version of UiPath Orchestrator (19.10 and later) to help leverage the power of RPA to help drive rich app experiences.

For more information on data flow between **Apps** and **Orchestrator**, see [Hybrid data flow diagram](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/data-flow-between-uipath-apps-and-orchestrator#data-flow-between-uipath-apps-and-orchestrator).

## Integration Workflow

![docs image](/images/apps/apps-docs-image-92980-302659ab.webp)

1. All connections to Orchestrator are made from a single place, the Apps Service application.
2. All calls to Orchestrator are authenticated calls in line with the security model exposed by Orchestrator. Please see the section about [Authenticating](https://docs.uipath.com/orchestrator/automation-cloud/latest/api-guide/authenticating).
3. Credential obtained from the user to talk to Orchestrator is used for all communication with Orchestrator both at design time when authoring the app as well as runtime when executing the app. The identity of the user who is designing or running the app itself has no bearing here.
   * After initially obtaining the credential from the app designer, the credential is stored in the Apps backend with encryption at rest to enable seamless and uninterrupted design and runtime experience for all users of the app
4. Apps service sets up a secure webhook callback over HTTPS on process lifecycle events to help detect when processes start, stop, error out, etc. This follows the best practices mentioned in the [About Webhooks](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-webhooks) page.
5. No process-related data is stored on the Apps backend. The only information that is persisted is metadata around the identity of the process/es that are being used by a specific app.
6. Apps can invoke both attended and unattended Orchestrator processes. An app designer can choose to run a process through the connected Orchestrator or directly on the local computer on which the app is running using UiPath [RobotJS](https://docs.uipath.com/robot/standalone/2024.10/user-guide/about-the-robot-javascript-sdk).
* In the local robot scenario, process execution is invoked from the browser to the locally running robot and communication does not leave computer boundaries.
* In the process execution via Orchestrator option, the complete lifecycle of the process is managed by Orchestrator, and UiPath Apps plays no role in the same other than listening to process lifecycle events using the webhook callback.

## Outbound IP ranges

The Apps service uses the outgoing IP ranges listed below for all external communications. The following table shows the available outbound IP ranges for each region.

The current outbound IP ranges will be deprecated on January 26, 2026. To avoid disruption, make sure to add the outbound IP ranges listed under the **Upcoming outbound IP ranges** column before this date.
:::important
If the upcoming outbound IP ranges are not allowed by January 26, 2026, you will be unable to use this service. Attempts to use this service may result in errors.
:::

| Region | Current outbound IP ranges | Upcoming outbound IP ranges |
| --- | --- | --- |
| Europe | ``` 20.93.15.208 ``` | ``` 94.245.89.4/30 94.245.93.8/30 ``` |
| Europe (Secondary) | ``` 20.13.60.212 ``` | ``` 20.67.88.64/30 20.67.88.112/30 ``` |
| Europe - Community | ``` 4.207.32.162 ``` | ``` 94.245.93.132/30 94.245.93.148/30 ``` |
| Europe - Community (Secondary) | ``` 20.13.110.150 ``` | ``` 20.67.88.116/30 20.67.88.132/30 ``` |
| US | ``` 20.121.170.55 ``` | ``` 104.211.63.160/30 104.211.58.236/30 ``` |
| US (Secondary) | ``` 20.72.203.238 ``` | ``` 13.66.167.4/30 13.66.163.204/30 ``` |
| Canada | ``` 20.200.104.214 ``` | ``` 20.151.112.252/30 20.151.113.120/30 ``` |
| Canada (Secondary) | ``` 20.220.98.56 ``` | ``` 40.86.219.188/30 40.86.224.148/30 ``` |
| Singapore | ``` 20.44.206.197 ``` | ``` 104.215.184.68/30 104.215.185.96/30 ``` |
| Japan | ``` 20.89.117.202 ``` | ``` 20.89.104.152/30 20.89.104.200/30 ``` |
| Japan (Secondary) | ``` 104.46.238.159 ``` | ``` 40.74.64.240/30 40.74.65.80/30 ``` |
| Australia | ``` 20.167.34.255 ``` | ``` 13.75.193.84/30 13.75.193.112/30 ``` |
| Australia (Secondary) | ``` 20.11.199.185 ``` | ``` 13.77.46.56/30 13.77.40.228/30 ``` |
| India | ``` 4.224.9.5 ``` | ``` 40.80.89.64/30 40.80.89.136/30 ``` |
| India (Secondary) | ``` 13.71.90.136 ``` | ``` 104.211.218.152/30 104.211.222.120/30 ``` |
| UK | ``` 172.165.145.81 ``` | ``` 51.104.16.124/30 51.104.16.168/30 ``` |
| UK (Secondary) | ``` 51.141.6.153 ``` | ``` 51.140.205.20/30 51.140.205.248/30 ``` |
| GXP US (Secondary) | ``` 52.143.81.192 ``` | ``` 13.66.166.60/30 13.66.160.164/30 ``` |
| GXP US | ``` 20.246.192.220 ``` | ``` 104.211.56.184/30 40.114.71.160/30 ``` |

Traffic from this IPs needs to be allowed through the Organization DMZ firewall and any other intermediate firewalls including the firewall on the computer/s in which Orchestrator application is hosted.

* The associated port on which Orchestrator application is hosted needs to be exposed through the DMZ on all relevant firewalls (see the previous point).
* An Orchestrator user who has read and execute access to relevant processes whose credential will be used from UiPath Apps to talk to Orchestrator.
* If using local robot process execution through RobotJS, please ensure RobotJS is properly configured using instructions provided at [RobotJS](https://docs.uipath.com/robot/standalone/2024.10/user-guide/about-the-robot-javascript-sdk).

### Best practices

* Ensure that the On-Premise hosted Orchestrator is only accessible through a secure HTTPS channel.
* Create a low privilege user in Orchestrator that only has read and execute access to just the desired processes/folders and use that for the integration.

### CORS policy requirements for Storage Buckets

When using storage buckets from an on-premises or hybrid Orchestrator, add `https://cloud.uipath.com` to the `acceptedRootURLs` list in the [UiPath.Orchestrator.dll.config file](https://docs.uipath.com/installation-and-upgrade/docs/uipath-orchestrator-dll-config).

:::note
* If your Orchestrator instance is hosted in Automation Cloud, this configuration is
already in place.
* For external buckets, configure the allowed origins as described in the [CORS and CSP configuration](https://docs.uipath.com/orchestrator/v0/docs/cors-csp-configuration) guide.”
:::

UiPath Apps uploads and downloads files using the SAS URL generated by Orchestrator when interacting with storage buckets hosted in an on-premises environment. End users must have the appropriate permissions granted through that SAS URL to perform both upload and download operations.

:::important
All access control is defined and enforced by the underlying storage account configuration. UiPath does not manage or override these permissions.
:::

If users encounter errors when uploading or downloading files through UiPath Apps, the **storage account’s SAS policies or access restrictions** should be reviewed and updated by the storage owner to ensure the required level of access.

## Validating the Configuration

**Apps Designer says unable to connect to Orchestrator**
* Are the UiPath Apps outgoing IPs allowlisted?
* Is the Orchestrator port allowlisted?
* Is the correct URL with the port being used in the Orchestrator URL field?
* Has it been confirmed that the credentials provided when connecting to Orchestrator are correct?
* Do the credentials provided have the permissions to list/run folders and processes?

**Apps Designer shows no processes or wrong processes**
* Does the user whose credential was configured during App Design have read access to the folder in which the desired processes reside?

**When previewing an App and/or running an app and invoking a process, there is an error**
* Are the UiPath Apps outgoing IPs still allowlisted?
* Is the Orchestrator port still allowlisted?
* Does the user whose credential was configured during App Design still exist?
* Does the user whose credential was configured during App Design still have the same credentials?
* Does the process and the exact version that is executed still exist in Orchestrator in the same folder or anything has changed?
* If running processes locally, is RobotJS configured correctly, and is able to properly handshake with the robot?
* Has the process being executed on the local robot been downloaded to the robot prior to executing the same through the app?
* Does the user whose credential was configured during App Design have to execute access to the process?

## Unsupported Scenarios

Connecting UiPath Apps with an on-premise Orchestrator with **custom self-signed certificates** is not supported.

A secure connection (HTTPS) between UiPath Apps and Orchestrator is needed for mutual authentication to work properly. To achieve this secure connection, both parties must trust each other's certificates. For this to happen, either of the following conditions must be satisfied:

1. Both parties should have certificates obtained from standard Certificate Authorities (CA), such as Google, VeriSign, or others. UiPath cloud products already have this, so nothing needs to be done on this part. This needs to be done for on-premise product deployments.
2. If the on-premise deployment uses an internal or self-signed certificate, the connection will not work. For that, the certificate has to be added to the trusted root of the other party. Note that this cannot be done for UiPath cloud products, as no custom certificates can be added to the UiPath cloud systems.