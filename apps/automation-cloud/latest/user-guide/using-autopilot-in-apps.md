---
title: "Using Autopilot in Apps"
visible: true
slug: "using-autopilot-in-apps"
---

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

Autopilot in Apps allows you to create an app using natural language, images, PDF documents or entities. Autopilot can help you accelerate your app development, implement various VB expressions with ease, digitise legacy paper forms, or build data-driven apps based on your existing entities in Data Service.

Autopilot in Apps supports localization across all supported languages. You can write the text prompt in languages other than English, and use images or PDF files that are not written in English. Autopilot can also generate VB expressions which you can use in apps. If you select the **Create entity** option, Autopilot also generates an entity for your app and uploads data to it.

You can use the resulting app immediately as-is, or you can perform any desired changes or improvements using the existing Apps controls and features.

:::important
All Autopilot AI features are turned on by default. To disable Autopilot features in Apps, an **Admin** can disable AI capabilities from the **[Governance Policy](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies)** in **Automation Ops.**
:::

## Templates

Autopilot for Apps also provides a series of predefined templates. These include:

* A lead capture app that collects personal details, company details, lead source and a file.
* An employee info collection app that collects personal details, employment details, a start date and two files.
* A form with name, email, and phone fields.

They can be used as-is, or modified using the Apps controls.

## Using Autopilot

You can access Autopilot from the Apps homepage.

  ![docs image](/images/apps/apps-docs-image-427141-50900cba.webp)

To use Autopilot in Apps, you need:

* [The AI Trust Layer policy](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies) to be enabled by the admin within Automation Ops.
* A Document Understanding license (for app generation from an image or PDF).

## Best practices

* Text in images and PDFs should be sufficiently readable for the AI to digitize them.
* PDFs and images should contain forms.
* Images should be larger than 50 x 50 pixels, but smaller than 10,000 x 10,000 pixels.

## Feature limitations

* Autopilot does not support custom rules.
* PDFs or images with a large number of fields may not function optimally.
* Autopilot currently only supports single-page forms.
* Autopilot may not correctly process forms with large volumes of text.
* Autopilot currently only supports generation of an app from a single entity.
* Autopilot does not support rendering data from an entity.
* Autopilot currently only supports the integration of entities. Prompts related to storage buckets or processes are not currently supported.

## Control support

Autopilot currently supports the following controls:

* **Button**
* **Checkbox**
* **Radio button**
* **Date picker**
* **Dropdown**
* **Slider**
* **Textbox**
* **Textbox email**
* **Textbox number**
* **Page container**
* **Container**
* **Label**
* **Header**
* **Text area**
* **Multi-select dropdown**
* **List**
* **Edit grid**

The following controls are currently not supported in Autopilot:

* **Rich text editor**
* **File uploader**
* **Switch**
* **Table**
* **Tabs**
* **Image**
* **Document viewer**
* **Divider**
* **File downloader**
* **Container layout**
* **Custom list**
* **Custom HTML**

## Licensing

Every user of an organization receives five Autopilot actions per day to use across all products, including Apps. Across app and page creation, as well as expression generation, each request consumes one Autopilot action.

Apps checks for the available Autopilot actions when the request is made. If you have exhausted all Autopilot actions, Apps returns an error message. If generation of the AI output fails, no Autopilot actions are deducted.

For more information on licensing plans, please visit [the Licensing plan breakdown page](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-licensing#plan-breakdown).