---
title: "Runtime language best practices"
visible: true
slug: "runtime-language-best-practices"
---

Setting the correct runtime language is important because:

* It helps screen readers pronounce text correctly.
* It improves accessibility compliance for multilingual users.
* It reduces browser translation interruptions.
  :::important
  Changing the Runtime Language for an already published app does not affect the published version. To apply a new Runtime Language:
  1. Change the runtime language in
  design time.
  2. Republish the app.
  :::

## Tips

1. Each app should be designed in a **single language**. The Runtime Language setting applies to the entire page and does not support per-control or mixed-language configurations.
2. If you still encounter browser translation prompts, you can disable them by selecting the option **Never translate this site** in the browser settings.
3. Runtime language and selected Preferences Language should be kept same to avoid any issues.