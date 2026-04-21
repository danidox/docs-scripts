---
title: "Responsive and mobile-friendly embedded apps"
visible: true
slug: "responsive-and-mobile-friendly-embedded-apps"
---

You can add logic to your external webpage, making your embedded app responsive to screen size changes. This can be useful if you use small-screen devices, such as mobile phones, because it mitigates the need for you to scroll multiple times to see the embedded app content.

If you do not add this logic to your webpage, the embed maintains a static height and displays a scroll bar.

## Designing responsive and mobile-friendly embedded apps

1. Allowlist the communications with your external domain, by adding an additional parameter to your existing embed or iFrame: `&target=https://mywebsite.com`. The following code shows an example:
   ```
   <embed title="Embedded app" src="<PUBLIC-APP-URL>?el=VB&target=https://mywebsite.com">
   ```
2. To make your embed aware of size updates, add the following JavaScript logic to the webpage hosting the embedded app:
   :::note
   The specific values vary depending on the design of your app.
   :::
   ```
   <script>  
   const MIN_HEIGHT = 800; // Minimum height of the app  
   var embed = document.querySelector('embed');  window.addEventListener('message', function(event) {  
   if (event.data.event === "APP_CONTENT_HEIGHT_UPDATED" && event.data.height) {  embed.style.height = Math.max(event.data.height, 800);  
   }  
   if (event.data.event === "APP_CONTENT_RESIZED" && event.data.height !== MIN_HEIGHT) {  
   if(event.data.height > 0) {  embed.style.height = Math.max(parseInt(event.data.height) - 10, 850);  
   }  
   }  
   }); 
   </script>
   ```

The script performs the following operations:

* When a control is added to or removed from the app, the script triggers the `APP_CONTENT_HEIGHT_UPDATED` event, and updates the height of the `embed` variable.
  + The `APP_CONTENT_HEIGHT_UPDATED` event triggers `APP_CONTENT_RESIZED`, which reduces the height of the `embed` variable by 10 pixels.
    - The `APP_CONTENT_RESIZED` event triggers another `APP_CONTENT_RESIZED` event, which again reduces the height of the `embed` variable by 10 pixels.

The script repeats these operations, until:

* The `embed` variable is at the minimum height where a scroll bar is not required to view the app.
* The `embed` variable is reduced to the initial value, which is specified by `MIN_HEIGHT`.

### Demo

#### Responsive and mobile-friendly embedded app

#### Introduction

This webpage embeds a mobile app inside a device frame. The app displays content responsively for mobile usage. An iFrame loads content dynamically, and displays it inside the device frame. The app content adjusts its height based on its content, in order to prevent scrollbars.

##### Demo embedded app - try it yourself

Use the buttons inside the iFrame to interact with the app and modify the content.

|  |
| --- |
| [Use demo app on GitHub](https://uipath.github.io/apps-demo-pages/app-content-height-updates/) |