---
title: "Viewing audit logs"
visible: true
slug: "viewing-audit-logs"
---

The **Audit** tab on the **AI Trust Layer** page offers a comprehensive view of AI-related operations, with details about requests and actions, the products and features initiating requests, as well as the used models and their location. You can monitor all AI-related operations and ensure their compliance with your established guidelines and policies. Audit logs also provide visibility into the inputs and outputs for Gen AI Activities, Agents, Autopilot, Autopilot for Everyone, and Document Understanding generative features. Note that you can view log entries created in the last 60 days.

The audit data is displayed as a table, with each of its columns providing a specific information about the AI-related operations:

* **Date (UTC)**: This displays the exact date and time,when each operation was requested. It allows for accurate tracking of requests according to their chronological order, facilitating timely audits.
* **Product**: The specific product that initiated each operation. This visibility allows tracing any operation back to its originating product for enhanced understanding and accountability.
* **Feature**: The specific product feature that initiated the operation, facilitating issue traceability to particular features, if any occurred.
* **Tenant**: The specific tenant within your organization that initiated the operation. This insight enables a more detailed overview and helps recognize patterns or issues at the tenant level.
* **User**: The individual user within the tenant who initiated the operation. It allows for tracing activities at a granular user level, enhancing the oversight capabilities. For GenAI Activities, the user is represented by the person who created the connection. An N/A value indicates a service-to-service communication where a user is not available.
* **Model Used**: The specific AI model employed to process each operation. This insight provides a better understanding of which models are handling which types of requests.
* **Model Location**: The location where the used model is hosted. This information can assist potential troubleshooting or audit requirements that could arise from model performance in specific locations.
* **Status**: The status of each operation—showing if it was successful, failed, or blocked. This quick way of identifying operational issues is crucial for maintaining a smooth, efficient environment.

