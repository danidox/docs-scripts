---
title: "Managing accounts and groups"
visible: true
slug: "managing-accounts-and-groups"
---

Organization administrators manage user accounts, robot accounts, and groups at the organization level. Account and group management controls how users and robots authenticate, which services they can access, and which licenses and roles they receive.

Accounts represent identities in the organization. UiPath supports both user accounts, which represent individual users, and robot accounts, which are used to run unattended automations. Groups are collections of accounts that simplify access management by allowing roles, licenses, and robot settings to be assigned once and inherited by all members.

Depending on the cloud offering that you are using, refer to the following procedures:

* [Managing accounts and groups for Test Cloud and Test Cloud Public Sector](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#managing-accounts-and-local-groups-for-test-cloud-and-test-cloud-public-sector)
* [Managing accounts and groups for Test Cloud Dedicated](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-group#managing-accounts-and-groups-for-test-cloud-dedicated)

## Accounts

User accounts allow people to sign in to the organization and access UiPath services. Robot accounts represent non-human identities and are used to run unattended automations. Robot accounts can be added to groups so that they inherit roles, licenses, and configuration defined at the group level.

Account creation and management behavior depends on whether the organization uses local accounts or integrates with an external directory. Some account properties, such as names or passwords, may be restricted for directory-managed accounts.

## Groups

Groups define a reusable set of access rules. By adding accounts to groups, administrators can control permissions, license allocation, and robot behavior at scale.

UiPath includes built-in groups, such as **Everyone** and **Administrators**, as well as custom groups created by administrators. Built-in groups cannot be renamed or deleted. All users added to an organization are members of the Everyone group by default.

Custom groups can be used to:

* Assign roles across services
* Allocate licenses automatically
* Apply robot configuration consistently
* Simplify access audits and maintenance

## Inheritance and access management

When an account belongs to one or more groups, it inherits all roles, licenses, and settings assigned to those groups. An account can also have roles or licenses assigned directly, depending on configuration.

Access is enforced across UiPath services based on the combined result of:

* Group memberships
* Direct role assignments
* License allocation rules

Roles and permissions are evaluated and enforced by the relevant UiPath services, such as Orchestrator.

## Account and group lifecycle

Administrators can add, edit, and remove accounts and groups as organizational needs change. Removing an account immediately prevents that identity from accessing the organization. Removing a group revokes any roles, licenses, or robot configuration that accounts inherited from that group.

An organization must always have at least one administrator. Built-in users, built-in groups, and directory-managed identities have additional restrictions on editing or removal.