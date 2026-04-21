---
title: "Pasting from multi-line tables into a web form"
visible: true
slug: "copying-from-multi-line-tables-and-pasting-into-a-web-form"
---

In cases where you need to fill in the same web form for multiple entries, you can use the Autopilot and Clipboard AI to assist you in copying, validating, and pasting the required data.

For this to work:

* headers in the table must correspond with the fields in the web form.
  :::note
  In case the headers do not correspond with the fields, use the Clipboard AI mapper to mitigate the association.
  :::
* the browser window with the web form is active

To copy the information from the multi-line table to a web form using the integrated Clipboard AI:

1. Select **Paste in** and select the name of the browser window with the web form.
2. Once the values in the first row were pasted in the web form, you can submit the form. Autopilot displays the message "Row 1 was pasted" under the table.
   :::important
   You must manually submit the form after every paste operation.
   :::
3. To continue filling out the same web form with the values in the next row, select **Paste next row in [Web form name]**.
4. Repeat step 3 until all the entries in the table have been pasted. Autopilot displays the message "All rows have been pasted."