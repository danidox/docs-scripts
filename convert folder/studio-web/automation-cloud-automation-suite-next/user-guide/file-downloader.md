---
title: "File Downloader"
visible: true
slug: "file-downloader"
---

## General

* **Source** - The source of the document users can download. Only URLs and variables of type AppsFile are accepted, configured as follows:
  ```
  New AppsFile("https://imageURL.com")
  ```
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Label -** The display text of the control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

No events.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::

* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Font** - The font attributes for both the label and the control text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Text` | String | Text used as a built-in label for the **File Downloader,** and displayed preceding the control. |
| `Tooltip` | String | Information text which appears when the user hovers over the File Downloader control. |
| `Value` | `AppsFile` | Current file to be downloaded. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |