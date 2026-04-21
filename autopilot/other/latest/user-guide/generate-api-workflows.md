---
title: "Generate, edit, and analyze API workflows"
visible: true
slug: "generate-api-workflows"
---

Autopilot chat uses a proprietary tool, namely API Workflow Assistant, to generate, edit, and analyze API workflows based on your input.

## Generate API workflows

This phase focuses on generating new API workflows from scratch, based on your prompts. Depending on the complexity of your workflow, you can prompt specific instructions, such as:

* What APIs to use (for example, Salesforce, Gmail, Workday)
* What actions to perform with each API (for example, create a case, send an email, retrieve a list of workers)
* What rules should govern the workflow (for example, if a case priority is high, send a notification).
* What error handling mechanism should be used during execution.

### How it works

When you prompt Autopilot to generate a workflow, Autopilot analyzes your request to understand the core purpose. It then activates its specialized API Workflow Assistant tool to design the workflow structure, identify necessary API calls, determine action sequences, and anticipate data flow. If details are missing, Autopilot may ask clarifying questions. It then generates a preview for your review.

### Prompt examples for generating API workflows

| Prompt | Autopilot interaction |
| --- | --- |
| **First prompt:** "Create a workflow that manages new customer sign-ups." | Autopilot may ask for more details, or it may provide a basic template. |
| **Adding specifics:** "When a new customer signs up in our web form (via Webhooks), I want to add them to Salesforce as a new Lead and then send them a welcome email via Gmail." | Autopilot generates a draft workflow. |
| **Reviewing initial draft:** "Only send the welcome email if their email domain is test.com. Also, if they are from California, set their Salesforce Lead Status to Hot Lead, else, set it to New Lead." | Autopilot refines the workflow with the specified conditions. |
| **Handling errors:** "Add error handling to ensure that if the Salesforce lead creation fails, I get a notification on my Slack channel." | Autopilot designs and integrates mechanisms, such as **Ttry-Catch** blocks or notification activities to make your workflow robust. |

### Complex prompt examples

* **New employee onboarding (uses Workday and Slack APIs)** "Create a workflow that triggers when a new employee is added to Workday. The workflow should extract the employee name, job title, department, and start date. Then, use the Slack API to post a welcome message in the #office channel, including the employee name, job title, and department. Additionally, send a direct message to the employee with instructions on how to access company resources and complete their onboarding tasks."

  ![New employee onboarding prompt example in autopilot chat](/images/autopilot/autopilot-new-employee-onboarding-prompt-example-in-autopilot-chat-588580-bfe2d5e9.webp)
* **Case escalation (uses Salesforce and Gmail APIs)** "Create a workflow that monitors Salesforce cases with a priority of High and a status of New. If a case remains in this state for more than 4 hours, extract the case details (case number, subject, description, customer name, and contact email). Then, use the Gmail API to send an email to the support manager with the subject 'Urgent Case Escalation' and include the case details in the email body. The email should also contain a link to the case in Salesforce."

  ![Case escalation prompt example in autopilot chat](/images/autopilot/autopilot-case-escalation-prompt-example-in-autopilot-chat-588590-8311f508.webp)

### Simple prompt examples

* **Sales lead notification (uses Salesforce and Slack APIs)** "Create a workflow that sends a Slack message to the #sales channel when a new lead is created in Salesforce with a rating of Hot."

  ![Sales lead notification prompt example in autopilot chat](/images/autopilot/autopilot-sales-lead-notification-prompt-example-in-autopilot-chat-588600-47f3835d.webp)
* **New employee onboarding (uses Workday and Gmail APIs)** "Create a workflow that sends a welcome email to a new employee personal email when their Workday record is created."

  ![New employee notification prompt example in autopilot chat](/images/autopilot/autopilot-new-employee-notification-prompt-example-in-autopilot-chat-588612-f29c3646.webp)

## Edit API workflows

This phase focuses on modifying, improving, or adjusting existing API workflows, so that they meet your evolving needs.

### How it works

When you ask Autopilot to edit a workflow, Autopilot parses your request to understand the required changes. It then instructs its API Workflow Assistant to locate and modify specific activities, parameters, or logical blocks within the existing workflow. Autopilot ensures data consistency and then generates an updated preview of the changes for your review.

### Prompt examples for editing API workflows

| Prompt | Autopilot interaction |
| --- | --- |
| **Simple change:** "Instead of Gmail, use Outlook to send the welcome email." | Autopilot modifies the activity and flags any new missing connections. |
| **Adding new steps:** "After the welcome email is sent, add a step to create a new contact in HubSpot with the customer's email and name." | Autopilot inserts the new activity into the flow. |
| **Modifying parameters:** "In the Add Lead to Salesforce step, set the Lead Source field to Web Signup." | Autopilot adjusts the specific parameter within the activity. |
| **Modifying conditions:** "Update the condition for Hot Lead in Salesforce to California OR New York." | Autopilot modifies the conditional logic. |
| **Removing steps:** "Remove the step that sends the Slack notification if Salesforce lead creation fails." | Autopilot deletes the specified activity. |
| **Performing multiple edits:** "Change the subject of the welcome email to Welcome to Our Service, [Customer Name]! and also add a step to send a summary of the new signup to a Google Chat space." | Autopilot applies multiple changes in one go. |
| **Reviewing the changes:** "Show me the updated workflow." | Autopilot generates a new preview of the pending internal changes, often including descriptions of affected activities, and waits for your review. No permanent changes are made to your file at this stage. |
| **Accepting the changes:** "Confirm the edits." | Autopilot instructs the API Workflow Assistant to commit the pending changes by overwriting the existing project file with the updated workflow, making the edits permanent. |

## Analyze API workflows

This phase focuses on gaining insights into your existing API workflows, understanding their structure, and debugging potential issues.

### How it works

When you prompt Autopilot to analyze a workflow, Autopilot activates the analytical capabilities of its API Workflow Assistant. Then, it extracts specific information, diagnoses potential issues, and provides insights into the workflow structure, logic, and performance. Autopilot presents these findings in a clear, understandable manner.

### Prompt examples for analyzing API workflows

| Prompt | Autopilot interaction |
| --- | --- |
| **Summarizing:** "Summarize this workflow." | Autopilot provides a high-level overview of what the workflow does. |
| **Identifying outputs and inputs:** "What inputs does this workflow require?", or "What outputs does this workflow produce?" | Autopilot lists the defined input and output parameters. |
| **Listing used connections and APIs:** "What APIs are used in this workflow?" | Autopilot lists the connected applications (for example, Salesforce, Gmail, or Outlook). |
| **Describing activities or parts of the workflow:** "Explain what the Create Lead in Salesforce activity does.", or "Describe the logic within the If Customer Region block." | Autopilot provides a detailed explanation of the specified part of the workflow. |
| **Troubleshooting:** "Why is the 'Send Welcome Email' activity failing?", or " "Analyze this workflow to find any potential infinite loops or dead ends."  Provide the context for error messages. | Autopilot examines the workflow for potential issues and suggests solutions, such as modifying activities or adding error handling. |
| **Asking for optimization:** "Are there any best practices for error handling that I should implement in this workflow?", or "Can this workflow be optimized for better performance?" | Autopilot offers suggestions based on automation best practices. |