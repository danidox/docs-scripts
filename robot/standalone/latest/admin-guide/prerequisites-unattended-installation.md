---
title: "Prerequisites"
visible: true
slug: "prerequisites-unattended-installation"
---

Before proceeding with the robot installation, check out the [compatibility matrix](https://docs.uipath.com/robot/standalone/latest/admin-guide/about-backward-and-forward-compatibility#compatibility-matrix), as well as the [hardware and software requirements](https://docs.uipath.com/robot/standalone/latest/admin-guide/hardware-and-software-requirements#hardware-and-software-requirements).

## User permissions to run automations

Ensure that the user account set to run the automation meets the following requirements:

* Is part of the **Remote Desktop Users** group. Otherwise, add it in **Computer Management** &gt; **System Tools** &gt; **Local Users and Groups** &gt; **Groups** &gt; **Remote Desktop Users**.
* Has the User Rights Assignments, under **Local Computer Policy &gt; Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; Local Policies &gt; User Rights Assignment**:
  + [Allow log on locally](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/allow-log-on-locally)
  + [Access this computer from the network](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/access-this-computer-from-the-network) - only for High-Density Robots
  + [Allow log on through Remote Desktop Services](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/allow-log-on-through-remote-desktop-services) - only for High-Density Robots You can add the group, where your user is a member, in these policies, as shown in the image.
  ![docs image](/images/robot/robot-docs-image-446736.webp)