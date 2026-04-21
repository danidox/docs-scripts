---
title: "Redirecting robots through a proxy server"
visible: true
slug: "redirecting-unattended-robots-through-a-proxy-server"
---

Whenever your infrastructure uses a proxy for machines/users to connect to the internet, you will also need to configure the Robot to use it.

There are two possible configurations based on the Robot installation mode:

1. Attended Robot - user-mode installation
2. Unattended Robot - service-mode installation

## Configuring the proxy for Attended robots (user-mode)

Attended robots inherit the proxy settings configured for your web browser.

If your proxy needs basic authentication, Assistant will prompt you to input your credentials when you first try to connect the Robot to Orchestrator.

You can setup the proxy by using the old way described at [Configuring using the web browser](https://docs.uipath.com/robot/standalone/latest/admin-guide/redirecting-unattended-robots-through-a-proxy-server#configuring-the-proxy-using-the-web-browser) or using the [Windows proxy settings](https://docs.uipath.com/robot/standalone/latest/admin-guide/redirecting-unattended-robots-through-a-proxy-server#configuring-the-proxy-using-windows-settings)

## Configuring the proxy for Unattended robots (service-mode)

To correctly configure the Service Mode robots to use the proxy, you need to modify both the `proxy.json` file and the corresponding Windows Settings of the user account(s) that will run automations.

For configuring the proxy in `proxy.json` follow the [Configuring the proxy settings](https://docs.uipath.com/robot/standalone/latest/admin-guide/redirecting-unattended-robots-through-a-proxy-server#configuring-the-proxy-using-the-proxyjson-file)

For configuring the proxy for the user account(s) that will run automations, follow the [Configuring the proxy for Attended Robots](https://docs.uipath.com/robot/standalone/latest/admin-guide/redirecting-unattended-robots-through-a-proxy-server)

## Configuring the proxy using the web browser

1. Open the **Internet Properties** window.
2. On the **Connections** tab, select **LAN settings**. The **Local Area Network (LAN) Settings** window opens. Depending on your setup, you can set a proxy configuration script or a proxy server.
   ![docs image](/images/robot/robot-docs-image-447965.webp)

   1. To use a proxy script, select **Use automatic configuration script**, and provide the address to the script.
   2. To manually set up the proxy server, select **Use a proxy server for your LAN**, then provide the address of the proxy server and the port.
3. To save your settings, select **OK**.
4. In your web browser, test the connection by accessing the Orchestrator URL.

## Configuring the proxy using Windows settings

1. Open the **Proxy** settings window.
2. To use a proxy script, under **Automatic proxy setup**, switch on the **Use setup script**. Provide the address to the script.
3. To manually set up the proxy server, under **Manual proxy setup**, switch on the **Use a proxy server**. Provide the address of the proxy server and the port.
   :::important
   Adding the `http://` prefix to the proxy server address prevents Robot from making HTTPS calls. To ensure the proxy works as expected, remove the `http://` prefix entirely or add the proxy address with both `http://` and `https://` prefixes. For example:
   * Incorrect - `http://proxyaddress`,
   * Correct - `https://proxyaddress`, `http://proxyaddress; https://proxyaddress`
   :::
4. To save your settings, select **Save**.

## Configuring the proxy using the `proxy.json` file

Starting with 2025.10, to configure the proxy for the Unattended Robot (service-mode), you need to modify the `proxy.json` file. If you are updating from an older version and you already have a proxy setup in place, it is automatically migrated to the new file.

1. Navigate to: `%ProgramData%\UiPath\Shared`.
2. Search `proxy.json`file and open it using a text editor with administrator privileges, such as Notepad++.

The `proxy.json` file supports multiple configurations, but not all at the same time. If both `ScriptAddress` and `ProxyAddress` are present, `ScriptAddress` takes precedence.

   ```
   {
     "ScriptAddress": "http://localhost/proxy.pac",
     "ProxyAddress": "http://1.1.1.1:1234/",
     "BypassLocalAddresses": true,
     "BypassList": "server\\.domain\\.local$;www.google.com;192\\.168\\.\\d{1,3}\\.\\d{1,3}",
     "UserName": "myUser",
     "Password": "myPassword",
     "Domain": "myDomain"
   }
   ```
   :::note
   The bypass list should contain an array of regular expression strings that contain the URIs of the servers to bypass. When you want to escape a character in a regex, you will need to use `\\` (eg: `.` is escaped as `\\.`).
   :::

   1. To use a proxy script, provide the following json:
      ```
      {
      "ScriptAddress" : "http://proxy.address/proxy.pac"
      }
      ```
   2. To provide a proxy address, provide the following json:
      ```
      {
        "ProxyAddress": "http://proxy.address:1234/",
        "BypassLocalAddresses": true,
        "BypassList": "server\.domain\.local$;www.google.com;192\.168\.\d{1,3}\.\d{1,3}",
        "UserName": "myUser", #used for basic auth
        "Password": "myPassword", #used for basic auth
        "Domain": "myDomain"
      }
      ```
3. Save the `proxy.json` file.
4. Restart the Robot service or the device.

## Configuring the proxy settings during Robot installation

To add the proxy settings while installing Unattended robots (service-mode), use the dedicated command line parameters in your installation command.

For example, the following command installs the Robot in Service Mode and uses a script to configure proxy:

```
UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot,RegisterService PROXY_SCRIPT_ADDRESS=http://localhost/proxy.pac
```

The following command installs the Robot in Service Mode and sets up the Basic Authentication for proxy settings:

```
UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot,RegisterService PROXY_ADDRESS=http://my.proxy.net:8008 PROXY_USERNAME="myUser" PROXY_PASSWORD="myUser" PROXY_DOMAIN="myUser"
```

## Checking the proxy server connection

1. Connect the Robot to Orchestrator
2. Deploy some packages to an environment which contains the previously configured Robot.
3. Navigate to the `%userprofile%\.nuget\` folder and check if the corresponding process and activities packages have been downloaded.
4. Run the corresponding job to check if it runs successfully.