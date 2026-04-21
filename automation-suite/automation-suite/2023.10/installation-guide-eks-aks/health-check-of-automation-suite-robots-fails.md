---
title: "Health check of Automation Suite Robots fails"
visible: true
slug: "health-check-of-automation-suite-robots-fails"
---

## Description

After installing Automation Suite on AKS, when you check the health status of the Automation Suite robots pod, it returns an unhealthy status: "[POD_UNHEALTHY] Pod asrobots-migrations-cvzfn in namespace uipath is in Failed status".

## Potential issue

On rare occassions, database migrations for Orchestrator and Automation Suite robots may run at the same time. In this case, migrating the database of Automation Suite robots fails. In Argo CD, you can see two migration pods: one with a healthy status, one with an unhealthy status.

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/278315)

## Solution

The database migration for Automation Suite robots is automatically retried, and renders successful. However, Argo CD does not update the status. You can ignore the unhealthy status.