---
title: "Data residency Test Cloud"
visible: true
slug: "test-cloud"
---

## Organization and tenant services data

Test Cloud organization data includes critical information such as user identity, metadata, and license details. Each organization is assigned a unique hosting region based on licensing plans and regions selected by admins.

Each cloud organization has a single region, and enterprise customers have multi-regionality options for their organizations' tenants.

### Data residency for cloud organizations

* **Free**: Data for cloud organizations downgraded to a Free plan is stored in community data centers in the European Union.
* **Application Testing Standard Trial**: Customers on **Application Testing Standard Trial** plans inherit the organization region. If your organization was created using a non-commercial Free plan, the data is hosted in the European Union. If you are creating an organization on the Application Testing Standard Trial plan for the first time, you can choose the region where your organization data resides.
* **Application Testing Standard**: Customers on **Application Testing Standard** plans inherit the organization region.
* **Application Testing Enterprise**: Customers on **Application Testing Enterprise** plans inherit the organization region. If you upgraded from a previous plan, the organization will inherit the previous organization's region. If you are interested in upgrading your plan, [contact a sales expert](https://www.uipath.com/company/contact-us).

### Data residency for cloud tenants

* **Free**: A single cloud tenant is provisioned by default for a cloud organization created using Free plan. Data for this tenant is stored in community scale unit in the European Union.
* **Application Testing Standard Trial**: Customers on **Application Testing Standard Trial** plans will inherit the tenant(s) region(s), as follows:
  + If your organization was created using **Free** plan, tenant data is hosted in the European Union.
  + For newly created tenants, the data is stored in the same region as the cloud organization region selected during sign up.
* **Application Testing Standard**: Customers on **Application Testing Standard** plans will inherit the tenant(s) region(s), as follows:
  + If your organization was created using **Free** plan, tenant data is hosted in the European Union.
  + For newly created tenants, the data is stored in the same region as the cloud organization region selected during sign up.
* **Application Testing Enterprise**: Customers on Enterprise plans will inherit the tenant(s) region(s), as follows:
  + If your organization was created using a **Free** plan, tenant data is hosted in the European Union.
  + For newly created tenants, the data is stored in the region chosen by administrators during creation.

Establishing the region for newly created cloud tenants has no effect on already-created cloud tenants in your organization. Customers using Enterprise plans can request changes to regions elections they made in the past for their cloud organization or their tenants. You can [contact support](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) to request to schedule the data move to a different region.
:::note
In cases where Enterprise customers do not explicitly make region elections for their organizations or default tenants, we proactively move the customer data (from the organization and tenant services) to the corresponding scale units, to ensure the cloud services are deployed in optimal regions worldwide. We use predefined rules to determine region selection. However, in certain situations, our rules might default services to Enterprise scale units in the European Union, if a more suitable location was not identified.
:::

#### Resources

