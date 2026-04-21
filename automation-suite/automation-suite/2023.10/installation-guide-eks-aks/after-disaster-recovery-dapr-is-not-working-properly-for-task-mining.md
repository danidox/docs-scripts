---
title: "After Disaster Recovery Dapr is not working properly for Task Mining"
visible: true
slug: "after-disaster-recovery-dapr-is-not-working-properly-for-task-mining"
---

After a Disaster Recovery, **Dapr** is not restored properly, and the certificates needed by **dapr** to provide services for Process Mining and Task Mining are incorrect. The **dapr**, **processmining**, and **taskmining** applications appear to be healthy first, but will then go back to progressing state and the environment becomes unstable. When logging in to Process Mining or Task Mining, the application may not load, or return unexpected errors.

This page describes the steps you should take to resolve the issue.

## Overview of the steps

1. Delete all **dapr** secrets and the mutatingwebhookconfiguration.
2. Resync all **dapr** secrets and the mutatingwebhookconfiguration.
3. Restart **dapr-sentry** deployment and wait to the deployment is finished.
4. Restart **dapr-operator** deployment and wait to the deployment is finished.
5. Restart **dapr-sidecar-injector** deployment and wait to the deployment is finished.

A detailed description of the steps is provided next.

## Deleting dapr secrets and the mutatingwebhookconfiguration

1. Go to **Applications** in ArgoCD.
2. Select the **dapr** application card to open the **dapr app details tree**.
3. Locate the dapr **secrets**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/320864)

The secrets must be recreated. You can do this by deleting each secret.
4. Open the context menu of the secret and select **Delete**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/320873)
5. In the **Delete resource** confirmation dialog enter the name of the secret and select **OK** to confirm.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/320882)
6. Repeat steps **4** and **5** for the remaining secrets.
7. In the **dapr app details tree**, locate the **mutatingwebhookconfiguration**.
   :::note
   You can recognize the **mutatingwebhookconfiguration** from the label **MWC**.
   :::
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/321189)
8. Open the context menu of the secret and select **Delete**. In the **Delete resource** confirmation dialog enter the name of the **mutatingwebhookconfiguration** and select **OK** to confirm.

## Syncing the dapr secrects and the mutatingwebhookconfiguration

1. Some of the secrets are immediately recreated. This is indicated by a green check mark on the secret card.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/320887)

If a secret is not recreated, you need to sync to recreate the secret.
2. Locate the secret you want to recreate and select **Sync** from the context menu.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/320892)
3. In the pop-up panel, select **SYNCHRONIZE.**
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/320896)
4. Repeat steps **2** and 3 for all the secrets that you want to recreate.
5. In the **dapr app details tree**, locate the **mutatingwebhookconfiguration**.
   :::note
   You can recognize the **mutatingwebhookconfiguration** from the label **MWC**.
   :::
6. Open the context menu for the **mutatingwebhookconfiguration** and select **Sync**.
7. In the pop-up panel, select **SYNCHRONIZE.**

## Restarting the deployment

After you deleted and synchronized the **secrets** and the **mutatingwebhookconfiguration**, you need to restart the deployment.

1. In the **dapr app details tree**, locate the **dapr-sentry** deploy card.
2. Open the context menu and select **Restart**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/321203)

A confirmation dialog is displayed.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/321208)
3. Select **OK** to confirm the restart. The **dapr-sentry** deployment starts. When the deployment is finished, a green heart appears. Wait for the deployment to be finished.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/321217)
4. In the **dapr app details tree**, locate the **dapr-operator** deploy card.
5. Open the context menu and select **Restart**.
6. In the confirmation dialog, select **OK** to confirm the restart. Wait for the deployment to be finished.
7. In the **dapr app details tree**, locate the **dapr- sidecar-injector** deploy card.
8. Open the context menu and select **Restart**.
9. In the confirmation dialog, select **OK** to confirm the restart. Wait for the deployment to be finished.
   :::important
   Restart the deployments in the described order and make sure a deployment is ready before starting the next deployment.
   1. dapr-sentry
   2. dapr-operator
   3. dapr-sidecar-injector
   :::

You can now check that **dapr** is working correctly by looking at **processmining**, as previously described. Now there should be **3** containers in the pod and the **daprd** container should be present in the **LOGS**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/321228)

Task Mining should work properly now.