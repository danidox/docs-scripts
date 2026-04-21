---
title: "Exporting logs"
visible: true
slug: "exporting-logs"
---

:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

!['Enterprise label' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555) This feature is only available if you are on the **Enterprise** licensing plan.

The Unified logs experience allows you to export logs in CSV format using one of the following methods:

* **Export** option in the user interface: From the **Audit logs** section of your organization or tenant, select **Export**.
* [Audit Logs APIs](https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/audit-logs): Use the Audit logs APIs.
* UiPath custom script: Run a UiPath-developed script to export logs from UiPath's long term audit log store.

For long-term retention or compliance purposes, both the unified and classic logs experience allow you to configure robot log exports to automatically send data from Orchestrator to Azure Blob Storage, AWS S3, or Google Cloud Storage, where log files are generated hourly and can be processed using your own BI or monitoring solutions.

## Exporting logs using script

If you are using the unified logs experience, you can use a dedicated script, to export audit logs that are no longer available through the Audit Logs interface. The script supports retrieving logs up to 2 years in the past.

This script is useful when:

* You need access to older audit logs for compliance or investigation purposes.
* You want to automate long-term log archival.

### Prerequisites

1. Copy the following script into a `.sh` file of your own:
   ```
   appId=$1
   appSecret=$2
   organizatioNameOrId=$3
   fromDate=$4
   toDate=$5
   mode=${6:-s}
   cloud=${7:-cloud}

   if [[ $# -lt 5 ]]; then
     echo "Error: Not all required input parameters provided."
     echo "Usage: $0 <appId> <appSecret> <organizatioNameOrId> <fromDate> <toDate> <mode>(optional: v for verbose, s for silent)"
     exit 1
   fi

   # Validate "fromDate" date format (MM/DD/YYYY)
   if ! date -d "$fromDate" &>/dev/null; then
     echo "Error: Invalid date format for 'fromDate'. Please use MM/DD/YYYY format."
     exit 1 
   fi

   # Validate "to" date format (MM/DD/YYYY)
   if ! date -d "$toDate" &>/dev/null; then
     echo "Error: Invalid date format for 'toDate'. Please use MM/DD/YYYY format."
     exit 1
   fi

   echo $(date +"%Y-%m-%d %H:%M:%S.%3N") "Start Getting UiPath Token."
   response=$(curl --data-urlencode -X POST "https://${cloud}.uipath.com/${organizationNameOrId}/identity_/connect/token" -$mode \
               -d "grant_type=client_credentials" \
               -d "scope=PM.Audit.Read" \
               -d "client_id=$appId" \
               -d "client_secret=$appSecret" \
               -H "Content-Type: application/x-www-form-urlencoded")

   access_token=$(echo "$response" | jq -r '.access_token')

   if [[ "$access_token" == null ]]; then
     echo "Error: Access token is null or empty in the response. Please verify the appId and appSecret."
     exit 1
   fi

   base_dir=$(date +"%Y-%m-%d%H:%M:%S.%3N")
   echo $base_dir "Start Downloading UiPath Platform Audit logs."
   # Define the base URL
   base_url="https://${cloud}.uipath.com/${organizatioNameOrId}/orgaudit_/api/query/downloadeventsfromlongtermstore"

   mkdir -p $base_dir
   # Iterate through time intervals
   current_date=$(date -u -d "$fromDate" +"%Y-%m-%dT%H:%M:%SZ")
   seconds_in_a_day=$((24*60*60))
   while [ "$(date -d "$current_date" +%s)" -le "$(date -d "$toDate" +%s)" ]; do
     next_date=$(date -u -d "$current_date + $(($seconds_in_a_day-1)) seconds" +"%Y-%m-%dT%H:%M:%SZ")
     
     # Construct the full URL with the current time interval
     formatted_current_date=$(date -u -d "$current_date" +"%Y-%m-%dT%H:%M:%SZ" | sed 's/\//%2F/g')
     formatted_current_date="${current_date}"
     formatted_next_date=$next_date | sed 's/\//%2F/g'
     formatted_next_date="${next_date}"
     full_url="$base_url?from=$formatted_current_date&to=$formatted_next_date"

     echo $full_url

     echo "Downloading UiPath Audit Log from $current_date to $next_date"
     curl -X GET "$full_url" -$mode \
          -H "Authorization: Bearer $access_token" \
          -o "${base_dir}/${current_date////-}_to_${next_date////-}.zip"  # Save the response to a file
     
     # Move to the next time interval
     current_date=$next_date
     one=1
     current_date=$(date -u -d "$current_date + $one seconds" +"%Y-%m-%dT%H:%M:%SZ")
   done

   for zip_file in "$base_dir"/*.zip; do
     zip_file_name="$(basename "$zip_file")"
     unzip -q "$zip_file" -d "$base_dir/auditlogs/"
     echo "Extracted ${zip_file_name%.*}"
     rm "$zip_file"
   done

   shopt -s nullglob
   for zip_file in "$base_dir/auditlogs"/*.zip; do
     zip_file_name="$(basename "$zip_file")"
     unzip -q "$zip_file" -d "$base_dir/auditlogs/${zip_file_name%.*}"
     for data_file in "$base_dir/auditlogs"/${zip_file_name%.*}/*.txt; do
       data_file_name="$(basename "$data_file")"
       mv "$data_file" "$base_dir/auditlogs/${data_file_name%.*}_${zip_file_name%.*}.txt"
       rm -r "$base_dir/auditlogs/${zip_file_name%.*}"
     done
     rm "$zip_file"
   done
   shopt -u nullglob

   echo $(date +"%Y-%m-%d %H:%M:%S.%3N") "Downloaded UiPath Platform Audit logs and saved them according to UTC date"
   ```
