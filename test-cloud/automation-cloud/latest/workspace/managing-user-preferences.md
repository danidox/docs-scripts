---
title: "Managing user preferences"
visible: true
slug: "managing-user-preferences"
---

The **user** menu is available from any page and you can access it by selecting the icon with your initials in the top-right corner of the screen.

From this menu you can open the **Preferences** page for your account, or sign out.
:::note
Feature availability depends on the cloud offering you use. For details, refer to the [feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

## Selecting the user language

By default, the language selected for your organization applies to the user interface. But you can choose a different language for the user interface for yourself.

To change the language of the user interface:

1. Select the user icon and then select **Preferences**.
   !['Preference option' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/390897)

The **Preferences** page opens in a new browser tab.
2. On the **General** tab, under the **Preferences** section, select an option from the **Language** list.

The interface language changes to the selected language in both the current tab and other UiPath platform tabs.

You can close the **Preferences** browser tab.

When a page is not available in the selected language, the localization defaults to English.

For details about the supported languages across our products, refer to [Localization support](https://docs.uipath.com/overview-guide/docs/localization-support) .

## Selecting the theme

By default, all pages are displayed in light theme. But you can choose to switch to the dark theme, which is more comfortable on the eyes in a dark ambiance.

To change the theme of the user interface:

1. Select the user icon and then select **Preferences**.
   !['Preferences option' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/390902)
2. Select **Theme** from the left navigation panel.
3. Select your preferred option. The following table describes each option:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Option
    </p>
   </th>
   <th>
    <p>
     Details
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d10260e131">
    <p>
     <strong>
      Sync with operating system settings
     </strong>
    </p>
   </td>
   <td headers="d10260e134">
    <p>
     The theme is automatically set to light or dark theme according to your current operating system theme setting.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d10260e131">
    <p>
     <strong>
      Dark theme
     </strong>
    </p>
   </td>
   <td headers="d10260e134">
    <p>
     All pages display in dark theme, if available.
    </p>
    <p>
     If dark theme is not available for a service, light theme is automatically selected. Dark theme is used whenever possible.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d10260e131">
    <p>
     <strong>
      Light theme
     </strong>
    </p>
   </td>
   <td headers="d10260e134">
    <p>
     This is the default setting.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d10260e131">
    <p>
     <strong>
      High contrast theme
     </strong>
    </p>
   </td>
   <td headers="d10260e134">
    <p>
     Enhances the contrast for a set of UI elements.
    </p>
    Note:
    <p>
     High contrast theme is not available when syncing
                                             with the operating system settings.
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Leaving an organization

You can choose to remove yourself from an organization to which you belong. By doing so, you no longer have the option to sign in to that organization.

By leaving an organization, you lose access to all the tenants and all the services (products) in that organization.
:::note
This option is not available if a [directory integration](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/authentication-models-for-test-cloud#the-directory-accounts-model) is active for the organization.
:::

**To leave an organization**:
1. If you belong to multiple organizations, make sure you are signed in to the organization that you want to leave.
2. Select the user icon in the top-right corner of the window and select **Preferences**.

The **Preferences** page opens in a new tab.
3. On the **General** tab, under **Organization**, select **Leave Organization**.
   :::note
   If you are the only organization administrator in the organization, you cannot leave the organization. As alternatives, consider:
   * Assigning another user as organization administrator (by adding them to the Administrators group).
   * [Deleting the organization](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#deleting-your-organization), if neither you or others need to use it any more.
   :::

A confirmation dialog opens.
4. In the dialog, select **Confirm**.

You are signed out. When you sign in again, you will no longer be able to access the organization that you left.

## Viewing consumable entitlements

You can view your free consumable entitlements bundled with your user license in the **Licensing** panel.

You can view the following details:

* The total number of units (start date, expiration date, and if the units reset monthly, their reset date)
* The total number of consumed units vs. the total number of available units
:::note
Each user has access to individual, user-level entitlements. Only the logged-in user can consume these entitlements, other users within the same organization cannot access or use another person’s entitlements.
:::