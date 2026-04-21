---
title: "Supported Process Argument Types"
visible: true
slug: "officially-supported-process-argument-types"
---

Please find below a list containing the input and output argument types supported when adding a process to an app.

## Supported Argument Types

| Supported Type | .NET type | Description | Limitation (If any) |
| --- | --- | --- | --- |
| Text | [System.String](https://docs.microsoft.com/en-us/dotnet/api/system.string?view=netcore-3.1) | Text |  |
| Number (Integer, Double, Float, Decimal) | [System.Int16](https://docs.microsoft.com/en-us/dotnet/api/system.int16?view=netcore-3.1), [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/system.int32?view=netcore-3.1), [System.Int64](https://docs.microsoft.com/en-us/dotnet/api/system.int64?view=netcore-3.1), [System.UInt16](https://docs.microsoft.com/en-us/dotnet/api/system.uint16?view=netcore-3.1),[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/system.uint32?view=netcore-3.1),[System.UInt64](https://docs.microsoft.com/en-us/dotnet/api/system.uint64?view=netcore-3.1),[System.Double](https://docs.microsoft.com/en-us/dotnet/api/system.double?view=net-5.0), [System.Single](https://docs.microsoft.com/en-us/dotnet/api/system.single?view=net-5.0)  [System.Decimal](https://docs.microsoft.com/en-us/dotnet/api/system.decimal?view=net-5.0) | Integer/Floating point Numeric type & Decimal value |  |
| Boolean | [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/system.boolean?view=netcore-3.1) | True/False |  |
| DateTime | [System.DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime?view=netcore-3.1), [System.DateTimeOffset](https://docs.microsoft.com/en-us/dotnet/api/system.datetimeoffset?view=netcore-3.1) | Date and time | Customers should always use UTC or include a DateTimeOffset |
| Supported Type[](List) | [System.Array](https://docs.microsoft.com/en-us/dotnet/api/system.array?view=netcore-3.1) | Array of supported types. For example array of text or numbers |  |
| List &lt;ST&gt; (List) | [System.Collections.Generic.List](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=netcore-3.1) | List of supported types. |  |
| IList &lt;ST&gt; (List) | [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/system.collections.ilist?view=netcore-3.1) | Iterable list of supported types. |  |

:::important
* Data without timezone information should be treated as UTC.
* Data with timezone information will be displayed to the end-user in their browser’s timezone.
:::
:::note
If a data type is not explicitly supported, the following logic is applied:
* If the datatype ends with “[]”, it is an array.
* If the datatype came back as “null”, it is interpreted as “anything” by Apps
* If the datatype is neither "[]" nor "null", it is interpreted as an “object”
:::

## Supported Inference Types

For any.NET type variable not supported by Apps in its out of the box format, the Job history can be used to infer with the DataType, At least 1 job that matches the current version of the process is needed. Keep in mind that this type of auto-detection is not always precise. Please verify them on the UiPath Process properties page and change them if needed.

| Supported Inference Type (SIT) | .NET type | Description |
| --- | --- | --- |
| DataTable | [System.Data.DataTable](https://docs.microsoft.com/en-us/dotnet/api/system.data.datatable?view=netcore-3.1) | The Tabular Data field detection inference is based and may not identify types correctly, even if they are Supported Types. |
| SIT[](List) | [System.Array](https://docs.microsoft.com/en-us/dotnet/api/system.array?view=netcore-3.1) | List of supported inference types. |
| UiPath Generic | [UiPath.Core.GenericValue](https://docs.uipath.com/studio/standalone/2024.10/user-guide/uipath-proprietary-variables) | Common default type in Studio. |
| Object | [System.Object](https://docs.microsoft.com/en-us/dotnet/api/system.object?view=netcore-3.1) | A generic Object |

:::important
**Object fields such as DataTable &gt; DataColumn also use inference based detection**, even when those fields are Supported Types. This may lead to unpredictability, so you can manually specify fields for DataTable and other Objects within App Studio. DataTable: Only the data from a DataTable can be used within an app. Field Constraints, Expression Columns, and Primary Keys are not supported.
:::

## Following Arguments Will Be Supported in Future

| Supported Type (ST) | .Net Type | Description |
| --- | --- | --- |
| TimeSpan | [System.TimeSpan](https://docs.microsoft.com/en-us/dotnet/api/system.timespan?view=netcore-3.1) | A time interval |
| IEnumerable | [System.Collections.Generic.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1?view=netcore-3.1) | Iterable list of Choices. Treated same as Enum/ChoiceSet |
| ChoiceSet | [System.Enum](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum) | List of Choices |

:::note
* The process payload size limit between Robot Service and Robot Executor is 10 MB.
* The entire process arguments of a single process cannot exceed 10 MB.
:::