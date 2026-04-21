---
title: "Preview activities and packages"
visible: true
slug: "preview-activities-and-packages"
---

Administrators can enable or disable the availability of preview packages and activities in Studio Web by using the **Preview packages and activities** [Automation Ops option](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-studio-web-policies#activities).

Follow the steps below to deploy a governance policy that enables preview packages and activities:

1. Navigate to **Automation Ops** from the left navigation menu in UiPath Automation Cloud.
2. Select **Governance** &gt; **Policies**.
3. Select **Add Product Policy** above the table.
4. Enter a unique name for your policy, select Studio Web from the **Product** list, and then select **Add**.
5. In the policy configuration page, navigate to the **Activities** tab.
6. Under **Feeds**, check the **Enable preview packages and activities** option, and then select **Save**.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/384084)
7. Navigate to the **Deployment** tab next to **Policies**.
8. Select the tenant you wish to apply the governance policy to from the list.
9. Select your newly-created policy from the drop-down menu in the **Product Policy** column, under the **No License** category, and then select **Save**.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/384097)

## Common issues

If preview packages are not available in Studio Web, see this table containing common issues.

| Issue | Solution |
| --- | --- |
| Was the new policy deployed? | Navigate to **Automation Ops** &gt; **Governance** &gt; **Deployment** &gt; **Tenants** and select the **Edit** button next to the tenant. Under **No License**, select the policy that enables preview packages. |
| Was the new policy enabled after deployment? | Users need to log out and log back in Automation Cloud to ensure the new policy becomes active. |
| Did the user refresh the Studio Web browser tab after logging in? | After logging out and back in, if Studio Web is opened in a different browser tab, refresh that tab. |
| Does the user have an Automation Express license? | Users with Automation Express licenses are ungovernable and cannot have Studio Web policies applied to them, meaning that they cannot access preview packages and activities. |
| The **Preview packages and activities** governance option is disabled, but users can still access preview activities. | If any preview activities are used in a project before a governance policy that disables them is deployed or the **No Policy** deployment option is selected for the user, preview activities and packages continue to be available in that project. |