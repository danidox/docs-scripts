---
title: "Prompting guide for generating automations"
visible: true
slug: "prompting-guide-for-autopilot-for-developers"
---

This guide helps you write effective prompts and prepare necessary resources for creating accurate workflows with Autopilot.

For generic instructions, refer to [Writing effective prompts](https://docs.uipath.com/autopilot/other/latest/user-guide/effective-prompts#writing-effective-prompts---generic-instructions).

## Provide clear, individual instructions

Break tasks into small, clear actions. Autopilot generates accurate sequences when prompted with concise, separate steps.

**Prompt examples:**
* "Log into ACME, download a file, and email it."
* For an **If-Else** activity: "If username and password are empty, log message "Not able to extract credentials from asset". Else log message "credentials details are extracted correctly"."

## Prepare the Object Repository for UI Automations

* Define the UI elements in the Object Repository first. Otherwise, the UI automation may fail.
* Ensure elements have accurate names and context, to help Autopilot semantically match elements.

## Pre-create Orchestrator assets

Assets are shared variables or credential resources in Orchestrator. Make sure assets already exists in an Orchestrator folder before using them in an automation, as Autopilot cannot create assets dynamically.

**Prompt examples:**
* Vague: "Use the credentials to log in."
* Better: "Get values from the ACME credential asset."
* Best: "Get values from the ACME_credential asset, which is in the Test folder in Orchestrator."

## Pre-create Orchestrator queues

Queues are containers that allow you to hold an unlimited number of queue items. Make sure queues exist in an Orchestrator folder before using them in an automation, as Autopilot cannot create queues dynamically.

**Prompt examples:**
* Vague: "Use the queue to insert data."
* Better: "Insert transaction into queue ACMELoan."
* Best: "Insert transaction into queue ACMELoan, which is in the Test folder in Orchestrator."

## Specify activities explicitly

Clarify which activities to use. Autopilot favors activities previously used in the current workflow.

**Prompt example:**
* Explicit: "Send an email using UI Automation, not Outlook."

## Understand Autopilot limited context

Autopilot recognizes only the resources in the current file:

* Variables defined in the current file.
* Activities previously used in the current workflow.
* Assets and packages available via Data Manager.

Autopilot cannot access:

* Other workflow files.
* Global variables.
* The full project structure.

## Effective prompts examples

* **Website login:** "Create a web automation workflow that navigates to https://acme-test.uipath.com/login and types in Username and Password."
  :::important
  Objects in the Object Repository must exist prior to prompting Autopilot.
  :::
* **Website login using Orchestrator assets:** "Get values from the ACME_credential asset, which is in the Test folder in Orchestrator. Log in to https://acme-test.uipath.com using the retrieved username and password, then click log in."
  :::important
  Assets must exist in Orchestrator prior to prompting Autopilot.
  :::
* **Extract emails and create report:** "Extract the latest 100 emails from Outlook from the current month. Create an Excel file with sender and subject details."
* **Email-to-Word PDF summary:** "Get all my emails with the subject Feature Request. If any email has attachments of type PDF, download the file, summarize it, create a new word file in the current folder, and append the summarization."
* **Convert log file to Word document:** "Read text file at 'C:\Users\USERNAME\Desktop\Robot.log', write contents into a Word file, and save it as 'AutoPilotDoc.docx' at 'C:\Users\USERNAME\Desktop'."
  :::important
  Make sure the file paths exist and are accessible.
  :::
* **Read an email from Outlook using UiPath.Mail.Activities:** "Read an email from outlook using UiPath.Mail.Activities."
* **Call OData Users API and log the response:** "Call OData/Users Orchestrator APIs and display the response as a log message."
* **Academic grading:** "Read an Excel file with candidate's names, marks, and email addresses. If the score is more than 45, send an email using Outlook to the candidate saying they passed. Otherwise, send an email saying they failed."