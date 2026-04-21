---
title: "Exploring the user interface"
visible: true
slug: "exploring-the-test-cloud-user-interface"
---

As you explore the user interface, you can discover various components and features that empower you to manage your tasks and access functionalities relevant to your user personas.

## Portal navigation

Figure 1. Test Cloud portal navigation

![Test Cloud portal navigation](/images/activities/scripts-test-cloud-portal-navigation-537260-2f81f99a.webp)

### The header

The portal header provides the context of your location inside the Test Cloud interface. It is a persistent element that remains at the top of every page. Depending on the service context you are in, the header bar provides additional navigation capabilities that are specific to that service.

Figure 2. The Test Cloud header

![The Test Cloud header](/images/activities/scripts-the-test-cloud-header-535339-bf7ae4ac.webp)

:::important
Occasionally, the Automation Cloud logo may display instead of the Test Cloud logo. You can fix this issue by clearing your browser's local storage or cache.
:::

The portal header offers quick access to essential features and tools, as follows:

* **The app launcher** – Allows you to switch between different products or modules within the Test Cloud interface.
* **Your current location** – Shows your location within the Test Cloud interface.
* **The help menu** – Provides access to comprehensive documentation, support resources, the option to submit feedback, and assistance channels for any questions or issues you may encounter.
  :::note
  The documentation offers a search feature powered by generative AI. The search generates answers using UiPath's official documentation as a reference. While the search aims for accuracy, we suggest you cross-check the responses with the documentation for complete precision.
  :::

Figure 3. The Test Cloud help menu

  ![The Test Cloud help menu](/images/activities/scripts-the-test-cloud-help-menu-530780-4ca07bdd.webp)
* **The notifications menu** – Keeps you informed about updates, alerts, and notifications relevant to your user persona and activities within the Test Cloud interface. Also allows you to configure notification settings. For more information on notifications, visit [About notifications](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-notifications#notifications-panel).
* **The tenant picker** – Displays the active tenant and allows you to switch tenants.
* **The user menu** – Grants you access to your profile preferences, allowing you to customize your experience as needed.

### The left rail

The left rail provides access to core sections of the Test Cloud interface, and displays your favorite services. The options displayed in the left rail depend on your user persona and role.

The left rail can be condensed, while showing the following services: Home, Orchestrator, and Studio.

Figure 4. Condensed Test Cloud left rail

  ![Condensed Test Cloud left rail](/images/activities/scripts-condensed-test-cloud-left-rail-530772-2c9738cf.webp)

When you expand the left rail, it displays the services that you have available in your tenant.

Figure 5. Expanded Test Cloud left rail

  ![Expanded Test Cloud left rail](/images/activities/scripts-expanded-test-cloud-left-rail-531107-62573df5.webp)

1. **Home**: Allows you to return to the **Homepage**, your central hub for platform navigation and task management. The **Home** option is visible by default, and you cannot remove it from your favorites.
2. **Favorite services icons**: Help you switch between your favorite services and modules available within the Test Cloud interface, ensuring you can access the tools specific to your responsibilities. By default, the following favorites are shown: Home, Orchestrator, Studio, and Test Manager. Note that you can view only the favorite services relevant to your user persona.
3. **Favorites**: Shows the **Home** option and a maximum of four favorite services. You cannot remove the **Home** option from your favorites.
4. **All services**: Displays all services and modules to which you have access. This is where you can add or remove services from favorites using the **Favorite** icon. Services and modules are grouped as follows:
   1. Services grouped by UiPath pillar: **Build**, and **Operate**.
   2. All the remaining navigation links, including **Admin**, are grouped under the **More** category. If you are an organization administrator, the **Admin** section contains tools and controls for configuring and managing the Test Cloud interface according to your organization's needs.

## Homepage

The **Homepage** serves as the landing page after you log in. It is designed to provide a personalized experience based on your role within the organization and the services provisioned in the tenant you are currently in.

Test Cloud allows you to view your Test Manager projects, your recent test executions, access your Orchestrator services, and view metrics on license consumption and distribution.
:::note
The **Organization Administrator** role gives you full **View** permissions for the **Home** page. Users with the **User** role do not have **View** permissions on the following widgets on the **Home** page: **License allocation**.
:::

### Widgets

The **Homepage** is customized to cater to the application testing user persona, offered by Test Cloud. The following mapping illustrates the widgets available for the **Application Tester** and **Application Test Developer** personas:

* **Carousel banner**: Promotes getting started experiences, announcements, webinars, feature releases, and other application testing relevant content.
* **Test Manager projects**: Offers quick access to the Test Manager projects available in the current tenant.
* **Recent test executions**: Displays the recently run test executions.
* **Orchestrator services**: Quick-access cards to your Orchestrator tenants. Select **Manage** to land on the **Tenants** page, where you can edit the tenants and their enabled services, if you have the required permissions.
* **License allocation**: The snapshot view of user and robot license allocations, displaying the total number of licenses available in your organization versus the total number of licenses allocated. A license is considered allocated if it belongs to a service. The following tabs are available:
  + **Users** - For user-specific licenses assigned to a user account, providing the right to use certain UiPath® functionality or products.
  + **Robots & Services** - For robot and service specific licenses, used for executing unattended processes, or to provide certain functionality.

## Search box

The search box is displayed in the homepage header, and it retrieves information from the Marketplace and UiPath® documentation databases.

Figure 6. Search box on Test Cloud homepage

  ![Search box on the Test Cloud homepage](/images/activities/scripts-search-box-on-the-test-cloud-homepage-537267-3395856c.webp)

### Search box functionality

The following examples show the behavior of the search box, while using `gmail` as a keyword:

* **Search**: The first four Marketplace results are shown at the top, followed by the first four UiPath® documentation results.
* **See all results**: Select **See all** to be redirected to the respective search surface on Marketplace or UiPath® documentation. Once redirected, the `gmail` search keyword shows up in the Marketplace and UiPath® documentation search boxes as well.

## Notifications panel

Notifications are displayed in the **Notifications panel**. To access the **Notifications panel**, select the bell icon, located in the top navigation bar.

  !['Notifications panel' image](/images/activities/scripts-notifications-panel-image-100222-bb1193d6.webp)

### Notifications settings page

You can modify the settings of your notifications from the **Notifications** settings page.

Select the **user account**!['User account icon' image](/images/activities/scripts-user-account-icon-image-user_account_icon_AutomationCloud_screenshot-cc4fd585.png) icon, go to **Preferences**, and then go to **Notifications**.

You can also access the **Notifications** settings page through the **Notifications panel**. Select the **settings**!['Settings icon' image](/images/activities/scripts-settings-icon-image-gear_icon_notifications_panel_screenshot-f313693c.png) icon in the Notifications panel.

### Notifications page

The **Notifications** page keeps track of all the notifications that your organization received. The page allows you to check notifications that you cleared, but want to revisit.

To access the **Notifications** page, select the **Notifications page** icon in the top-right of the **Notifications panel**.

### Notification subscriptions

To personalize notifications received in the **Notifications panel**, you can subscribe to, or unsubscribe from events or severity types.

### Data retention policy for notifications

Notifications clear after a 30 day period.