---
title: "About AI Trust Layer"
visible: true
slug: "about-ai-trust-layer"
---

The AI Trust Layer is UiPath’s governance and control framework for all generative AI activity across products and services. It provides centralized control, security, and observability for how both UiPath-managed and third-party LLMs are used.

AI Trust Layer ensures every generative AI request follows organization-wide security, privacy, and usage rules. It applies these policies consistently across products by acting as a shared control point for all LLM traffic.

## What the AI Trust Layer governs

The AI Trust Layer governs generative AI usage across the following:

* UiPath products and services such as Autopilot<sup>TM</sup>, Studio, Test Manager, Process Mining, and more.
* UiPath-managed LLMs and third-party LLMs, including bring-your-own-LLM configurations.
* Model selection, access controls, data privacy, and usage tracking.

## AI Trust Layer sub-services

To enable modularity and governance, the AI Trust Layer is organized into the following sub-services, each responsible for a specific set of actions:

* **LLM gateway**: LLM gateway is the interface between UiPath services and third-party LLM providers. It serves as the central entry point for all LLM traffic, applying governance and configuration logic before requests reach external models. Capabilities specific to LLM gateway involve:
  + [Managing AI Trust Layer policies](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-ai-trust-layer-policies): Check existing AI Trust Layer policies in **Automation Ops >** **Governance**, and their deployments.
  + [LLM configuration](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-llms#configuring-llms): Integrate your existing AI subscriptions while maintaining governance framework provided by UiPath, by replacing the UiPath LLM subscription or bringing your own LLM.
* **Context Grounding** (also referred to as Enterprise Context Service, or ECS): Context Grounding enhances prompts with relevant context before they are sent to an LLM. You can use [Context Grounding](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/governing-contextual-data-for-genai-features) to create and manage data indexes used by UiPath GenAI features and agents. Index management is available in Orchestrator.
* **LLM observability**: LLM observability is responsible for monitoring, usage visibility, and audit logging for all LLM interactions across UiPath services. Capabilities specific to LLM observability involve:
  + [Usage summary](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/checking-usage-summary): Tracks LLM usage per tenant, service, and model.
  + [Audit logging](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/viewing-audit-logs#viewing-audit-logs): Captures details of LLM interactions for traceability, compliance, and debugging.
  + [PII masking](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/pii-masking): Ensures personally identifiable information is pseudonymized before reaching LLMs used in generative AI features.

## AI Trust Layer and other services

While AI Trust Layer includes sub-services, it also governs flows involving other services and components, including:

* UiPath generative AI features that rely on accessing LLMs, such as features provided by Autopilot<sup>TM</sup>, IXP, Autopilot for Everyone, Agents
* Specialized LLMs, such as CommPath and Helix Extractor
* GenAI Connectors

These services interact with AI Trust Layer, but may have their own configuration spaces. For example, Autopilot for Everyone is governed by AI Trust Layer, in terms of the LLMs used, but is managed from a separate tab at the organization and tenant level.

## Security and trust

A key principle of AI Trust Layer is ensuring data privacy:

* All data flowing through AI Trust Layer is encrypted (TLS 1.2+ in transit, AES-256 at rest).
* UiPath guarantees zero third-party training on your data.