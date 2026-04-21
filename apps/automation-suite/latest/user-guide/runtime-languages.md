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

**Example**

If in App Designer we set the Runtime Language to Spanish (ES), the runtime will render:

```
<html lang="es">
```

This ensures that assistive technologies and browsers correctly interpret the app content.

:::note
For best practices and tips, visit the [Runtime language best practices](https://docs.uipath.com/apps/automation-suite/latest/user-guide/runtime-language-best-practices#runtime-language-best-practices) guide.
:::