---
title: "Automation testing"
visible: true
slug: "rpa-testing"
---

Automation or RPA testing requires validating automated processes to guarantee that they function correctly. Challenges in automation testing can involve having complex automation processes, ensuring that all parts of the automated process are covered and tested, using data variations, and integrating with other ALM (Application Lifecyle Management) tools. For each of these challenges, UiPath® platform can help you manage these challenges by offering you a powerful IDE where you can design your automation tests, a feature that verifies how much of your process has been covered and tested, the ability to perform data-driven testing, using files, auto-generated data, entities, or queues, and allows you to integrate with a multitude of ALM tools.

## Creating automation tests

The capabilities with which you can automate reliable and scalable automation tests are the following:

* How to make your test more powerful using data-driven testing. Visit [Data-driven testing](https://docs.uipath.com/studio/standalone/2023.4/user-guide/data-driven-testing) to read about how you can perform data-driven testing.
* How to enhance testing efficiency by creating mocks of your test cases. Visit [Mock testing](https://docs.uipath.com/studio/standalone/2023.10/user-guide/mock-testing) to read about how you can perform mock testing.
* How to reduce the risk of undetected errors using automation activity coverage. Visit [Activity coverage](https://docs.uipath.com/studio/standalone/2023.4/user-guide/rpa-testing-activity-coverage) and [Descriptor coverage](https://docs.uipath.com/studio/standalone/2023.4/user-guide/descriptor-coverage) to read about how you can ensure that your test cases are covered and lack redundancies.
* How to track and asses the performance of each module of your test, using profile execution.Visit [Profile Execution](https://docs.uipath.com/studio/standalone/2023.4/user-guide/profile-execution) to read about how you can fix performance issues within your test cases.

## Executing automation tests

The following video shows you how to publish the test cases that you created within Studio, in the previous tutorial, to Orchestrator, and the options you have to execute them. After you finish designing your test cases, proceed as follows:

1. Publish the test cases to Orchestrator as NuGet packages
2. Create a test set based on the NuGet package
3. Select the test cases that you want to be part of this test set.
4. You can execute your test sets in one of the following ways:
   * Trigger the execution from Test Manager. Visit [Executing tests](https://docs-dev.uipath.com/test-manager/automation-cloud/latest/user-guide/executing-tests) to read about how to run and manage your test executions within Test Manager.
   * Schedule the execution using a Test Schedule, that you can configure however you want. Visit [Scheduling test executions](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/scheduling-test-executions) to read about how you can schedule the execution of your tests.
   * Integrate with a CI/CD pipeline, such as Azure DevOps or Jenkins, and use them to execute your test sets and see the results. Visit [AzureDevOps](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/azure-devops-extension) and [Jenkins](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/azure-devops-extension) to read about how to integrate with these pipelines.

## Managing automation tests

After you design your tests with Studio, and then execute them using Orchestrator or CI/CD integrations, then you can go ahead and manage your testing portfolio using Test Manager. Test Manager offers full artifact traceability between the business process (represented by the test project), the requirements of the business process, the test cases you've created for these requirements, the test results of these test cases, as well as the defects.

Moreover, the video demonstrates how to analyze the information about the activity coverage that you have achieved as part of your test execution.