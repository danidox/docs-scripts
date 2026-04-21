---
title: "Setting up Linux robots"
visible: true
slug: "setting-up-linux-robots"
---

To set up robots in a [Linux environment](https://docs.uipath.com/robot/standalone/latest/admin-guide/docker-installation#installing-on-linux), you need an existing [unattended setup](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-robots-modern-folders#unattended-setup) in Orchestrator.

The following procedure downloads the docker image on Linux and connects the Robot to Orchestrator:

1. In a command line terminal, [download the Docker image](https://docs.uipath.com/robot/standalone/latest/admin-guide/docker-installation#installing-on-linux):
   ```
   docker pull uipathprod.azurecr.io/robot/uiautomation-runtime:latest24.10
   ```
2. Once the image is displayed in your Docker environment, accept the license agreement, and connect the robot to Orchestrator.
   1. Using the client ID and the client secret of the machine template:
      ```
      docker run -e LICENSE_AGREEMENT=accept -e ORCHESTRATOR_URL="https://cloud.uipath.com/organization/tentant/orchestrator_"-e CLIENT_ID="$Client_ID" -e CLIENT_SECRET="$Client_secret" -tid uipathprod.azurecr.io/robot/uiautomation-runtime:latest24.10
      ```
   2. Using the machine key:
      ```
      docker run -e LICENSE_AGREEMENT=accept -e ORCHESTRATOR_URL="https://cloud.uipath.com/organization/tentant/orchestrator_" -e MACHINE_KEY="$KEY" -tid uipathprod.azurecr.io/robot/uiautomation-runtime:latest24.10
      ```
3. To see the status of the robots on your machine, run:
   ```
   docker ps -a
   ```
4. To disconnect a robot, run:
   ```
   docker stop {container_id}
   ```
5. To stop the robot, but keep it connected to Orchestrator, run:
   ```
   docker kill {container_id}
   ```
6. To retrieve the logs from the container, run:
   ```
   docker cp <ContainerId>:/home/robotuser/.local/share/UiPath/Logs <TargetPath>
   ```