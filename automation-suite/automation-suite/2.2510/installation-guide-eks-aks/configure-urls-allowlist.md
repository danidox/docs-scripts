---
title: "Configuring an allowlist for connector
         domains"
visible: true
slug: "configure-urls-allowlist"
---

If you have restrictions in place that prevent data from leaving your cluster, you must configure an allowlist for the specific domain of each connector you want to use.

For some connectors, the domain may depend on values or credentials you provide during connection creation.

The following table lists the domains you must add to the allowlist for each connector and provides samples for some of them.

Expand Table

| Connector | Domain |
| --- | --- |
| Act! 365 | `app.act365.com` |
| ActiveCampaign | Based on user sandbox. Sample: `uipath1663561860.api-us1.com` |
| Active Directory | Based on user sandbox |
| Adobe Acrobat Sign | Based on user sandbox |
| Adobe PDF Services | `pdf-services-{environment}.adobe.io` |
| Amazon Bedrock | Based on user sandbox |
| Amazon Connect | Based on user sandbox. Sample: `connect.{aws.region}.amazonaws.com` |
| Amazon Polly | Based on user sandbox. Sample: `polly.{aws.region}.amazonaws.com` |
| Amazon SES | Based on user sandbox. Sample: `email.{aws.region}.amazonaws.com` |
| Amazon Transcribe | Based on user sandbox. Sample: `transcribe.{aws.region}.amazonaws.com` |
| Amazon Web Services | Based on user sandbox. Sample: `{serviceName}.{region}.amazonaws.com` |
| Anthropic Claude | `api.anthropic.com` |
| Asana | Based on user sandbox. Sample: `app.asana.com` |
| Azure AI Document Intelligence | Based on user sandbox. Sample: `{endpoint}.cognitiveservices.azure.com` |
| AWeber | `api.aweber.com` |
| Azure Maps | `atlas.microsoft.com` |
| BambooHR | `api.bamboohr.com` |
| Box | `api.box.com` |
| Brevo | `api.brevo.com/v3` |
| Calendly | `api.calendly.com` |
| Campaign Monitor | `api.createsend.com` |
| Citrix ShareFile | Based on user sandbox. Sample: `{subdomain}.{apicp}/sf/v3` |
| Cisco Webex Teams | `webexapis.com` |
| Citrix Hypervisor | Based on user sandbox |
| Clearbit | `person.clearbit.com` |
| Confluence Cloud | `api.atlassian.com` |
| Constant Contact | `api.cc.email` |
| Customer.io | `track.customer.io` |
| Datadog | Based on user sandbox |
| DeepSeek | `api.deepseek.com` |
| Deputy | Based on user sandbox |
| DocuSign | Based on user sandbox |
| Drip | `api.getdrip.com` |
| Dropbox | `api.dropboxapi.com/2` |
| Egnyte | Based on user sandbox |
| Eventbrite | `eventbriteapi.com` |
| Exchangerates | `api.exchangeratesapi.io` |
| Expensify | `integrations.expensify.com` |
| Facebook | `graph.facebook.com` |
| FreshBooks | `api.freshbooks.com` |
| Freshdesk | `Based on user sandbox. Sample: {domain}.freshdesk.com` |
| Freshsales | Based on user sandbox. Sample: `{domain}.myfreshworks.com/crm/sales/api`, `{domain}.freshsales.io/api/` |
| Freshservice | Based on user sandbox. Sample: `clouddeveloper.freshservice.com` |
| GetResponse | `api.getresponse.com/v3` |
| GitHub | `api.github.com` |
| Gmail | `googleapis.com` |
| Google Cloud Platform | `compute.googleapis.com` |
| Google Docs | `docs.googleapis.com` |
| Google Drive | `googleapis.com` |
| Google Maps | `maps.googleapis.com` |
| Google Sheets | `sheets.googleapis.com` |
| Google Speech-to-Text | `speech.googleapis.com` |
| Google Text-to-Speech | `texttospeech.googleapis.com` |
| Google Vertex | Based on user sandbox. Sample: `{region}-aiplatform.googleapis.com` |
| Google Vision | `vision.googleapis.com` |
| Google Workspace | `googleapis.com` |
| GoToWebinar | `api.getgo.com` |
| Hootsuite | `platform.hootsuite.com` |
| HubSpot Marketing | `api.hubapi.com` |
| HubSpot CRM | `api.hubapi.com` |
| HyperV | Based on user sandbox |
| Icertis | Based on user sandbox. Sample: `{tenantName}.icertis.com/api` |
| iContact | `app.icontact.com` |
| Insightly CRM | `api.insightly.com` |
| Intercom | Based on user sandbox |
| Jina AI | `api.jina.ai/v1`, `r.jina.ai` |
| Jira | For OAuth 2.0 app: `api.atlassian.com` For Basic authentication: based on user sandbox. |
| Keap | `api.infusionsoft.com` |
| Klaviyo | `a.klaviyo.com` |
| LinkedIn | `api.linkedin.com` |
| Mailchimp | Based on user sandbox |
| Mailgun | Based on user sandbox |
| MailerLite | `connect.mailerlite.com` |
| Mailjet | `api.mailjet.com` |
| Marketo | Based on user sandbox. Sample: `136-TVZ-720.mktorest.com` |
| Microsoft 365 | `graph.microsoft.com` |
| Microsoft Azure | `management.azure.com` |
| Microsoft Azure OpenAI | Based on user sandbox. Sample: `{subdomain}.openai.azure.com` |
| Microsoft Azure Active Directory | `graph.microsoft.com` |
| Microsoft Dynamics 365 CRM | Based on user sandbox |
| Microsoft Outlook 365 (Legacy) | `graph.microsoft.com` |
| Microsoft Outlook 365 | `graph.microsoft.com` |
| Microsoft Sentiment | Based on user sandbox |
| Microsoft Teams | `graph.microsoft.com` |
| Microsoft Translator | `api.cognitive.microsofttranslator.com` |
| Microsoft Vision | Based on user sandbox. Sample: `{subscription.region}.api.cognitive.microsoft.com` |
| Miro | `api.miro.com` |
| NetIQ eDirectory | Based on user sandbox |
| Okta | Based on user sandbox |
| OpenAI | `api.openai.com` |
| Oracle Eloqua | Based on user sandbox |
| Oracle Netsuite | Based on user sandbox |
| PayPal | `{environment}.paypal.com` |
| PDFMonkey | `api.pdfmonkey.io` |
| Perplexity | `api.perplexity.ai` |
| Pinecone | Based on user sandbox |
| Pipedrive | `api.pipedrive.com` |
| QuickBooks Online | Based on user sandbox |
| Quip | `platform.quip.com/` |
| Salesforce | Based on user sandbox. Sample: `uipath-b1-dev-ed.develop.my.salesforce.com` |
| Salesforce Marketing Cloud | Based on user sandbox. Sample: `{tenantName}.rest.marketingcloudapis.com` |
| SAP Concur | Based on user sandbox |
| SAP Cloud for Customer | Based on user sandbox. Sample: `{tenantName}.crm.ondemand.com` |
| SAP BAPI | Based on user sandbox |
| SAP OData | `{sap_host}/sap/opu/odata/sap` |
| SendGrid | `api.sendgrid.com/v3/` |
| ServiceNow | Based on user sandbox |
| Shopify | Based on user sandbox. Sample: `{store_name}.myshopify.com` |
| Slack | `slack.com` |
| SmartRecruiters | `api.smartrecruiters.com` |
| Smartsheet | Based on user sandbox. Sample: `api.{region}` |
| Snowflake | Based on user sandbox. Sample: `cz99177.west-us-2.azure.snowflakecomputing.com` |
| Stripe | `api.stripe.com` |
| Sugar Enterprise | Based on user sandbox |
| Sugar Professional | Based on user sandbox |
| Sugar Sell | Based on user sandbox |
| Sugar Serve | Based on user sandbox |
| System Center | Based on user sandbox |
| TangoCard | Based on user sandbox. Sample: `{environment}.tangocard.com/raas/v2` |
| Todoist | `api.todoist.com` |
| Trello | `api.trello.com` |
| Twilio | `api.twilio.com` |
| VMware ESXi vSphere | Based on user sandbox |
| X | `api.twitter.com` |
| WhatsApp Business | `graph.facebook.com` |
| WooCommerce | Based on user sandbox |
| Workable | Based on user sandbox. Sample: `{subdomain}.workable.com` |
| Workday | Based on user sandbox |
| YouTube | `googleapis.com/youtube/v3` |
| IBM watsonx.ai | `us-south.ml.cloud.ibm.com` |
| WhatsApp Business | graph.facebook.com |
| Zendesk | Based on user sandbox. Sample: `{tenantName}.zendesk.com` |
| Zoho Campaigns | Based on user sandbox |
| Zoho Desk | Based on user sandbox. Sample: `desk.{environment}` |
| Zoom | `api.zoom.us` |
| ZoomInfo | `api.zoominfo.com` |
| Zoho Mail | Based on user sandbox |