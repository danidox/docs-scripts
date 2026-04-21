---
title: "Migrate from Test Suite to Test Cloud"
visible: true
slug: "migrate-test-suite-to-test-cloud"
---

This section provides key considerations and high-level steps for migrating from Test Suite under the Flex pricing plan to Test Cloud under the Unified Pricing plan.

For more information on pricing, browse our [pricing plans](https://licensing.uipath.com/) or reach out to your point of contact.

## Benefits of migrating to Test Cloud

If you are unsure on whether to upgrade to Test Cloud, here are some of the key benefits and considerations:

* Test Cloud was designed with innovation as its primary focus. Thanks to this, Test Cloud is the next evolution of the capabilities offered by UiPath® Test Suite. Unlike UiPath® Test Suite, Test Cloud is a dedicated offering, much like Test Cloud, but focused solely on application testing. For reference, the capabilities offered by UiPath® Test Suite have always been part of our broader automation (RPA) offering in Auttomation Cloud, and have covered both RPA testing and application testing.
* All new application‑testing features will be released only in Test Cloud, no longer in UiPath® Test Suite, regardless of the delivery option. Continuing to use the capabilities offered by UiPath® Test Suite means missing out on future innovations for application testing.
* Test Cloud is licensed exclusively under our new [Unified Pricing plan](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/licensing-test-cloud#licensing). In contrast, the capabilities offered by UiPath® Test Suite remain available only under the legacy [Flex Pricing plan](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/flex-licensing-plan-framework). This means upgrading to Test Cloud ensures both technical and commercial alignment with the future of the UiPath platform.
* If your IT team is concerned about security reviews for Test Cloud, the good news is Test Cloud is not a new tool entering your organization. The application runs on the same secure infrastructure as Automation Cloud. Think of Test Cloud as a different user experience on top of the same secure foundation. In other words, there is no need for additional security reviews or approvals for Test Cloud.

## Kickstart the migration process

If you need help kickstarting your migration process, we have got you covered. Here is what you need to do first:

### Reach out to your points of contact

If you have a dedicated UiPath® Technical Account Manager (TAM), reach out to them first to plan and execute your migration. If no TAM is assigned to your account, our professional services team can step in to lead and execute the migration on your behalf.

Moreover, our support team can help clarify the steps and share a checklist of required activities and tools, although they do not perform the migration itself.

### Share initial information for your migration

When reaching out to us about your migration plans, make sure you have the following information ready. This will help us understand your context and quickly map your situation to the right migration approach:

* **Where is your current environment hosted?**: The delivery option you are using.
* **What are you currently using UiPath for?**: Whether it is application testing, RPA/automation testing, or both application testing and RPA/automation testing.
* **Where are these activities performed?**: Let us know whether application testing and RPA/automation testing are managed within the same [organization](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/managing-test-cloud-overview#organizations), or in separate organizations.
* **What activities are you planning to migrate?**: Indicate whether it is just application testing to Test Cloud or you also want to upgrade RPA/automation testing capabilities to the [Unified Pricing Plan](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/licensing-test-cloud#licensing).

## Planning and assessment

During this phase, your goal is to understand the current setup and plan the scope of migration.
:::tip
Some of the high-level steps listed below will ensure you properly kickstart the migration.
:::

* Align stakeholders, define objectives, and set success metrics.
* Gather details on current assets (packages, workflows, test cases).
* Clarify what is being migrated: application testing, RPA/automation testing, or both.
* Review user roles, access permissions, and governance needs.
* Develop a migration roadmap with tasks, owners, and timelines.
* Identify potential challenges and outline the migration strategy.

## UiPath Cloud readiness setup

This section highlights how to prepare the Test Cloud environment for migration:

* Set up and configure tenants and organizational structure.
* Configure access roles and user permissions as needed.
* Connect Test Manager to ALM tools, such as Jira or Azure DevOps.
* Enable Test Manager and confirm licensing availability.
* Mirror environments and folder structure from the current setup.
* Review license allocation and ensure provisioning is complete.

## Asset and package migration

Next, move reusable components and packages to Test Cloud:

* Inventory assets such as queues, credentials, and storage buckets.
* Identify deprecated or unused assets to exclude from migration.
* Export packages and assets from the source Orchestrator instance.
* Use migration tools or manual steps to import to Test Cloud.
* Validate asset values, types, and references after migration.
* Re-publish packages to target environment to ensure compatibility.

## Test case and artifact migration

This is the part where test cases and related orchestrator artifacts are migrated:

* Use the project [export](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/export-project) and [import](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/import-project) capabilities to transfer Test Manager projects.
* Reconfigure project settings after import (for example, integrations or roles).
* Reorganize test cases in the new structure if necessary.
* Ensure test cases are linked to ALM test objects, where applicable.
* Validate test sets and confirm they can execute successfully.
* Verify all required artifacts are available in the target environment.

## Environment setup and connectivity

These steps outline what needs to be done to ensure robots and test environments function as expected:

* Deploy unattended test robots in the new environment.
* Assign users and robots to the appropriate folders.
* Validate access to test machines via VM or on-premises resources.
* Confirm network connectivity and test credential access.
* Run sample workflows to validate robot execution behavior.

## Validation and test execution

Next, you need to validate the migration through test execution:

* Execute smoke tests to validate overall system behavior.
* Compare expected versus actual results for migrated tests.
* Address missing variables, assets, or broken dependencies.
* Re-map test data sources and environment references, if needed.
* Document test outcomes and validation evidence in reports.
* Share summary of results and confirm validation completion.

## CI/CD integration

If required, follow these steps to integrate test automation into your pipeline.

* Adjust CI/CD integrations (for example, Jenkins or Azure DevOps) appropriately.
* Configure pipelines to trigger test sets during deployment stages.
* Add test validation steps post-deployment in CI/CD pipelines.
* Ensure results sync back to ALM or defect tracking systems.
* Provide sample YAML or configuration files for reuse.

## Reporting and test insights

The steps below outline how to build dashboards and test visibility tools:

* Define reporting needs such as coverage, pass rate, and trends.
* Enable and configure UiPath Insights or other reporting solutions.
* Create dashboards to visualize testing activity and outcomes.
* Schedule automated report generation and delivery cadence.
* Share dashboards and insights with key stakeholders regularly.

## Handover and documentation

Lastly, finalize the migration and enable long-term ownership by finalizing documentation, completing the knowledge transfer, and handing over ownership.