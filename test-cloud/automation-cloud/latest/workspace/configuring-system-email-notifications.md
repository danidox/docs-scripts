---
title: "Configuring system email notifications"
visible: true
slug: "configuring-system-email-notifications"
---

Email notifications provide alerts for events like password recovery, license status, product updates, and resource-specific notifications such as job or robot alerts.

Notifications can be related to user accounts (password recovery), or be related to events from services such as Orchestrator.

## Using default email settings

Default email settings are preconfigured parameters provided by UiPath for sending system email notifications. Default settings use the SendGrid SMTP server and are designed to work out of the box, requiring no additional customization.

1. Go to **Admin**, select your organization, and then select **Mail Settings**. The **Mail Settings** page for the organization opens.
2. Select the **Use default mail settings** checkbox to use the default SendGrid SMTP server. The default SMTP settings are described on the page and cannot be changed.

This applies the custom configuration to all emails sent within the context of the organization.

### Default email settings

The default mail settings use the SendGrid SMTP server with the settings described in the following table:

|  |  |  |
| --- | --- | --- |
| **Setting** | **Description** | **Value** |
| **Sender address** | The email address that is used as the source of the emails being sent. It represents the identity of the sender and is displayed in the recipient's inbox as the address from which the email originated. | admin@mydomain.com |
| **Sender name** | The human-readable name associated with the sender's email address. It appears alongside the sender's email address in the recipient's inbox. | mydomain.com mailer |

## Using custom email settings

Customizing mail settings helps you tailor your email communication to precise specifications.

1. Go to **Admin**, select your organization, and then select **Mail Settings**. The **Mail Settings** page for the organization opens.
2. Select the **Use custom mail settings** checkbox to set up your own server.
3. Configure the custom email settings, by providing the neccessary information for your SMTP configuration.
4. After entering the SMTP details, select **Test mail settings** to validate your settings. The **Test mail settings** page opens.
5. Add an email address for sending the test email, and select **Send**. This sends a test email to a designated email address to ensure that your configuration is correct and functioning as expected. Make sure to check your inbox for the test email.
6. Once the test email is successfully sent and received, select **Save** to save the custom SMTP settings. This applies the custom configuration to all emails sent within the context of the organization.

### Custom email settings

To configure custom email settings for your own SMTP server, provide the necessary information for your SMTP configuration, as described in the following table:

|  |  |  |
| --- | --- | --- |
| **Setting** | **Description** | **Example** |
| **Hostname** | The SMTP server that handles the sending of your emails. | Smtp.office.com |
| **Domain** | The email server responsible for handling emails. | Provider.com |
| **Port** | The communication port used for sending emails. Port 25 is commonly used, but some email providers also offer ports like 587. | 25 |
| **Timeout** | Maximum duration that the system waits for a response from the SMTP server. If the server does not respond within the specified timeout period, the attempt is considered unsuccessful. | 180,000 ms |
| **Use TLS encryption** | When enabled, it ensures that sensitive data remains confidential during transit. | N/A |
| **Require authentication** | When enabled, you should provide valid credentials (username and password) before the system is allowed to send emails through the SMTP server. | Username: name@name.com  Password: ******** |
| **Sender address** | The email address that is used as the source of the emails being sent. It represents the identity of the sender and is displayed in the recipient's inbox as the address from which the email originated. | admin@mydomain.com |
| **Sender name** | The human-readable name associated with the sender's email address. It appears alongside the sender's email address in the recipient's inbox. | mydomain.com mailer |