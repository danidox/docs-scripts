---
title: "Generating tables from documents"
visible: true
slug: "generating-tables-from-structured-documents"
---

To generate a table from a document within Autopilot:

1. In the chat box, drag and drop the document. Alternatively, use the **Attach file** button.
   :::note
   * You can upload PDFs or images of the document.
   * You can use the **Capture screenshot** or the **Capture active window** to automatically add the image of the document to Autopilot.
   :::
2. Write the prompt "Extract information from this invoice.", then select **Send**.

Autopilot uses Document Understanding to extract text from the document and provides a summary of the extracted information.
3. After Autopilot responds, write the prompt "Generate a table with this information."

Autopilot generates a table with the information in the invoice, and displays a **Paste in** button. This is where Clipboard AI steps in.

   :::note
   The **Paste in** button displays the last active application. For example, if you were using Excel before rendering the table in Autopilot, the button shows "Paste in Excel".
   :::