2. Run the script in a WSL (Windows Subsystem for Linux) environment and ensure the following tools are installed:
   ```
   sudo apt install dos2unix unzip jq
   ```
3. Prepare the script for execution using the following commands:
   ```
   dos2unix <script-name>.sh
   chmod +x <script-name>.sh
   ```
4. Create a confidential external application in your tenant and assign the following API scope: `PM.Audit.Read` (application).
5. Collect the following application credentials:
   * Application ID (`client_id`)
   * Application secret (`client_secret`)

### Steps

1. Set the required variables in your terminal:
   ```
   client_id='<your-client-id>'
   client_secret='<your-client-secret>'
   org_name='<your-org-name>'
   start_date='MM/DD/YYYY'
   end_date='MM/DD/YYYY'
   ```
2. Run the script using the following command: `./<script-name>.sh $client_id $client_secret $org_name $start_date $end_date`. For example:
   ```
   client_id='<clientId>'
   client_secret='<clientsecret>'
   org_name='test_org'
   start_date='09/01/2025'
   end_date='10/01/2025'
   ./<script-name>.sh $client_id $client_secret $org_name $start_date $end_date v
   ```

## Configuring robot logs export
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

To export Robot logs generated in your Orchestrator services to Azure, AWS S3, and Google Cloud Storage, follow the specific procedures described further. Logs are saved in a `.csv` file in the `uipathrobotlogs` container. The export is done on a per-tenant basis which facilitates the following:

* Storing logs that must be retained for compliance and audit purposes.
* Analyzing and visualizing log output in your own reporting or BI tools.
  :::note
  When configuring the log export page, we do not support backfilling of 30 days worth of logs.
  :::

1. Log in to your UiPath account.
2. Navigate to **Admin** and select the tenant in the panel on the left.
3. Select **Services**.
4. On the card for Orchestrator, select the **More** icon and select **Log Export Configuration**.

