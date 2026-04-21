---
title: "Using UI Automation for browser interactions"
visible: true
slug: "using-ui-automation"
---

UI Automation Cloud capabilities offer powerful and comprehensive features designed to enhance productivity by building browser-based cross-platform automation which enables you to automate repetitive tasks, reduce manual input errors, and improve overall efficiency.

UI Automation Cloud offers an extensive range of capabilities that simulate human behavior (for instance, clicking screen elements, typing text, data scraping, or screen scraping) when interacting with web applications.

To implement end-to-end business scenarios, these capabilities can be integrated with other API-based activity packages, such as Microsoft 365 or Integration Service activity packages, enabling seamless data transfer and real-time synchronization between them.

You can troubleshoot UI-based automations by quickly understanding the cause of the errors when viewing the executions via the Live Streaming and the robot Recording capabilities.

Additionally, UI Automation Cloud capabilities offer an out-of-the-box solution to automate the nFactor authentication for web business applications, which helps build automation implying multiple authentication Factors that are chained together. For more details, see [UI Automation Browser Connection](https://docs.uipath.com/activities/other/latest/user-guide/ui-automation-connection).

## Supported browsers for UI Automation

Studio Web in Automation Suite does not support browser automation.

## Installing the UiPath browser extension

You can install the UiPath browser extension from Studio Web, or from the Web Store.

### Installing the UiPath browser extension from Studio Web

To install the UiPath browser extension from Studio Web, take the following steps:

1. Open Studio Web in your selected browser.
2. Open your **RPA Workflow** project.
3. Add the **Use Application/Browser** activity, or any UI Automation activity to your project. A warning message appears indicating you need to install the UiPath extension browser.
4. Select **Install extension**. A new browser tab opens prompting you to install the extension you need.

   !['Install extension' image](/images/studio-web/studio-web-install-extension-image-595840.webp)
5. Select **Get/Add extension** to install the extension, and then return to your Studio Web project to continue automating your browser.

### Installing the UiPath browser extension from the Web Store

To install the UiPath browser extension from the Web Store, take the following steps:

1. Access the corresponding Web Store link of the browser you want to use:
   1. If you use Google Chrome, access the [Chrome Web Store](https://chromewebstore.google.com/detail/uipath-studio-web-automat/conkfbpnllelocpogdmbilgmnkabjfmf).
   2. If you use Microsoft Edge, access the [Microsoft Edge Web Store](https://microsoftedge.microsoft.com/addons/detail/uipath-extension-for-stud/hmpkmollbbcoopahpbplbdaapacncbbc).
   3. If you use Safari, access the [App Store](https://apps.apple.com/ro/app/uipath-browser-automation/id6477574719).
2. Select **Get/Add extension** to install the extension, and then return to your Studio Web project to continue automating your browser.

## Use cases

Here are some of the most common use cases for UI Automation with Studio Web.

#### Automate business scenarios

* **Customer service automation** Automating responses to common customer inquiries: get inquiries data from Outlook, upload it into business applications, and generate automatic responses.
* **Accounting automation** Create expense reports, automatically categorizing expenses and transactions to streamline bookkeeping processes.
* **Order processing** Automate order fulfillment processes with SAP Fiori, including order entry, invoicing, and shipping.
* **Employee onboarding** Use automated workflows to streamline the hiring process and onboard new employees in Workday.

#### Web scraping

* **Customer feedback analysis** Analyze customer reviews and feedback about your products and services on various review sites and social media web platforms. Use the UI Automation web scraping capabilities to gather data in real time and analyze it to improve your products or services.
* **Price comparison** Compare prices of products from various e-commerce websites. Use web scraping tools to extract pricing data from multiple sources and aggregate it for further comparison.
* **Lead generation** Generate leads by collecting contact information, such as email addresses and phone numbers, from various websites. Use the UI Automation web scraping capabilities to automate lead generation and save time and effort.
* **Product review scraping** Scrape product reviews for e-commerce websites from different sources to get insights into product quality, customer satisfaction, and potential issues. Use web scraping tools to gather reviews and analyze them to improve their products or services.

#### Automated testing

UI Automation can perform automated testing on user interfaces and ensure that they function properly under different scenarios.

## Activities

The [UI Automation activities](https://docs.uipath.com/activities/other/latest/ui-automation/about-the-ui-automation-activities-pack) are really easy to use, even if you have no previous experience in automation. These activities offer drag-and-drop interfaces, allowing you to perform point-and-click interaction to quickly build automation.

Multiple UI Automation activities available in Studio Web, including:

* [Browser Dialog Scope](https://docs.uipath.com/activities/other/latest/ui-automation/n-browser-dialog-scope)
* [Browser File Picker Scope](https://docs.uipath.com/activities/other/latest/ui-automation%22/n-browser-file-picker-scope)
* [Check/Uncheck](https://docs.uipath.com/activities/other/latest/user-guide/n-check)
* [Check App State](https://docs.uipath.com/activities/other/latest/user-guide/n-check-state)
* [Check Element](https://docs.uipath.com/activities/other/latest/user-guide/n-check-element)
* [Click](https://docs.uipath.com/activities/other/latest/user-guide/n-click)
* [Close Popup](https://docs.uipath.com/activities/other/latest/ui-automation/n-close-popup)
* [Extract Form Data](https://docs.uipath.com/activities/other/latest/ui-automation/n-extract-form-data-generic)
* [Extract Table Data](https://docs.uipath.com/activities/other/latest/user-guide/n-extract-data)
* [Fill Form](https://docs.uipath.com/activities/other/latest/ui-automation/n-fill-form)
* [Get Attribute](https://docs.uipath.com/activities/other/latest/user-guide/n-get-attribute)
* [Get Clipboard](https://docs.uipath.com/activities/other/latest/ui-automation/n-get-clipboard)
* [Get Text](https://docs.uipath.com/activities/other/latest/user-guide/n-get-text)
* [Get URL](https://docs.uipath.com/activities/other/latest/user-guide/n-get-url)
* [Go To URL](https://docs.uipath.com/activities/other/latest/user-guide/n-go-to-url)
* [Highlight](https://docs.uipath.com/activities/other/latest/user-guide/n-highlight)
* [Hover](https://docs.uipath.com/activities/other/latest/user-guide/n-hover)
* [Inject Js Script](https://docs.uipath.com/activities/other/latest/ui-automation/n-inject-js-script)
* [Keyboard Shortcuts](https://docs.uipath.com/activities/other/latest/user-guide/n-keyboard-shortcuts)
* [Mouse Scroll](https://docs.uipath.com/activities/other/latest/user-guide/n-mouse-scroll)
* [Navigate Browser](https://docs.uipath.com/activities/other/latest/user-guide/n-navigate-browser)
* [Set Clipboard](https://docs.uipath.com/activities/other/latest/ui-automation/n-set-clipboard)
* [Select Item](https://docs.uipath.com/activities/other/latest/user-guide/n-select-item)
* [Set Runtime Browser](https://docs.uipath.com/activities/other/latest/ui-automation/n-set-runtime-browser)
* [Set Value](https://docs.uipath.com/activities/other/latest/ui-automation/n-set-value)
* [Take Screenshot](https://docs.uipath.com/activities/other/latest/user-guide/n-take-screenshot)
* [Type Into](https://docs.uipath.com/activities/other/latest/user-guide/n-type-into)
* [Use Browser](https://docs.uipath.com/activities/other/latest/user-guide/n-application-card)