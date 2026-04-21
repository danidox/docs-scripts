---
title: "About accounts and groups"
visible: true
slug: "about-accounts"
---

An account allows a user or robot to authenticate on your UiPath® platform and to receive product access, roles, licenses, and robot configuration for working with the resources of your various UiPath products.

Groups are collections of objects that you want to manage together, in the same way, regarding product access, roles, licenses, or robot configuration.

## Account types

In the UiPath platform you can create **user accounts** and **robot accounts**.

### User accounts

Use these types of accounts to identify a person. You can assign licenses, roles, and add these accounts to groups.

There are two types of user accounts:

* **Local users**: These accounts are linked to a UiPath account. This type of account is created within Test Cloud and it is also managed from there by an organization administrator. Users own the account itself, but organization administrators can work with the reference of it to edit, delete, or manage roles and group memberships for it.
* **Directory users**: These accounts are defined outside of the UiPath platform, in a cloud active directory such as Microsoft Entra ID. You must link the directory to the UiPath platform to use this type of accounts. When linked, UiPath can search for and reference directory users so that you can view them, assign roles to them, or add them to UiPath groups. The benefit is that you do not need to define these identities twice: you define them once in your directory and can use them in UiPath too.

For more information, refer to [Authority over accounts and groups](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-accounts#authority-over-accounts-and-groups).

### Robot accounts

Robot accounts are helpful for when you need to run back-office **unattended** processes that should not be the responsibility of any particular user. These are our RPA-specific equivalent of service accounts. Similar to the accounts that Windows services run as application identities in the OAuth model, they are a non-user identity to be used to run unattended processes.

#### Default robot accounts

Each new organization includes a default robot account, which is automatically assigned the **Automation Users** group membership and preconfigured in Orchestrator for every new tenant. This account allows you to run unattended automations without additional setup.

#### Working with robot accounts

Robot accounts behave like user accounts in terms of permissions. In UiPath Orchestrator, you can add robot accounts and configure permissions for them in the same way as for any other account.
:::note
If only robot account groups are assigned to a folder, the individual robot accounts within those groups cannot be used to run jobs. To allow a robot account to execute jobs in a folder, the individual Robot account must be explicitly assigned to that folder.
:::

The only differences compared to user accounts are:

* Robot accounts are not allowed any interactive-related process configuration
* No email address is required to create a robot account.

You can find and work with robot accounts in broadly the same way as you work with user accounts:

* Organization administrators can create and manage robot accounts from the **Admin > Accounts & Groups** page - except not from the **Users** tab, but from the dedicated **Robot accounts** tab. Robot accounts can also be included in groups and managed as part of the group.
* When assigning roles in Orchestrator, searching for accounts shows users, groups, and also robot accounts for selection.

## Groups

Groups are used to simplify account administration. They are a collection of accounts which should have similar access, robot configuration, and licensing needs, and which you want to manage together.

For example, you might want to create a group for all of your administrators, or a group for all of your accounting employees because you know their job requires them to use the same UiPath functionality in the same way, so they should have the same licenses, robot configuration, and roles. Whenever changes to licensing or roles are required for that category of user, you update the group and the changes apply for all of its members.
:::tip
If, by exception, one of the group members requires additional roles, you can assign the extra roles to the account individually. In this case, the account benefits from the roles that were assigned individually, and the ones inherited from the groups it is in.
:::

### Types of groups

#### Local groups

Groups are natively available in the UiPath platform. If a group was created from the **Admin > Accounts and Groups > Groups** tab, then it is a local group.

#### Directory groups

If a directory is linked and includes groups, you can find and work with those directory groups in the UiPath platform in the same way as you would work with local groups.

### Inheritance

While an account is a member of a group, it inherits roles, licenses, and robot configuration from that group.

#### Roles inheritance

If assigned to more than one group, an account gets the union of all permissions assigned to the groups to which they belong.

Roles inherited through group memberships are only available while the account is connected.

You can include directory accounts in local groups. You can also **include directory groups in local groups**, even though you cannot include a local group inside of another local group.

This allows the directory administrator to fully onboard an account with the roles, licenses, and robot setup they need, without the need for additional actions in the UiPath platform.

This is achieved by adding a directory group inside a local group that is fully set up in the UiPath platform. The directory administrator then needs to only add the account to their directory group and the account inherits the setup and is ready to work.

When the various services allow access, they look at different aspects:

* When accessing a service, access is allowed based on the account's group memberships.
* When attempting to access or use resources in a service, the action is allowed based on the roles of the account, which it either inherits from a group or the required roles were granted to the account directly.

#### License inheritance

If you define license allocation rules for the group, accounts inherit these user licenses when they become members of the group.

This can happen in two ways, depending on the type of user license:

* Named user licenses: When an account becomes a member of the group, they are automatically assigned one of the available licenses. Be aware that simply removing the account from the group does not deallocate the license, because named user licenses are tied to the identity of the account.
* Multiuser licenses: A multiuser license is shared by up to three group members who use the license at different times. When one member uses the license, the other two cannot use it.
  :::important
  **Direct license allocation overwrites group allocation.** If you allocate a user license to an account directly, that account no longer benefits from any group allocation.
  :::

### Working with groups

* **Creating or deleting groups, adding or removing group members**: An organization administrator can manage groups, as well as add or remove accounts from groups from the **Admin > Accounts and Groups > Groups** tab in the UiPath platform.
* **Assigning licenses to groups**: Organization administrators also assign license allocation rules to groups from the **Admin > Licenses** page.
* **Roles for groups**: Roles are assigned to groups by the administrators of each individual service from within the service, same as for accounts. For example, learn [about users and user groups](https://docs.uipath.com/orchestrator/v0/docs/about-managing-user-access) in the Orchestrator service.

### Without user groups

If you don't want to work with user groups, grant the required roles to each account by [explicitly assigning service-level roles to each account.](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/role-management#direct-provisioning)
:::note
If you have a linked directory, make sure to also add your directory accounts to the default group **Everyone**. All local accounts are automatically added to this group. This way, all accounts are granted the [User](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/roles#organization-level-roles) organization-level role so that they can access the UiPath platform, but no roles for your services - you must assign those to each account.
:::

### Default local groups

Default groups are available in any organization and are pre-configured with organization-level roles for platform capabilities and service-level roles for UiPath services.

The default groups are **Administrators**, **Automation Users**, **Automation Developers**, **Citizen Developers**, **Automation Express**, and **Everyone**.

You can assign a fully-functional and complex access schema to users with only one action: adding them to the appropriate group. Refer to [Roles](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/roles#roles) for information about the roles included for each group.

You cannot remove roles that are assigned to the default groups and you cannot delete the groups.

If you need more control, you can create custom groups and assign your own mix of roles, or you can directly assign a role to an account.

## Account and group icons

On pages where you manage accounts, groups, or roles, specific icons are displayed for each type to help you recognize the type of account or the type of group.

### Account icons

  !['UiPath user account' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31951) - **UiPath user account**: user account that is linked to a UiPath account and signed in using basic authentication

  !['SSO user account' image](/images/activities/scripts-sso-user-account-image-UserIcon-8e12d233.png) - **SSO user account**: user account linked to a UiPath account that signed in using SSO; also applies to user accounts that have both a UiPath user account and a directory account

  !['Directory user account' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30945) - **Directory user account**: the account originates from a directory and signed in with Enterprise SSO

  !['Robot account' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/33083) - **Robot account**

### Group icons

  !['Local group' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31483) - **Local group** (or plainly, **group**): the group was created in the UiPath platform.

  !['Directory group' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30873) - **Directory group**: the group originates in a linked directory.

## Authority over accounts and groups

### Local accounts and groups

If an account or group was created from the UiPath platform:

* The organization administrator is responsible for and has the required privileges to manage the accounts and groups that belong to their organization.
* Managing accounts and groups is done within UiPath and includes creating, editing, deleting, licensing of accounts, and adding or removing accounts from groups, as well as adding or removing groups.
* Roles can be assigned by the organization administrator within services, or by a service-level administrator.

### Directory accounts and groups

If the account or group was created in a directory that is linked to UiPath:

* The directory administrator is responsible for and has the required privileges to manage the accounts and groups that belong to the directory.
* Managing accounts and groups is done within the directory and includes creating, editing, deleting of accounts, and adding or removing accounts from groups, as well as adding or removing groups.
* Directory accounts and groups are licensed from UiPath, either individually, or in bulk through group membership.
* Roles are assigned from within Admin section by either the organization administrator or service-level administrators. Roles can be assigned either individually or in bulk, through group membership.
* You can include directory accounts in local groups. You can also include a directory group inside a local group, which is not possible with local groups.