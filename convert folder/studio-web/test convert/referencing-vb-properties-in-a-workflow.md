---
title: "Using VB properties in apps in Studio Web"
visible: true
slug: "referencing-vb-properties-in-a-workflow"
---

Every control in an app has a number of properties associated with it. As an app developer, you can interact with these properties using the VB expression language and its syntax.

When you reference a VB property within a control, simply specify the property you wish to reference. When you reference a VB property of a control inside an automation, you need to specify a top-level item, otherwise the expression is invalid.

The following are examples of common VB expressions, as well as the top-level items you need to specify when using them in a workflow.

## Referencing current user data

* To reference the first name of the current user in a control, use `CurrentUser.FirstName`.
* To reference the first name of the current user in a workflow, use `UserContext.User.CurrentUser.FirstName`.
  :::note
  You can also reference other properties of the current user, such as `DisplayName`,`LastName`,`Group` or `email`.
  :::

## Referencing a property of a control

* To reference a property in a control, such as the **Text** property of a **Label**, use `MainPage.Label.Text`.
* To reference a property in a workflow, such as the **Text** property of a **Label,** use `Controls.MainPage.Label.Text`.

## Referencing a media file

To reference a media file in both controls and workflows, use `appMedia.[media_name]`

## Referencing an app variable

* To reference an app variable in a control, specify the variable name `[variable_name]`
* To reference an app variable in a workflow, use `AppVariable.[variable_name]`

## Referencing and converting file type variables

When using a **Set Variable Value** activity, the system automatically generates an Apps variable of the type `AppsFile`**.** Apps file type variables and Studio file type variables are distinct, but you can convert variables from one file type into the other.

Use the following expressions in the **Expression editor** when configuring a control or workflow:

* To convert an Apps variable to a Studio variable for use in a workflow, for example with an **Upload Storage File** activity, use: `AppVariable.file_apps.ToLocalResource`
* To convert a Studio variable to an Apps variable for use within your app, use: `file_sw.ToAppsFile`

## Referencing a file added using a File Uploader control

* To reference a file added in a **File Uploader** in a control, use: `MainPage.FileUploader.Value`
* To reference a file added in a **File Uploader** in a workflow, use: `Controls.<fileuploader_controlName>.value`.