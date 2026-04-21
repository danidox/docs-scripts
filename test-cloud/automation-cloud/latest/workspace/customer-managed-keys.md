---
title: "Customer-managed keys"
visible: true
slug: "customer-managed-keys"
---

## Customer-managed keys for Test Cloud and Test Cloud Public Sector

This procedure applies only for Test Cloud and Test Cloud Public Sector

!['Enterprise' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555) Depending on your licensing plan , this feature is available as follows:

* Flex licensing: This feature is available for the Standard and Advanced platform plans.
* Unified Pricing licensing: This feature is available only for the Enterprise platform plan.
:::warning
Enabling this feature has serious implications with regards to data access. Should key issues arise, you risk losing access to your data.
:::

The following table describes common problematic scenarios and their solutions.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Scenario
    </p>
   </th>
   <th>
    <p>
     Solution
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d58454e56">
    <p>
     Your credentials for accessing the Azure Key Vault (AKV) have expired or have been deleted.
    </p>
   </td>
   <td headers="d58454e59">
    <p>
     If you can still log in using your email and password (non-SSO)...
    </p>
    <p>
     ... and if you
     <em>
      are
     </em>
     an organization administrator, you can update your credentials in the
     <strong>
      Encryption
     </strong>
     section of the organization
     <strong>
      Admin
     </strong>
     page.
    </p>
    <p>
     ... and if you
     <em>
      are not
     </em>
     an organization administrator, you can ask, via a support ticket, to be promoted to an administrator role; you can then update
                                 your credentials in the
     <strong>
      Encryption
     </strong>
     section of the organization
     <strong>
      Admin
     </strong>
     page.
    </p>
    <p>
     If you can no longer log in, provide your organization ID through a support ticket, and we can invite and promote you as an
                                 administrator. You can then update your credentials in the
     <strong>
      Encryption
     </strong>
     section of the organization
     <strong>
      Admin
     </strong>
     page.
    </p>
    <p>
     Once you regain login access, we recommend that you create a new AKV key and credentials set, then configure the customer-managed
                                 key using this new information, thus ensuring that nobody else has access to your credentials.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d58454e56">
    <p>
     Your AKV key has expired.
    </p>
   </td>
   <td headers="d58454e59">
    <p>
     Your customer-managed key still works, but we recommend that you switch to a new key.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d58454e56">
    <p>
     Your AKV key was deleted.
    </p>
   </td>
   <td headers="d58454e59">
    <p>
     You can restore your AKV key from the Azure portal during the retention period.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d58454e56">
    <p>
     Your AKV key was purged, but it had a backup.
    </p>
   </td>
   <td headers="d58454e59">
    <p>
     You can restore the key from the Azure portal backup. By default, the restored key has the same ID as the original one, which
                                 you should not change.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d58454e56">
    <p>
     Your AKV key was purged and it did not have a backup.
    </p>
   </td>
   <td headers="d58454e59">
    Warning:
    <p>
     There is no solution for this scenario. In this situation, your UiPath&reg; customer data is lost.
    </p>
   </td>
  </tr>
 </tbody>
</table>

### Overview

In addition to the standard TDE at the storage level, certain services also employ Implicit Application-Level Encryption (ALE). This means that data is encrypted at the application layer before being stored, providing an added layer of security.

