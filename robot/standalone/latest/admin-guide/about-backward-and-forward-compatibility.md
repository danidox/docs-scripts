---
title: "Compatibility matrix"
visible: true
slug: "about-backward-and-forward-compatibility"
---

The [compatibility matrix](https://docs.uipath.com/overview/other/latest/overview/compatibility-matrix) in our Overview guide displays how Robot interacts with the standalone, Automation Suite, and cloud instances of Orchestrator.

## Robot & Standalone Orchestrator

✅ - Compatible

❌ - Not compatible

:::important
* Studio and Robot always need to have the same version when installed on the same machine. For example, if you have Studio
2022.4.x installed, Robot must be 2022.4.x as well. It is usually recommended to first upgrade your Orchestrator and then your Robots. In this scenario, the Robots have to be reconnected to Orchestrator after the update.
* Automation projects created in Studio version 2021.10.6 and newer that have Windows and Cross-Platform compatibility cannot
run on of robots older than 2021.10.6 because of the [.NET version discrepancy](https://docs.uipath.com/robot/standalone/2021.10/user-guide/net6-projects-fail-to-run).
:::

| Product Version | Orchestrator 2025.10.x | Orchestrator 2024.10.x | Orchestrator 2023.10.x | Orchestrator 2023.4.x | Orchestrator 2022.10.x | Orchestrator 2022.4.x | Orchestrator 2021.10.x |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Robot 2025.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot 2024.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot 2023.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot 2023.4.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot 2022.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot 2022.4.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot 2021.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Robot, Studio & Orchestrator in Automation Suite

The below matrix provides information about the interoperability between Automation Suite Orchestrator and Robot and Studio. Patches are implicitly supported in this matrix unless specifically mentioned otherwise.

✅ - Compatible

❌ - Not compatible

|  | **Automation Suite 2.2510.0** | **Automation Suite 2024.10** | **Automation Suite 2023.10** | **Automation Suite 2023.4** | **Automation Suite 2022.10** | **Automation Suite 2022.4** | **Automation Suite 2021.10** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Robot and Studio 2025.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot and Studio 2024.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot and Studio 2023.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot and Studio 2023.4.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot and Studio 2022.10.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Robot and Studio 2022.4.x** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Robot, Studio & Orchestrator in Automation Cloud

:::important
We ensure backward compatibility with the three latest enterprise Robot and Studio releases. If you are currently using the third-latest Robot version, you should make arrangements to upgrade the Robot before we release the next Robot version, to avoid compatibility issues.
:::

|  | Cloud Orchestrator Service |
| --- | --- |
| **Robot and Studio version 2025.10** | ✅ |
| **Robot and Studio version 2024.10** | ✅ |
| **Robot and Studio version 2023.10** | ✅ |
| **Robot and Studio version 2023.4** | ❌ |
| **Robot and Studio version 2022.10** | ❌ |

## Robot & Studio in Automation Cloud™ Public Sector

This matrix shows the support for compatibility between Automation Cloud™ Public Sector Orchestrator and the Robot, and Studio. Unless otherwise stated, patches are included.

:::important
We ensure backward compatibility with the three latest enterprise Robot and Studio releases. If you are currently using the third-latest Robot version, you should make arrangements to upgrade the Robot before we release the next Robot version, to avoid compatibility issues.
:::

|  | Cloud Orchestrator Service - Public Sector |
| --- | --- |
| **Robot and Studio version 2025.10** | ✅ |
| **Robot and Studio version 2024.10** | ✅ |
| **Robot and Studio version 2023.10** | ✅ |
| **Robot and Studio version 2023.4** | ❌ |

## Automation projects

:::important
Projects opened or created in a newer Studio version cannot be reliably opened with older Studio versions. This is due to internal changes, such as new frameworks versions and feature enhancements, which are incompatible with older Studio versions. If you need to maintain compatibility with a prior Studio version, avoid opening your project in the newer Studio version until your team and environment are fully upgraded. We strongly recommend using version control (for example, Git or UiPath Cloud) and creating backups before upgrading in order to revert if backward compatibility issues arise.
:::

Projects created with alpha or beta Studio versions might not be compatible with newer Studio builds, nor can they be executed by newer Robots.

We support **backward compatibility**, except for breaking changes announced in the official [release notes](https://docs.uipath.com/release-notes/other/latest), and following the [product lifecycle](https://docs.uipath.com/overview/other/latest/overview/product-lifecycle).

Newer Robots can execute projects created with older versions of Studio. For example, a project created with Studio 2023.4 should work on a 2024.10 Robot or newer.

We do not support **forward compatibility**. Projects compiled (published) with newer versions of Studio or the UiPath Command Line Interface (CLI) might not work with older Robots. For example, a project created in Studio 2024.10 might not work with a 2023.4 Robot.

The following table outlines how projects created or published in Studio work with Robot:

| **Studio/Robot** | **Robot 2025.10** | **Robot 2024.10** | **Robot 2023.10** | **Robot 2023.4** | **Robot 2022.10** | **Robot 2022.4** | **Robot 2021.10** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Studio Web** | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Studio 2025.10** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Studio 2024.10** | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Studio 2023.10** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Studio 2023.4** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Studio 2022.10** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Studio 2022.4** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Studio 2021.10** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |