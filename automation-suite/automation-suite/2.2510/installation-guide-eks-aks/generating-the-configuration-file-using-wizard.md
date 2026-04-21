---
title: "Generating the configuration file using a wizard"
visible: true
slug: "generating-the-configuration-file-using-wizard"
---

You can generate the `input.json` configuration file either manually or using the Automation Suite Installer Wizard. While the wizard offers a more user-friendly approach, it currently does not accommodate all possible configuration scenarios.

In some specific instances, manual creation of the configuration file might be required. For details, see [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#configuring-inputjson).

To generate `input.json` using the Automation Suite Installer Wizard, take the following steps:

1. Launch the wizard on port 80 on the local host by running the following command:
   * On Linux/macOS:
     ```
     ./uipathctl config generate
     ```
   * On Windows:
     ```
     uipathctl.exe config generate
     ```To launch the wizard on a different port and host, run the following command:
   * On Linux/macOS:
     ```
     ./uipathctl config generate --port <your port> --host <your IP address>
     ```
   * On Windows:
     ```
     uipathctl.exe config generate --port <your port> --host <your IP address>
     ```
2. In a browser of your choice, launch the wizard by accessing the following URL: `http://localhost:80`.

If you chose a different host and port, make sure to replace `localhost` and `80` with the IP address and port where you want to launch the wizard.
3. Accept the license agreement.
4. Indicate the platform where you want to host Automation Suite. You can choose from the following options:
   * **Automation Suite on AKS**
     :::note
     The instructions in this guide are applicable if you choose this option.
     :::
   * **Automation Suite on EKS**
     :::note
     The instructions in this guide are applicable if you choose this option.
     :::
   * **Automation Suite on OpenShift**
   * **Automation Suite on Linux**
5. Specify your deployment mode. You can choose from the following options:
   * **Online** - Choose this option to install Automation Suite in an online environment. This deployment mode requires internet access during installation and runtime.
   * **Offline** - Choose this option to install Automation in an offline environment. This deployment mode requires an OCI-compliant container registry.

For details, refer to [Deployment scenarios](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/deployment-scenarios#deployment-scenarios).
6. Indicate your deployment type. You can choose from the following options:
   * **Highly Available** - Choose this option if you want to install Automation Suite in multi-node HA-ready mode.
   * **Lite mode** - Choose this option if you want to install Automation Suite in lite mode.

For details, refer to .
7. Provide additional details on your initial configuration. Depending on your previous selection, you may have to provide details such as the Automation Suite FQDN, admin username and password, storage class, namespace, ArgoCD project, and ArgoCD application namespace.
8. Indicate the Automation Suite products you want to enable.

For details, refer to [Automation Suite products](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/automation-suite-products#automation-suite-products).
9. Provide the details on your SQL database configuration, such as the following:
   * Whether you want to bring your own database or you want the Automation Suite installer to create it for you
   * Whether you want to use Kerberos authentication
   * The Redis cache details

For details, refer to [SQL database](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#sql-database).
10. Specify the storage configuration details, such as storage type or bucket details.

For details, refer to [Storage](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#storage).
11. If you opted for an offline installation, provide the details of your OCI-compliant registry.

For details, see [Configuring the OCI-compliant registry](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-the-oci-compliant-registry#configuring-the-oci-compliant-registry).
12. Provide your certificates details.

For details, refer to [Certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/certificate-requirements#certificate-requirements).
13. Provide details on your load balancer configuration.

For details, refer to [Networking](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/networking#networking).
14. Specify the products for which you want to perform advanced configuration such as overwrite platform-level configurations with service-level configurations such as connections strings, objectstore setup, etc.
15. Specify whether you want to bring your own components or allow the Automation Suite installer to install them.

If you bring your own components, you must manually update the generated `input.json` file. For details, refer to [Bring your own components](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#bring-your-own-components).
16. Download the `input.json` configuration file.

Any feature that is not available during the `input.json` configuration using the Automation Suite Installer Wizard, can be manually included after downloading the configuration file.