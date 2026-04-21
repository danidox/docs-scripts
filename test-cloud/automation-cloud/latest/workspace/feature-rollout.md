---
title: "Feature rollout"
visible: true
slug: "feature-rollout"
---

New products and features are introduced progressively across these cloud offerings. In general, new functionality becomes available first in Test Cloud, and is subsequently made available in Test Cloud Public Sector and Test Cloud Dedicated, subject to compliance, infrastructure, and release readiness requirements. Availability may therefore vary depending on the cloud offering you use.

![docs image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/644028)

## Feature rollout Test Cloud

### When do updates become available

The updates that we announce in the Automation Cloud<sup>TM</sup> release notes become available progressively, depending on the following:

* your licensing plan
* your organization and tenant [region](https://docs.uipath.com/overview-guide/docs/data-residency-cloud)

Therefore, the updates reach different users at different times.

The date when a change is first announced in the release notes is the date when it first becomes available. If you do not notice the change yet, you can expect to notice it soon.

**Community release**: Changes are first made available to Community users. This is when we publish the release notes.

**Enterprise release**: If you are an Enterprise user, deployment is typically made available within a one hour to 14-day window post Community deployment. In certain cases, some features may require additional time before becoming available in Enterprise. [Canary tenants](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-tenants#using-a-canary-tenant), utilized for testing, typically receive updates three days after the announcement. The precise timeframe for when these changes become accessible to you in your selected hosting region varies, depending on when the changes have been successfully deployed to all regions.

We do not announce Enterprise releases or releases to the different regions separately.

The following table serves as an example of when a feature becomes available to Community users, as well as Enterprise users:

| Release note date | Community release date | Enterprise release date |
| --- | --- | --- |
| July 14, 2025 | July 14, 2025 | starting with July 14, 2025 |

#### Enterprise-only changes

If a change is exclusive to the Enterprise plan, we flag it using the Enterprise label (![Enterprise label](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555)) in the release notes. For such changes, the first release goes out to Enterprise and Enterprise trial users directly. You can expect to notice these changes as early as the release note date, but it can take a few days until they become available in your region.

The following table serves as an example of when a feature becomes available to Enterprise users only:

| Release note date | Community release date | Enterprise release date |
| --- | --- | --- |
| 14 July 2025 | N/A | starting with 14 July 2025 |

#### Delayed update organizations

  !['Enterprise label' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555) This feature is available for Enterprise customers with an **Advanced Tier** license.

[Contact the UiPath Sales team](https://www.uipath.com/company/contact-us) for more information on how to become an Advanced Tier customer.

If your organization is hosted in a delayed update region, you receive updates for Automation Cloud and its services at least two weeks after they reach other enterprise organizations, which is subject to the previously described rules.

The exact number of days it takes for the changes to become available in your delayed update organization, in your chosen hosting region, can be slightly higher than 14 days, depending on when we finish deploying the changes to all the regions.

You can use a typical enterprise organization as your pre-production environment to test updates, and use your delayed update organization as your production environment. After the updates are available in your enterprise organization, you can expect the changes to appear in your delayed update organization roughly two weeks later.

#### **Regions**

The delayed update feature is available in the **United States** and the **European Union** hosting regions.

#### **Services that benefit from delayed updates**

UiPath services may support delayed updates in the United States or the European Union. To see which services support delayed updates in these regions, refer to the [Data residency](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/data-residency-cloud#global-cloud-regions) page, specifically the **Global cloud regions** section.

### Status page

To stay up to date with uptime for all UiPath® services, planned maintenance periods, or incidents, refer to the [Status page](https://status.uipath.com/).

## Feature rollout Test Cloud Public Sector

Our approach to introducing new features or updates in Test Cloud Public Sector is designed to ensure a seamless and effective transition for you.

### What to expect

1. **Release notes**: After we finalize the development and testing of new features or updates, we announce them through release notes. These release notes are accessible at [https://docs.uipath.com/](https://docs.uipath.com/).
2. **Transparency**: Our release notes are designed to be transparent and informative. They detail what the new feature entails, and any changes it brings to existing functionality.
3. **Timing**: Users should expect to view new features or updates shortly after the release notes are made available. The specific timing may vary based on the complexity of the feature or update, but we aim to make them accessible as soon as possible following the announcement.

To stay up to date with uptime for all UiPath® services, planned maintenance periods, or incidents, refer to the [Status page](https://status.uipath.us/).

## Feature rollout Test Cloud Dedicated

One of the main advantages of Test Cloud Dedicated is the ability to control upgrades. It satisfies specific requirements for updating your vital UiPath applications, giving you leverage over key aspects such as the following:

* Scheduling when your platform and UiPath services can undergo updates, preventing any business disruption. For instance, you can avoid updates during peak seasons such as end-of-the-year holidays.
* Determining the schedule for deploying new features to your platform. This enables you to plan the validation of automations and new features in both testing and production environments.

### Release process

This page explains how updates are delivered, controlled, and communicated across environments in Automation Cloud Dedicated, using a deployment model based on rings.

#### Release overview

Automation Cloud Dedicated releases happen every two weeks. Each sprint delivers a payload that includes: new features and enhancements, security patches, infrastructure, configuration updates, and bug fixes.

All updates follow a ring-based rollout strategy governed by a service deployment plan.

#### Rollout schedule and environments

The deployment lifecycle of Automation Cloud Dedicated involves the following components:

* Release cadence – Releases follow a once every two weeks schedule. Each sprint includes cumulative updates, such as new features, improvements, security patches, and bug fixes.
* Ring-based rollout – The releases progress through multiple environments in sequence, with Sandbox being the first environment. The following environments depend on you preferred schedule and deployment architecture. The Sandbox environment is a shared instance that you can use for validating updates in advance. This is when release notes are published.
  :::note
  The rollout flow excludes blackout windows and freeze periods.
  :::

#### Types of releases

Automation Cloud Dedicated provides you with two types of updates:

* Standard release: Regular deployment of product, infrastructure, and configuration updates every two weeks.
* Hotfix releases: Emergency fix for security vulnerabilities or high-impact bugs.

#### Hotfixes and emergency releases

For high-priority fixes, the deployment lifecycle follows these exceptions:

* Releases are fast tracked across all rings.
* Ring delays, maintenance windows, and blackout windows may be bypassed based on urgency.
:::note
Only regressions from previous Automation Cloud Dedicated behavior are eligible for hotfixes.
:::

#### Upgrade controls

Automation Cloud Dedicated provides flexibility over when updates are deployed. You can configure your production environment using the following upgrade control types:

* Delayed release: Postpone updates for up to 30 days.
* Blackout window: Prevent deployments during a fixed period. The rules of a blackout period are the following:
  + Can last a maximum of 30 consecutive days.
  + Must be followed by a 10-day open period before another blackout can be applied.
  + Must be submitted at least five business days in advance.
  + Cannot block deployments schedules within the next 48 hours.For example, you can extend a blackout window that ends in less than two days, but you can adjust a blackout window that ends in more than five days.
* Maintenance window: Ensure upgrades occur outside of business hours. The maintenance window is typically scheduled between 3PM and 9PM EST. A 6-hour continuous window is recommended for upgrades across all production environments.
:::note
The Sandbox environment is excluded from blackout and maintenance periods.
:::

#### Communications and user responsibility

To ensure you are aware of how releases are rolling out to your Automation Cloud Dedicated organization, you must check the following resources:

* Release notes: Published on the same day the Sandbox environment is upgraded.
* Status page notifications: Used for any downtime, with at least seven days notice.

As an Automation Cloud Dedicated user, you are expected to do the following:

1. Regularly check the release notes and status page updates.
2. Review the release notes once published.
3. Validate the changes in Sandbox and any other approved environments.
4. Open a support ticket to pause the production release if you discover regressions or performance issues.

#### Rollout example

For example, if a sprint release is deployed to Sandbox on July 7, and the production delay is 30 days, the timeline would be as follows:

1. Sandbox upgrade performed on July 7.
2. Release notes published on July 7.
3. Production upgrade performed on August 9.

### About upgrade controls

We provide two types of controls:

1. Delayed release: This allows you to postpone updates for up to 30 days.
2. Blackout window: We ensure no updates take place for a specific period with a blackout window of up to 30 days.

To ensure Test Cloud organizations stay updated, we have placed the following restrictions:

* Blackout windows can only last for a continuous period of 30 days. This is to accommodate a 30-day freeze period for your end of the year needs.
* Each blackout window must be followed by a break of at least 10 days, which ensures that UiPath has ample time to roll out updates after a prolonged blackout window.
* Any modifications to the blackout window must be submitted via a ticket 5 business days ahead of the intended change.
* You are not allowed to implement any changes that would result in time being blocked within the next 48 hours, which was previously unblocked.

The following section describes a few examples to help you understand these guidelines better:

* If you are in a blackout window that concludes in 5 days, you can either extend or reduce this window since it will not block any new timeframe.
* If the blackout window finishes in 1 day, it cannot be extended because the following day would then be blocked.
* If there is no current blackout window, and you wish to establish one that begins in 1 day, such a window cannot be created.

### Managing the upgrade controls

To configure both upgrade controls available in Test Cloud, you must reach out to our [support team](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) and raise support tickets.