* Licensing plans
* [Managing organization settings](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#managing-organization-settings)
* [Managing tenant settings](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenants#managing-tenants)

The following table describes data residency for Test Cloud organizations and tenants, according to every licensing plan:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-B3230E2B-8DC4-42BA-8832-A36C3A7195F3__TABLE_JS5_42X_HGC" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Data residency for Test
                                    Cloud organization and tenants
   </th>
   <th>
    Free
   </th>
   <th>
    Application Testing Standard Trial
   </th>
   <th>
    Application Testing Standard
   </th>
   <th>
    Application Testing
                                    Enterprise
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d138520e229">
    <strong>
     Cloud organization
                                       regions
    </strong>
   </td>
   <td headers="d138520e232">
    European Union
                                    only
   </td>
   <td headers="d138520e235">
    Inherited
   </td>
   <td headers="d138520e238">
    Inherited
   </td>
   <td headers="d138520e241">
    <p>
     Inherited (can be changed)
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d138520e229">
    <strong>
     Tenant
                                       regions
    </strong>
   </td>
   <td headers="d138520e232">
    European Union
                                    only
   </td>
   <td headers="d138520e235">
    One region inherited from the organization
   </td>
   <td headers="d138520e238">
    One region inherited from the organization
   </td>
   <td headers="d138520e241">
    <p>
     Inherited for Default Tenant (can be changed)
    </p>
    Note:
    <p>
     Multiple regions are available for new tenants.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d138520e229">
    <strong>
     Max. number of
                                       tenants
    </strong>
   </td>
   <td headers="d138520e232">
    1
   </td>
   <td headers="d138520e235">
    Unlimited
   </td>
   <td headers="d138520e238">
    Unlimited
   </td>
   <td headers="d138520e241">
    Unlimited
   </td>
  </tr>
 </tbody>
</table>
:::note
The **Free** plan is for non-commercial use only. If you want to test Test Cloud before buying a license, start with an **Application Testing Standard Trial** plan.
:::

## Global cloud regions

UiPath provisions and processes cloud data in the region where each service is hosted. This page explains the following:

* Where each service is available.
* How UiPath handles data residency.
* What exceptions apply to data residency.

### Service provisioning and data handling

Before you check the data residency of each service, keep the following in mind:

* Products are provisioned either at the tenant level or the organizational level.
* When a product is available in a region, UiPath stores and processes data mainly in that region.
  :::note
  Some services might process data beyond their designated storage region. However, no data is stored outside the services' respective region.
  :::
* If a product uses AI-powered features, data may be temporarily routed to a nearby region where a specific model is available. UiPath does not store data in the routed region. Product sections document this behavior in detail. For details on the regional availability and data residency of the LLM models used by UiPath services, check [AI features and model routing](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/ai-features-and-model-routing#ai-features-and-model-routing).

**Legend**:
* ✅: Available
* ❌: Not available

| Service | Provisioning type | European Union | United States | Japan | Canada | Australia | Singapore | United Kingdom | India | Switzerland | United Arab Emirates | United States  (delayed region) | European Union  (delayed region) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Action Center**  <sup>(Actions and Processes)</sup> | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Agents** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **AI Computer Vision** | Tenant level | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Routed to European Union | ✅ | ❌ | ❌ |
| [**AI Trust Layer**](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-ai-trust-layer#about-ai-trust-layer) (including **LLM gateway**, and **LLM observability**) | Organization level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Apps** | Organization level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| **Assistant Web** | Organization level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Routed to European Union | ✅ | ✅ | ✅ |
| **Cloud portal** | N/A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Automation Ops** | Organization level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Autopilot for Testers** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Autopilot for Developers** | Tenant level | ✅ | ✅ | ✅ | Routed to United States | Routed to European Union | Routed to European Union | Routed to European Union | Routed to European Union | Routed to European Union | ✅ | ✅ | ❌ |
| **Autopilot Chat** | Tenant level | ✅ | ✅ | ✅ | Routed to United States | Routed to European Union | Routed to European Union | Routed to European Union | Routed to European Union | ❌ | ❌ | ✅ | ❌ |
| **Autopilot for Everyone** | Tenant level | ✅ | ✅ | ✅ | Routed to United States | Routed to European Union | Routed to European Union | Routed to European Union | Routed to European Union | ✅ | ✅ | ✅ | ❌ |
| **Context Grounding** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| **Data Fabric** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Routed to European Union | ✅ | ✅ | ❌ |
| **GenAI Activities** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Healing Agent** | Tenant level | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Insights** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅<sup>1</sup> | ✅<sup>2</sup> | ✅ | ✅ |
| **Integration Service** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Maestro** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Orchestrator** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[ACR - VM](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/automation-cloud-robots-vm)** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[ACR - Serverless](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/automation-cloud-robots-serverless)** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **ScreenPlay** | Tenant level | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Solutions** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Studio Web** | Organization level | ✅ | ✅ | ✅ | ![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/359336) | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| **Task Mining** | Tenant level | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Test Manager** | Tenant level | ✅(+ Performance Testing in Test Cloud only) | ✅(+ Performance Testing in Test Cloud only) | ✅(+ Performance Testing in Test Cloud only) | ✅ | ✅(+ Performance Testing in Test Cloud only) | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

<sup>1</sup> Dashboard definitions (dashboard name, widgets, alerts, schedules, and other dashboard-related metadata) are hosted in Germany.

<sup>2</sup> Dashboard definitions (dashboard name, widgets, alerts, schedules, and other dashboard-related metadata) are hosted in India.

### Platform considerations

The cloud portal includes the home page, all pages under **Admin**, and the **Resource center** (Help) page. For a list of all services handled by an organization administrator, refer to [Administration services and capabilities](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#administration-services-and-capabilities).

### AI Computer Vision considerations

Keep the following in mind when checking data residency for AI Computer Vision:

* Design-time data is centralized in the European Union and in the United States of America, no matter the region of origin.
* The service is available worldwide and it can be accessed from any location around the world. For more details, check the [Public endpoints](https://docs.uipath.com/ai-computer-vision/automation-cloud/latest/user-guide/public-endpoints) page.
* In the case of a regional Azure failure, to ensure continued service operation for our customers, global AI Computer Vision traffic (using the `cv.uipath.com` endpoint) may be temporarily failed over/redirected to another Azure data center location. The redirection will happen in the same geography, if possible (for example, traffic usually served by the North Europe Azure data center will be redirected to West Europe, if possible, in case of a regional failure in North Europe). In case redirection in the same geography is not possible (examples include, but are not limited to: insufficient GPU availability in Azure or disasters affecting both the primary and secondary regions in a geography), traffic may be redirected to another geography. The redirection will happen for a limited time, until the regional failure has stopped and the service has stabilized.

### Document Understanding considerations

Keep the following in mind when checking data residency for Document Understanding:

* For the Switzerland and European Union (delayed) regions, Document Understanding supports only Modern Projects.

### Safe deployment practices

UiPath cloud services follow a regular two-week release cadence, in line with established safe and secure deployment practices. Releases are introduced progressively to ensure stability and allow customers to evaluate updates before broad availability.

#### Progressive rollout

Depending on the cloud offering and configuration, new releases may be introduced in phases:

* **Initial availability:** Updates may first become available to community users or environments, where applicable.
* **General availability:** Updates are subsequently rolled out to enterprise environments within a window that can range from one hour up to 14 days, depending on deployment configuration and operational requirements. For example, in environments with dedicated infrastructure, updates are typically introduced after initial validation in multi-tenant environments, before being made available to enterprise and dedicated customers.

#### Delayed update deployments

UiPath cloud offerings are available in cloud scale units in the United States and the European Union with delayed deployments. To ensure GxP regulatory compliance in life sciences, UiPath® offers Enterprise customers the option of a delayed update scale unit for their cloud setup. Typically, customers utilize a standard scale unit for testing (in any of the [standard cloud regions](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud#global-cloud-regions)), alongside a second organization on a delayed update scale unit for production. UiPath cloud offerings are available to customers in a delayed update scale unit accessible in the United States, and a second one in the European Union is available to enterprise customers.

Each cloud release reaches delayed update scale units at least 14 days after standard scale units, enabling customers to complete an evaluation before the update is released in the delayed scale unit.

Further details regarding delayed update scale units are available in the release note page for each year..