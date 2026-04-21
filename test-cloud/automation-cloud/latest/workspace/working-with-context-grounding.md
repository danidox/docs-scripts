---
title: "Working with Context Grounding"
visible: true
slug: "working-with-context-grounding"
---

This section includes information on how to use Context Grounding effectively.

## Getting started

To use Context Grounding with agents or Autopilot for Everyone, create an index following the steps described in [Creating indexes](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-indexes).

To use Context Grounding with activities, create a connection to the UiPath GenAI activities connector and make sure you use Studio Web or Studio Desktop version 2024.4 or newer.

## Managing the ingestion pipeline

You can manage the ingestion pipelines through:

* Orchestrator or Agents, from the **Indexes** page. See [Managing indexes](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-indexes).
* The **Update Context Grounding Index** activity, part of the UiPath GenAI activities package.

## Querying data with Context Grounding

After creating an index in Orchestrator, indexes are accessible throughout the UiPath platform. These indexes serve as persistent storage for documents ingested from your data sources, offering a reusable resource for various UiPath products:

* In Autopilot for Everyone, Context Grounding enhances user interactions by enabling searches across existing indexes to provide accurate answers to queries. For details, refer to [Context Grounding in Autopilot for Everyone](https://docs.uipath.com/autopilot/other/latest/everyone-admin-guide/context-grounding).
* GenAI Activities benefit from Context Grounding by allowing content generation based on information stored in permissioned knowledge bases. For details, refer to [GenAI Activities](https://docs.uipath.com/activities/other/latest/integration-service/uipath-uipath-airdk-about).
* For agents, indexes play a crucial role in providing context during runs. For details, refer to [Contexts](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-contexts).

**Monitoring Context Grounding**

Understanding how Context Grounding influences your workflows is crucial for optimizing performance and troubleshooting. Here's how you can trace and view Context Grounding outputs across different UiPath products.

In **Agents**, access the **Trace** view of the agent run to see comprehensive details. This view provides all search results and citations from the Context Grounding query, offering insights into the agent's decision-making process.

To gather detailed information about Context Grounding in GenAI activities:

1. Place a [Log Message](https://docs-staging.uipath.com/activities/other/latest/workflow/log-message) activity immediately after the Content Generation activity in your workflow sequence.
2. Use the following output variables to capture specific information:
   * **Top Generated Text**: View the LLM generation response after workflow execution.
   * **Citations**: Examine the semantic search results that influenced the generation output. This works only for PDF and JSON data types.

## Context Grounding in GenAI Activities

Context Grounding interacts with your data in three phases:

1. **Establish your data source for Context Grounding.**
   * Context Grounding follows shared folder permissions. Use a folder with appropriate access to manage and query from data.
   * Create a connection to the supported Integration Service data sources or add data to a shared Orchestrator bucket location.
2. **Ingest data from your data source into Context Grounding.**
   * Create and sync indexes in Orchestrator.
   * Use the [Update Context Grounding Index](https://docs.uipath.com/activities/other/latest/integration-service/uipath-uipath-airdk-update-context-grounding-index) activity to sync an index you have created.
3. **Query and ground prompts with your data.**
   * Use the Content Generation activity, agents, or Autopilot for Everyone to query over documents and use information to augment or ground prompts.

## Common Context Grounding patterns

The core components of Context Grounding are designed to provide a mechanism that supports finding pertinent information within and across documents, and surfacing only the most relevant pieces needed for a high-quality, low-latency generation from an LLM.

**Searching within documents**

The Context Grounding service helps you find specific information within a single document more effectively. Instead of just matching keywords, it understands the meaning and context of your search query. For example, if you're looking for information about "apple pie recipes" in a cookbook, it would understand that you're interested in desserts and baking, not technology or fruit farming.

**Searching across documents**

Context Grounding helps you find information spread across multiple documents. It can understand the relationships between different pieces of information and provide more relevant results. For example, if you're researching "climate change effects on agriculture" across various scientific papers, it pulls together relevant information from multiple sources, understanding that topics like rainfall patterns, crop yields, and temperature changes are all related to your query.

This means you can use Context Grounding for:

* **Data extraction and comparison**: Context Grounding can automatically identify and extract specific types of information from documents, then compare them in meaningful ways. Imagine you have a stack of résumés and want to compare candidates' work experiences. The service could extract job titles, durations, and responsibilities, then present them in a way that makes comparison easy, even if the information is formatted differently in each résumé.
* **Summarization**: Context Grounding can create summaries of long documents or multiple related documents. It doesn't pick out random sentences, but understands the key points and overall message. For example, if you have a long report on market trends, the service can provide a summary highlighting the main findings, key statistics, and overall conclusions.

## Notifications

You can subscribe to receive notifications from Context Grounding. Visit [Notifications panel](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/exploring-the-user-interface#notifications-panel) to learn more.

Events serve as triggers for notifications. The Context Grounding events that generate notifications are:

* Ingestion Job Completed
* Ingestion Job Failed
* Ingestion Job Started

You can also subscribe to events based on their severity, such as **Success** or **Error**.

## Bringing your own vector database

Use your existing vector database to ground agent responses in trusted enterprise data, without duplicating content or changing your current architecture.

This guide shows how to connect externally managed vector databases (such as Databricks Vector Search or Azure AI Search) to UiPath agents using API Workflows, enabling retrieval-augmented generation (RAG) with your own data sources.

By the end of this guide, you will be able to:

* Query an external vector database from a UiPath agent.
* Return the most relevant content as structured context.
* Ground agent responses in your organization’s data securely and in real time.

**When to use the Bring Your Own Vector Database (BYOVD) pattern**

Use BYOVD when:

* Your data is already indexed in an external vector store.
* You want agents to access up-to-date enterprise knowledge.
* You need to avoid copying or re-indexing data into UiPath.
* You require full control over data storage, security, and embeddings.

### How it works

BYOVD allows agents to ground generative AI responses in your trusted data sources. Instead of relying on a built-in Context Grounding index, you use [API workflows](https://docs-dev.uipath.com/studio-web/automation-cloud/latest/user-guide/about-api-workflows) that securely query your external vector database and return relevant context to the agent’s large language model.

This approach gives you flexibility to integrate any vector database with a public API, while maintaining control over data access, authentication, and retrieval logic.

UiPath enables BYOVD through API workflows that act as tools for agents. At runtime:

1. **User query**: The user submits a prompt to the agent.
2. **Tool selection**: The agent’s LLM determines that additional context is required and selects the custom vector search tool.
3. **API Workflow execution**: The agent invokes the published API Workflow, passing the user’s query as input.
4. **Vector search**: The workflow queries the vector database to retrieve the most semantically relevant content.
5. **Context return:** The workflow returns the retrieved content as structured JSON.
6. **Response formulation**: The agent uses this context to generate a grounded, accurate response.

This approach supports Retrieval-Augmented Generation (RAG) without requiring native ingestion into the Context Grounding service.

### Architecture overview

The BYOVD solution consists of three main components:

* **Vector database**: Your existing system (for example, Databricks Vector Search or Azure AI Search).
* **API workflow**: A UiPath Integration Service workflow that:
  + Accepts a query.
  + Calls the vector database API.
  + Returns relevant results.
* **Agent tool**: The published API Workflow, added as a tool that the agent can invoke.

### Security and credential management

Before building the workflow, store all API keys and secrets securely. Do not hard-code credentials in your workflow. Instead, use the Orchestrator credentials store:

* **Store credentials in Orchestrator**: Add your API keys and other secrets as credential assets in your Orchestrator tenant. This provides centralized, secure management of sensitive information.
* **Retrieve credentials at runtime**: In your API Workflow, use the [Get Credential](https://docs.uipath.com/activities/other/latest/workflow/get-robot-credential) activity to access stored credentials when the workflow runs. The activity returns the username as a string and the password (for example, an API key) as a `SecureString`, preventing secrets from being exposed in logs or workflow definitions.

### Prerequisites

Before you begin, ensure you have:

* An active vector database (such as Databricks Vector Search or Azure AI Search) with indexed data.
* A valid API endpoint and authentication credentials stored as credential assets in Orchestrator.
* An embedding model endpoint and key, also stored securely (for Azure client-side vectorization only).

### Setup

You can implement BYOVD using one of three approaches: model-native endpoints, client-side vectorization (where the API workflow performs the vectorization), or integrated vectorization.

The following sections provide step-by-step instructions for configuring each approach. The examples use Databricks and Azure AI Search, but the same pattern applies to other vector databases. Choose the setup that aligns with how your vector database handles query vectorization.

### Databricks vector search (model-native endpoint)

Use this option when Databricks handles query vectorization natively.

**Why use this option:**
* A simple configuration
* Only one API call per query
* No separate embedding model required

**Steps**
1. Get the Databricks details:
   1. Retrieve the Endpoint URL.
   2. Store your Databricks Personal Access Token as a credential asset in Orchestrator.
2. In Studio, create a new API workflow project and define the following arguments:
   * `in_QueryText` (`String`)
   * `in_TopK` (`Int32`, with a default value of `5`)
   * `out_Results` (`String`)
3. Use the [Get Credential](https://docs.uipath.com/activities/other/latest/workflow/get-robot-credential) activity to retrieve the Databricks Personal Access Token from Orchestrator at runtime.
4. Add an [HTTP Request](https://docs.uipath.com/activities/other/latest/developer/http-request) activity to call the Databricks endpoint:
   * **Endpoint**: the Databricks Vector Search endpoint
   * **Method**: `POST`
   * **Headers**: `Authorization: Bearer <Personal Access Token>`
   * **Body**: Construct the JSON body required by the Databricks API, mapping your input variables.
5. Publish the workflow to your Orchestrator tenant.
6. Add the workflow as a tool to your agent, providing a clear name and description for the LLM to use.

### Azure AI Search (client-side vectorization)

Use this option when your Azure AI Search index expects vector inputs.

**Why use this option:**
* Full control over embedding models
* Compatibility with existing vector indexes

**Steps**
1. Get the API details:
   * For Azure AI Search: Retrieve the Endpoint URL, Index name, and store your API Key as a credential asset in Orchestrator.
   * For the embedding model: Retrieve the Endpoint URL and store the API Key for your embedding service as a credential asset in Orchestrator.
2. In Studio, create a new API workflow project and define the following arguments:
   * `in_QueryText` (`String`)
   * `in_TopK` (`Int32`, with a default value of `5`)
   * `out_Results` (`String`)
3. First, vectorize the query:
   1. Add a [Get Credential](https://docs.uipath.com/activities/other/latest/workflow/get-robot-credential) activity to retrieve your embedding model's API key.
   2. Add an [HTTP Request](https://docs.uipath.com/activities/other/latest/developer/http-request) activity to call your embedding model with the `in_QueryText`.
   3. Deserialize the JSON response and store the resulting embedding vector in a variable (e.g., `queryVector`).
4. Query Azure AI Search:
   1. Add a **Get Credential** activity to retrieve your Azure AI Search API key.
   2. Add a **HTTP Request** activity and configure it as follows:
      * **Endpoint**: Your Azure AI Search endpoint.
      * **Method:** `POST`.
      * **Headers:** Add an `api-key` header with your Azure AI Search API key variable, as follows: `api-key: <API key>`.
      * **Body:** Construct the JSON body for the Azure AI Search vector search query, embedding your `queryVector` variable.
5. Publish the workflow to your Orchestrator tenant.
6. Add the published workflow as a tool to your agent, providing a clear description for the LLM to use.

### Azure AI Search (integrated vectorization)

Use this option when your Azure AI Search index supports built-in vectorization.

**Why use this option:**
* Simplest Azure setup
* No embedding calls in the workflow
* Single API request per query

**Steps**
1. Get the API details:
   * Retrieve your Azure AI Search Endpoint URL, Index name, and store your API Key as a credential asset in Orchestrator.
2. In Studio, create a new API workflow project and define the following arguments:
   * `in_QueryText` (`String`)
   * `in_TopK` (`Int32`, with a default value of `5`)
   * `out_Results` (`String`)
3. Add a [Get Credential](https://docs.uipath.com/activities/other/latest/workflow/get-robot-credential) activity to retrieve your Azure AI Search API key from Orchestrator.
4. Add an [HTTP Request](https://docs.uipath.com/activities/other/latest/developer/http-request) activity and configure it as follows:
   * **Endpoint**:
     ```
     https://<service>.search.windows.net/indexes/<index-name>/docs/search?api-version=2023-11-01
     ```
   * **Method**: `POST`
   * **Headers**: Add an `api-key` header with your Azure AI Search API key variable, as follows: `api-key: <API key>`
   * **Body**: Construct the JSON body to perform a vector search using the query text. Azure AI Search handles vectorization automatically.
     ```
     {
       "vectorQueries": [
         {
           "kind": "text",
           "text": "<%= in_QueryText %>",
           "fields": "contentVector",
           "k": "<%= in_TopK %>"
         }
       ],
       "select": "chunk, source_document"
     }
     ```
5. Publish the workflow to your Orchestrator tenant.
6. Add the published workflow as a tool to your agent, providing a clear description for the LLM.

## Frequently asked questions

**What is Context Grounding?**

Context Grounding is a new UiPath® feature, part of the AI Trust Layer. It provides a mechanism to search and retrieve relevant context from data to ground prompts and guide more precise generations from large language models (LLMs) through UiPath GenAI features and products.

**Why is Context Grounding important?**

Context Grounding provides evidence via user-provided data to LLMs to influence their generations. This makes predictions more tailored to your use cases and data, rather than based on the general data upon which LLMs are trained. This allows both attended and unattended automations which leverage GenAI to be more accurate and precise.

**How does Context Grounding work?**

Context Grounding provides two services:

* **Managed Vector DB as a Service:** We make it easy for you to convert your data into embedding representations.
* **Retrieval Augmented Generation (RAG) as a Service**: Context Grounding queries data from various automation products, retrieves the most relevant results, and augments prompts with those results to ensure generations are more specific.

**How do I use Context Grounding?**

You can use Context Grounding through [UiPath GenAI Activities](https://docs.uipath.com/activities/other/latest/integration-service/uipath-uipath-airdk-content-generation), [Autopilot for Everyone](https://docs.uipath.com/autopilot/other/latest/everyone-admin-guide/context-grounding), and [Agents](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/about-agents).

**Does Context Grounding eliminate hallucinations?**

No, but it does significantly reduce the likelihood of hallucinations because generations are based on information queried from user-provided data. By default, Context Grounding provides a citation, or proof of knowledge, from which the generation was based. This means you can verify and validate the source. When Context Grounding isn't able to find a highly confident corresponding answer in the provided data, it does not try to make up answers. Instead, it generates a response such as: "An answer could not be found".

**Do I have access to Context Grounding?**

Context Grounding is accessible to all tenants and organizations.

For details regarding data residency, refer to the [Data residency page](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/data-residency-cloud).

**How is Context Grounding licensed?**

Context Grounding charges for searches or RAG as it is executed through its supported UiPath product surfaces. For details, refer to [Context Grounding licensing](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/context-grounding-licensing#context-grounding-licensing).

**Is Context Grounding available only in cloud deployments?**

Starting with the 2.2510 release, Context Grounding is also available in Automation Suite.

**What types of data can I use in Context Grounding?**

Context Grounding currently works the following data formats: PDF, JSON, CSV, DOCX, TXT, XLS.

**Can I import additional business data into Context Grounding?**

To leverage Context Grounding, you need to import data into UiPath Orchestrator storage buckets or indexes. You can then use Context Grounding activities to ingest and index, and manage the queried data to ensure highly relevant results.

**Is there a limit on the amount of data I can include in Context Grounding?**

The limit of data you can use to ground your prompts is based on the model context window token size limits. Refer to the model you are using to execute the RAG (e.g., in GenAI activities) to determine potential token limit thresholds.

* **Index limit**: There is a limit of ten indices per tenant. We recommend you maintain a 1-1 relationship between Orchestrator buckets from which you are ingesting data to prevent data leak across folders and ensure logical separation of data that may need to be queried by different users for different purposes. Context Grounding takes advantage of folder authorization permissions to help enforce this recommendation.
* **Storage**: There is no limit on storage across or within these indices. However, we impose some limits on customers who have exceedingly high amount of data ingested.

**Is Context Grounding the same as RAG?**

Context Grounding does provide a RAG service at runtime for UiPath GenAI experiences. However, it also provides a managed vector database as a service to help manage the data used at runtime. This guarantees a high-quality search and generated results.

**How is my data stored or shared with Context Grounding?**

All data shared with UiPath is treated with standard enterprise compliance, encryption, and security standards.

Context Grounding is part of the AI Trust Layer, which means your data is never stored outside of UiPath, nor is it used to train third-party models.

**How do you ensure data security?**

Context Grounding is tenant-scoped and takes advantage of existing RBAC and AuthZ policies in UiPath, in addition to encrypting data at rest and in transit.

Because it is tenant-scoped, no data is shared across indices within the same tenant or across tenants.

**How is Context Grounding permissioned?**

Context Grounding is tenant-scoped. We support folder-level authorization in Orchestrator buckets, and Context Grounding leverages existing authentication and Automation Ops policies applied to the GenAI Activities.

**Can I dynamically select which LLM to use?**

In the UiPath GenAI activities you can select which LLM to use for executing the RAG portion that Context Grounding supports. You can select any LLM available in the LLM Gateway. UiPath then manages the ingestion and semantic search strategies to optimize the generation.