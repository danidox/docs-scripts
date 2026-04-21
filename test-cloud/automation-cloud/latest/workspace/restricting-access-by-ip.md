---
title: "Restricting access by IP"
visible: true
slug: "restricting-access-by-ip"
---

![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555) This feature is available on all tiers in the Enterprise licensing plan.

If you want to secure access to your organization and only allow users that are within your corporate network to access it, you can specify the IP addresses you want to allow and we block all other traffic.

!['Restricting access by IP' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30629)

## Before you begin

### Prerequisites

To use this security option you need domain expertise on your corporate network and IP ranges.

### Scope

The IP restriction impacts:

* Your users who sign in through the user interface
* Your programs and automations that use the platform APIs or the APIs of UiPath services
* Robots that consume the platform APIs or the APIs of UiPath services.

If the agent - user, robot or program - does not have one of the trusted IPs, after you enforce IP restriction, they cannot interact with your organization, all its tenants, their services, or related APIs.

### Supported IP addresses

* You can define trusted IP ranges for addresses of the types IPv4 or IPv6.
* You must use the Classless Inter-Domain Routing (CIDR) IP format.
* You cannot define trusted IP ranges for private addresses.

### Testing environment

We strongly recommend performing this configuration and testing it in a non-production environment before applying the configuration in production to avoid disruptions to your users and your automation projects.

## Adding trusted IP ranges
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

If your private network uses a known set of IP addresses, you can add them in Security Settings to only allow users from those addresses to access your organization.

1. Go to **Admin**.
2. Make sure that the organization is selected at the top of the left pane and then select **Security Settings**.

The **Security Settings** page for the organization opens.
3. Along the top, select the **IP Restriction** tab:
   !['IP restriction tab' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30741)
4. Add a set of IP addresses.

You can add trusted IP ranges one by one by selecting **Add trusted IP range**, or add them in bulk by selecting **Upload CSV**. For detailed instructions, navigate further.

After you enable IP restriction, as described further, only users and programs that have an IP that was declared in one of the trusted IP ranges can access your organization. If the IPs are not declared, the users encounter an **Access forbidden** message when trying to access the organization.

**Next steps**: After you have added all of the IP sets, proceed with the instructions in the next section to enable IP restriction.

### Adding trusted IPs one by one

1. Select **Add trusted IP range**. The **Add trusted IP range** panel opens at the right of the window.
2. Fill in the **IP set name** field with a suggestive name for this range.
3. Under **Add IP range(s)**, in the field, type a trusted IP address. The address can be IPv4 or IPv6 and must be in Classless Inter-Domain Routing (CIDR) format.
4. To add another address, select **Add more** under the field to add another field.

Users who have an IP that is included in this range will be able to access your organization. Users with any other address will not.
   :::note
   Your current IP is shown at the top of the panel so that you make sure to include it, otherwise you won't be able to enable IP restriction. This is because if your IP address is not included in a trusted range, enabling IP restriction would lock you out.
   :::
5. Select **Add** at the bottom of the panel.

The panel closes and the set is displayed on the page.
6. Repeat the previous step to add as many sets of IP addresses as you need.

### Adding trusted IPs in bulk

1. On your local machine, create a new CSV file as follows:
   * The header (first row or first value) must include `IP Ranges`.
   * Add each trusted IP range (in CIDR format) as a new value, or a new row.
   * If working in a table format, you should obtain a one-column table with `IP Ranges` being the first row. If working in CSV format, you should have one row, with `IP Ranges` being the first value.
2. Save the file locally under any name, with a **.csv** extension.
3. On the **IP Restriction** page, select **Upload CSV**.

The **Upload CSV** dialog opens.
4. Select **Upload file** and select the CSV file you created.

The upload begins and a success message is displayed along the top after it completes.Imported IP ranges are displayed in the list of trusted IP ranges with an **IP set name** of the form **Imported on <date>**. You can edit the set to update the name.

   !['IP restriction tab' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/200871)

In case any errors are detected in the uploaded file, the import is aborted. The **Error Summary** displays information about what IP ranges could not be imported and why. Select **OK** to close the dialog. You must fix the indicated errors and then try again.

## Enabling or disabling IP restriction

Enable IP restriction to block traffic from IP addresses other than the trusted IP ranges you have declared, or disable it to allow access from any IP.

1. Go to **Admin**.
2. Make sure that the organization is selected at the top of the left pane and then select **Security Settings**.

The **Security Settings** page for the organization opens.
3. Along the top, select the **IP Restriction** tab.
4. On the right, under **Enforcement type**, select an option:
   * To enable IP restriction, select **Allow only trusted IPs**.

Only agents that use an IP which is included in one of the trusted IP ranges can access your organization.
   * To disable IP restrictions, select **Allow all IPs**.

Even if trusted IP ranges are defined on the page, access is allowed from any IP when this option is set.
5. In the confirmation dialog, select **Confirm** to enable IP restriction.

Depending on your cloud offering, you must [contact Support](https://www.uipath.com/company/contact-us/contact-technical-support) for assistance in IP range restrictions. The support team will handle the setup of these restrictions based on your specific CIDR ranges.

## Getting help

In case you accidentally lock yourself out, or encounter other issues, [contact Support](https://www.uipath.com/company/contact-us/contact-technical-support) for assistance.