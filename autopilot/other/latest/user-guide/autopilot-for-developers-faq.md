---
title: "Frequently asked questions"
visible: true
slug: "autopilot-for-developers-faq"
---

This FAQ page answers common questions about generating automations with Autopilot.

## Q1: What data has Autopilot been trained on?

Internal company data only; no customer data involved.

## Q2: Does Autopilot collect any data?

At the moment, no data is being collected for the purpose of improving the models. In the future, data collection may be introduced for Community licensing plans. For Enterprise licensing plans, any data collection would only occur after clear communication and explicit consent.

## Q3: What models power Autopilot and Healing Agent?

The automation generation capabilities of Autopilot and the Healing Agent use a mix of UiPath proprietary models and third-party large language models. Depending on the use case, it may use **Google Gemini 2.5 Flash, Gemini 2.5 Pro**, or **Gemini 2.0 Flash** to deliver optimal performance.

## Q4: Do I benefit from Autopilot improvements without regularly updating Studio?

Yes. The Autopilot Generation Service, responsible for interpreting messages and generating code, receives monthly updates. Users with Studio version 2024.10 or later benefit from these updates. However, some features require newer Studio versions. We recommend keeping your Studio updated.

## Q5: Do I need the latest Studio version to use Autopilot effectively?

Although the Autopilot Generation Service updates independently, certain features require recent Studio versions. For optimal performance and access to all features, regularly update Studio.

## Q6: Where can I find best practices and examples for writing Autopilot prompts?

For generic instructions, refer to [Writing effective prompts.](https://docs.uipath.com/autopilot/other/latest/user-guide/effective-prompts#writing-effective-prompts---generic-instructions)

For Autopilot for developers specific instructions and examples, refer to [Prompting guide for generating automations](https://docs.uipath.com/autopilot/other/latest/user-guide/prompting-guide-for-autopilot-for-developers).

## Q7: Which UiPath products support generating automations with Autopilot?

You can use generate automations within the following UiPath products:

* Studio Web
* Studio 2024.10 and later
* Apps
* Integration Service

## Q8: How does Autopilot integrate with existing UiPath tools?

Autopilot integrates seamlessly with UiPath tools by leveraging capabilities such as UI Automation, Integration Service, and Document Understanding within Studio, Studio Web, and Apps.

## Q9: Do I need extensive coding experience to use Autopilot?

No. Autopilot operates primarily through natural language, enabling developers without extensive coding knowledge to automate tasks effectively.

## Q10: How does Autopilot manage data security and privacy?

Autopilot ensures data security and privacy by:

* Complying with global data protection regulations such as the General Data Protection Regulation (GDPR)
* Employing encryption for data in transit and data at rest
* Implementing role-based access control
* Adhering to secure development practices
* Conducting regular security audits and applying security updates
* Maintaining rigorous authentication and authorization protocols
* Preparing incident response plans for security breaches

## Q11: What languages does Autopilot support?

Autopilot uses LLM capabilities to handle text prompts in supported languages. For more details, visit [Overview – Localization support](https://docs.uipath.com/overview/other/latest/overview/localization-support).

## Q12: Does Autopilot integrate with third-party applications?

Yes. Autopilot supports integration with many third-party applications, enhancing its flexibility and extending its automation capabilities.

## Q13: What is the Autopilot chat?

The Autopilot chat is an agentic Autopilot, which assists you in creating and debugging workflows, or searching official documentation. It has contextual logic, so it offers suggestions and fixes based on the context where it is used. Currently, the Autopilot chat is available in:

* [Orchestrator](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-orchestrator#orchestrator)
* [API workflows in Studio Web](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-studio-web#studio-web)
* [Studio 2025.10+](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-studio-desktop#studio)