The **Configuration** panel opens at the right of the window.
5. Enable the **Send robot logs to custom storage** toggle.
6. Depending on your cloud offering, continue with the following steps:
   * Test Cloud:
     1. From the **Storage Type** drop-down, select the storage provider you want to export logs to. The following options are available:
        + **Azure**
        + **AWS S3**
        + **Google Cloud Storage**
          :::note
          The log export feature does not support **AWS KMS**.
          :::
     2. After performing the provider-specific steps, the `.csv` is generated. [Download .csv example](https://documentationexamplerepo.blob.core.windows.net/examples/AutomationCloud/RobotLogs.csv)
     3. Logs will be delivered on an hourly basis. This time interval is not configurable.
   * Test Cloud Public Sector and Test Cloud Dedicated:
     + Continue using procedure described in the [Azure](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/exporting-logs#azure) section.

### Azure
:::tip
You can configure static IPs to the allowlist and not open your network to all external IPs. Go to Settings > Networking > Public access > Firewall > Address range in Azure Blob Storage to add the static IPs. Check the [Configuring the firewall](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-the-firewall-for-cloud#insights) page for the full list of IPs. ![docs image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/558254)
:::

The following storage options are supported:

* Standard locally-reduntant storage (LRS)
* Standard geo-redundant storage (GRS)
* Standard read-access geo-redundant storage (RA-GRS)
* Standard zone-redundant storage (ZRS)
* Premium LRS

For more information on types of storage, check the [Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview) page from the official Azure documentation.

1. From the **Storage Type** drop-down, select **Azure Storage Account**.
   !['Configuration' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31763)
2. In the **Azure Blob Connection String** field, enter the blob connection string as retrieved from Azure Portal.
   !['Azure Portal Access keys' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31395)
3. On the **Container Name** field, enter the name of the container used to store the .`csv` in Azure. By default, that is `uipathrobotlogs`. If a custom container name is provided and it does not yet exist, the container will be created for you.
4. Select **Save**. A notification is displayed letting you know that you successfully configured robot logs export.
5. In your Blob Storage Account in Azure Portal:
   * Select **Network under Settings** in the left-hand panel.
   * Select **Allow access from > All networks**.
   * Select **Save** to save the changes.

     !['Networking' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31231)
6. Within an hour, a `.csv` log file is generated in the blob storage. The `.csv` is generated in the `uipathrobotlogs` container, under the following folder hierarchy `[tenant_key]/[year]/[month]/[day]/[hour]/output`. It is recommended to map one tenant to a container, as the tenant key is the only way to distinguish between tenants if multiple are routed to one container.
   !['Azure Portal overview' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30825)

### AWS S3
:::tip
You can configure static IPs to the allowlist and not open your network to all external IPs. Use access policies in AWS S3 to add deny all requests unless it is from the `aws:SourceIp` list as described in the [Bucket policies for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) page from the AWS S3 user guide. Check the [Configuring the firewall](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-the-firewall-for-cloud#insights) page from the Automation Cloud admin guide for the full list of IPs. ![docs image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/558278)
:::

1. From the **Storage Type** drop-down, select **AWS S3**.
   !['Configuration' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30769)
2. In the **Bucket Name** field, enter the name of the bucket as configured in AWS.
   :::note
   The same bucket name cannot be shared by multiple organizations.
   :::
3. In the **Region Name** field, enter the name of the regions where logs are to be exported. E.g., `us-west-1`.
4. Make sure to grant the IAM user provided via the prompt **s3:PutObject** and **s3:DeleteObject** access to your bucket.

### Google Cloud Storage

1. From the **Storage Type** drop-down, select **Google Cloud Storage**.
   !['Configuration' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30753)
2. In the **Bucket Name** field, enter the name of the bucket as configured in Google Cloud Platform.
   :::note
   The same bucket name cannot be shared by multiple organizations.
   :::
3. Grant the appropriate access to the UiPath® service account, as specified in the following prompt:
   1. In Google Cloud Platform, navigate to **Storage > Browser**.
   2. Find the bucket for which you want to edit permissions.
   3. Select the vertical ellipsis and select **Edit Bucket Permissions**.
   4. Select **Add members** and enter the service account you use to access the bucket.
   5. From the **Select a role** drop-down, select **Storage Object Admin**. For more information, refer to [Identity and Access Management](https://cloud.google.com/storage/docs/access-control/iam) in the GCP documentation.

      !['Grant access' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30853)

## Deleting log export settings

1. Expand the tenant you want to delete log export settings for.
2. For the Orchestrator service in that tenant, select **Log Export Configuration**. The **Configuration** right-hand panel is displayed.
3. Disable the **Send robot logs to custom storage** toggle.
4. On the **Delete Configuration** window, select **Delete** to confirm. The configuration is successfully deleted.