---
title: "General troubleshooting"
visible: true
slug: "general-troubleshooting"
---

## The remote certificate is invalid because of errors in the certificate chain: UntrustedRoot

The `net::ERR_CERT_AUTHORITY_INVALID` error occurs when your certificate expires or is involved in a certificate rotation process, indicating that it is now invalid.

It is most likely that the error occurs for the following reasons:

* You cannot access Automation Cloud.
* Your robot is disconnected.

Figure 1. Your connection is not private warning

  !['Your connection is not private'image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/459857)

Figure 2. UiPath Error message

  ![UiPath error message image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/460982)

To fix this error, take the steps, described in the following example:

1. In a browser window, navigate to your cloud organization via the access URL.
2. Select the **Not secure** warning prompt. Then select **Certificate is not valid** from the dropdown menu.

Figure 3. Certificate is not valid warning

   ![Certificate is not valid image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/459666)
3. In the **Certificate Viewer**, select the **Details** tab. Then select **Export** and save the certificate.

Figure 4. Details tab

   ![Details tab image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/459695)
4. On your local machine, open **certlm.msc** and right-select the **Personal** folder, then select **All Tasks**, then select **Import**. Select the previously generated certificate and import it.

Figure 5. Importing certificate

   ![Import certificate image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/459702)
5. In the same **certlm.msc** window from the previous step, select the **Trusted Root Certification Authorities** folder, then select **All tasks**, then select **Import**. Select the previously generated certificate and import it again.

Figure 6. Importing certificate

   ![Import certificate image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/459712)
6. Connect the robot again to check that the error is fixed.

Select the **View site information** icon. Select **Connection is secure** from the dropdown menu.

## Browser group policies

Signing in to your Orchestrator service from the Assistant redirects you to the SSO page. In some browsers, you may be prompted to open UiPath Assistant. This happens due to the Assistant's protocol handler not being added to the browser's group policies.

To prevent this behavior, make sure to follow the next steps, depending on the browser (Chrome/Microsoft Edge):

1. Open **Registry Editor**.
2. Navigate to `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome`/ or `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge`, depending on the browser you use.
3. Add a new key and name it `AutoLaunchProtocolsFromOrigins`.
4. Select **(Default)** to edit the key.
5. In the **Edit String** dialog, in the **Value data** field, add `[{"allowed_origins": ["https://myOrchestrator.uipath.com/"],"protocol": "com.uipath.robot.oidc"}]` and select **OK**.
   :::important
   The `AutoLaunchProtocolsFromOrigins` policy requires Chrome 85 or later.
   :::
6. Close all browser tabs and relaunch the browser.
7. Verify that your browser applied the new policy by navigating to `chrome://policy` or `edge://policy`. The recently added policy should be listed under the **Chrome Policies** or **Microsoft Edge** section with the **OK** status.