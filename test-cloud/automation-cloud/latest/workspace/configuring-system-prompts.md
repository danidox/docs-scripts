---
title: "Configuring consent prompts"
visible: true
slug: "configuring-system-prompts"
---

As an administrator, you can establish up to 10 consent prompts for users logging into your organization. These prompts ensure each user is informed about internal policies they need to consent to before they can use UiPath.

For record-keeping, you have access to detailed logs for each consent interaction. These logs capture the identity of the logged-in user, the login date, whether they accepted or rejected the prompt, and the expiry date of an accepted consent. The expiration of an accepted consent does not disconnect the user, however, they are prompted to confirm their consent again with their next login.

Users who choose to decline are prevented from logging in, but have the option to accept the consent if they reconsider.

## Consent prompt behavior

To access the portal, users must accept all active consent prompts configured in your organization.

If a user accepts some prompts but declines at least one, they are not allowed to access the portal. On the next sign-in attempt, the portal displays only the consent prompts the user previously declined. The portal remembers the prompts that the user already accepted, so they do not need to review those again.

## Configuring a consent prompt

To configure a consent prompt, follow these steps:

1. Navigate to **Admin** > **User Consent** for your organization.
2. Select **Create user consent** to create a new consent. The **Create user consent** window is displayed. On the left side you can configure your consent prompt. On the right side, you can notice a real-time preview of your consent prompt.
   :::note
   You can only configure one consent prompt per organization.
   :::
3. Set a title in the **Title** field. Provide a short, clear summary of the policy content for which users are to provide their consent.
4. Add the content in the **Content** field. You should detail the specific policies the user needs to consent to. You can format your messages as needed, and you can incorporate tables using Markdown.
   :::note
   Copying and pasting a markdown table directly into the **Content** field does not render as a table but maintains the raw markdown syntax. For correct table rendering, either delete the last character of the copied text after pasting and then add it back, or manually enter the entire table.
   :::
5. Enter the text for the radio buttons defined for consenting and declining options
   * On the **Radio button - consent** field, enter the text for the consenting option. This option allows users to use the platform.
   * On the **Radio button - decline** field, enter the text for the declining option. This option prevents users from using the platform. Users who choose to decline have the option to agree if they reconsider.
6. Under **Settings**, select your preferred **Recurrence** option:
   * Choose **Once** to show the consent prompt a single time.
   * Choose **Repeat** to configure recurring prompts. You can set the frequency intervals to specific days, weeks, months, or years as needed. The expiration of set recurring time does not disconnect the user, however, they are prompted to confirm their consent again with their next login.
7. Under **Settings**, set a **Priority order** for the consent prompt. The priority defines the display order of consent prompts shown to users. You can configure up to 10 prompts, and assign each one a priority from 1 (displayed first) to 10 (displayed last).
8. Select **Save** to keep your changes.

## Editing the existing consent prompt

To edit an existing consent prompt, follow these steps:

1. Navigate to **Admin** > **User Consent** for your organization.
2. Select **Edit user consent** to edit the existing consent. The **Edit user consent** window is displayed. On the left side you can configure your consent prompt. On the right side, you can notice a real-time preview of your consent prompt.
3. Make the necessary edits to your consent prompt. For details about the available options, refer to [Configuring a consent prompt](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-system-prompts).
4. Select **Save** to keep your changes. The **Content changes** window is displayed, where you can choose to keep the existing user records from the initial consent prompt, or to reset the record.
   !['Content changes' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/464076)
5. Select **Keep existing user records and only prompt new message to users who have not yet accepted** to keep existing user records, or **Delete existing user records and re-prompt new message to all users** to delete existing user records and require all users to accept the edited consent prompt.

## Deleting the existing consent prompt

Deleting a consent prompt erases the consent records, requiring all users to accept any newly created prompts again. To delete a consent prompt, follow these steps:

1. Navigate to **Admin** > **User Consent** for your organization. The **User consent** window is displayed showing an overview of the existing consent prompt.
   !['User consent window' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/464087)
2. Select **Delete** to delete the existing prompt. The **Delete user consent** window is displayed.
3. Select **Delete** to confirm deleting the consent prompt or **Cancel** to return to the **User consent** window without deleting the prompt.