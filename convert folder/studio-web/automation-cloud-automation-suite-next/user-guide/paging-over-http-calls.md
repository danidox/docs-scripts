---
title: "Paging over HTTP calls"
visible: true
slug: "paging-over-http-calls"
---

The following tutorial demonstrates how to use the **Do While** activity to handle API pagination by making repeated HTTP calls until all data is retrieved.

Pagination indicators, such as cursors, end-of-page flags, or limits, are typically included in the response headers, response body, or as query parameters.

This example retrieves a list of breweries using the **OpenBreweryDB** API. According to the OpenBreweryDB API specification, pagination is handled using **offset-based** (page-based) parameters. To paginate through the dataset, include **per_page=X&page=Y** as query parameters in the HTTP request.

1. [Create an API workflow](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-api-workflows#creating-api-workflows).
2. Add a **HTTP** activity and configure it as follows:
   * **Method**—GET
   * **Request URL**—
     ```
     https://api.openbrewerydb.org/v1/breweries?per_page=10&page=1
     ```
3. **Debug** your API workflow to retrieve the first listing of breweries.
4. Add a **Script** activity and provide the following code:
   ```
   const url = new URL($input.request.url);
   const currentPage = Number(url.searchParams.get("page"));

   return { nextPage: currentPage + 1, 
   content: $input.content}
   ```

Using **$input** instead of **$context** ensures you always reference the output of the last executed activity, especially inside a loop block. The JavaScript code returns a JSON object with **nextPage** and **content** properties. These properties allow you to control the loop, for example: continue while **nextPage &lt; 10** or **content is not null**.
5. Add a **Loop &gt; Do While** activity above the existing **HTTP** activity.
   1. Move both **HTTP** and **Script** activities inside the **Do While** activity body.
   2. Set the **Condition** for the **Do while** activity to `$input.nextPage < 5`.
   3. For the **HTTP** activity, open the Expression editor of the **Request URL** property and update the expression to:
      ```
      "https://api.openbrewerydb.org/v1/breweries?per_page=10&page=" + ($input.nextPage == null ? 1 : $input.nextPage)
      ```
6. Debug your workflow again and notice the result array in the **Output** tab of the **Run output** panel.
7. Outside of the **Do While** activity, add a **Response** activity and configure it as follows:
   * **Type**—Success
   * **Details**—Open the Expression editor and write the following:
     ```
     $context.outputs.Do_While_1.results.flatMap(result => result.content.map(brewery => brewery.name))
     ```This summarizes the response at step 6 and lists only the names of the breweries.
8. Copy the result from the **Output** tab of the **Run ouput** panel and configure it as an **Output** schema:
   1. Open the **Data manager** panel.
   2. In the **Output** tab, select **Generate From Payload**.
   3. Paste the copied result, and select **Generate Schema**.