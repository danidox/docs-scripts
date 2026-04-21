---
title: "About OData and references"
visible: true
slug: "about-odata-and-references"
---

The Orchestrator API implementation is based on the OData protocol. OData (Open Data Protocol) is an ISO/IEC approved OASIS standard that defines a set of best practices for building and consuming RESTful APIs.

The Open Data Protocol (OData) enables the creation of REST-based data services, which allow resources, identified using URLs and defined in a data model, to be published and edited by Web clients using simple HTTP messages. This specification defines the core semantics and the behavioral aspects of the protocol.

The default format for the Orchestrator OData metadata endpoint is JSON, and the metadata URL is `https://{yourDomain}/odata`. To change the default format to XML, append `/?$format=xml` to this URL.

For more information on protocol principles and definitions, we recommend checking the official OData [official documentation](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html).
:::note
We aim at compliance with the OData standard, but cannot guarantee it. While the standard mandates that the metadata endpoint should return XML format by default, we return JSON for historical compatibility.
:::

## Logical resources and metadata

The Orchestrator API provides custom methods for querying stats about various entities registered in Orchestrator. Each logical resource is an OData entity. All entities (such as Robot, Process, Queue) have properties, relationships, and operations.

![docs image](https://docs.uipath.com/api/binary/orchestrator/2/308085/219757)

## Available operations

### CRUD operations

These types of operations are available on logical resources most. CRUD operations include GET, POST, PUT and DELETE requests, but please note that not all logical resources make use of all these verbs due to both technical and business reasons.

### Requesting data

It is possible to request particular information from a particular resource, in conjunction with GET operations, through OData-specific parameters.

They enable you to query, filter, sort, select and expand information. More details can be found in the [official OData documentation](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752283).

### Custom actions

The following custom actions and actions which are not tied to a logical resource are available in the Orchestrator API:

* **Stats methods** provide aggregates information on different entities;
* **Account methods** provide authentication methods to Orchestrator;
* **Queues methods** are used by the Robot to access queues, while the `QueueDefinitions` endpoint should be used instead for external systems via API;
* **QueueProcessingRecords methods** offer statistical and aggregate information about queues;
* **RobotsService** resources can be used by Orchestrator to communicate with the Robot.
  ![docs image](https://docs.uipath.com/api/binary/orchestrator/2/308085/219785)