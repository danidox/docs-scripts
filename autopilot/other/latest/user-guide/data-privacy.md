---
title: "Data privacy"
visible: true
slug: "data-privacy"
---

UiPath values data privacy and aims towards protecting all users' right to privacy when sharing data while using the UiPath Autopilot functionality.

UiPath Autopilot ensures the security and privacy of data through a comprehensive approach that includes compliance with global data protection regulations like GDPR, ensuring legal standards in data handling are met. The platform employs data encryption for both data in transit and at rest, safeguarding against unauthorized access. Additionally, robust access control mechanisms, such as role-based access control (RBAC), restrict system and data access to authorized users only, enhancing data security.

The platform also adheres to secure development practices, which minimizes the risk of software vulnerabilities. Regular security audits and updates help in keeping the platform resilient against emerging threats. Furthermore, strong user authentication and authorization processes are in place to prevent unauthorized system access. In the event of a security breach, UiPath Autopilot is equipped with an incident response plan to effectively mitigate potential impacts on data security and privacy.

## Processed data

We process requests containing information relating to your user query and the context in which the query is made. The context might involve workflow definitions, available User Interface (UI) objects, and any possible activities or code definitions based on your interactions with this functionality.

## Processing operations

The primary objective of our data processing is to ground our model in the context of your unique user experience. This approach helps us better understand your particular needs and enables us to build output that matches your expectations in a given context.

## Data centers

UiPath hosts data in several data centers, geographically distributed to accomodate your organization tenant region:

* **North America**: For users within the United States and Canada, data processing is managed in UiPath data centers located in North America.
* **Europe**: For users in European countries, including in the United Kingdom, data processing is managed in UiPath data centers located in Europe.
* **Japan**: For users in Japan and other Asia, Pacific, and Japan (APJ) regions not specifically mentioned, data processing is managed in UiPath data centers located in Japan.


:::note
UiPath only retains telemetry data in the mentioned data centers.
:::

## Rerouting Azure OpenAI endpoints

UiPath uses Azure OpenAI Services to power AI features across its Autopilot services. For tenants in regions without a UiPath-hosted data center, Autopilot transits this data through various server locations around the world to allow AI-powered features. These routes depend on the Autopilot service used:

* **Autopilot for developers**
  + **Studio Web:** currently uses an Azure endpoint located in the European Union to provide these features in Canada, the United Kingdom, Singapore, and India. No data is saved outside of the respective region.
  + **Apps:** currently uses an Azure endpoint located in the European Union to provide these features in Australia, India, and Singapore. No data is saved outside of the respective region.
* **Autopilot for testers**
  + **Test Manager:** uses region-specific Azure endpoints for the United States, the European Union, the United Kingdom, Japan, India, and Australia. The Azure endpoint located in Japan provides these feature in Singapore. No data is saved outside of the respective regions.

This routing ensures AI-powered features are available in regions without local UiPath data centers while maintaining [data residency compliance](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/data-residency-cloud#global-cloud-regions).

## Autopilot for Everyone chat data

To learn how Autopilot for Everyone handles data received through chat interaction, read [Chat history storage management](https://docs.uipath.com/autopilot/other/latest/everyone-user-guide/chat-history-storage-management).

## References

[UiPath Data Residency](https://docs.uipath.com/overview-guide/docs/data-residency-cloud) policy is the place where you can find all regions where UiPath Automation Cloud™ and our cloud services can be hosted, depending on your licensing plan and region preference.

The [UiPath Privacy Principles for Sub-processors](https://www.uipath.com/legal/trust-and-security/privacy#content-4) set out the general rules for processing of personal data in accordance with UiPath's instructions, transfers and security of personal data, as well as for cooperation between UiPath and [sub-processors](https://www.uipath.com/hubfs/legalspot/UiPath_Subprocessors.pdf).

Security is very important to us. [UiPath Security](https://www.uipath.com/legal/trust-and-security/security) information is available for you to check at any time.

For more information about how UiPath handles and processes personal data, we encourage you to read our [Privacy Policy](https://www.uipath.com/legal/privacy-policy).