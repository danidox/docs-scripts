---
title: "Key concepts"
visible: true
slug: "key-concepts"
---

Solutions enable you to seamlessly work on multiple projects addressing one business process. With solutions, you no longer need multiple Studio Web instances to work on complex automations. You can create different types of automation projects that utilize shared resources within a single solution. You can thus use a complex array of tools in a unified developer experience that shares the same fundamental concepts for any project you design.

Solutions bring together the concepts of automations and resources.

**Automations** represent the executing components of the UiPath® Platform. Thanks to rapid advancements over the past year, Studio Web offers you the capabilities to create more than just RPA workflows.

Currently, solutions support RPA workflows, apps, agentic processes, agents, and API workflows, with support under development for new automation project types.

![Automation project](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614560)

**Resources** are platform constructs that enable a solution to fulfill business process requirements. Everything in the UiPath Platform that can be used or referenced in an automation is considered a resource.

Common examples of solution resources include queues, assets, storage buckets, connections, and task catalogs.

![Resource configuration](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614564)

Defining the necessary resources in a solution is a key step in automating a business process. Resource definitions act as blueprints that enable the resources to be created during deployment. The definition of an automation process includes both the automation project itself and the settings configured for the resources within that process. For example, the definition of a queue resource is the property set of that queue, including the schema (if it exists).

![Queue resource](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614568)

The process required to create executable automations from published packages is called **deployment**.