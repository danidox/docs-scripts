---
title: "Creating indexes"
visible: true
slug: "creating-indexes"
---

Creating indexes is supported only in shared folders.

To create an index, take the following steps:

1. From the **Indexes** page, select the **Add Index** button. The **Add Indexes** window is displayed.
2. Under **General Details**, add an **Index name** and a **Description**.
   :::note
   Index names cannot include the following characters: `(`, `)`, or `-`. Storage bucket names do not have these restrictions. Keep this in mind if you plan to use matching names for indexes and storage buckets.
   :::
3. Under **Data Settings**, configure your preferred data source: **Storage Bucket** or **Connector**. Ensure your data is stored within shared folders.
   1. If you choose **Storage bucket**:
      * Select the Orchestrator folder containing the bucket.
      * Choose the file type matching the files in your specified bucket. Select **All** for all file types. Note that certain file types or large scale of documents may take longer to ingest.
      * Upload files directly using one of the following options:
        + Drag and drop files into the **File Upload** box.
        + Select **Add files** to open the file picker.
      * Review the uploaded files. You can remove individual files before saving.
   2. If you select **Connector**:
      * Navigate to the desired Orchestrator folder for connection creation.
      * Select the appropriate Integration Service connector.
      * Choose an existing connection or create a new one.

After establishing the connection, select the **Data Source** location (the folder in the external storage system), and the **File type**. Optional: Enable **Include subfolders** to access nested directories.
4. Under **Additional settings**, specify the ingestion pattern:
   * **Basic** – Ingests text-based documents.
   * **Advanced** – Ingests both image-based and text-based documents. This option entails specific costs. For details, refer to [Context Grounding licensing](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/context-grounding-licensing).
5. Use the **Enable schedule** toggle to turn on scheduling to run ingestions automatically. When scheduling ingestions, you can configure the following options:
   * **Timezone** – Select the timezone in which the ingestion will run.
   * **Frequency** – Choose how often the ingestion runs:
     + **Daily** – Runs every day at a specified hour.
     + **Weekly (default)** – Runs on one or more selected weekdays at a specified hour.
     + **Monthly** – Runs on one or more selected dates of the month. You can also choose from two preconfigured options: Last day of the month, or Last working day of the month.
6. Select **Save**.