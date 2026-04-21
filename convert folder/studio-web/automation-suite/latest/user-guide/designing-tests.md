---
title: "Designing tests"
visible: true
slug: "designing-tests"
---

After your **Tests** project is available in **Studio Web**, you can begin designing your test cases by adding activities to a test case from that project. These activities help you simulate user actions, validate expected results, and build robust, automated test logic.

Designing test cases in **Tests** projects resembles designing workflows in RPA workflow projects. For detailed information on managing project files, configuring activities, or handling other project resources, refer to the [Designing RPA workflow projects] chapter.

This page walks you through creating a basic test case using the [Testing Activities](https://docs.uipath.com/activities/other/latest/workflow/about-the-testing-activities-pack) package in Studio Web.

## Steps

To create a simple test case in Studio Web, follow these steps:

1. In Studio Web, navigate to your previously created **Tests** project. Alternatively, open a Tests project from Test Manager by going to the test case's Automation tab and selecting **Open in Studio Web**.
2. In the **Explorer** panel, select the test case created when you linked from Test Manager (or choose any other test case in the project).
3. Add activities to the test case: Studio Web supports a wide range of activities across multiple categories, including from the Testing Activities package.
   1. Select **Add activity** in the Designer panel.
   2. Use the search bar to find and add the **Assign Variable Value** activity.
      1. Create a string variable named `userEmail` and input it in the **To Variable** field.
      2. In the **Set Value** field, enter an email address, such as: "johndoe@exmaple.com".
   3. Add a **Log Message** activity and enter a message such as: `"Validating email address: " + userEmail`.
   4. To verify the value, add a **Verify Expression** activity, and use the following expression: `userEmail = "johndoe@example.com"`.
   5. Add a final **Log message** activity to indicate the test case has completed.
   ![Overview of a test case in Studio Web's designer panel](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/603446)