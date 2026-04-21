---
title: "FAQ"
visible: true
slug: "faq"
---

1. **What is an API workflow?** API workflows are composite services purpose-built for API integration use cases. They let you define deterministic logic to manage and safeguard interactions with critical business systems and data. Designed for system-to-system communication, API workflows allow for transformation, validation, and orchestration of API payloads using a dedicated design-time and runtime experience.
2. **What can I build with an API workflow?** An API workflow is a composable, callable service that defines a request/response contract and orchestrates logic in between. Further, you can consume these services across UiPath products or by your enterprise systems, enabling reusability, modular design, and clean integration patterns.
3. **What content types are supported?**

API workflows currently support headers for `Content-Type: application/json` and `Content-Type: application/x-www-form-urlencoded`.

And Official UiPath connectors automatically transform potential SDKs or XML Webservices to JSON.
4. **How are API workflows different from traditional RPA workflows?** API workflows focus on high-speed, API-first system integration, ideal for backend, structured data exchanges. RPA excels in UI automation, legacy interactions, and use cases where APIs are unavailable, occasionally combined with API connectivity. Together, they offer the best of both worlds—ensuring flexibility and full coverage across your tech stack.
5. **How can I trigger or consume API workflows?** Use API workflows through or from within:
   * **Agents—**Add the API workflow as a tool.
   * **Maestro**—Add API workflows as tasks within your process.
   * **Studio**—Add API workflows to existing or new RPA processes with the Run Job activity.
   * **Orchestrator**—Use standard Orchestrator trigger support or manual start.
6. **Why would I use an API workflows with agentic tooling (for example, Agent Builder)?** API workflows provide a secure, deterministic foundation for agents to interact with enterprise systems. They ensure only necessary data is accessed, while supporting governance, scalability, and modular reuse of logic.
7. **Can I consume APIs on my on-premise applications in an API workflow?** API workflows run on Automation Cloud Serverless robots and connect through Integration Service. To access on-premises APIs, one of the following is required:
   * Expose APIs securely via your firewall or API gateway.
   * Establish a VPN connection between UiPath and your network.
   * Configure an allowlist [to include Integration Service IPs](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/configuring-firewall) and [Serverless static IPs](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/static-ip-configuration).