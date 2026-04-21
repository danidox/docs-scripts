---
title: "Deploying the Robot to multiple machines"
visible: true
slug: "deploying-to-multiple-machines-unattended"
---

You can deploy Studio, Robot, and Assistant to multiple virtual or physical machines using various mass deployment tools. The steps to follow differ depending on the infrastructure and deployment tools used in your organization. There are a few general principles to consider before deploying, such as making sure that the target computers:

* Meet the hardware and software requirements.
* Run on the same operating system.
* Are part of the same network group.
* Have access to the resource from which the installation will be pushed.

Options available for mass deployment include:

* Redistribute the installer through high-availability network storage.
* Deploy through [System Center Configuration Manager](https://learn.microsoft.com/en-us/mem/configmgr/core/understand/introduction) (SCCM). When using SCCM, take into account that:
  + The version that is installed must match the version that is advertised.
  + The installation must be performed from the command line in silent mode.
* Deploy through [Group Policy](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects).
* Deploy through [Remote Desktop Services](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds).
* Deploy though third-party solutions such as [PDQ Deploy](https://help.pdq.com/hc/en-us/articles/220509287-How-It-Works-PDQ-Deploy).
* Deploy through [Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/overview.html).