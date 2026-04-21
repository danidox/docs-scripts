---
title: "SDK Specifications"
visible: true
slug: "sdk-specifications"
---

## Methods and properties

You can include the following methods and properties in your custom application or web page.

## Init

The `init` method is optional. It returns the **IRobotSDK** instance, which enables you to store it as a variable for later use.

```
const robot = UiPathRobot.init();
```

## Settings

The `settings` property of type Settings allows you to change the default port number, the poll interval time in milliseconds, or to disable sending telemetry data.

```
const robot = UiPathRobot.init();
robot.settings.portNumber = 1234;
robot.settings.pollTimeInterval = 1000;
robot.settings.disableTelemetry = true;
```

## On

The `on` method is used to attach event handlers to the SDK.

The available SDK events are `consent-prompt`, `missing-components` and `open-uipath-protocol`.

## consent-prompt

The UiPath JavaScript SDK comes with a built-in consent overlay displayed every time your custom application or web page needs to connect to the Robot.

This consent overlay can be overridden with a custom handler.

```
const robot = UiPathRobot.init();
robot.on('consent-prompt', consentCode => console.log(consentCode));
```

## missing-components

The `missing-components` event is raised when the Robot JS Service is not running. In this case, the SDK displays an error, which can be overridden with a custom handler.

```
const robot = UiPathRobot.init();
robot.on('missing-components', () => console.log('Missing Components'));
```

## open-uipath-protocol

Before being shown the consent prompt you might be asked to allow the browser to open a uipath-web URL in the associated application.

By default, RobotJS will automatically try to open this URL, but users can override this behavior by providing a custom event handler.

```
const robot = UiPathRobot.init();
robot.on('open-uipath-protocol', (protocolUrl) => console.log('RobotJS protocol URL: ' + protocolUrl));
```

## Get Processes

The `getProcesses` method retrieves the list of available processes. Returns a Promise to an array of [RobotProcess](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications) objects. If the Robot is connected to Orchestrator, it retrieves the processes from the environment and folder the Robot is a part of. Otherwise, local processes are retrieved.

```
const robot = UiPathRobot.init();
const processes = await robot.getProcesses();
for(let i=0; i<processes.length; i++){
    console.log(processes[i].name + " (" + processes[i].description + ") - Id=" + processes[i].id);
}
```

## Get Input Arguments Schema

Using the `inputArgumentsSchema` property of an installed process, you can retrieve the input arguments of a process. Before using the `inputArgumentsSchema` property, you need to first install the process.

The `installProcess` method installs a process and returns a Promise to an object of type [InstallProcessResult](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications), which contains an array of [InputArgumentSchema](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications) objects.

```
const robot = UiPathRobot.init();
const processes = await robot.getProcesses();
const installedProcess = await robot.installProcess(processes[0].id);
for(let i=0; i<installedProcess.inputArgumentsSchema.length; i++){
    console.log("Argument " + i + ":");
    console.log("  name: " + installedProcess.inputArgumentsSchema[i].name)
    console.log("  type: " + installedProcess.inputArgumentsSchema[i].type)
    console.log("  isRequired: " + installedProcess.inputArgumentsSchema[i].isRequired)
    console.log("  hasDefault: " + installedProcess.inputArgumentsSchema[i].hasDefault)
}
```

:::note
In TypeScript, the method `install` of a [RobotProcess](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications) object can be used to install a process.
:::

```
const robot = UiPathRobot.init();
const processes = await robot.getProcesses();
const myProcess = processes.find(p => p.name === "MyProcess");
const installedProcess = await myProcess.install();
```

## Start Job

The `startJob` method receives an already created `Job` and starts it. It returns a Promise to an object of type [JobResult](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications), which contains the output arguments.

The `createJob` method creates a robot Job using the Process Id. It can optionally receive the job input arguments. It returns a [Job](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications) object.

:::note
Starting with v2022.10, the process list is refreshed in parallel with the process execution, prior to this, the process list was refreshed before the process started. This means that when running a process for which an update is available, the job might run with the older version of the process.
:::

```
robot = UiPathRobot.init();
processes = await robot.getProcesses();
const calculatorProcess = processes.find(p => p.name.includes('Calculator'));
const arguments = {
    "input1" : 23,
    "input2" : 42,
    "operation" : "add"
};
const job = robot.createJob(calculatorProcess.id, arguments);
const result = await robot.startJob(job);
console.log(result.Sum);
```

:::note
In TypeScript, a Job can be created by using the [Job](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications) class constructor.
:::

