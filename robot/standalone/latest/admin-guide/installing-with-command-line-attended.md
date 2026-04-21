---
title: "Installing with Command Line"
visible: true
slug: "installing-with-command-line-attended"
---

To install attended robots using command line interface (CLI), mix the available [command line parameters](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-installations#using-the-command-prompt). For an attended installation, do not add the `RegisterService` parameter to the `ADDLOCAL` command.

:::important
The following parameters are available for the `UiPathStudio.msi` command exclusively:
* `ADDLOCAL`: `Studio`, `ExcelAddin`, `Packages`, `SapPlugin`
* `SAP_SOL_MAN_HOST`
:::