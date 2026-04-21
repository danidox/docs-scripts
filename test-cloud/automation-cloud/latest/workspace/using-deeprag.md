---
title: "Using DeepRAG"
visible: true
slug: "using-deeprag"
---

DeepRAG (Deep Research–Augmented Generation) is a [Context Grounding](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-context-grounding) and synthesis layer that enables agents to analyze and connect information across multiple documents, producing citation-backed, enterprise-grade answers. You use it to build agents that perform deep research, investigative analysis, and evidence-based reasoning at scale. To learn more about agents, refer to the [Agents user guide](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/about-this-guide).

DeepRAG operates in three phases:

1. Planning – Analyzes your question, identifies sub-tasks, and defines research scope.
2. Iterative research loop – Queries indexed data, extracts relevant evidence, and consolidates findings.
3. Synthesis – Integrates all evidence into a cohesive, citation-backed response.

Each result includes traceable references to the original source, ensuring auditability and compliance across enterprise data backend.

## Key capabilities

Here are the key capabilities of DeepRAG:

* Multi-document synthesis – Synthesizes information across up to 1,000 pages in a single query.
* Citation-backed answers – Includes document names, page numbers, and timestamps for every key finding.
* Agentic reasoning – Plans, researches, and adapts during execution, rather than only retrieving results.
* Enterprise scale – Processes structured and unstructured data from multiple sources through a single index.
* Traceability and compliance – Maintains complete audit trails of sources used in synthesis.

## When to use DeepRAG

Use DeepRAG when your agents needs to:

* Analyze multiple documents to answer a complex question.
* Generate a comprehensive summary across diverse data sets.
* Validate findings with high-fidelity citations.
* Perform regulatory, medical, or legal research requiring traceability.

Use **Semantic Search** for quick fact lookups, and **DeepRAG** for detailed analysis or synthesis across document sets. For details on using context in agents, refer to the [Agents user guide](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-contexts).

Table 1. DeepRAG vs. other approaches

| Feature | Semantic search | DeepRAG |
| --- | --- | --- |
| Purpose | Find relevant chunks | Synthesize multiple docs |
| Document limit | Unlimited | 1,000 pages |
| Processing | Instant | Minutes |
| Output | Snippets | Comprehensive synthesis |
| Cost | Low | Medium |
| Citations | Basic | Detailed |

## Configuring DeepRAG

Before using DeepRAG, ensure you meet the following prerequisites:

* Your data is stored in the correct file format: native PDFs or TXT files, up to 512 MB per file.
* You have AI Units for ingestion and query execution. For details, refer to [Context Grounding licensing](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/context-grounding-licensing#context-grounding-licensing).

Next, complete the following actions:

**Step 1 – Prepare documents**
1. Use well-organized folders and clear naming conventions.
2. Include document metadata and page numbers.
3. Avoid duplicates and ensure files are OCR-applied if scanned.
:::note
For high accuracy, use native PDFs and structure documents by category or identifier.
:::

**Step 2 – Create an index**

In Agent Builder:

1. Select the **Context** node and select **Create new**. Here is a sample configuration for an index:
   1. **Name**: Medical_Records_2025
   2. **Description**: Aggregated patient records for review
   3. **Ingestion mode:** Advanced.
2. Upload your documents and wait for ingestion to complete.
   * Ingestion cost: 0.2 AIU × number of pages. For example, 1,000 pages = 200 AIU.

**Step 3 – Configure the agent**

Configure your agent. Here is an example:

* **Agent name** – Medical Record Summarizer
* **Description** – Analyzes patient medical records with full citations
* **Context** – Configure the context. For example:
  + Index: Medical_Records_2025;
  + Search strategy: DeepRAG
  + Search strategy prompt – Write an effective prompt, such as: "Analyze all medical records and provide a comprehensive summary including: Diagnoses and treatments, Medical history, Medications, Lab results."
* **Specify the output format** – For example: "Structured summary with citations". Always include detailed output format instructions and conflict-handling instructions in your prompt.
:::note
If the DeepRAG-generated summary exceeds the output size limit, retrieve the complete summary externally. Use the **DeepRAG ID** (from traces) together with the [Context Grounding Summary – DeepRAG](https://docs.uipath.com/activities/other/latest/integration-service/uipath-uipath-airdk-context-grounding-summary-deep-rag) GenAI activity to fetch the full synthesized output outside the agent run. This allows you to access the entire response without truncation.
:::

## Writing effective prompts for DeepRAG

DeepRAG automatically generates verified citations that point to the exact pages in the source documents where supporting evidence is found. You do not need to request citations or specify how they should be formatted—this happens by default. In fact, adding citation or formatting instructions can interfere with results and should be avoided.

To get reliable, high-quality outputs, focus your prompt on role clarity, task specificity, and concrete requirements.

Use the following pattern:

ROLE: You are a [domain expert] reviewing [document type].

TASK: Analyze all documents and [specific goal].

REQUIREMENTS:

1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

OUTPUT FORMAT: [Structured output format]

**Good prompt example**: You are a medical professional reviewing patient records. Create a comprehensive summary including diagnoses, history, medications, and lab results.

**Poor prompt example**: Summarize the patient’s records.

The good example clearly defines the role, sets a specific task, and outlines concrete requirements, allowing DeepRAG to retrieve and ground its response effectively, while automatically handling citations behind the scenes.

## Optimizing DeepRAG performance

Use the following information to optimize your context's performance:

| Scenario | Typical duration | Optimization tips |
| --- | --- | --- |
| ≤ 200 pages | < 10 mins | Use focused questions and native PDFs. |
| 500–800 pages | <20 mins | Split large files and refine prompt scope. |
| 1,000 pages | < 30 mins | Remove duplicates |

**Cost model**
* Ingestion = 0.2 AIU × pages
* DeepRAG query = 0.20 AIU per 30K tokens (0.2–0.4 AIU per 500 pages)

## Troubleshooting

| Issue | Cause | Solution |
| --- | --- | --- |
| No valid files to use for DeepRAG | Wrong file format or Basic ingestion mode selected | Use only PDF/TXT |
| Timeout (60 min) | Too large corpus or complex prompt | Split documents; simplify queries. |
| Missing citations | Weak prompt or unstructured sources | Verify PDFs have consistent numbering. |
| Low-quality summaries | Generic prompt or poor document quality | Improve prompt specificity; clean document hierarchy. |

## Use cases for DeepRAG

Here are some real-life business scenarios where DeepRAG can be useful:

**Medical record summarization**: Analyze 200–400 page patient files to extract diagnoses, treatments, medications, and labs with citation-backed summaries.
* Prompt example: Analyze all patient medical records and generate a clinical summary including chief complaints, diagnoses, medications, and treatment recommendations.
* Result: 5–10× faster review and 70–90% accuracy in healthcare implementations

**Contract analysis**: Review multiple agreements to identify principal terms, covenants, and default clauses.
* Prompt example: Analyze all credit agreements and extract financial terms, covenants, and default provisions.
* Result: Enables risk analysis with full audit trail for compliance and legal workflows.

**Regulatory and compliance review**: Summarize audit reports, filings, and SOPs to highlight compliance gaps with page-level references.
* Prompt example: Review all regulatory filings and summarize compliance status, identifying non-conformities with citations.