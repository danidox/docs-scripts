---
title: "Set External Context"
visible: true
slug: "set-external-context"
---

## Introduction

You can set up an external context when launching your application. This is especially helpful when starting an app from somewhere else, for example a robotic process automation (RPA) process.

### Demo app - try it yourself

To try setting the external content yourself, use the demo app or follow the [procedure](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/set-external-context#procedure).

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/master/demo-apps/expressions/ExternalContext_3.0.0_DemoApp.uiapp) |
| [Preview demo app in cloud](https://cloud.uipath.com/7e10edca-b5b7-4762-9e98-2ef2d8f502ab/apps_/default/run/production/2373f357-451a-4598-a85e-5067a3af53bb/6f585644-bf9e-4225-96e0-88e415d0d1b4/ID56774dfbc894464eae2ab432492598c6/public?el=VB&origin=orchestratorFolder) |

## Demo app - instructions to use

1. Run the [demo app](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/set-external-context#introduction). All the expressions using the `App.QueryParam` function should display their default values.
2. To reset expressions to their default values, click the **Next page** button.
3. Copy the following syntax and append it in the app URL after the `el=vb` part:
   ```
   &intv=3200&guidv="81a130d2-502f-4cf1-a376-63edeb000e9f"&sv=queryparam&bv=true&dv=1000000.222&datetimev="2/1/2022 11:00:00 AM"&datetimeoffv="4/2/2007 7:23:57 PM"&listv={"data":["apps","engineering","team"]}&file={"Name":"image","FileSize":25}
   ```
4. To display an image in the document viewer, add `URL="https://my-public-image-URL"` in the `file` parameter. For example:
   ```
   file={"Name":"image","FileSize":25, URL="https://my-public-image-URL"}
   ```
5. Press Enter and watch the values being updated.

## Procedure

:::note
To reference the external context using VB expressions, use the `App.QueryParam()` function. Query parameters are case sensitive For example, `intv` and `INTV` are treated differently.
:::

1. Add a **Textbox** control.
2. For the **Text** property, open the **Expression editor**.
3. Bind the query parameter function to the **Text** property by using the `App.QueryParam()` function:
   ```
   App.QueryParam(Of Integer)("intv", 100).ToString
   ```
   :::important
   Inside the `App.QueryParam()` brackets, specify the data type of the value you are passing in the URL. For example, if the value is an integer, you need to specify `App.QueyParam(Of Integer)`.
   :::
4. Publish the app. At the initial runtime, you should see the default value specified using the `App.QueyParam()` function, which is `100`.
5. Add query parameters after the `el=vb` part in the runtime URL by using the `&` character, then press Enter. For example, `el=vb&intv=250`.

The textbox should display `250`.