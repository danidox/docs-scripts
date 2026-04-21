---
title: "Custom HTML"
visible: true
slug: "custom-html"
---

The Custom HTML Control targets advanced users and offers the flexibility of HTML, CSS, and JavaScript programming languages to craft custom, interactive controls as required by their business needs. The control includes dedicated editors for HTML, CSS, and JavaScript code, with the added advantage of incorporating externally hosted CSS and JavaScript files via URLs.

## Demos

### Custom HTML: creating charts

#### Introduction

This app shows how to create different types of charts using JavaScript libraries such as d3.js or chart.js.

#### Demo app - try it yourself

To try the interactive charts yourself, use the demo app.

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/5703d81733eb42c934762af0be3ec8e50139b2e5/demo-apps/controls/custom-html/CustomHTMLChart_DemoApp.uiapp) |

#### Demo app - instructions to use

1. In UiPath Apps, create a new app and import the downloaded demo app.
2. Preview your app to interact with all chart types.

### Custom HTML: creating a interactive pie chart using variable functions

#### Introduction

This app combines entities, **Custom HTML**, and **Edit Grid** controls to display an interactive pie chart. The interactivity is activated by selecting an option from a dropdown menu, which changes the pie chart sections and the records in the edit grid. Subsequently, clicking on a chart section updates data in the edit grid.

#### Demo app - try it yourself

