---
title: "Updating the cluster configuration"
visible: true
slug: "updating-the-cluster-configuration"
---

After regenerating the `cluster_config.json` file but before performing the upgrade, you can make various changes, such as updates to the database configuration, certificate configuration, and more. For details, see [Performing advanced configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/advanced-installation-experience#step-14%3A-applying-advanced-configuration).

Additionally, there are a few service-specific configurations that you must apply before upgrading. To check which changes are required for your Automation Suite cluster, see the following table:

Expand Table

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Conditions </p> </th>
   <th> <p> Actions </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p> 1. You installed Automation Suite 2023.4 or earlier in an offline environment. </p>
      <ul>
        <li> AND </li>
      </ul>
<p> 2. You upgrade to Automation Suite 2023.10 or later. </p> </td>
   <td> You must manually add <code>install_type: offline</code> to the <code>cluster_config.json</code> file. <button> assignment </button><pre>&#123; "install_type": "offline" "fqdn": "&lt;sample_fqdn&gt;" , &hellip; }</pre> </td>
  </tr>
  <tr>
   <td> <p> 1. Orchestrator is installed on the old Automation Suite version. </p>
      <ul>
        <li> AND </li>
      </ul>
<p> 2. You upgrade from Automation Suite 2022.10. </p> </td>
   <td> Set the following parameter in the <code>cluster_config.json</code> file to confirm that you agree with blocking classic folder executions. Without consent, the upgrade will fail. <button> assignment </button><pre>... "orchestrator": &#123; "enabled": true, "block_classic_executions": true, ...</pre><p> For details, see <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/orchestrator-configuration#orchestrator-specific-configuration"> Orchestrator-specific configuration </a> . </p> </td>
  </tr>
  <tr>
   <td> <p> 1. Apps is installed on the old Automation Suite version. </p>
      <ul>
        <li> AND </li>
      </ul>
<p> 2. You upgrade from Automation Suite 2022.10 or earlier. </p> </td>
   <td>
      <ol>
        <li> Create a database for Apps with the following default name: <code>AutomationSuite_Apps</code> . </li>
        <li> If you want to overwrite the default SQL connection string, update the ODBC connection string for the Apps database in the <code>cluster_config.json</code> file. </li>
      </ol>
<button> assignment </button><pre>&#123; "apps": &#123; "sql_connection_str": "SERVER=sqlserver.mycompany.com,1433;DATABASE=AutomationSuite_Apps;DRIVER=&#123;ODBC Driver 17 for SQL Server};UID=testadmin;PWD=***;MultipleActiveResultSets=False;Encrypt=YES;TrustServerCertificate=NO;Connection Timeout=30;" } }</pre><p> For an example of the ODBC connection string, see <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/database-configuration#database-configuration"> Database configuration </a> . </p> </td>
  </tr>
  <tr>
   <td> <p> 1. AI Center is installed on the old Automation Suite version and connects to an external Orchestrator. </p> </td>
   <td>
      <ol>
        <li> <p> Copy the Orchestrator certificates to the server node on which you plan to trigger the upgrade. For details, see <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/copy-orchestrator-certificate#copy-the-orchestrator-certificate"> Copy the Orchestrator certificate to the virtual machine </a> . </p> </li>
        <li> Update the <code>cluster_config.json</code> file with the following configuration: <button> assignment </button><pre>"aicenter": &#123; "enabled": true, "orchestrator_url": "https://orchestrator.example.com", //Specify the Orchestrator URL for AI Center "identity_server_url": "https://orchestrator.example.com/identity", //Specify the Identiy URL for AI Center "orchestrator_cert_file_path": "/opt/UiPathAutomationSuite/UiPath_Installer/orch.cer", //Specify the path to the Orchestrator certificate "identity_cert_file_path": "/opt/UiPathAutomationSuite/UiPath_Installer/orch.cer", //Specify the path to Identity certificate file "metering_api_key": "test" //Specify the metering API key }</pre> </li>
        <li> Ensure that <code>cluster_config.json</code> includes the following parameter: <button> assignment </button><pre>&#123; "sql_connection_string_template": "DOTNET connection string templates", "sql_connection_string_template_odbc": "ODBC connection string templates" }</pre> </li>
      </ol>
</td>
  </tr>
  <tr>
   <td> <p> 1. Document Understanding is already installed on the old Automation Suite version. </p>
      <ul>
        <li> AND </li>
      </ul>
<p> 2. You upgrade from Automation Suite 2023.10.3 or earlier to Automation Suite 2023.10.4 or later. </p> </td>
   <td>
      <ol>
        <li> Add the <code>pyodbc_connection_string</code> connection string in the <code>data_manager</code> section: <button> assignment </button><pre>"documentunderstanding": &#123; ... "datamanager": &#123; ... "pyodbc_sql_connection_str": "***" // python sql connection string } }</pre> </li>
      </ol>
</td>
  </tr>
  <tr>
   <td> <p> 1. Document Understanding was not installed on the old Automation Suite version. </p>
      <ul>
        <li> AND </li>
      </ul>
<p> 2. You upgrade from Automation Suite 2023.10.3 or earlier to Automation Suite 2023.10.4 or later. </p> </td>
   <td>
      <ol>
        <li> Add or merge the entire Document Understanding section: <button> assignment </button><pre>"documentunderstanding": &#123; "enabled": true, "sql_connection_str": "" // dotnet connection string, "datamanager": &#123; "sql_connection_str": "" // odbc connection string "pyodbc_sql_connection_str": "***" // python sql connection string } }</pre> </li>
      </ol>
</td>
  </tr>
  <tr>
   <td> <p> 1. Process Mining is installed on the old Automation Suite version. </p>
      <ul>
        <li> AND </li>
      </ul>
<p> 2. You want to use latest version of Airflow which needs PostgreSQL. </p><p>Note: <p> For Process Mining on Automation Suite 2023.10.9 or higher, using PostgreSQL for the Airflow database is the recommended option. </p></p></td>
   <td>
      <ol>
        <li> Update the <code>sqlalchemy</code> connection string template applicable for PostgreSQL in the <code>cluster_config.json</code> file before the upgrade. </li>
      </ol>
<p><code>postgresql_connection_string_template_sqlalchemy_pyodbc</code></p><button> assignment </button><pre>postgresql+psycopg2://&lt;user&gt;:&lt;password&gt;@&lt;postgresql host&gt;:&lt;postgresql port&gt;/&lt;airflow db name&gt;</pre><p>Note: <p> When upgrading from Microsoft SQL Server to PostgreSQL database data migration is not required. </p> Note: <p> For details, refer to <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/updating-the-sql-database#providing-the-new-connection-strings-for-installed-products"> Providing the new connection strings for installed products </a> . </p></p></td>
  </tr>
  <tr>
   <td> 1. Process Mining is not installed on the old Automation Suite version.
      <ul>
        <li> AND </li>
      </ul>
2. You want to use latest version of Airflow which needs PostgreSQL. <p>Note: <p> For Process Mining on Automation Suite 2023.10.9 or higher, using PostgreSQL for the Airflow database is the recommended option. </p></p></td>
   <td>
      <ol>
        <li> Add the <code>sqlalchemy</code> connection string template applicable for PostgreSQL in the <code>cluster_config.json</code> file before the upgrade. </li>
      </ol>
<p><code>postgresql_connection_string_template_sqlalchemy_pyodbc</code></p><button> assignment </button><pre>postgresql+psycopg2://&lt;user&gt;:&lt;password&gt;@&lt;postgresql host&gt;:&lt;postgresql port&gt;/DB_NAME_PLACEHOLDER</pre><p>Note: <p> When upgrading from Microsoft SQL Server to PostgreSQL database data migration is not required. </p> Note: <p> For details, refer to <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/updating-the-sql-database#providing-the-new-connection-strings-for-installed-products"> Providing the new connection strings for installed products </a> . </p></p></td>
  </tr>
 </tbody>
</table>