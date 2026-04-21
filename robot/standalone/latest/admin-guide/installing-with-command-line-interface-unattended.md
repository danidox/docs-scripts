---
title: "Installing with Command Line Interface"
visible: true
slug: "installing-with-command-line-interface-unattended"
---

To install unattended robots using command line interface (CLI), mix the available [command line parameters](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-installations). For an unattended installation, it is required to add the `RegisterService` parameter to the `ADDLOCAL` command.

:::important
The following parameters are available for the `UiPathStudio.msi` command exclusively:
* `ADDLOCAL`: `Studio`, `ExcelAddin`, `Packages`, `SapPlugin`
* `SAP_SOL_MAN_HOST`
:::