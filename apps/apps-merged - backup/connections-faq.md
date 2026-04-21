---
title: "FAQ for connections in Apps"
visible: true
slug: "connections-faq"
---

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

## What is the difference between a shared connection and a personal connection?

Personal connections are configured in personal folders. While designing your app, you can select a connection from your personal workspace. At runtime, this connection becomes unavailable to other users.

Shared connections are the connections which reside in a shared folder. As a runtime user, you can also use the same connection, provided you have access to the shared folder.

## How can I get a raw response from the API?

You can use the `RawResponse` property in the Response object. This property stores the string output from the API. To access the raw response, use the following expression:

```
<PageName>.<ControlName>.<RuleName>.Response.RawResponse
```

## Can I use the result of a connection API Rule and bind it to a table control?

Yes, you can convert `ListItems` into `ListSource` using the `ToListSource` extension method.

You can write this expression in the **data source** of the Table control:

```
<PageName>.<ControlName>.<RuleName>.Response.Value.ToListSource
```

If you cannot find the `ToListSource` method, this means the value type is not a `List` type.

## Where do I get more details on individual connectors?

To get more details on individual connectors, access [the Integration Services User Guide documentation page](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/release-notes-integration-service-2023).

The left sidebar contains a list of pages containing information for each officially supported connector, its API, and authentication methods.

## Can I onboard my own APIs? Can I use them via connections in Apps?

Yes, you can integrate custom APIs using [the Connector Builder.](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/connector-builder-about)

## Can I capture an API error at runtime?

Yes. To capture a runtime error thrown by an API, use the following expression in a control:

```
<PageName>.<ControlName>.<API>.Error
```