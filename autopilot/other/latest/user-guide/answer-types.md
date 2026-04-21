---
title: "Prompt-to-response flow"
visible: true
slug: "answer-types"
---

There is a predefined interaction flow that Autopilot follows to answer each query:

## 1. Creating the prompt

When you type your prompt into the chat box, you can also upload images or valid files. By hitting Send, Autopilot receives your prompt, reviews it, and determines any valid future actions.

## 2. Determining actions

Once Autopilot receives the prompt, it analyzes its intent, along with any images or files, and determines which (if any) actions it should perform to answer your query.

## 3. Executing pre-response actions

A pre-response action is an automation or a data source query that Autopilot runs in the background before responding to the query. This helps collect any information or context needed to provide a relevant answer.

If Autopilot decides it should use pre-response actions to help answer your request, it can perform up to six pre-response actions automatically.

## 4. Suggesting non-pre-response actions

A non-pre-response action is an automation which is not configured as a pre-response. If Autopilot decides to use a non-pre-response action, it recommends and sets up the automation to the user by inferring argument values from the conversation context. You can then validate the argument values and execute the automation. Only one non-pre-response action can be recommended at a time.

## 5. Responding to your query

Once all actions are complete, Autopilot generates a response. It may use information from pre-response actions, non-pre-response actions, and its LLM-trained knowledge. The Clipboard AI paste menu, if applicable, is displayed at the end of your table, prompt respsonse, or file upload.

## 6. Adding citations

Any relevant citations, such as those sourced from actions, appear under the previously generated response.

## 7. Suggesting further prompts

Finally, Autopilot provides prompt suggestions based on the conversation so far. Select one of these prompt to send it to Autopilot.