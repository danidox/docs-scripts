---
title: "Responsive app design"
visible: true
slug: "responsive-app-design"
---

A responsive app seamlessly adapts to various screen sizes and resolutions. Designing your app to be responsive and multi-device friendly also provides accessibility benefits. Use the **Container** control to achieve responsive app design.

Refer to [**Container**](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/container#container) for more information.

To configure a **Container** control to be responsive:

1. Select **Add control**, then **Containers,** and drag the **Container** inside your app.
   :::note
   Apps establishes the focus order for **containers** inside a **Container** layout control based on their position in the **Project Explorer** panel.
   :::
2. In the **Properties** panel, select **Style.**
3. Select **Allow wrapping** and **Allow scrolling.**
4. In **Size**, set the **Width** to a fixed value of your choice**.**
5. Select the **Additional options** button**.**
6. In **Maximum size,** set the M**aximum Width** to **100%.**
7. In **Advanced,** set the **flex grow** and **flex shrink** properties to `1`.

Controls within the **Container** wrap to the next line when there is not enough space available.

The **Container** uses all of the available space, but does not expand beyond the available space.