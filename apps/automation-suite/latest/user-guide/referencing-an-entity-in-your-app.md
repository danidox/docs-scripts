---
title: "Referencing an Entity in Your App"
visible: true
slug: "referencing-an-entity-in-your-app"
---

To create better, more complex apps, UiPath Apps can connect and interact with entities from UiPath Data Service.

Data Service is a persistent data storage service that brings powerful no-code data modeling and storage capabilities to your Robotic Process Automation (RPA) projects.

:::note
After the data is loaded, it is refreshed only when a rule is executed. Any updates made on Data Service via processes or other means are not picked up automatically. Make sure that you refresh the data explicitly in these scenarios.
:::
:::note
For the moment, there is no infinite scroll for entities.
:::

## Referencing an Entity From Data Service

Once an entity has been created in Data Service, you can reference that entity from an app.

:::note
If the entity in Data Service is changed, the changes are automatically synced after refreshing or reopening the app.
:::

The following example shows you how to add an existing entity to an app:

1. From an existing app in App Studio, expand the dropdown menu at the right of the **Add control** button.
2. Select **Entity**.

   ![docs image](/images/apps/apps-docs-image-292073-4f1bbab5.webp)
3. A list of tenants for the current account is displayed. Select the tenant that hosts the entities you need to import, then click **Next**.

   ![docs image](/images/apps/apps-docs-image-292082-1d70b9bb.webp)
4. The **Add entity** wizard opens, displaying the list of entities in the selected tenant.
5. Select one or more entities. The right-hand panel displays the list of fields of the highlighted entity.
   :::note
   If you select an entity which has as fields other entities, the dependent entities are selected automatically. Deselecting an entity which has as fields other entities does not deselect the dependent entities.
   :::

   ![docs image](/images/apps/apps-docs-image-292086-b664cb3b.webp)
6. Check the box next to the entity you want to use in your app and click **Add**.
   :::note
   * Entity permissions are managed in Data Service. Make sure you have the right permissions for the entity you want to add from
   Data Service.
   * You can access the record ID of a newly created record in an entity, using the following syntax: `ControlName.CreateEntityRecordRuleName.RecordId`
   :::

## Binding an Entity

Entities can be bound to the following controls:

* Dropdowns (simple and multiselect)
* Radio buttons
* Edit grids
* Lists
* Tables

The following example shows how to reference the entity called **Country** to a **Table** control.

### Before You Start

Make sure the entity is imported in your app.

### Procedure

1. In your app, add a **Table** control.
2. Select the table and go to **General** tab.
3. In the **Data source** property, you can reference an entity:
   * Open the **Query builder**, select the entity you want to reference, apply conditions if necessary to filter out the entity records, and then click **Save**.

   ![docs image](/images/apps/apps-docs-image-292109-e7fcdfa3.gif)

The column headings are automatically populated with the names of the entity fields.

The **Country** entity is now linked to the table.

:::note
To use simple controls (such as **List**, **Dropdown**) with entities, save the entity to an app variable, then use the variable to display the entity fields.
:::