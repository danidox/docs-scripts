---
title: "Encryption"
visible: true
slug: "encryption"
---

## Overview

UiPath enforces encryption for data in transit and at rest across its cloud services. All inbound communications to UiPath services require TLS 1.2 or higher. Data at rest is encrypted using Transparent Data Encryption (TDE), which leverages AES 256-bit encryption.

Depending on the UiPath service and cloud offering, additional encryption mechanisms and key-management options may be available.

## Application-Level Encryption (ALE)

For Test Cloud and Test Cloud Public Sector, in addition to TDE, some services support **Application-Level Encryption (ALE)**:

* In some services, ALE is applied automatically (implicit ALE).
* In other services, ALE is optional and can be enabled by you (opt-in ALE).
* Some services do not currently support ALE.

When ALE is available and enabled, either implicitly or by opting in, you can choose how encryption keys are managed.

For services that support ALE, the following key-management options may be available:

* **UiPath-managed key:** This option allows UiPath to create, store, and protect the keys used for encrypting your data. This is the default option, and it is automatically enabled in the **Encryption** tab of your **Admin** section.
* **Customer-managed key:** This option grants you full control and responsibility over the creation, storage, and protection of the encryption keys used for safeguarding your data. Unlike the UiPath-managed key, where UiPath manages these tasks by default, with a customer-managed key (CMK), you directly handle these aspects in your own secure environment.
    :::tip
    Useful resources:
    * [Overview of CMKs](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/customer-managed-keys#customer-managed-keys-for-test-cloud-and-test-cloud-public-sector): Understand and use Customer
    Managed Keys.
    * [Switching from customer-managed to UiPath-managed
    keys](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/switch-from-customer-managed-to-uipath-managed-keys#switching-from-customer-managed-to-uipath-managed-keys): Your guide for migrating from UiPath Key to CMK.
    * [Enabling a firewall for the customer-managed
    key](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/enabling-a-firewall-for-your-key-vault#enabling-a-firewall-for-the-customer-managed-key): Learn to set up a firewall for CMKs.
    :::

    !['Encryption settings' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30837)

## Infrastructure-level encryption

For Test Cloud Dedicated, encryption at rest is applied at the infrastructure level. Encryption at rest is enabled by default for data stores such as SQL and Azure storage (Blob, disks, and files). Currently, UiPath manages the TDE protector as the default setting.

* **UiPath-managed key**: UiPath creates, stores, and protects the keys used for encrypting your data. This is the default option, and it is automatically enabled.
* **Customer-managed key**: Your encryption keys reside in your own Azure Key Vault, giving you full control over key creation, storage, rotation, and access permissions.

## Key rotation and management

For Test Cloud Dedicated, you can use key rotation and management, because automatic key rotation is enabled by default where infrastructure-level encryption is used.

* Key auto-rotation occurs every 18 months.
* The rotation process decrypts and re-encrypts only the database encryption key.
* The system automatically updates the TDE protector with the latest key version available in Azure Key Vault within 24 hours.

This combination of automatic key updates and scheduled rotation provides an end-to-end, zero-touch key rotation mechanism for encryption at rest.

## Encryption per service

The specifics of the encryption for each service or resource can be found in the following table.

For more information about ALE with Customer-Managed Keys, and guidance on how to set it up, visit [ALE with CMK](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/customer-managed-keys#customer-managed-keys-for-test-cloud-and-test-cloud-public-sector).

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Product
    </p>
   </th>
   <th>
    <p>
     Resource
    </p>
   </th>
   <th>
    <p>
     Encrypted resource fields
    </p>
   </th>
   <th>
    <p>
     Encryption applied
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d132210e228">
    <p>
     <strong>
      Action Center
     </strong>
    </p>
    <p>
     <strong>
      (Actions
     </strong>
     and
     <strong>
      Processes)
     </strong>
    </p>
   </td>
   <td headers="d132210e231">
    Tasks
   </td>
   <td headers="d132210e234">
    Data
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Optional - as opted in when creating the parent entity (i.e. the task catalog)
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     AI Center
    </strong>
    &trade;
   </td>
   <td headers="d132210e231">
    Dataset, data labeling sessions, pipeline data, and
                              artifacts
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Optional
       <sup>
        1
       </sup>
       - as opted in by the
                                       user
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Agents
    </strong>
   </td>
   <td headers="d132210e231">
    Traces
   </td>
   <td headers="d132210e234">
    LLM input and output data within logs
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Test Cloud
    </strong>
   </td>
   <td headers="d132210e231">
    External applications
   </td>
   <td headers="d132210e234">
    Customer access data
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Test Cloud
    </strong>
   </td>
   <td headers="d132210e231">
    Directory connections
   </td>
   <td headers="d132210e234">
    Customer access data
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Test Cloud
    </strong>
   </td>
   <td headers="d132210e231">
    External identity providers
   </td>
   <td headers="d132210e234">
    Customer access data
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Automation Hub
    </strong>
   </td>
   <td headers="d132210e231">
    Customer idea data
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Not available
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Automation Ops
    </strong>
   </td>
   <td headers="d132210e231">
    <p>
     API access keys
    </p>
    <p>
     Access Tokens
    </p>
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Not available
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Context Grounding
    </strong>
   </td>
   <td headers="d132210e231">
    &nbsp;
   </td>
   <td headers="d132210e234">
    &nbsp;
   </td>
   <td headers="d132210e237">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Data Fabric
    </strong>
   </td>
   <td headers="d132210e231">
    Entity fields
   </td>
   <td headers="d132210e234">
    Specific data output
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <strong>
       Connection
                                       protocol
      </strong>
      : TLS 1.2
     </li>
     <li>
      <strong>
       TDE
      </strong>
      : AES
                                    256
     </li>
     <li>
      <strong>
       ALE
      </strong>
      :
                                    Optional
      <sup>
       1
      </sup>
      - as opted in by the user when creating
                                    the parent entity
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Document Understanding
    </strong>
   </td>
   <td headers="d132210e231">
    Document Manager sessions, document storage
    <style>
     .css-1s0agg2 path{fill:var(--color-primary);}
    </style>
    Note: FormsAI sessions are not available on
                                 CMK-enabled accounts.
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Optional
       <sup>
        1
       </sup>
       - as opted in by the
                                       user
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Insights
    </strong>
   </td>
   <td headers="d132210e231">
    Dataset, reporting
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Not available. Data that is ALE encrypted at its origin arrives encrypted in Insights.
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Integration Service
    </strong>
   </td>
   <td headers="d132210e231">
    Event data
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Not available
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     IXP
    </strong>
   </td>
   <td headers="d132210e231">
    All datasets
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Not available
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Marketplace
    </strong>
   </td>
   <td headers="d132210e231">
    &nbsp;
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Not available
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Maestro
    </strong>
   </td>
   <td headers="d132210e231">
    Variables
   </td>
   <td headers="d132210e234">
    All
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Orchestrator
    </strong>
   </td>
   <td headers="d132210e231">
    Queue Items
   </td>
   <td headers="d132210e234">
    <p>
     Specific Data
    </p>
    <p>
     Output
    </p>
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Optional - as opted in when creating the parent entity (i.e. the queue)
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Orchestrator
    </strong>
   </td>
   <td headers="d132210e231">
    Asset Values
   </td>
   <td headers="d132210e234">
    Value
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Orchestrator
    </strong>
   </td>
   <td headers="d132210e231">
    Credential Stores
   </td>
   <td headers="d132210e234">
    Orchestrator credential stores content
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Orchestrator
    </strong>
   </td>
   <td headers="d132210e231">
    Credential Stores
   </td>
   <td headers="d132210e234">
    Non-Orchestrator credential stores access data
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Orchestrator
    </strong>
   </td>
   <td headers="d132210e231">
    Storage Buckets
   </td>
   <td headers="d132210e234">
    Non-Orchestrator storage buckets access data
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Process Mining
    </strong>
   </td>
   <td headers="d132210e231">
    &nbsp;
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Not available
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Task Mining
    </strong>
   </td>
   <td headers="d132210e231">
    Recorded data (includes PII masking)
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Optional
       <sup>
        1
       </sup>
       - as opted in by the
                                       user
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Test Manager
    </strong>
   </td>
   <td headers="d132210e231">
    Credentials for third party integration
                              Note: Credentials for integrations announced to be deprecated are not encrypted.
   </td>
   <td headers="d132210e234">
    Configuration
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <p>
       <strong>
        Connection protocol
       </strong>
       : TLS 1.2
      </p>
     </li>
     <li>
      <p>
       <strong>
        TDE
       </strong>
       : AES 256
      </p>
     </li>
     <li>
      <p>
       <strong>
        ALE
       </strong>
       : Implicit
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d132210e228">
    <strong>
     Test Manager
    </strong>
   </td>
   <td headers="d132210e231">
    Attachments
   </td>
   <td headers="d132210e234">
    Database and storage
   </td>
   <td headers="d132210e237">
    <ul>
     <li>
      <strong>
       Connection protocol
      </strong>
      : TLS 1.2
     </li>
     <li>
      <strong>
       TDE
      </strong>
      : AES 256
     </li>
     <li>
      <strong>
       ALE
      </strong>
      : Implicit
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

1 - The customer or their account teams must [submit a ticket](https://customerportal.uipath.com/support/add-case) to enable ALE. The UiPath engineering team manages these requests, so please allow a few days for processing. Once we've enabled ALE, you can configure in the **Admin** section whether or not to use CMK.