To try the interactive pie chart yourself, use the demo app or follow the [procedure](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/custom-html#procedure).

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/master/demo-apps/controls/custom-html/CustomHTMLPieChart_DemoApp.zip) |
| [Preview demo app in cloud](https://cloud.uipath.com/7e10edca-b5b7-4762-9e98-2ef2d8f502ab/apps_/default/run/production/2373f357-451a-4598-a85e-5067a3af53bb/6f585644-bf9e-4225-96e0-88e415d0d1b4/IDceaaab1240fe4d3e9515a9271ccc2f5d/public) |

#### Demo app - instructions to use

1. Preview the demo app.
2. From the "Filter Tickets by Customer Name" dropdown, select an option. The total count of tickets, the pie chart representation, and data in the edit grid should change.
3. Hover over a chart slice. The tooltip displays the category name and the ticket count.
4. Click a chart slice. The edit grid displays the records for the selected category.

#### Procedure

To see how entities and variables are used in the Custom HTML control, download the following app files to your local machine:

* [Entity schema](https://documentationexamplerepo.blob.core.windows.net/examples/Apps/ticket_entities_schema.json)
* [Data for the Tickets entity](https://documentationexamplerepo.blob.core.windows.net/examples/Apps/tickets_entity_data.csv)
* [Data for the Tickets Source entity](https://documentationexamplerepo.blob.core.windows.net/examples/Apps/ticketsource_entity_data.csv)
* [App file](https://documentationexamplerepo.blob.core.windows.net/examples/Apps/CustomHTMLPieChart_DemoApp.uiapp)

After downloading, proceed with the following steps:

1. In UiPath Data Service, click **Import Schema**:
   1. Select the previously downloaded `ticket_entities_schema.json` file.
   2. In the **Entities** tab, check the Tickets and Tickets Source boxes.
   3. Switch to the **Choice Sets** tab, and check the Continents and Friction Level boxes.
   4. Click **Import**.
2. In UiPath Data Service, select the Tickets Source entity:
   1. Click **Import data**.
   2. Select the previously downloaded `ticketsource_entity_data.csv` file, then click **Open**.
   3. Switch to the **Data** tab to see the uploaded records.
3. In UiPath Data Service, select the Tickets entity:
   1. Click **Import data**.
   2. Select the previously downloaded `tickets_entity_data.csv` file, then click **Open**.
   3. Data for **Relationship** and **Choice Set** type fields are not imported automatically. You need to manually fill in data for these fields.
   4. Switch to the **Data** tab. For every Tickets record, update the values for the Source field by randomly selecting Chat, Phone, or Email.
   5. In the **Data** tab, for every Tickets record, update the values for the Friction field by randomly selecting 1, 2, or 3.
4. To import the app file, follow this step, then go to step 14.

In UiPath Apps, create a new VB app:

   1. Click **Import from file**.
   2. Select the previously downloaded `CustomHTMLPieChart_DemoApp.uiapp` file, then click **Open**.
   3. To fix the errors, replace the entity in the imported app with the one you previously created in steps 2 and 3.
   4. In the imported app, select the dropdown control named "CustomFilterDropdown", open the expression editor for the List Source property, and then save it.
5. To create the app from scratch, follow steps 5 to 14.

In UiPath Apps, create a new VB app.
6. In your app, [reference the entities](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/referencing-an-entity-in-your-app#referencing-an-entity-from-data-service) created in steps 1 to 3.
7. Create the following variables, based on Data Service entities:

   | Variable name | Type | Referenced entity |
   | --- | --- | --- |
   | `allTickets` | ListSource | Tickets |
   | `filteredTicketListSource` | ListSource | Tickets |
   | `selectedSourceType` | Text | - |
   | `ticketSourceTypes` | ListSource | Tickets Source |
8. Add a **Dropdown** control to your app, and rename it "CustomerFilterDropdown":
   1. In the **Label** field, rename it to "Filter tickets by customer name".
   2. In the **List source** field, open the expression editor and write the following VB expression:
      ```
      New ListSource(of String)With{.data = allTickets.data.Select(Function(x) x.CustomerName).Distinct.ToList}
      ```
   3. Switch to the **Events** tab, then click **Create rule**.
   4. Add the **Set Value** rule, with the following input:

      |  |  |
      | --- | --- |
      | **Item to set** | ``` filteredTicketListSource ``` |
      | **Value** | ``` Fetch(of Tickets)(createFilterGroup(New QueryFilter(){addFilter(If((MainPage.CustomerFilterDropdown.SelectedItem Is Nothing),"","CustomerName"), "=", MainPage.CustomerFilterDropdown.SelectedItem)}, Nothing, 0), Nothing, Nothing, Nothing, New ExpansionFieldOption(){addExpansionFieldOption("Source", New String(){"Id","Source"}), addExpansionFieldOption("CreatedBy", New String(){"Id","Name"}), addExpansionFieldOption("UpdatedBy", New String(){"Id","Name"})}) ``` |
9. Add a **Header** control to your app, and rename it "TicketCountHeader":
   1. In the **Text** field, open the expression editor and write the following VB expression:
      ```
      (filteredTicketListSource.totalRecords).ToString +" Tickets"
      ```
10. Add a **Custom HTML** control to your app, and rename it "Chart":
    1. Open the **Code editor** and replace the placeholder content with the following code snippets:

       | Editor | Code | Usage |
       | --- | --- | --- |
       | HTML | ``` <script src="https://cdn.jsdelivr.net/npm/chart.js"> </script> <div class="chartContainer">   <canvas class="pieChart" id="myChart"></canvas> </div> ``` | Generates a template JavaScript chart from an open-source library and applies the style classes on that chart. |
       | CSS | ``` .chartContainer {   height: 100%;   background-color: #ffffff;   font-family: Arial, Helvetica, sans-serif;   font-weight: bold;   color: #526069;   display: flex;   align-items: center;   justify-content: center; }  .pieChart {   width: 50%;   max-width: 400px;   max-height: 400px; } ``` | Defines two style classes: `.chartContainer` and `.pieChart`. |
       | JavaScript | ``` // Create an object to store counts var counts = {"Email": 0, "Phone": 0, "Chat": 0};  // Mock data to see the chart in designer, You can assign it with empty array if you don't want to see chart in designer var Tickets = [   {Source: { Source: 'Phone' }}, ];  // Function to count the number of tickets per Source function countTickets(tickets) {   counts = {"Email": 0, "Phone": 0, "Chat": 0};   // Reset counts to zero   for (var i = 0; i < tickets.length; i++) {     counts[tickets[i].Source.Source]++;   } }  countTickets(Tickets); // Count tickets in the initial data  // Create a Chart var ctx = document.getElementById('myChart').getContext('2d'); var myChart = new Chart(ctx, {   type: 'pie',   data: {     labels: ['Email', 'Phone', 'Chat'],     datasets: [{       label: '# of Tickets',       data: [counts["Email"], counts["Phone"], counts["Chat"]],       backgroundColor: [         'rgba(255, 99, 132, 0.2)',         'rgba(54, 162, 235, 0.2)',         'rgba(255, 206, 86, 0.2)'       ],       borderColor: [         'rgba(255, 99, 132, 1)',         'rgba(54, 162, 235, 1)',         'rgba(255, 206, 86, 1)'       ],       borderWidth: 1     }]   },   options: {     onClick: function(evt, elements) {       if (elements.length) {         var chartElement = elements[0];         var label  = this.data.labels[chartElement.index];         OutputSource = label;         console.log(OutputSource); // You can see the stored value in browser's console on each click         App.setVariable('selectedSourceType', OutputSource);       }     }   } });  // Function to update chart's data function updateChart(data) {   NewTickets = data;     // New data to update the chart     countTickets(NewTickets);     myChart.data.datasets[0].data = [counts["Email"], counts["Phone"], counts["Chat"]];     myChart.update();  let sourceWithData = Object.keys(counts).find(ticketSource => {   return counts[ticketSource] > 0; }); if(sourceWithData) {   App.setVariable('selectedSourceType', sourceWithData); } }  //Listen for updates to the ticket data and update chart async function registerOnChangeEvent() {   App.onVariableChange('filteredTicketListSource',(listSource) => {     updateChart(listSource.data);   })   const listSource = await App.getVariable('filteredTicketListSource');   if(listSource?.data?.length > 0) {     updateChart(listSource.data);   } }  registerOnChangeEvent(); ``` | Defines the variable functions and adds the interactivity to the chart. |
    2. Click **Save**.
    3. Switch to the **Style** tab, and set the following **Size**:

       |  |  |
       | --- | --- |
       | **Width** | 1000 px |
       | **Height** | 400 px |
11. Add a **Header** control to your app, and rename it "sourceTypeHeader":
    1. In the **Text** field, open the expression editor and write the following VB expression:
       ```
       "Tickets created through " & selectedSourceType
       ```
12. Add an **Edit Grid** control to your app, and rename it "TicketsListByType".
    1. In the **Data source** field, open the expression editor and write the following VB expression:
       ```
       Fetch(of Tickets)(createFilterGroup(Nothing, New FilterGroup(){createFilterGroup(New QueryFilter(){addFilter(MainPage.TicketsListByType.SearchColumn, "contains", MainPage.TicketsListByType.SearchTerm)}, Nothing, 0), createFilterGroup(New QueryFilter(){addFilter("Source.Source", "=", selectedSourceType), addFilter("CustomerName", "contains", MainPage.CustomerFilterDropdown.SelectedItem)}, Nothing, 0)}, 0), New PaginationProps(MainPage.TicketsListByType.PageStart, MainPage.TicketsListByType.PageLimit), New SortOption(){addSortOption(MainPage.TicketsListByType.SortColumn, Not(Not(MainPage.TicketsListByType.isDescending)))}, Nothing, New ExpansionFieldOption(){addExpansionFieldOption("Source", New String(){"Id","Source"}), addExpansionFieldOption("CreatedBy", New String(){"Id","Name"}), addExpansionFieldOption("UpdatedBy", New String(){"Id","Name"})})
       ```
13. For the **MainPage**, switch to the **Events** tab, then click **Create rule**.
    1. Add a **Set Value** rule, with the following input:

       |  |  |
       | --- | --- |
       | **Item to set** | ``` allTickets ``` |
       | **Value** | Open the **Query builder**, select the Tickets entity, then click **Save**. |
    2. Add a second **Set Value** rule, with the following input:

       |  |  |
       | --- | --- |
       | **Item to set** | ``` filteredTicketListSource ``` |
       | **Value** | Open the **Query builder**, select the Tickets entity, then click **Save**. |
14. Preview the app, select an option in the dropdown and notice the chart updating. Click on a chart section and notice the edit grid updating with the data from the selected section.

### Custom HTML: creating date-time pickers

#### Introduction

This app shows how to create a custom date-time picker.

#### Demo app - try it yourself

To try the date-time picker yourself, use the demo app.

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/5703d81733eb42c934762af0be3ec8e50139b2e5/demo-apps/controls/custom-html/CustomHTMLDateTimeControl_DemoApp.uiapp) |

#### Demo app - instructions to use

1. In UiPath Apps, create a new app and import the downloaded demo app.
2. Preview your app to interact with the date-time picker.

### Custom HTML: creating password fields

#### Introduction

This app shows how to create password fields.

#### Demo app - try it yourself

To try the password field yourself, use the demo app.

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/5703d81733eb42c934762af0be3ec8e50139b2e5/demo-apps/controls/custom-html/CustomHTMLPasswordControl_DemoApp.uiapp) |

#### Demo app - instructions to use

1. In UiPath Apps, create a new app and import the downloaded demo app.
2. Preview your app to interact with the password field.

### Custom HTML: creating signature input fields

#### Introduction

This app shows how to create signature input fields.

#### Demo app - try it yourself

To try the signature input yourself, use the demo app.

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/5703d81733eb42c934762af0be3ec8e50139b2e5/demo-apps/controls/custom-html/CustomHTMLSignature_DemoApp.zip) |
| [Preview demo app in cloud](https://cloud.uipath.com/7e10edca-b5b7-4762-9e98-2ef2d8f502ab/apps_/default/run/production/2373f357-451a-4598-a85e-5067a3af53bb/6f585644-bf9e-4225-96e0-88e415d0d1b4/IDc1c5161f6a204ab29918f6e8ee992ac4/public?el=VB) |

#### Demo app - instructions to use

1. In UiPath Apps, create a new app and import the downloaded demo app.
2. You may notice some errors. To fix them, replace the referenced storage bucket "Demo app" with one in your tenant.
3. Preview the app to interact with the signature input field.

## General

* **Open code editor** - Opens a three-panel editor for adding the HTML, CSS, and JavaScript code.
* **Accessible label** - The description of the control. This property is used by screen readers for enhanced accessibility.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, makes the control inactive at runtime. The HTML, CSS, and JavaScript content loads, but is unresponsive to user actions, such as clicking.

## Events

No events.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal)**.
  :::
* **Border** - The border for the control. Border **Thickness** and **Radius** can be configured.
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).
  :::note
  The Custom HTML control can dynamically resize itself based on its content. This is done by calling `App.setHeight(heightInPixels)` from JavaScript inside the HTML control. assignment
  ```
  const height = document.body.scrollHeight;
  App.setHeight(height);
  ```
  :::

## Code editor for Custom HTML

The code editor of the the Custom HTML control provides three panels to input code in HTML, CSS, and JavaScript programming languages. Each editor supports IntelliSense, or the automatic code completion, and syntax highlighting.

The code from the panels is compiled into a project and rendered in Apps Studio for preview. To observe the functionality of the control, preview the app.

![docs image](/images/apps/apps-docs-image-346261-45109ae8.webp)

:::important
* Each editor has a maximum content size of 5MB. When the content exceeds this size, you can no longer save your changes.
* IntelliSense does not work for CSS and JavaScript codes written within the HTML editor.
:::

### Adding external resources

If you already have styles or scripts defined, you can reference them in the control, without writing the code in the corresponding CSS or JavaScript panels.

To reference existing `.css`or `.js` files:

1. In the **Code editor** of the Custom HTML control, switch to the **External resources** tab.
2. Under the CSS section, add an external CSS file. The file must be hosted at a network-accessible URL to ensure compatibility and availability where the app is running.
3. Under the JavaScript section, add an external script file. The file must be hosted at a network-accessible URL to ensure compatibility and availability where the app is running.
4. When you finished adding all the external resources, click **Save**.

   ![docs image](/images/apps/apps-docs-image-346342-eb6b1a37.webp)

### Accessibility shortcuts for the Tab key

By default, the Tab key adds a tab space inside the current editor. To customize the behavior of the Tab key, use the following shortcuts:

| OS | Shorcut | Behavior |
| --- | --- | --- |
| Windows | CTRL+M | Instructs the Tab key to navigate between the panels and change focus on the visible buttons of the editor. Press CTRL+M again to return to the default Tab behavior. |
| MacOS | CTRL+Shift+M | Instructs the Tab key to navigate between the panels and change focus on the visible buttons of the editor. Press CTRL+Shift+M again to return to the default Tab behavior. |

### The HTML editor

In this panel you can input the structure of your control, which is usually contained inside the `<body></body>` tags of a HTML code block.

For example, to add the container element for an interactive pie chart in your app, you would use the following HTML snippet:

```
<canvas id="myChart" class="chart-container" style="width:100%;max-width:600px"></canvas>
```

Where:

* `id="myChart"` refers the JavaScript "myChart" element that generates the interactive pie chart inside the HTML element. For details, see The JavaScript editor.
* `class="chart-container"` refers to the "chart-container" CSS class that adds the style for the pie chart inside the HTML element. For details, see The CSS editor.

### The CSS editor

In this panel you can input the style of your control and the elements inside it.

For example, to add colors and a border to the pie chart, you would use the following CSS snippet:

```
.chart-container {
    background-color: #f3f7e9;
    border: 1px solid #cccccc;
}
```

### The JavaScript editor

In this panel you can create the interactive part of your control, such as timely content updates, maps, or animated 2D/3D graphics.

For example, to create a pie chart for Apple products sales world-wide, and to design it to display values for the selected slice, you would:

1. Add the following JavaScript external resource:
   ```
   https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js
   ```
2. Use the following JavaScript snippet:
   ```
   const ctx = document.getElementById('myChart').getContext('2d');
   const myChart = new Chart(ctx, {
     type: 'pie',
     data: {
       labels: ['iPhone', 'iPad', 'MacBook', 'Apple Watch', 'AirPods'],
       datasets: [{
         label: 'Sales',
         data: [120000, 80000, 50000, 40000, 30000],
         backgroundColor: [
           '#5CB85C', // Green
           '#F0AD4E', // Orange
           '#D9534F', // Red
           '#5BC0DE', // Light blue
           '#999',    // Gray
         ],
         borderColor: '#fff',
         borderWidth: 2,
       }],
     },
     options: {
       plugins: {
         legend: {
           position: 'top',
         },
         title: {
           display: true,
           text: 'Apple Products Sales',
         },
       },
     },
   });
   ```

### Using variables in Custom HTML

To establish the communication between the Custom HTML control and other controls or integrations, we recommend [creating variables](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/variables-in-apps) and using the `setVariable()`, `getVariable()`, and `onVariableChange()` built-in functions.

#### getVariable()

In the JavaScript editor, use this function to get the value of an existing variable.

For example, to pass the value of a variable to an `internalValue`, you would use the following JavaScript snippet:

```
async function init() {
  let internalValue = await App.getVariable('<app_variable_name>');
}
init();
```

:::note
* The`getVariable()` function is asynchronous, which requires that you use `await`.
* If you call `getVariable()` inside a function, make that function `async`. In the example provided, we created the `init()` function and immediately invoked it.
* If you call `getVariable()` at a top-level, embed it inside an `async` function.
:::
To handle errors such as invalid variable names, use the try-catch statement. For example:

```
async function init() {
  try {
    const value = await App.getVariable("test");
  } catch (e) {
    console.log("Error in evaluating app variable:", e);
  }
}
init();
```

#### setVariable()

In the JavaScript editor, use this function to set a value to an existing variable. The first argument is the variable name, and the second argument is the value you want to set.

```
async function setValue() {
  await App.setVariable('<app_variable_name>', <app_variable_value>);
}
setValue();
```

:::note
To wait for the set operation to complete before executing other code use `await`.
:::
To handle errors such as invalid variable names, or type mismatch between the variable and the set value, use the try-catch statement. For example:

```
try {
  App.setVariable('<app_variable_name>', <app_variable_value>);
} catch (e) {
  console.log("Error in setting app variable:", e);
}
```

#### onVariableChange()

In the JavaScript editor, use this function to listen to changes of an existing variable value and access the latest variable value.

```
App.onVariableChange('<app_variable_name>', value => {
  console.log("Latest value: ", value);
});
```

In the following example, we assign the function returned by the `onVariableChange()` to the `deregister` variable. Then, if you want to stop listening to variable changes, you can invoke the `deregister()` function:

```
const deregister = App.onVariableChange('<app_variable_name>', value => {
  console.log("Latest value: ", value);
});

// To stop listening for value changes, the deregister function can be invoked like below
deregister();
```

:::note
* The listener starts after the Custom HTML control renders completely. If a variable value changes before the Custom HTML control
is initialized, the updated value is not captured. To get the latest variable value, call `getVariable()` before calling `onVariableChange()`.
* The HTML control and the functions inside it are initialized after the control is displayed at runtime.
:::

#### Variable types

| App variable type | Sample response from variable functions |
| --- | --- |
| Text (String) | "Hello world" |
| UInt64 (Int) | 100 |
| Decimal number | 50.25 |
| True/False (Boolean) | true |
| DateOnly | 2024-01-02  (Format: YYYY-MM-DD) |
| DateTimeOffset | 2024-01-06T09:54:41.9170000Z  (Equivalent JS Format: Date object ISO string) |
| AppsFile - value of a **File picker** control | JS File object ![docs image](/images/apps/apps-docs-image-354030-5a14c48f.webp) |
| AppsFile - value created from URL For example:  ``` new AppsFile("https://image.jpg") ``` | File object:  ``` {FileSize: 0, Name: "", URL: "https://image.jpg", __infoType: "$metadata"} ``` |
| GUID | "5637F7DB-391D-4C8B-805D-0A918531CA3E" |
| List(Of string) | ["Banana", "Kiwi", "Apple", "Lemon"] |
| ListSource(Of &lt;Entity&gt;) | ``` {   data: [{Name: "John", Age: "28", ...},{Name: "Kane", Age: "48", ...}],   totalRecords: 2 } ``` |
| &lt;Entity&gt; (Single entity row) | ``` {   Name: "John",    Age: "28",    ... } ``` |
| ListSource(Of &lt;Choiceset&gt;) | ``` {   data: [{DisplayName: "Male", Id: "00F3372D-3920-EC11-AE72-0003FFBA1E91", Name: "Male", ...}, {DisplayName: "Female", Id: "01F3372D-3920-EC11-AE72-0003FFBA1E91", Name: "Female", ...}],   totalRecords: 2 } ``` |
| Datatable | ``` [{From: 'Ahmedabad', To: 'Azua', ...},{From: 'banglore', To: 'Dominican Republic',...},...] ``` |

## Best practices for Custom HTML

* Do not include sensitive data in the Custom HTML control due to its client-side access.
* Do not use the `<html>` and `<head>` tags inside the HTML editor, as the code is appended inside the `<body>` tags automatically.
* Add CDN URLs of external resources such as Bootstrap, jQuery, or other JavaScript SDKs in the **External resources** tab.
* If you want to stop listening to the variable change, use the `deregister()` function.
* Avoid large data loops to prevent slowing down the application and to keep the control responsive.
* Minimize the usage of DOM elements as much as possible: create DOM elements only when necessary and remove them when they become obsolete.
* Use infinite or virtual scrolling for large datasets over standard scrolling.
* Create and maintain a clean, optimized, and redundancy-free code.

## Functional limitations

* Custom HTML does not provide the ability to trigger control rules.
* The control can communicate with other UiPath components, such as Processes, Queues, or Storage Buckets, only through the use of variables.
* To access Process or Queue data, you must assign a variable for every Process or Queue property.
* To connect the control to Apps, you must use the variable functions: `getVariable()`, `setVariable()`, `onVariableChange()`.
* The dimensions of the HTML control do not dynamically adjust for displaying pop-ups or dropdown menus. You must manually set the size of the HTML control to fit these menus.
* You cannot interact with the HTML control during design-time.
* The `setVariable()`, `getVariable()`, and `onVariableChange()` functions operate only at runtime.
* Changes to variable names or variable deletions do not automatically reflect in the code editors. You need to manually update the code with the current variables.
* Transfers of image data from the HTML control to a storage bucket, or to an entity using a data URL, should not exceed 1 MB in file size. Files which exceed this size may cause performance issues.
* The control can communicate with other UiPath components, such as Processes, Queues, or Storage Buckets, only through the use of variables.
* Preprocessed CSS code, using LESS or SCSS, is incompatibile with the HTML control.
* The following APIs fail silently when used, due to security concerns:
  + Downloading using the `download` attribute.
  + Opening modals using `Window.alert()`, `Window.confirm()`, `Window.print()`, `Window.prompt()`.
  + Pointer and orientation locking.
  + Navigating the top-level browser context.
  + Entering full screen using `requestFullscreen()`.
  + Screen capturing using `MediaDevices.getDisplayMedia()`.
  + Accessing camera or microphone using `MediaDevices.getUserMedia()`.
  + Requesting payments.
  + Accessing the location using `navigator.geolocation()`.
  + Sharing data using `navigator.share()`.

## Debugging the code of a Custom HTML control

### Adding and filtering console logs of a Custom HTML control

1. Add a `console.log()` in the JavaScript editor.
2. Open the browser console by pressing F12, then select the **Console** tab.
3. In the console settings, check the **Selected context only** box.
4. From the JavaScript context dropdown at the top of the console page, select the `html-control-base.html` option for the desired HTML control.

The logs from the selected control are displayed in the console.

See the video for more details:

### Adding breakpoints

1. Add a `console.log()` in the JavaScript editor.
2. Open the browser console by pressing F12, then select the **Console** tab.
3. At the right-hand side of the log, click on the VM message.

The debugger opens. Select your breakpoint by clicking on the desired line number.

See the video for more details:

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `AccessibleLabel` | String | The description of the control, used by accessibility technologies such as screen readers. |
| `Hidden` | Boolean | Determines the visiblity of the **Custom HTML** control. If true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **Custom HTML** control is disabled. If true, disables interaction with the control at runtime. HTML, CSS and JavaScript content loads, but is unresponsive to user actions. |