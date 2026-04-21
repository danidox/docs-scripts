---
title: "About licensing"
visible: true
slug: "about-licensing"
---

:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

This chapter provides information regarding the UiPath licensing. While the majority of the details and procedures outlined in this chapter apply to both **Unified Pricing** and **Flex**, be aware that certain sections address aspects specific to one commercial licensing plan or the other. In such cases, the relevant commercial licensing plan name is clearly indicated in the section heading and often reiterated at the beginning of the content for clarity.

The following information is aimed at helping you understand how UiPath® licenses its software. You can think of a license as an agreement between you and UiPath, authorizing you to use a certain set of functional capabilities in UiPath software.

Our commercial offering provides a flexible variety of licensing SKUs for how to deploy and use UiPath software. For the current list of available SKUs, refer to the [UiPath Licensing](https://licensing.uipath.com/) page.

## Commercial licensing plans

UiPath offers two commercial licensing plans: Unified Pricing and Flex. Each of these commercial plans consists of distinct platform, robot, and user licenses, and consumption units.

To learn more about our commercial licensing plans, refer to the following:

* [Unified Pricing: Licensing plan framework](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/unified-pricing-licensing-plan-framework#unified-pricing%3A-licensing-plan-framework)

For product-specific details on each of the two commercial licensing plans, refer to the corresponding user guide. For instance, to find information on Orchestrator licensing, refer to the Orchestrator user guide.

## License types

### User licenses

To learn more about user licenses, refer to the following:

* [User licensing](https://docs.uipath.com/overview-guide/docs/user-licensing) for general information
* The documentation of each product for details about a user license that is specific to that particular product

### Platform service licenses

To learn more about these types of licenses, refer to [Service licensing](https://docs.uipath.com/overview-guide/docs/service-licensing).

## Resource quotas

Automation Cloud enforces quotas on the following resources: local users, robot accounts, local groups, and external apps. This approach is necessary to maintain healthy use of our services and avoid potential misuse.
:::note
* Directory users directly linked to local users are counted in the quota.
* Standard directory users (not linked to local users) are not counted in the quota.
* Default local groups are not counted in the quota.
* Global client registrations are not counted in the quota.
:::

The specific quotas vary according to your licensing plan subscription, as follows:

* If you are on Unified Pricing, the following order is followed:
  1. **Enterprise**: Offers the largest quotas amongst all plans.
  2. **Standard**
  3. **Basic**
  4. **Community**
* If you are on Flex, the following order is followed:
  1. **Enterprise**: Offers the largest quotas amongst all plans.
  2. **Pro and Pro Trial**
  3. **Community and Free**

When the maximum limit is reached for a particular resource, the system throws the following error: “Quota reached, cannot create more objects.” In such cases, you have the following options:

* Upgrade your licensing plan to a plan that offers a higher quota.
* Upon request, UiPath can also revise the limitation specifically for your organization. To help with such scenarios, contact [Support](https://customerportal.uipath.com/support/add-case).