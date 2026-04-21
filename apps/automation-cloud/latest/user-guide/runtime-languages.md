---
title: "Runtime language"
visible: true
slug: "runtime-languages"
---

The **Runtime Language** setting allows App Designers to specify the language that the application uses at runtime.

By setting the runtime language, you help browsers and assistive technologies correctly interpret the app’s content, ensuring a smoother experience for multilingual users.

## Using runtime languages

A Runtime Language dropdown is available in the App Designer's **General Settings** and under the **Properties** panel of your project. The dropdown lists all supported languages (aligned with the languages available in the UiPath Portal). The selected language determines the lang attribute applied to the HTML document at runtime.

At runtime, language resolution follows this order:

1. **Runtime Language** set for the app
2. **English (en)** as the default fallback

Default and Backward Compatibility:

* New apps: the Runtime Language defaults to the user's Portal Language Preference.
* Existing apps: the language remains English, maintaining current behavior.

The Runtime language applies only to Apps Runtime. Action Apps continue to follow the user's Portal Language Preference.

:::important
Changing the Runtime Language for an already published app does not affect the published version. To apply a new Runtime Language:
1. Change the runtime language
in design time.
2. Republish the app.
:::

**Example**

If in App Designer we set the Runtime Language to Spanish (ES), the runtime will render:

```
<html lang="es">
```

This ensures that assistive technologies and browsers correctly interpret the app content.

:::note
For best practices and tips, visit the [Runtime language best practices](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/runtime-language-best-practices#runtime-language-best-practices) guide.
:::