---
title: "User scenarios for the Autopilot chat"
visible: true
slug: "user-scenarios"
---

The following examples describe how you can leverage Autopilot based on your scenario:

## Generating workflows, sequences, or code

**What you do:** Use natural language in the chat to describe what you want to build.

**How Autopilot helps:**
* Converts your input into a draft automation sequence.
* Allows follow-ups such as "Can you change the order of these steps?" or "Use a different activity here."
* Maintains full context of your request to incrementally build or adjust the automation.

**For example:**

"Create a process that reads unread Outlook emails, saves the attachments to a folder, and logs the filenames to Excel."

Follow-up: "Add a step to delete the email after saving the attachment."

## Editing workflows, sequences, or code

**What you do:** Ask for changes to specific parts of an existing automation.

**How Autopilot helps:**
* Recognizes references to named sequences or selected activities.
* Applies changes such as "Use a different variable," or "Replace this with a conditional check."
* Iterates on suggestions with you to refine the update in-place.

**For example:**

"Update the Data Extraction sequence to use the invoiceList variable instead of inputData."

Or: "Replace the last three steps with a Try-Catch block."

## Explaining workflows, sequences, or code

**What you do:** Ask for explanations of workflow logic, activity purpose, or sequence behavior.

**How Autopilot helps:**
* Summarizes selected parts of the workflow in human-readable language.
* Responds to questions such as "What does this sequence do?" or "Why is this loop used?"
* Supports deeper exploration through contextual follow-up questions.

**For example:**

"Explain what the Send Notifications sequence does."

Follow-up: "Why is it filtering on status = failed?"

## Reviewing workflows, sequences, or code

**What you do:** Request a review or optimization of part of your automation.

**How Autopilot helps:**
* Evaluates logic, error handling, and efficiency in the selected segment.
* Suggests improvements such as "Simplify these steps" or "Improve exception handling."
* Adapts feedback based on your goals, such as robustness, readability, or performance.

**For example:**

"Is there a more efficient way to process these invoices?"

Follow-up: "Can you suggest how to reduce the number of Excel write operations?"

## Solving design-time errors

**What you do:** Ask about validation errors or broken configurations during workflow design.

**How Autopilot helps:**
* Analyzes the error in context of the current workflow and variable scope.
* Suggests fixes such as "Add this missing argument" or "Update this property value."
* Lets you adjust or clarify the fix through chat.

**For example:**

"Why am I getting a variable not defined error in the email loop?"

Follow-up: "Add the missing variable with default value True."

## Solving runtime errors

**What you do:** Respond to runtime exceptions or failed execution paths during debugging.

**How Autopilot helps:**
* Highlights the step that caused the error and explains what went wrong.
* Allows follow-ups such as "What input caused this?" or "How should I fix it?"
* Proposes corrective actions or changes based on current context.

**For example:**

"Why did the Read Range step fail during execution?"

Answer: "The Excel file path is null. Would you like to add a null check before this step?"

## Accessing documentation and knowledge base content

**What you do:** Ask questions about activities, errors, or best practices during development.

**How Autopilot helps:**
* Returns context-aware answers pulled from official docs and KB articles.
* Handles queries such as "How does this activity work?" or "What does this error mean?"
* Provides links to full documentation while keeping you focused in your context.

**Example:**

"How does the Deserialize JSON activity handle nested objects?"

Or: "What are the recommended patterns for retrying failed transactions?"