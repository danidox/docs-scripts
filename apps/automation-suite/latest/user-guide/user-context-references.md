---
title: "User context references"
visible: true
slug: "user-context-references"
---

## Overview

**App Studio** offers the possibility to create personalized apps using the runtime user context.

With this feature you can provide a more personal experience for your users. For example, you can have a personal welcome message for every logged in user, or pass in the current user email ID the to the RPA process.

To access the context of the current user, in the **Expression editor**, type `CurrentUser.` . A list of available properties unfolds:

DisplayName : Retrieves the display name of the current user.

FirstName : Retrieves the first name of the current user.

LastName : Retrieves the last name of the current user.

Email : Retrieves the email of the current user.

Groups : Retrieves the group list the current user is a member of.

![docs image](/images/apps/apps-docs-image-290197-d9188104.webp)

## Example

The following example shows how to build a welcome message addressed to the logged in user.

1. In Apps Studio, add a **Label** display control.
2. For the **Text** property, open the **Expression editor** by clicking the "tune" icon ![](/images/apps/apps-image-280277-e5d8b471.webp).
3. Create your welcome message by concatenating the message string and the current user property, as follows:
   ```
   "Welcome" + CurrentUser.DisplayName
   ```
4. Preview your app. You should be seeing your message, followed by your display name, as you are previewing the app from your account.