Additionally, the filtering capability allows you to narrow down your audit based on criteria such as the date, product, used model, status, or source. The **Source** filter allows you to choose between viewing all calls, only UiPath-managed calls, or exclusively custom connection calls (using customer-managed subscriptions, as defined in [Configuring LLMs](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-llms#configuring-llms)).

Furthermore, when you select an entry from the Audit table, you can access a **Details** section for a more in-depth review, which includes all data available in the Audit table, as well as the LLM call source and the exact deployment associated with the call.
:::warning
Audit log input and output fields may appear temporarily empty when viewing recent entries. This is a known latency issue and data typically becomes available shortly after.
:::

## Exporting audit logs

  ![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555) This feature is available on the Enterprise licensing plan.

The **Export** option enables you to export audit logs.

### Exporting logs

**Triggering and downloading an export**
1. Go to **Admin > AI Trust Layer** and select the **Audit** tab.
2. Select **Export**.
3. Choose to export with or without inputs and outputs. Only one export can be processed at a time. You must wait for the current export to complete before initiating a new one.
   :::note
   The system processes exports asynchronously, with those including inputs and outputs requiring additional time.
   :::
4. Upon export completion, you receive notifications via email and in the **Notifications** panel.
5. Exported files are accessible through the **View Exports** option in the **AI Trust Layer > Audit** tab for a period of seven days.

The interface displays the number of remaining exports with inputs and outputs for the current month. Please note that once you reach the monthly limit, exporting with inputs and outputs will be suspended until the next month.

**Filtering data for exports**

Use the available filter options to narrow down the data you wish to export:

* **Product** – Select the products you want to export data from.
* **Model Used** – Choose specific models to filter the export.
* **Status** – Filter by Failed or Successful requests. A Failed status appears when an Automation Ops policy blocks a model, product, or feature.
* **Date** – Select a time range (e.g., Last day, Last week, Last 30 days) and choose between local or UTC time zones.

Filtering allows you to bypass the size and maximum rows per export limits, by selecting only the data you want to export.

### Viewing exports

The **View Exports** pane displays the exported data, the user who generated the request, and the status of the export. This pane is also where you can download your exports by selecting the **Download** action.

If an error occurs, your monthly export limit is not affected, and you can generate a new export.

Table 1. Export statuses

| Status | Definition |
| --- | --- |
| Pending | The request is being processed. The status transitions to Completed or Failed once processing is complete. |
| Failed | Sometimes, a request can fail. A failed request does not count towards your monthly export allowance if you are exporting with inputs and outputs. |
| Completed | The processing is complete, and the file is ready for download. |
| Downloaded | The file was downloaded. |
| Expired | The file has reached the end of its 7-day availability window and can no longer be downloaded. |

**CSV structure**

Audit logs consist of the following columns:

Table 2. Audit logs CSV structure

| Column name | Type | Description |
| --- | --- | --- |
| Date | DateTime | When the action was registered. |
| ActionId | String/UUID | A unique identifier for the specific action. Can be used to further trace information across the UiPath platform and get more insights. |
| Product | String | Name of the product where the action took place. |
| Feature | String | Name of the feature that triggered the action. |
| User | String | The user who triggered the action. |
| Tenant | String | The tenant where the action took place. |
| Model | String | The model that processed the input. |
| ModelLocalization | String | The region of the model. |
| Status | String | Status for the action which can be failed or succeeded. |

**Export limitations**

Inputs and outputs longer than 32,767 characters are truncated from the end. A message is automatically added to the truncated row to inform you the truncation of the information took place.

Inputs and outputs are processed to remove commas (”,”) so that you can easily process information without CSV malfunctions.

**License duration and grace period**

During the grace period, previously stored data remains accessible. However, no new data is saved in either Warm or Cold storage during this time. It's important to note that the data in Cold storage will eventually expire. The expiration timeline is calculated based on your license duration plus an additional two or three years, depending on your previous license type. This approach ensures that you have ample time to access your historical data even after your license has expired.

### Data retention and storage

Data is stored in the tenant region you selected when creating the organization and the tenant, according to the following rules:

Table 3. Export limits per license type

| Feature | Enterprise Standard | Enterprise Advanced |
| --- | --- | --- |
| Active storage (UI Visible) | 60 days | 60 days |
| Warm storage (Export available) | 90 days | 180 days |
| Cold storage (Archived) | 2 years | 3 years |
| Maximum rows per export | 200K | 200K |
| Maximum export size | 1 GB | 1 GB |
| Exports with inputs and outputs | 4 per month | 4 per month |
| Exports without inputs and outputs | Unlimited | Unlimited |

**Disabling the storage of inputs and outputs**

You can disable saving inputs and outputs in exports by deploying an Automation Ops policy applicable at tenant, group, or user level. For details, refer to [Settings for AI Trust Layer Policies](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies).

Once this feature is disabled, the inputs and outputs are no longer saved and cannot be recovered.
:::important
UiPath cannot recover the data if you choose not to save it. Before making this decision, ensure compliance with your company's policies and relevant local or global regulations.
:::

## Handling PII and PHI data in audit logs

When using generative AI features in UiPath, it's important to understand that audit logs may include Personally Identifiable Information (PII) or Protected Health Information (PHI). These details can appear in both the input prompts sent to Large Language Models (LLMs) and in the responses they generate. This applies to interactions executed through both attended and unattended automations.

The **Details** section of each audit log entry displays the full input and output content when prompts saving is enabled. This includes metadata such as:

* Action ID
* Tenant
* Product
* Feature
* User
* Timestamp

### Hiding sensitive data for compliance

If your compliance rules require hiding PII and PHI data in audit logs, you can configure the AI Trust Layer policy to control visibility:

1. Go to **Automation Ops™ > Governance** and select or create an AI Trust Layer policy.
2. In the **Feature Toggles** tab, make sure to set the **Enable prompts saving for Audit?** option to **No**.

With this setting, neither prompts nor LLM outputs are retained in the audit logs. The log will display the entry metadata, but the input/output content will appear as “Blocked by policy.”
:::note
This configuration allows you to hide sensitive content from log entries, maintain compliance requirements, and control visibility of sensitive data while preserving audit capabilities. Once hidden, you cannot recover the prompts for further use.
:::

### Viewing PII logs

**Redacting PII and PHI**

You can choose to retain audit logs while masking sensitive content by enabling the PII masking option. For details, refer to [PII masking](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/pii-masking).

The **AI Trust Layer Audit Log** offers full visibility into how personally identifiable information (PII) is handled during interactions with Large Language Models (LLMs).

With the audit log, you can:

* Verify whether PII was detected in a given prompt.
* Confirm if masking (pseudonymization) was applied to the detected entities.
* Review the actual input sent to the LLM, ensuring that no raw PII was exposed.

This level of transparency supports compliance efforts, builds trust with stakeholders, and provides a detailed audit trail for every interaction where PII in-flight masking is enabled.
:::note
Use the audit log to validate that sensitive data is consistently protected during AI-powered automations.
:::