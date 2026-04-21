---
title: "About Context Grounding"
visible: true
slug: "about-context-grounding"
---

Context Grounding is a component of the UiPath AI Trust Layer which allows you to bring in your data to generate more accurate, reliable GenAI predictions. Context Grounding is designed to make your business data LLM-ready without the need for any additional subscription to embedding models, vector databases, or large language models (LLMs). You can create representative indexes and embeddings of business data that UiPath GenAI features can reference for contextual evidence at runtime.

Context Grounding is a tenant-scoped platform service designed to support UiPath generative AI experiences (such as GenAI Activities, Autopilot for Everyone, and UiPath Agents) by grounding your prompts with relevant information before they are executed by the LLM via retrieval augmented generation (RAG).

Providing RAG as a service to UiPath generative AI experiences helps to:

* Overcome LLM context window limitations: for both small and large models, RAG helps improve accuracy, reliability, scalability, and efficiency of models as they interact with knowledge bases.
* Reduce risk of hallucination through references to ground truth data stores.
* Give generative apps access to specialized and proprietary knowledge sources.
* Give generative apps access to up-to-date sources of information.
* Enable positive feedback loops between data stores and user-queries.

## Core components

The terminology and core components of Context Grounding include:

Figure 1. Context Grounding component architecture

  !['Context Grounding component architecture' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/455462)

**Ingestion and indexing: make your business data LLM-ready**
* Ingestion: Convert business data into representative embeddings using UiPath-managed embedding models.
* Embedding: A representation of business data that an LLM can understand and search through.
* Index: A folder in a vector database that organizes the embeddings.
* Vector DBs: UiPath-managed vector database that stores embeddings organized in indexes.

**Retrieval**
* Search through LLM-ready business data to find the most relevant information. Context Grounding uses a variety of extraction, chunking, retrieval, and re-ranking techniques that are optimized based on different data formats and queries.
* Products that use Context Grounding (GenAI Activities, Autopilot for Everyone, Agents) interpret prompts as a query to search through embeddings, and produce the most relevant results based on cosine similarity search. These search results are an intermediate, precursor step to RAG, to augment prompts with relevant context from business data.

**Retrieval Augmented Generation**
* Ground and update prompts with the most relevant information from the semantic similarity search results, then execute a generation via an LLM hosted through the LLM Gateway of the AI Trust Layer.

## Key features

Key features of Context Grounding include:

* Multi-document support: PDF, JSON, CSV, XLSX, DOCX, TXT files.
* Enhanced multi-modal ingestion: Support for documents containing both images with text and text-based content. Enables processing of non-native (like scanned) PDFs.
* Advanced structured queries support for CSV data. This feature is available when adding an index to an agent.
* Multilingual support: Ability to ingest and query from documents in all UTF-8 encoded languages.
* Managed ingestion and indexing pipelines: UiPath optimizes the ingestion and indexing of data in UiPath-managed vector databases.
* Multiple surfaces: Context Grounding is currently available as part of the UiPath GenAI Activities, Agents, and Autopilot for Everyone.
* Data retrieval: Query within documents or across datasets using a variety of techniques (e.g. query transformation, embedding, fine tuning, etc.) to ensure search results are highly relevant.
* Retrieval Augmented Generation: Ground prompts via just-in-time (JIT) in-memory or over a knowledge base.
* DeepRAG synthesis: Supports query-driven synthesis over document content using retrieval-augmented generation.
* Proof of knowledge: Provides a citation of the reference source and text from the semantic similarity search.
* Streaming support: Streaming API support to show generation as it is being produced.
* Support for multiple data sources:
  + UiPath Orchestrator bucket entities: You can ingest, index, and query data stored within shared folders in Orchestrator bucket entities.
  + Document storage systems: Through Integration Service connectors, such as Dropbox, Google Drive, and Microsoft OneDrive & SharePoint: Context Grounding can access data directly stored in third-party applications.

## Licensing

For details, refer to [Context Grounding licensing](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/context-grounding-licensing#context-grounding-licensing).

## Limitations and considerations

* Context Grounding currently supports specific file types: CSV, DOCX, JSON, PDF, TXT, XLSX.
* There is a limit of ten indexes per tenant, which can be increased upon request. We recommend you keep a 1-1 relationship with these and the folder path in the data source you want to use.
* Context Grounding follows folder permissions and authorization for shared folder entities. Users who do not have the appropriate permissions may not be able to view, update, delete, or use indexes that are affiliated with folders they do not have permissions to.
* To use Context Grounding through UiPath GenAI Activities, you must use Studio Web or Studio Desktop version 2024.4 or newer. For more information, refer to the [Working with Context Grounding](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/working-with-context-grounding#working-with-context-grounding) section.