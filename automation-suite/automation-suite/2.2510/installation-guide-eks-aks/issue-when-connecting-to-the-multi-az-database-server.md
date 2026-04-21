---
title: "Issue with connecting to the Multi-AZ database
            server"
visible: true
slug: "issue-when-connecting-to-the-multi-az-database-server"
---

## Description

You get the `Connecting to a mirrored SQL Server instance using the MultiSubnetFailover connection option is not supported` error when connecting to Multi-AZ database while using the `MultiSubnetFailover=True` parameter in the connection string.

## Solution

To fix the issue, you must ensure that you are using the listener endpoint and not the normal endpoint.

:::note
If you try to connect to the normal endpoint without the `MultiSubnetFailover=True` parameter in the connection string, this could lead to issues.
:::

If you are using a Multi-AZ with Always On SQL setup, more details about the options for RDS can be found in [Amazon documentation for Multi-AZ deployments for Amazon RDS for Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html).