```
robot = UiPathRobot.init();
processes = await robot.getProcesses();
const calculatorProcess = processes.find(p => p.name.includes('Calculator'));
const arguments = {
    "input1" : 23,
    "input2" : 42,
    "operation" : "add"
};
const job = new Job(calculatorProcess.id, arguments);
const result = await robot.startJob(job);
console.log(result.Sum);
```

## Job On

The `on` method of the `Job` object is used to attach event handlers to the job . The events available are `status` and `workflow-event`.

## status

The `status` event is raised during the job execution each time the status of the job has changed.

This event is also raised each time the [ReportStatus](https://docs.uipath.com/activities/docs/report-status) activity is executed.

```
const robot = UiPathRobot.init();
const job = robot.createJob('processId');
job.on('status', robotStatus => console.log(robotStatus));
await robot.startJob(job);
```

## workflow-event

The `workflow-event` event is raised during the job execution each time an activity that sends a workflow event is executed. It is the support for implementing partial results with the help of [send interim results](https://docs.uipath.com/activities/docs/send-interim-result) activity. The event handler has an argument of type [WorkflowEventData](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications).

```
const robot = UiPathRobot.init();
const job = robot.createJob('processId');
job.on('workflow-event', e => console.log(e.name));
await robot.startJob(job);
```

## Start Process

The method `start` of the object [RobotProcess](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications) is used to start a process by passing it input arguments, if available.

It returns an object of type [JobPromise](https://docs.uipath.com/robot/standalone/latest/developer-guide/sdk-specifications#sdk-specifications).

```
const robot = UiPathRobot.init();
const processes = await robot.getProcesses();
const myProcess = processes.find(p => p.name === "MyProcess");
const arguments = {
    "a" : 41,
    "b" " 27
};
const result = await myProcess.start(arguments);
```

## Process On Status

The `onStatus` method is used to attach an event handler to the 'status' event of the Job.

```
const robot = UiPathRobot.init();
const processes = await robot.getProcesses();
const myProcess = processes.find(p => p.name === "MyProcess");
const result = await myProcess.start().onStatus(status => console.log(status));
```

## Process On Workflow Event

The `onWorkflowEvent` method is used to attach an event handler to the 'workflow-event' event of the Job.

```
const robot = UiPathRobot.init();
const processes = await robot.getProcesses();
const myProcess = processes.find(p => p.name === "MyProcess");
const result = await myProcess.start().onWorkflowEvent(e => console.log(e.name));
```

## Stop Process

The `stopProcess` method is used to stop an executing robot process.

It returns a promise which is resolved on successful cancellation of the running robot process.

```
const robot = UiPathRobot.init();
const processes = await robot.getProcesses();
const myProcess = processes.find(p => p.name === "MyProcess");
const result = await myProcess.start();
await robot.stopProcess(myProcess);
```

## Model Definitions

## IRobotSDK

```
interface IRobotSDK {
    settings: Settings;
    getProcesses(): Promise<Array<RobotProcess>>;
    init(): IRobotSDK;
    on(eventName: string, callback: (argument?: any) => void): void;
    startJob(job: Job): Promise<JobResult>;
    stopProcess(process: RobotProcess): Promise<void>;
    installProcess(processId: string): Promise<InstallProcessResult>;
}
```

## Settings

```
class Settings {
    portNumber: number;
    pollTimeInterval: number;
    disableTelemetry: boolean;
}
```

## RobotProcess

```
class RobotProcess {
    id: string;
    name: string;
    description?: string;
    start: (inArguments?: any) => JobPromise;
    install: () => Promise<InstallProcessResult>;
}
```

## InstallProcessResult

```
class InstallProcessResult {
    inputArgumentsSchema: InputArgumentSchema[]
}
```

## InputArgumentSchema

```
class InputArgumentSchema {
    name: string;
    type: string;
    isRequired: boolean;
    hasDefault: boolean;
}
```

## JobPromise

```
class JobPromise {
    onStatus(eventHanlder: (argument?: any) => void): JobPromise;
    onWorkflowEvent(eventHanlder: (argument?: any) => void): JobPromise;
}
```

## Job

```
class Job {
    processId: string;
    argument?: any;
    jobId: string;
    on(eventName: string, eventHanlder: (argument?: any) => void): void;
}
```

## JobResult

```
class JobResult {
    [Key: string]: any;
}
```

## WorkflowEventData

```
class WorkflowEventData {
    name: string;
    payload: string;
}
```