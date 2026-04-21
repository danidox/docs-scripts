---
title: "Image"
visible: true
slug: "image"
---

Supported image file types are `JPEG`, `PNG`, `BMP`, `GIF`, and `WEBP`.

## ****Working with IResource****

If you obtain a file as an `ILocalResource`, it is automatically converted into an `IResource` using:

```
JobAttachment.fromResource(file) // file is a ILocalResource
```

:::important
The following functions have been deprecated and should no longer be used:
* `.toLocalResource`
* `.toAppsFile`
:::

**Page Navigation**

You can programmatically navigate to a specific page inside the Document Viewer using:

```
appsFile.NavigateToPage(pageNumber)
```

## Demos

### Media: Binding images

#### Introduction

This app shows how to bind media files to **Image** controls.

#### Demo app - try it yourself

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/5703d81733eb42c934762af0be3ec8e50139b2e5/demo-apps/controls/Image/Image_Control_Demo_App.uiapp) |
| [Preview demo app in cloud](https://cloud.uipath.com/7e10edca-b5b7-4762-9e98-2ef2d8f502ab/apps_/default/run/production/2373f357-451a-4598-a85e-5067a3af53bb/6f585644-bf9e-4225-96e0-88e415d0d1b4/ID6e02e38b26e34c2981e555f1bace681e/public?el=VB&origin=orchestratorFolder) |

#### Demo app - instructions to use

1. In UiPath Apps, create a new app and import the downloaded demo app.
2. Preview your app and switch to the Demo tab.
3. To upload your own media files, follow the instructions in the app.

## General

* **Source** - The source of the image you want to display.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Clicked On** - Configure what happens when the image is clicked.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## Binding a media file

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Source` | `IResource` | Source file of the **Image** control. |
| `Tooltip` | String | Information text which appears when the user hovers over the **Image** control. |
| `Value` | `IResource` | The value attached or outputted from the **Image** control. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |