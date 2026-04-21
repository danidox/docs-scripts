---
title: "Application testing"
visible: true
slug: "application-testing-best-practices"
---

To ensure the efficiency of your application testing workflows, integrate the following concepts in the design process of your testing projects:

## 1. Build a scalable test automation framework

Use the following components when designing automated test cases in Studio:

* **Object Repository**: Centralize UI elements for easy reuse across test cases and projects.
* **Workflows**: Design modular workflows for common actions.
* **Test Cases**: Assemble workflows into structured, automated test cases, using [test case templates](https://docs.uipath.com/studio/standalone/latest/user-guide/test-automation-test-case-templates) and [execution templates](https://docs.uipath.com/studio/standalone/latest/user-guide/execution-templates). Group related test cases into folders for improved visibility and organization.

## 2. Explore Test Manager for traceability and coverage

Improve traceability and coverage of your testing projects using Test Manager:

* Begin by creating or importing requirements to link test cases to business objectives.
* Achieve end-to-end traceability by connecting test cases to requirements.
* Analyze test coverage and discover potential gaps using [Insights dashboards](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/reporting#reporting-with-insights).
* Synchronize test artifacts with popular ALM tools via [UiPath Test Manager Connect](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/uipath-test-manager-connect).

## 3. Advance your testing projects with AI features

Leverage the AI features of Autopilot to enhance your testing projects:

* Test Manager AI features: Help you to review requirements quality, generate missing test scenarios, and gather test insights.
* Studio AI features: Help you to refactor code, generate expressions, test data and fuzzy verifications, and coded/low code test cases.

For more information on the AI features offered by Autopilot, visit [About Autopilot in Test Manager](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/about-test-manager#about-autopilot).

## 4. Optimize UI testing selector strategy

Employ UiPath Test Cloud to improve UI selector testing:

* Use Object Repository instead of static selectors for UI elements.
* Avoid absolute selectors that break with UI changes. Use anchor-based selectors for dynamic UI elements.
* Enable the [Simulate Click](https://docs.uipath.com/activities/other/latest/ui-automation/ui-prr-001) and [Simulate Type](https://docs.uipath.com/activities/other/latest/ui-automation/ui-prr-002) Workflow Analyzer rules to speed up interactions in web or desktop apps.
* Implement retry mechanisms to handle intermittent UI delays.

## 5. Implement data-driven testing

Use the available test data capabilities:

* Streamline test data management with Orchestrator test data queues and Data Service entities.
* Generate test data using AI.
* Parametrize test inputs instead of using hard-coded values.

## 6. Integrate UiPath tests into CI/CD pipelines

Follow these recommendations for integrating tests into CI/CD pipelines:

* Schedule and run automated tests in Test Manager.
* Trigger tests automatically using DevOps tools.
* Reduce test cycle time with parallel execution across multiple robots.
* Use API-based testing to minimize UI dependency.

## 7. Handle exception management and reporting

To handle the exceptions from test executions effectively:

* Log detailed execution results, including screenshots and error messages, in Test Manager.
* Use Try-Catch blocks for consistent error handling.
* Leverage Orchestrator logs for thorough debugging.
* Dispatch test execution reports via email.

## 8. Optimize test execution performance

Follow these methods for improved performance:

* Run tests in unattended mode for faster results.
* Replace static delays with dynamic wait mechanisms.
* Minimize UI interactions by using API and database validations.

## 9. Regularly maintain and update automated tests

Keep your automated tests updated:

* Update selectors periodically to match application changes.
* Remove obsolete test cases.
* Refactor workflows for improved efficiency.
* Use version control to track changes and encourage collaboration.