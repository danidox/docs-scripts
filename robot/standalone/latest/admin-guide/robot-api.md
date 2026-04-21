---
title: "RobotAPI"
visible: true
slug: "robot-api"
---

UiPath Robot API is a component designed to expand the functionality of your own Robot. It comes with several features, each addressing a specific aspect of automation management. These include:

* Individual job management: Provides the capability to run, stop, and track personal automation processes.
* Domain-specific interfaces: Allows for the development of tailored interfaces to meet unique automation needs.
* Local accessibility: Available only on the machine where the Robot is installed, ensuring secure and direct access.
* Version compatibility: Keeps consistent with the version of the installed Robot, which allows for backwards compatibility.

Robot API uses the UiPath.Robot.api library. Use the following feed to download the library:

```
https://uipath.pkgs.visualstudio.com/Public.Feeds/_packaging/UiPath-Official/nuget/v3/index.json.
```

## Compatibility matrix

| Robot Version | API 2025.10.x | API 2024.10.x | API 2023.10.x | API 2023.4.x | API 2022.10.x | API 2022.4.x | API 2021.10.x |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Robot 2025.10.x | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Robot 2024.10.x | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Robot 2023.10.x | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Robot 2023.4.x | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Robot 2022.10.x | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Robot 2022.4.x | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Robot 2021.10.x | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

## Common Robot API calls

| Description | .NET Robot API call |
| --- | --- |
| Including the client in your application | ``` var client = new RobotClient(); ``` |
| Getting the list of available processes | ``` var processes = await client.GetProcesses();  var myProcess = processes.Single(process => process.Name == "MyProcess");  var job = myProcess.ToJob(); ``` |
| Using the process key to start a job | ``` var job = new Job("812e908a-7609-4b81-86db-73e3c1438be4"); ``` |
| Starting a process execution | ``` {  await client.RunJob(job);  }  catch (Exception ex)  {  Console.WriteLine(ex.ToString());  } ``` |
| Adding input arguments | ``` job.InputArguments = {["numbers"] = new int[] { 1, 2, 3 }};  await client.RunJob(job); ``` |
| Exporting output arguments | ``` var jobOutput = await client.RunJob(job);  Console.WriteLine(jobOutput.Arguments["sumOfNumbers"]); ``` |
| Stopping a process | ``` await client.RunJob(job, cancellationToken); ``` |
| Monitoring the process status | ``` job.StatusChanged += (sender, args) => Console.WriteLine($"{((Job)sender).ProcessKey}: {args.Status}");  await client.RunJob(job); ``` |
| Using the event scheduler | ``` new RobotClient(new RobotClientSettings { EventScheduler = TaskScheduler.Default }) ``` |