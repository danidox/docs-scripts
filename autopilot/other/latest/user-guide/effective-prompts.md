---
title: "Writing effective prompts - generic instructions"
visible: true
slug: "effective-prompts"
---

Prompts serve as your communicating mechanism with Autopilot™, acting as the instructions that you use to obtain the desired output from Autopilot.

An effective and well-structured prompt can significantly improve Autopilot’s ability to produce useful results. Here are some tips on how to write effective prompts:

* Ensure that your instructions are clear and unambiguous.
* Create instructions that encourage action.
* Clearly state your expectations.
* Use active voice to enhance the clarity of your instructions.
* Define the desired format of the output.
* Incorporate relevant keywords to steer Autopilot’s response in a specific direction.
* Set boundaries and restrictions if necessary.
* Test different versions of your instructions and refine as needed.
* Pay attention to grammar and punctuation.
* Be mindful of Autopilot’s limitations.

## For expressions

Here are some examples of how you can write effective prompts for expressions in Studio.

### Date and time

* Find the next Sunday date.
* Download emails received today with the date format "dd/mm/yyyy".
* Convert from format "MM/dd/yyyy hh : mm : ss" to format "yyyy-MM-dd hh : mm : ss".
* Put a one second delay.

### Text and number

* Get last 4 digits.
* Get filename from full path.
* Verify if the result is a palindrome.
* Return the first palindrome number greater than 152.

### Data operations

* Fix the expression by declaring and initializing the variable before calling the first method on it.
* Store the list of strings inside an array.

### Files operations

* Get all `.pdf` files from the folder.

### Excel operations

* Read ranges B3 to B9 from the Excel sheet.

## For workflows

Here are some examples of how you can write effective prompts for workflows in Studio.

### Storage services

* When a new PDF is created in OneDrive, split its pages into separate files.
* Combine all PDF files in a OneDrive folder into a single PDF file and upload the merged file to a specified folder.
* Every Saturday, connect to our OneDrive and backup to AWS cloud storage all the new files added in the 'Projects' folder during the week.
* Upload signed Documents from DocuSign to Dropbox.

### Communication services

* Send the recording on Slack once recording is ready on Zoom.
* Send an SMS message via Twilio when a high-priority incident is created in ServiceNow.

### Microsoft 365

* When a new row is added to the vendors table notify the team over Slack and confirm via Microsoft Outlook.
* Add a new line to an Excel Spreadsheet for every unread email in an Microsoft Outlook folder, then mark the email as read.
* Create a flow that reads through the emails in a particular folder using Microsoft 365. Then Download the attachments, only consider those that are PDF. Then read the text from the PDF.
* Extract data from a new invoice file in once drive and store in Excel.
* Notify me on Teams when a critical bug is created in Jira.
* I need to extract the latest Bitcoin data from Yahoo Finance and write it to an Excel.

### Google Workspace

* Extract data from a new invoice file in Google Drive and store it in Google Sheets.
* Download new Zoom Recordings as video files and upload them to Google Drive.
* Trigger an automation from Gmail and store the attachment in the Google Drive.
* Create a new entry in Google Sheets for a new customer support ticket from Zendesk.
* Extract the latest 100 emails from Gmail from the current month and create a Google Sheets Report with the sender and subject.
* For new invoices received to Gmail create an expense report using Expensify.
* Summarize new Gmail email using OpenAI and share the summary via Slack.

### Salesforce

* For a new Salesforce lead, generate a personalized email using OpenAI and send the email via Outlook.
* When a Salesforce opportunity is won, post a kudos message to Slack.
* Send me a message to Teams when a new lead is created in Salesforce.
* Whenever a lead's status changes in Salesforce, send a notification on Slack to the sales team with the lead's details.

### Open AI

* Scrape product, price and rating from provided URL, send the result to OpenAI to find the best option considering rating and price.

## For requirement evaluation

