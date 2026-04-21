---
title: "Apps Configuration Checklist"
visible: true
slug: "apps-configuration-checklist"
---

## Overview

Creating a new app on on-premises is very similar to creating one in cloud. For more information on creating an app, see:

* [Using App Studio](https://docs.uipath.com/apps/automation-suite/latest/user-guide/using-app-studio#using-app-studio)
* [Overview of control and its properties](https://docs.uipath.com/apps/automation-suite/latest/user-guide/controls#controls-overview)
* [Add users/group to an app, testing and deployment](https://docs.uipath.com/apps/automation-suite/latest/user-guide/overview1#about-alm)

## Evaluation Guide

### Create App Journey

* Create a new app.
* Add multiple pages and design the UI with relevant controls.
* Add processes to the app and bind the process parameters to UI controls:
  + Include both Attended and Unattended processes.
* Preview the app to check the flow is working as expected.
* Add additional users or groups to the app.
* Update the app icon in **General settings**.
* Publish the app.
* Download the app.

### Import a Process From Orchestrator in Apps

In the cloud version of **UiPath Apps**, you have the option to select from the list of cloud Orchestrators or connect to on-premises Orchestrators by providing the credentials. For more information on this, see [Referencing a Process from Orchestrator](https://docs.uipath.com/apps/automation-suite/latest/user-guide/connecting-your-app-to-an-orchestrator-tenant#referencing-a-process-from-orchestrator).

In the Automation Suite version of **Apps**, you will have the ability to connect to the list of Orchestrators available in the same Automation Suite deployment.

  ![docs image](/images/apps/apps-docs-image-250762-8d66fc35.webp)

### Import an Entity From Data Service in Apps

To create better, more complex apps, UiPath Apps can connect and interact with entities from UiPath Data Service. Data Service is a persistent data storage service that brings powerful no-code data modeling and storage capabilities to your Robotic Process Automation (RPA) projects.

Once an entity has been created in Data Service, you can reference that entity from an app.

For more information on how to reference an entity, see [Referencing an Entity in your App](https://docs.uipath.com/apps/automation-suite/latest/user-guide/referencing-an-entity-in-your-app#referencing-an-entity-in-your-app).

### Referencing a Storage Bucket From Orchestrator

For a seamless integration, all the files uploaded using the **File Picker** control or the **Upload file to Storage bucket** rule are stored in a storage bucket in **Orchestrator**.

For more information on storage bucket, see [About Storage Buckets](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-storage-buckets) and [Managing Storage Buckets](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-storage-buckets).

Once a storage bucket has been created in **Orchestrator**, you can reference it from an app. For more information on how to refence a storage bucket, see [Referencing a Storage Bucket from Orchestrator](https://docs.uipath.com/apps/automation-suite/latest/user-guide/referencing-a-storage-bucket-from-orchestrator#referencing-a-storage-bucket-from-orchestrator).

### Runtime App Journey

* Log in as a different user and check if the app is available in the landing page to run.
* Run the app and check if it behaves as expected.

### Edit App Journey

* Import the app which was downloaded and create a new app using the imported one.
* Replace the processes associated in the import app with a different process from a different Orchestrator.
* Preview the app and make sure that it behaves as expected.