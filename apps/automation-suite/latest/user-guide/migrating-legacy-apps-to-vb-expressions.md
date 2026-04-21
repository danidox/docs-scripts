---
title: "Migrating legacy apps to VB expressions"
visible: true
slug: "migrating-legacy-apps-to-vb-expressions"
---

A legacy app is an app that has been created before the introduction of VB expression language, or that uses the legacy expression language.

The migration process takes the legacy app as input and generates a copy of the legacy app designed with VB expressions.

To migrate a legacy app to VB expressions:

1. Open the desired legacy app.
2. On the top toolbar, click **Migrate to VB**. A pop-up message informs you about the outcome of the migration.
3. Select **Continue** to migrate. A toast message informs you about the migration progress.
4. Check the notification panel to see if the app was migrated successfully.

The migrated app is displayed on the **Build** tab, with the following name syntax: app_name + migration timestamp.

:::important
Once migrated, the new VB app might display errors. These errors are caused by the incompatibility between legacy expressions and VB. To make your app functional, go through each error and manually adjust the expression to meet the VB requirements.
:::

## Migrated capabilities

The following list summarizes which Apps capabilities are migrated from legacy to the VB expression language. Not all capabilities are persisted, and they may need manual corrections. To help you rewrite the legacy expression in VB language, the migration algorithm provides a guiding string.

### App pages, controls, layouts

All app pages, controls, and layouts built within the legacy expression language are migrated to their related instance in VB expressions.

A couple of controls and elements are migrated differently:

File picker : Migrated as File downloader, if the File picker control is used as Download only.

Otherwise, the File picker control is migrated as File uploader.

Value binding : Value binding is not supported in VB expressions.

Data context : Data context is not supported in VB expressions.

:::note
The DataSource property is migrated as blank for several controls, such as Table, Dropdown, or List. Use the [Query Builder](https://docs.uipath.com/apps/automation-suite/latest/user-guide/the-query-builder#the-query-builder "Gets the number of records for an entity, for example SystemUsers.For example, for the Edit Grid control:") to rebuild the expression.
:::

### Expressions

All literal expressions are fully migrated. A literal expression is a value directly inputted by users.

Complex expressions, such as `Lookup`, are replaced by a string that serves as guidance in building the new VB expression.

### Integrations with Apps

All integrations, such as Processes, Queues, or Storage Buckets, are fully migrated.

Errors might occur if an integration name does not respect [the naming convention](https://docs.uipath.com/apps/automation-suite/latest/user-guide/best-practices-#naming-conventions) for VB elements. The migration algorithm renames the element on your behalf.

### Apps variables

During migration, variables are set to string data types, regardless of their original data type.

Errors might occur for variables that have other data types other than string assigned. In these cases, manual corrections are required.

Make sure the variable names respect [the naming convention](https://docs.uipath.com/apps/automation-suite/latest/user-guide/best-practices-#naming-conventions) for VB elements.

### Direct bindings

A direct binding is a link between two single elements only. For example, in a legacy app, the **Value binding** property of a **Textbox** control, or the **Storage Bucket** field of the **Upload file to storage bucket** rule.

Cross-page bindings are deprecated in VB expression language, therefore these types of bindings are not migrated. An error is displayed to elements that have cross-page binding, with a guiding string to help you rewrite the expression.

All simple expressions on control properties, such as Required, Readonly, or Hidden, are migrated.

### App rules

All rules that contain direct bindings are migrated. Complex expressions are removed or converted to a guiding string.

The following image compares the configuration for the **Set values** rule before (picture 1) and after (picture 2) migrating to VB expressions:

   ![docs image](/images/apps/apps-docs-image-328469-0f1512c1.webp)

A couple of rules are migrated differently:

Create/Update entity : The rule is migrated as the **Create entity** rule. Expressions in this rule are not preserved, therefore you need to reconfigure the rule.

Set values : If the rule has multiple items in the **Items To Set** field, they are migrated as separate **Set values** rules.

Expressions in this rule are replaced by strings that serve as guidance in building the new VB expression.

If/else : The rule is migrated without conditions.