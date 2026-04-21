---
title: "Building your first API workflow"
visible: true
slug: "your-first-api-workflow"
---

The following tutorial provides hands-on experience with key concepts behind the API workflow interface through a simple example using the Petstore public API.

In this example, you request "Pet information" from a language model (LLM) and use that data to add pets to the Swagger Petstore. The Swagger Petstore (https://petstore.swagger.io) offers accessible and easy-to-use API endpoints, available with or without authentication.

## Step 1: Calling the LLM

1. On your API workflow designer canvas, select **Add** (the plus + icon).
2. Select **Connector &gt; UiPath GenAI Activities &gt; Content Generation.**
3. Set up or select an existing connection in the **Properties** panel.
4. Configure these properties:
   * **Model—gpt-4o-mini-2024-07-18**
   * **Prompt** "For the swagger Petstore, create the details of a new fantasy creature that can be added to their inventory. Respond only with valid json. Return an array of 5 of these."
5. **Debug** your workflow up until this point.
6. See the results in the **Output** panel. You should see the raw input and output of the activity call. The response should look similar to the following:
   ```
   {
     "cacheReadInputTokens": 0,
     "created": 1745444601,
     "usage": {
       "total_tokens": 741,
       "completion_tokens": 686,
       "prompt_tokens": 55,
       "cache_read_input_tokens": 0
     },
     "contextGroundingCitationsString": "[]",
     "totalTokens": 741,
     "promptTokens": 55,
     "model": "gpt-4o-mini-2024-07-18",
     "id": "chatcmpl-BPcADRRpy7ZDZpBOxp6XJYk0HOpaa",
     "text": "```json\n[\n    {\n        ....  \"A stealthy creature that blends into the shadows, highly elusive.\"\n    }\n]\n```",
     "choices": [
       {
         "index": 0,
         "finish_reason": "stop",
         "message": {
           "content": "```json\n[\n  ...ws, highly elusive.\"\n    }\n]\n```",
           "role": "assistant"
         }
       }
     ],
     "completionTokens": 686,
     "object": "chat.completion"
   }
   ```

## Step 2: Using Script to properly format the response

The information you need sits within the `content.text` property, which is not properly formatted.

1. To your current API workflow, add the **Script** activity.
2. Open the Expression editor and write the following:
   ```
   const cleanedJsonStr = $context.outputs.v2_sub_generateChatCompletion_1.content.text
     .replace(/^```json\n/, '')
     .replace(/\n```$/, '');

   // Step 2: Parse into JSON
   let parsedObj;
   parsedObj = JSON.parse(cleanedJsonStr);
   return { aipet: parsedObj };
   ```

This JavaScript code parses the `content.text` object and returns it in a clean format.
3. **Debug** your workflow again. Observe the properly formatted response.

## Step 3: Iterating over the response array

The LLM returned multiple pet examples as an array, as indicated in the prompt at Step 1.

1. To your current API workflow, add the **Loop** &gt; **ForEach** activity.
2. Configure the For Each activity as follows:
   * **In**—
     ```
     $context.outputs.Javascript_1.aipet
     ```
   * **Item name**—currentItem
   * **Accumulate results**—OnThis command iterates through every item of the response array.

## Step 4: Adding the returned response to Petstore

1. Inside the **For Each** activity body, add the **HTTP** activity, and configure it as follows:
   * **Method**—POST
   * **Request URL**—`https://petstore.swagger.io/v2/pet`
   * **Request body**—Open the Expression editor and prompt the Autopilot field with: "Within this foreach, transform each object so it can be posted to the Swagger Petstore Pet creation. Find the values for each property in the previous step." The Autopilot response should look like the following (you can also copy this snippet):
     ```
      {
       id: $currentItem.id,
       name: $currentItem.name,
       category: $currentItem.category,
       photoUrls: $currentItem.photoUrls,
       tags: $currentItem.tags,
       status: $currentItem.status,
       age: $currentItem.age,
       properties: $currentItem.properties
     }
     ```
2. **Debug** your workflow. At this point, your API workflow should return a **Successful** status. This means that the pet data has been posted correctly to Pet store.

## Step 5: Returning a workflow response

This step exposes the final results of the workflow to external consumers in a clean, simplified format.

1. To your current API workflow, add the **Response** activity, and configure it as follows:
   * **Type**—Success
   * **Details**—Open the Expression editor and write the following:
     ```
     $context.outputs.For_Each_1.results.map(result => ({
       id: result.content.id,
       name: result.content.name,
       description: result.content.description
     }))
     ```

This snippet returns a custom JSON with the mentioned details.
2. Debug your workflow. Notice the final response with the three details.

## Step 6: Defining Input and Output schemas

This step makes the workflow objects available to external consumers.

1. For your current API workflow, open the **Data manager** panel.
2. For the **Input** tab:
   * Add a new property and named it "Genre".
   * Set the type to String.
   * Mark it as required.
3. For the **Output** tab:
   * Add three properties, and name them "id", "name", and "type". These are the properties returned by the workflow.
   * Set their type to String.
4. Select the **Content Generation** activity in your workflow.
   1. Update the Prompt field to: "For the swagger Petstore, create the details of a new " + $workflow.input.Genre + " creature that can be added to their inventory. Respond only with a json object holding the pet information." This new prompt uses the **$workflow.input.Genre** property defined in the Input schema.
5. Define a **Debug configuration** and provide a value for the Genre property:
   ```
   { Genre: "Fantasy" }
   ```

## Step 7: Publishing and executing

You have reached the end of a successful workflow build.

1. Publish the workflow to your Personal Workspace folder in Orchestrator.
2. Navigate to the subfolder where the corresponding process was created and select **Start job**.

Orchestrator reads the workflow input schema and requires you to input a Genre. Once you provide a value, the job starts.