You can instruct Autopilot<sup>TM</sup> in Test Manager to evaluate requirements from various perspectives such as user flow, consistency, relevance, clarity, completeness, and security, and then generate the top ten enhancement suggestions. You can also use Autopilot to perform specialized analyses focused only on:

* Security aspects like access, protection, authentication, vulnerability, and compliance.
* Performance aspects like response times, throughput, scalability, resource usage, and load handling.

You can also provide Autopilot with supporting documents, such as security guidelines, accessibility guidelines, audit reports, user accessibility specifications, and compliance checklists, to enhance the description of a requirement.

You can use out-of-the-box prompts from the [Prompt Library](https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/prompt-libraries) in Test Manager to help analyze your requirements, and you can also add your own custom prompts to the **Prompt Library**, for future requirement evaluations.

Visit [Quality-check requirements - Best practices](https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/ai-powered-quality-checks-best-practices) to check the best practices and guidelines available for evaluating requirements.

## For manual test generation

Autopilot<sup>TM</sup> in Test Manager uses AI to generate test cases and relies on the specificity of requirement descriptions. This includes the following components:

* Concise, user-focused statement that highlights the purpose of the requirement.
* Comprehensive description of the application logic showing the user journey.
* Clear, measurable acceptance criteria including both positive and negative scenarios.

Ensuring the specificity of requirement descriptions allows Autopilot<sup>TM</sup> to generate accurate and detailed test steps. You can also give Autopilot<sup>TM</sup> additional instructions, whether for end-to-end flow verification or rapid test idea generation, among others, to tailor the test case generation for certain scenarios.

You can provide supporting documents, such as process diagrams and mockups, compliance documents, and discussion transcripts, to give Autopilot<sup>TM</sup> additional context to generate more accurate and relevant test cases.

You can use out-of-the-box prompts from the [Prompt Library](https://docs-dev.uipath.com/test-manager/automation-cloud/latest/user-guide/prompt-libraries) in Test Manager to help generate manual tests, and you can also add your own custom prompts to the **Prompt Library**, for future test generations.

Visit [Generate tests for requirement - Best practices](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/ai-powered-test-generation-best-practices) to check the guidelines and best practices available for generating test cases using Autopilot<sup>TM</sup>.

## For code

To convert text into code, you can offer Autopilot instructions about generating any C# code, refactor existing code, or generate a UiPath automation.

For more information, visit [Convert text into code - Best practices](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/convert-text-into-code-best-practices).

## For manual tests

To convert manual test cases into automation, you need a consistent object repository, because Autopilot uses UI Automation capabilities to reference UI elements. It's important to maintain a consistent naming convention for UI elements within manual steps to ensure that the generated automation is relevant. You should also use common activity names in manual steps so they can be easily converted into corresponding UiPath APIs in Studio Desktop.

For more information, visit [Automate manual tests - Best practices](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/converting-manual-test-cases-into-automation-best-practices).

## For test data

When you generate synthetic test data, Autopilot considers the existing arguments within your workflow and the additional instructions provided in the prompt to generate test data. You can also provide instructions to follow a certain combination of data, or to customize your data set.

For more information, visit [Generate synthetic test data - Best practices](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/generate-synthetic-test-data-best-practices).

## For test result analysis

Autopilot<sup>TM</sup> in Test Manager provides insights into failed test cases and recommendations for reducing the failure rate in your test portfolio. The more test results you provide, especially with failed test cases, when you generate the report, the more effective it is. The goal of the test insights is to help understand the main reasons why your tests are failing.

Each section within the report displays information about a certain area of your test results, such as:

* **Common Errors**: groups similar error messages semantically to highlight the most frequent issues.
* **Error Patterns**: categorizes failed test cases into broader categories. These specific categories identify recurring themes and systemic problems, providing a more clear understanding of the underlying issues in your test execution.
* **Recommendations**: provides actionable recommendations for enhancements, designed to guide your next steps in optimizing the stability of your test execution.