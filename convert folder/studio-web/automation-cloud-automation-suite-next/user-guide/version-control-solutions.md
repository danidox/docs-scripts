---
title: "Version control for solutions"
visible: true
slug: "version-control-solutions"
---

Version control enhances team collaboration, allowing multiple users to view, track, and restore different versions of a solution at any time. This enables developers to build and test automations without overwriting each other’s work.

Version control for solutions is handled within the **Change History** panel through **snapshots**. You can think of snapshots as "checkpoints" of the solution as various stages in its development. Snapshots preserve the entire solution state, including its automation projects, resources, and deployment configuration.

There are three types of snapshots:

1. **Auto snapshot**: The current (latest) version of a solution. It appears as **Current version** at the top of the list of snapshots in the Change History panel.
2. **Manual snapshots**: Snapshots created manually by users. They have a name and an optional description. Selecting or hovering over a manual snapshot shows the name of its author and when it was created. Can only be opened in read-only mode.
3. **Publish snapshots**: Snapshots created automatically each time the solution is published. Their name is the published solution version. Hovering over a publish snapshot shows the name of its author and when it was created. Can only be opened in read-only mode.
   :::note
   All snapshots, including manual ones, are available for anyone who has access to the solution.
   :::

The Change History panel lists all snapshots chronologically, showing their:

* Version number and description (for example, "v1.1.0 - Feedback form included").
* Author and timestamp (for example, "2 months ago by John Doe").
* Title (for example, "Stable build before testing NetSuite integration").

When you select a snapshot from the Change History panel, you are viewing the solution as it existed at that particular point in time. A temporary banner message appears when browsing a past snapshot, informing you that you are viewing a past version of the solution in read-only mode.

  ![docs image](/images/studio-web/studio-web-docs-image-625012.webp)

To create a new manual snapshot:

1. Open the Change History panel. Ensure that the **Current version** snapshot is selected.
2. Select the **Create snapshot** button in the top-right corner of the panel.
3. Enter a name for your snapshot.
4. Optionally, press the **Tab** key or select the **Add description** field to enter a description.
5. Click anywhere in the Studio Web Designer or press the **Enter** key. The new snapshot is created and is added in the Change History panel.

One of the main features of snapshots is the ability to restore the solution to a particular point in time. By default, restoring a solution from a snapshot creates a copy of the latest snapshot (that is, **Current version**) for reference. This ensures that you do not lose any work that you did on the latest version of the solution.

To access the restore feature:

1. Open the Change History panel.
2. Select a manual snapshot or a publish snapshot.
3. Right-click the snapshot.
4. Select **Restore entire solution**. The **Restore snapshot** window appears.
5. Under the **Title** field, enter a mandatory name for the copy of the latest snapshot.
6. Optionally, enter a description of the updates made to the solution.
7. Select the **Restore** button. A banner message appears, informing you that the solution was successfully restored to that particular point in time.
8. Alternatively, select **Restore without saving** to discard the latest version of the solution.

Selecting **Restore without saving** restores the solution without saving the latest snapshot (the **Current version** snapshot). This means that the latest version of your solution is deleted.
:::note
Currently, you cannot restore a shared solution.
:::