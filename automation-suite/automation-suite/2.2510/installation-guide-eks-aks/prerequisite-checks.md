---
title: "Prerequisite checks"
visible: true
slug: "prerequisite-checks"
---

It is recommended to run prerequisite checks to ensure that you properly configured the cloud infrastructure and to validate `input.json` before starting the Automation Suite installation.

You can run a prerequisite check using the command. By default, this command verifies all the prerequisites. You can use the following flags:

* `--excluded`, if you want to exclude components from the execution.
* `--verbose`, if you want to access the detailed prerequisites check output. You can skip this flag for a more concise and simplified output.

The prerequisite and health checks/tests run in the `<uipath>` namespace. You must either grant the `uipathctl` tool the necessary permissions to allow the creation of the `<uipath>` namespace or create it yourself before running the checks/tests. Additionally, some checks/tests require that you enable the use of `hostNetwork`.

The checks in the following table are run on each node:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Check
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Description
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d14249e60">
    <p>
     SQL Connection
    </p>
   </td>
   <td headers="d14249e64">
    Validates that Automation Suite can successfully connect to the SQL server for UiPath&reg; products and shared services (such
                                 as Identity, Portal, Org Mamagement, etc.) using the SQL connection strings provided in the
    <code>
     input.json
    </code>
    file. This is mandatory for a successful installation.
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     SQL DB roles
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Validates the necessary roles and permissions required by UiPath&reg; products. This is mandatory for a successful installation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     SQL DB compatibility
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Validates SQL DB compatibility requirements.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     FQDN resolution
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Validates that the FQDN and the sub-domains are successfully resolvable.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Object Storage API
    </p>
   </td>
   <td headers="d14249e64">
    Validates that objectstore APIs are accessible based on access information provided in the
    <code>
     input.json
    </code>
    file. This is mandatory for a successful installation of the UiPath&reg; services.
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Cache / Redis
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Validates the connection to Cloud Redis or ElastiCache. This is mandatory for a successful installation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Capacity
    </p>
   </td>
   <td headers="d14249e64">
    Validates you have minimum CPU and RAM capacity on the worker nodes based on the products enabled in the
    <code>
     input.json
    </code>
    file.
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Storage Class
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Validates that the storage classes for File Storage are configured as required for Automation Suite Robots.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Optional Components
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Validates that your cluster has components that you chose to exclude from the Automation Suite installation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Ingress
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Validates that the cluster ingress is configured correctly and the FQDN URL requests can reach UiPath&reg; products.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Network Policies
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Checks if the network policies configured in Automation Suite are compatible with the cluster.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Registry
    </p>
   </td>
   <td headers="d14249e64">
    <p>
     Validates that Automation Suite can access the UiPath&reg; docker registry. This is mandatory for a successful installation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    <p>
     Cluster Connectivity
    </p>
   </td>
   <td headers="d14249e64">
    Validates whether the cluster communication is configured properly:
    <ul>
     <li>
      <p>
       Between two random pods completed
      </p>
     </li>
     <li>
      <p>
       Between pod and a multinode ClusterIP
      </p>
     </li>
     <li>
      <p>
       Between pod and a multinode ClusterIP without a clusterIP
      </p>
     </li>
     <li>
      <p>
       Between pod and a multinode ClusterIP using HostNetwork
      </p>
     </li>
     <li>
      <p>
       Between pod and a multinode ClusterIP without a clusterIP set using HostNetwork
      </p>
     </li>
     <li>
      <p>
       Between two pods colocated on the same node via ClusterIP
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14249e60">
    Queues
   </td>
   <td headers="d14249e64">
    Validates that queue APIs are accessible based on access information provided in
    <code>
     input.json
    </code>
    and that the required queues exist. This is mandatory for a successful installation.
   </td>
  </tr>
 </tbody>
</table>