Furthermore, some services/resources offer an optional, user-driven encryption known as Optional (Opt in) ALE. This gives you the option to decide whether those services/resources should employ ALE or not. **For the list of services or resources, and the types of encryption relevant to them, please refer to the [encrypted data](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/encryption#encryption-per-service) page in our documentation.**

For services with ALE, either implicit or opted in for, you have the ability to choose who handles the encryption key. It could be managed by either UiPath or yourself. To assist in this, [Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview) supports secret versioning, allowing you to generate a secret to use in configuring your key at the organization level.

After you enable the customer-managed key, previously backed up data is not re-encrypted, and any existing backups are removed once they expire. Only new data is encrypted using this option.

### Customer-managed keys explained

In the customer-managed key architecture, UiPath products or platform services (such as UiPath Orchestrator or UiPath Identity Service) generally encrypt sensitive customer data before storing it. When data access is required, the product or service calls your key management infrastructure to get the decryption key. This gives you control over the encrypted data in UiPath because you have the ability to refuse to return the key.

This process involves the following components:

* The key management service (KMS) - this is UiPath's internal tool, developed for key encryption purposes.
* The data encryption key (DEK or KMS DEK) - used to encrypt plain text data. Generally, the DEK is generated by the KMS or by UiPath's internal key vault, and is never stored anywhere in clear text.
* The key encryption key (KEK) - used to encrypt the DEK. The process of encrypting a key is known as key wrapping. Generally, the KEK is generated by you, it is stored in your key vault, and it constitutes the actual customer-managed key which is controlled by your key management service.
* The encrypted data encryption key (EDEK) - this is the DEK that is wrapped by the KEK. Generally, this key is stored by the service provider (such as Orchestrator); consequently, whenever a service needs to access encrypted data, the service calls the customer’s key management service to obtain the KEK needed to decrypt the EDEK, and to produce the DEK which is then used to decrypt the data.
* The UiPath internal key - this is used to encrypt data columns, including the CMK and the KMS DEK.

This diagram illustrates how the various components involved in enabling customer-managed keys work together:

  !['UiPath Key Management Service (KMS)' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30701)

### Enabling the customer-managed key
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::
:::important
Enabling customer-managed keys (CMK) has significant implications for data accessibility. If the key becomes unavailable or misconfigured, you may lose access to your data. If you lose your key, you can no longer connect to the vault. You should therefore always create a backup of the key on the Azure portal or in a secure key vault separate from Azure, in accordance with your organization's security policies. Depending on your cloud offering, the Azure Key Vault must be hosted in the Microsoft Azure Government cloud to comply with cloud boundary requirements.
:::

To enable customer-managed keys, you must configure the Microsoft Entra ID application representing Test Cloud to access the key encryption key in your Azure Key Vault.

Depending on your cloud offering, you can choose one of the following methods to configure the Microsoft Entra ID application:

* (Recommended) Automated setup: Use the UiPath-managed Microsoft Entra ID application ([multi-tenant model](https://learn.microsoft.com/en-us/entra/identity-platform/application-model#multitenant-apps)) for the following benefits:
  + No secrets or certificates to manage.
  + Quick and reliable setup.
  + UiPath maintains the Microsoft Entra ID application for you.
* Manual setup with a custom Microsoft Entra ID application registration: Use your own Microsoft Entra ID application and manage its configuration manually, with the following considerations:
  + You must create and manage application credentials.
  + Credentials expire and require periodic updates.
  + If credentials are not updated before they expire, users are blocked from signing in.

#### Automated setup with UiPath-managed Microsoft Entra ID application (Recommended)

Use this method if you want to simplify configuration and avoid managing secrets or certificates. UiPath recommends this approach for most organizations.

#### If you are a Microsoft Entra ID and organization administrator

If you are both a Microsoft Entra ID administrator and an organization administrator, take the following steps to configure the integration using the UiPath-managed multi-tenant application:

1. In the organization, go to **Admin > Security > Encryption**.
2. Choose **Customer managed key** and confirm the selection by entering your organization name in the confirmation dialog.
3. Select **UiPath managed multi-tenant application (Recommended)**.
4. Select **Grant consent**, then sign in with your Microsoft Entra ID account. After you grant consent, UiPath creates a Microsoft Entra ID application in Azure that represents your organization.
5. Create your key encryption key and set up Azure Key Vault.
6. Enter the Azure Key Vault key URI of the key encryption key.
   * If you provide a versionless key URI, UiPath uses the latest key version automatically (key rotation enabled).
   * If you provide a versioned key URI, UiPath encrypts all data with that specific key version.
7. Select **Test and save** to activate the integration. If an error occurs, verify your credentials and try again.

#### If you are an organization administrator only

If you do not have administrative privileges in Microsoft Entra ID but are an organization administrator, take the following steps to request admin consent and complete the integration:

1. In the organization, go to **Admin > Security > Encryption**.
2. Select `Customer managed key` and confirm the selection by entering your organization name in the confirmation dialog.
3. Select **UiPath managed multi-tenant application (Recommended)**.
4. Select **Grant consent**, then sign in with your Microsoft Entra ID account. Because you do not have Microsoft Entra ID admin rights, you should see one of the following prompts:
   1. **Request approval**, as depicted in the [Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/admin-consent-workflow-overview): Request admin approval. After your Microsoft Entra ID administrator approves the request, continue to the next step.
   2. **Needs admin approval**, as depicted in the [Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity-platform/application-consent-experience#app-requires-a-permission-that-the-user-has-no-right-to-grant): Ask your Microsoft Entra ID administrator to take the following steps:
      1. Navigate to this [URL](https://login.microsoftonline.com/common/oauth2/v2.0/authorize?scope=openid&prompt=select_account&response_type=code&redirect_uri=https://cloud.uipath.com/portal_/testconnection&state=1234&client_id=4ca9aa42-b0ea-4ceb-b2b1-17fa40827280) to open the Microsoft Entra ID consent prompt.
      2. Select **Consent on behalf of your organization**, then **Accept**.
5. After you receive confirmation that admin consent was granted, create your encryption key and set up Azure Key Vault, then return to UiPath and repeat steps 1 through 4.
   * A successful sign-in indicates that the integration is configured correctly.
   * If the sign-in fails, ask your Microsoft Entra ID administrator to verify that consent was granted properly.
6. Enter the Azure Key Vault key URI of the key encryption key.
   * If you provide a versionless key URI, automatic key rotation is enabled, and Test Cloud uses the latest key version.
   * If you provide a versioned key URI, Test Cloud encrypts all data with that specific key version.
7. Select **Test and save** to activate the integration. If an error occurs, verify your credentials and try again.

#### Manual setup with custom Microsoft Entra ID application registration

If you prefer to configure your own Microsoft Entra ID application instead of using the UiPath managed multi-tenant application, take the following steps. This option requires managing your own credentials and maintaining them over time. TOPLEVELNOTEMARKER
   :::important
   Credentials created through manual setup will expire periodically. You must renew them before expiration to avoid service disruptions. To reduce this operational overhead, consider using the [automated setup with UiPath managed Entra ID application](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/microsoft-entra-id-integration-for-automation-cloud-and-automation-cloud-public-sector#automated-setup-with-uipath-managed-microsoft-entra-id-application-(recommended)).
   :::

1. Create the Microsoft Entra ID app registration.
   1. In the [Microsoft Entra admin center](https://entra.microsoft.com/), go to **App registrations** > **New registration**.
   2. Enter a name of your choice.
   3. Set **Supported account types** to **Accounts in this organizational directory only**.
   4. Complete the registration.
2. Create credentials.

Go to **Certificates & secrets** in your app registration and choose one of the following methods:
   * To use a client secret:
     1. Select **New client secret**.
     2. Save the generated secret value. You will need this later.
   * To use a certificate:
     1. In a new browser tab, navigate to **Azure Key Vault**.
     2. Create a certificate:
        + Subject: `CN=uipath.com`
        + Content type: `PEM`
        + Maximum size: less than 10 KB
     3. Download the certificate in `.pem` format.
     4. Open the `.pem` file in a text editor. It should contain the following sections:
        + `-----BEGIN PRIVATE KEY----- / -----END PRIVATE KEY-----`
        + `-----BEGIN CERTIFICATE----- / -----END CERTIFICATE-----`
     5. Create a new `.pem` file containing only the lines between `BEGIN CERTIFICATE` and `END CERTIFICATE`.
     6. In the **Certificates & secrets** section of your app registration, upload this new `.pem` file.
     7. Keep a copy of the certificate. You will need it later to complete the integration.
        :::important
        Most credential types eventually expire. To prevent user sign-in issues, update the configuration before credentials expire. To avoid this overhead, use the [automated setup with the UiPath-managed Microsoft Entra ID application](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/customer-managed-keys#automated-setup-with-uipath-managed-microsoft-entra-id-application-(recommended)).
           :::
3. Collect integration details.

Gather the following values and provide them to the organization administrator:
   * Application (client) ID
   * Directory (tenant) ID
   * Client secret or certificate
4. Create your key encryption key and set up Azure Key Vault.

Prepare your encryption key and note the Azure Key Vault key identifier. Choose one of the following formats:
   * **Versionless key URI:** Enables automatic key rotation. UiPath always uses the latest key version.
   * **Versioned key URI:** Locks encryption to a specific key version. UiPath encrypts all data using that version.
5. Activate the integration in the organization.
   1. Sign in to UiPath as an administrator.
   2. Go to **Admin** > **Security** > **Encryption**.
   3. Select **Customer managed key**, and confirm the selection by entering your organization name.
   4. Select **Custom application registration ID and secret**.
   5. Enter the following details collected earlier:
      * Directory (tenant) ID
      * Application (client) ID
      * Client secret or certificate
      * Azure Key Vault key identifier
   6. Select **Test and save** to activate the integration.

If you receive an error message, check your credentials and try again.

#### Creating the key encryption key and setting up Azure Key Vault

Before you begin, review the following requirements and recommendations for using Azure Key Vault with Test Cloud.

* You can create the Key Vault in any region, but we recommend using the same region as your Test Cloud organization.
* UiPath requires access to the Key Vault used for the customer-managed key. To limit scope, we recommend creating a dedicated vault for this purpose.
* The feature works with any key size supported by Azure Key Vault.
* To perform cryptographic operations, you must grant **Wrap Key** and **Unwrap Key** permissions. These permissions are required regardless of whether you use [Azure RBAC](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli) (Role-Based Access Control) or [Key Vault access policies](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?WT.mc_id=Portal-Microsoft_Azure_KeyVault&tabs=azure-portal) to manage access.

To create a key encryption key and configure Azure Key Vault, take the following steps:

1. In the [Microsoft Azure portal](https://portal.azure.com/), go to **Azure Key Vault** and either select an existing vault or create a new one.
2. Create a new key and copy the key URI. You need the URI to configure it in Test Cloud.

Choose one of the following options for the key URI:
   * Versionless key URI: Enables automatic key rotation. Test Cloud always uses the latest version of the key.
   * Versioned key URI: Locks encryption to a specific key version. Test Cloud encrypts all data using that version.
3. Grant access to the previously created Microsoft Entra ID application.

Use either Azure RBAC or Key Vault access policies to grant the required permissions.
4. Return to Test Cloud to complete the configuration.

### Editing the customer-managed key

Once you enable this option, you can also edit any details related to the connection. To that end, select **Edit connection** under the **Customer managed key** option, and change any information as needed.

### Key rotation

It is good practice to routinely rotate your keys, so as to ensure the continuous protection of your encrypted data against any potential breaches.

#### Manual key rotation

Manual key rotation involves changing the entire CMK configuration itself. While you could change the whole configuration, it is recommend to change only the key identifier, or key version, to minimize breaking changes.

To perform manual key rotation, take the following steps:

1. Create a new key in the Azure Key Vault you previous configured.
2. In your organization, go to **Admin** > **Security**.
3. Under **Customer managed key**, select **Edit connection**.
4. Replace the existing key identifier with the new key URI.
:::note
Key rotation works only if both the old key and the new key remain valid.
:::

#### Automatic key rotation

Automatic key rotation enables UiPath to use the latest version of your key automatically, based on the rotation policy defined in Azure Key Vault. This approach reduces manual effort and improves security.

To enable the automatic key rotation process, take the following steps:

1. In Azure Key Vault, create a **rotation policy** for your key.
2. In your organization, go to **Customer managed key** configuration and provide the **versionless key identifier**. For configuration steps, refer to [Enabling the customer-managed key](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/customer-managed-keys#enabling-the-customer-managed-key).
3. After each key rotation in Azure Key Vault, UiPath automatically fetches and applies the latest key version. UiPath automatically checks for new key versions every hour. When a new version becomes available, it is retrieved and applied without requiring manual updates.
:::important
* Do not disable or modify access permissions for older key versions. Both the previous and current key versions must remain
accessible to maintain uninterrupted access to encrypted data during the rotation process.
* You can view both manual changes to the
customer-managed key configuration, such as updates to the key identifier, and automatic key rotation events in the **Audit logs** section under **Admin** in the organization .
:::

### Licensing downgrade

If your **Enterprise** plan expires, depending on your cloud offering, you are automatically downgraded to the **Free** plan, or you are downgraded to a view-only state. This is what you can expect in terms of data encryption:

* The **Customer managed key** option is still enabled for you, but it is greyed out in the interface. As such, you can no longer edit its values, such as changing key vault details.
* You can switch to **UiPath managed key (Default)**, but you will not be able to revert to **Customer managed key** until your plan is upgraded to **Enterprise**.

### Best practices for using customer-managed keys

There are some important details to keep in mind before you start using customer-managed keys:

* Once you start using a new key as part of the key rotation process, the old one can no longer be used to access and encrypt data. It is therefore important to keep any old keys in the key vault, namely to disable them instead of deleting them. This is especially important in disaster recovery scenarios, where UiPath might need to revert to a backup of an older version of the database. If that backup uses one of your old keys, you can rotate to it to regain data access. If you choose to remove a key, it is important that you use the [soft-delete](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) feature.
* If you lose your key, you can no longer connect to the vault. You should therefore always create a backup of the key on the Azure portal or in a secure key vault separate from Azure, in accordance with your organization's security policies.
* If you are leveraging Single Sign On to access UiPath services, you may consider creating a local account to function as a break glass account. Because the external identity provider information is included in the data encrypted by the customer managed key, SSO accounts will be inaccessible should your key vault become unreachable.
* For security purposes, users that do not have top-level administrator privileges should not have purge rights over the customer-managed key.
* If you no longer want UiPath to have access to your data, you can disable the key from the Azure Key Vault, as shown in the following image:
  !['Azure Key Vault' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31439)

Find out more about Azure Key Vault [recovery actions](https://learn.microsoft.com/en-us/azure/key-vault/general/key-vault-recovery?tabs=azure-portal).

## Customer-managed keys for Test Cloud Dedicated

You can use your own encryption key to protect data stored in UiPath-managed Azure resources in Test Cloud Dedicated environments. This gives you full control over key rotation, access permissions, and compliance requirements.

UiPath supports cross-tenant Customer-Managed Key (CMK) configurations. Your key resides in your own Azure Key Vault, while the encrypted resources remain in UiPath’s tenant.
:::warning
Enabling customer-managed keys affects how UiPath accesses your encrypted data. If the key or its access configuration becomes unavailable, you may lose access to your data.
:::

### Supported resources

You can use customer-managed keys to encrypt the following UiPath-managed resources:

* Azure Storage accounts
* Azure SQL Servers
* Azure Disks
* Snowflake
:::note
Azure Databricks and Azure Event Hubs do not support cross-tenant customer-managed keys (CMK). These services require the Key Vault to reside in the same Microsoft Entra tenant as the associated Azure resources, and therefore cannot be encrypted using cross-tenant CMK. These services are used internally by Insights to support telemetry and analytics processing:
* **Azure Event Hubs**: Buffers streaming telemetry, such as robot logs
and execution events, job execution data, queue item events, real-time monitoring. Data in Event Hubs is transient and not stored long term.
* **Azure Databricks**: Processes and stores analytical data, including
real-time monitoring data, historical aggregations, and processed robot execution metrics. These services use Microsoft-managed keys for encryption at rest and cannot be configured with customer-managed keys.
:::

### Architecture

When you enable customer-managed keys in a Dedicated environment, UiPath uses a cross-tenant encryption model with federated identity. This allows encryption keys to remain fully controlled by you, even though the data is stored in UiPath-managed Azure services.

The architecture is based on the Azure pattern for secure data encryption at rest using CMK and federated identity.

Key components of the capability's architecture are:

1. **UiPath tenant**: Hosts the Azure resources that require encryption.
2. **Your tenant**: Hosts the Azure Key Vault and the customer-managed key.
3. **Multitenant application**: Registered by UiPath and installed in your tenant to enable secure cross-tenant access.
4. **Managed identity**: Assigned to the UiPath app, used to authenticate against your Key Vault.
5. **Federated credentials**: Allow the UiPath app to use the managed identity without storing secrets.
6. **Azure Key Vault**: Stores your customer-managed key.

The encryption flow is as follows:

1. You raise a support ticket to receive the application’s registration ID and name.
2. UiPath registers a multitenant application and attaches a user-assigned managed identity.
3. You install the application in your Azure tenant.
4. You create the key in your Key Vault and share the key URI (with version) with UiPath.
5. You assign the following permissions to the application via Azure RBAC: `get`, `wrapKey`, `unwrapKey`.
6. UiPath configures the relevant Azure resources to use the key for encryption and decryption.

UiPath never stores your key. All operations are performed securely using Azure APIs and your own access controls.

### Prerequisites

Before enabling customer-managed keys, ensure you meet the following requirements:

* **Azure Key Vault** requirements:
  + Soft delete and purge protection are enabled.
  + Resource locks are configured on the Key Vault and keys.
  + Key must be of type RSA 2048-bit. These configurations prevent accidental deletion and ensure recoverability.
* Permissions and configuration:
  + Raise a support ticket to request UiPath a multi-tenant application registration ID and name.
  + You must create the key in your tenant and authorize access to it for UiPath’s application.
  + Key rotation is supported if your key has versioning enabled.

### Steps

1. Create or select an Azure Key Vault in your Azure tenant.
2. Configure the Key Vault and encryption key according to the following requirements:
   * Enable **soft delete** and **purge protection**. Ensures that deleted keys or vaults can be restored for up to 90 days.
   * Apply a **resource lock** on both the Key Vault and the key Prevents accidental deletions or changes.
   * Select **RSA 2048-bit** as the key type.
   * Ensure the Key Vault is in the same region as your Azure Disk resources (required for Azure Disk encryption).
   * Under **Networking**, select **Allow trusted Microsoft services to bypass this firewall**.For detailed steps, refer to [Configure cross-tenant customer-managed keys for a new storage account - Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-configure-cross-tenant-new-account?tabs=azure-portal#the-customer-grants-the-service-providers-app-access-to-the-key-in-the-key-vault). .
3. Install the UiPath multitenant application in your Azure tenant using the information provided by the support team.
4. Assign the Azure RBAC role **Key Vault Crypto Service Encryption User** to the UiPath application so it can access the Key Vault.

Alternatively, grant the UiPath application a **Key Vault Access Policy** with the following permissions: `get`, `wrapKey`, and `unwrapKey`.
5. Share the key URI with UiPath through the previously created support ticket.
   :::note
   You may use a single key for all supported resources or separate keys for each resource, such as SQL, storage, disk, Snowflake. If you choose to use different keys, provide UiPath with the corresponding key URIs through your support ticket.
   :::
6. Using the key URIs you provided, UiPath configures encryption on your Azure-based resources and applies customer-managed keys (CMK) to supported components, including storage, SQL, disk, and Snowflake resources. If you want to apply CMK to Snowflake resources, then you must follow these additional steps:
   1. Perform steps 1 to 2.5 in this [Snowflake community guide](https://community.snowflake.com/s/article/Azure-Tri-Secret-Secure-Configuration-changes-needed-on-Azure-Portal-with-screenshots).
   2. Provide the output from step 2.5 to UiPath via your support ticket.
   3. UiPath completes the [Tri-Secret Secure self-registration with Azure Key Vault](https://community.snowflake.com/s/article/Tri-Secret-Secure-self-registration-with-Azure-Key-Vault) mentioned at step 2.5 and step 3.1.
   4. UiPath shares the Azure consent link and Snowflake principal name.
   5. Continue the Snowflake procedure described [here](https://community.snowflake.com/s/article/Azure-Tri-Secret-Secure-Configuration-changes-needed-on-Azure-Portal-with-screenshots), starting with step 3.
   6. At step 4, if you require public access controls for the Key Vault (via specific IPs or virtual networks), contact UiPath for subnet details.
   7. UiPath completes step 4.5.
7. Notify when encryption with CMK is active.

### Data loss prevention

To avoid accidental data loss, UiPath recommends:

* Key rotation:
  + Azure services check for a new key version once per day. Changing the key version does not cause downtime. For more information, visit [Customer-managed keys for account encryption - Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json#update-the-key-version).
  + After rotating, wait 24 hours before disabling the previous version.
  + Older backups are not re-encrypted, so keep old key versions available for restores.
* Temporary revocation:
  + You can disable a key without deleting it.
  + This blocks access to encrypted resources but does not affect encryption state.
  + Access is restored when the key is re-enabled.
  + While disabled, operations will return 403 Forbidden errors.

Check the following table for scenarios where you could lose your data, and ways you can either prevent or mitigate the issue:

Table 1. Possible data loss scenarios

| Issue | Impact | Prevention | Mitigation |
| --- | --- | --- | --- |
| AKV resource lock removed | It is possible that AKV/key will be deleted. If deleted, resources become inaccessible within approximately 10 minutes. | Soft delete and purge protection makes sure that the AKV/key can be restored within 90 days. | Restore AKV or key within 90 days. |
| AKV/Current key deleted | Resources become inaccessible within approximately 10 minutes. | Soft delete and purge protection makes sure that the AKV/key can be restored within 90 days. | Restore AKV or key within 90 days. |
| Previous key version deleted | Breaks backup restoration | Soft delete and purge protection makes sure that the AKV/key can be restored within 90 days. | Restore AKV or key within 90 days. |
| Key compromised | Data at risk | Apply network protection on AKV. | N/A |
| Access revoked (RBAC/firewall change)  For example: Revoking the key vault's `get`, `wrapKey`, `unwrapKey` permissions from the server or changing the key vault's firewall rules. | Resources become inaccessible within approximately 10 minutes. | Use resource locks. | Restore permissions |
| Azure Key Vault outage | Resources become inaccessible within approximately 10 minutes. | We do not provision Azure Key Vaults in regions where cross-region fail over is not supported. For more information, refer to [Reliability in Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/disaster-recovery-guidance). | No action required |