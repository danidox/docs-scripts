---
title: "Performance best practices"
visible: true
slug: "performance-best-practices"
---

## Recommended maximums

:::note
The following maximum values are recommended for an optimal app performance. Exceeding these values may lead to performance degradation, but Apps does not impose any limit.
:::

1. Use maximum 200 controls on a page.
2. Include maximum five complex controls on a page, such as tables or grids.
3. Use page containers in maximum 10 tabs per **Tab** control.
4. Nest maximum five containers.
5. Nest maximum ten rules in an event.
6. Use **Table** controls to display maximum 200 read-only records.

## Optimized page load

1. Use the same page container and variables to load individual pages. Say you have a multi-step form, where steps are sequential and the content of every step resides in an individual page. On the starting page, instead of having containers for each step, reuse the same page container and load a different page into it by using a variable or the If-Then-Else rule.
2. Use less **Tab** and **Page** containers on a page, to improve the initial loading of the page.

## Recommended control configuration

1. Use **Edit grid** control to display and edit tabular records or large datasets. This control offers sorting, pagination, and server-side capabilities, enabling it to display more than 1,000 entity records.
2. For read-only **Edit grid** controls, disable the editing capabilities in the app designer to speed up rendering and to remove editing icons for a cleaner layout.
3. Enhance the rendering speed of the **Edit grid** control by adjusting the height to a maximum of 1200px. This modification concurrently optimizes the number of rows visible.
4. If you are using the same formatting style across multiple lines in a **Rich Text Editor** control, apply the style at once rather than for each individual line. Doing so saves the time spent to render the style for each line.
5. For **Image** controls, we recommend keeping image sizes above 50% of the original size. Use a lower resolution for small logos, and avoid using high-definition images to ensure optimal performance.
6. To ensure successful video playbacks in **IFrame** controls, use the embed links provided by the hosting site.
7. To improve readibility and app user experience, we recommend using seven options or less for **Radio Button** controls, and stacking them vertically when the width is restricted. To use more than seven options, use **Dropdown** controls.
8. Do not set the width of **Table** controls to `auto`, to prevent unexpected shifts in column widths due to varying content lengths, or to prevent tables from becoming too narrow on smaller screens. This also enable virtual scrolling in the table.
9. Use pixels to set the width and height of **Table** controls, to render tables more quickly, or to prevent table cells from overflowing or wrapping when the content is too large. This also enable virtual scrolling in the table.
10. To reuse the output of a `Fetch()` or a `GetChoiceSet()` function, assign the output to a variable of type `ListSource` using the **Set Value** rule.

## Recommended page design

1. Each page should contain a single use case. For example, in an organization management scenario, you can have an overview page and then a separate page for each department, such as IT, HR, Finance. For a typical add/edit scenario, consider using an **Edit grid** control instead of additional edit / add forms. Split complex pages into modular pages, then use page containers to display them.
2. In some cases, you may need to display contextual content on a page, where different sections on the page are mutually exclusive and become visible based on specific conditions, such as the value of an app variable. We recommend to implement this scenario as follows:
   1. Create separate pages for each section that needs to be displayed conditionally.
   2. On the main page where these sections should be displayed, add a page container.
   3. Use the **Open page** rule to display the relevant section in the page container by selecting the page container as the target.
   4. Add an **If-Then-Else** rule to determine which page should be rendered, based on the variable value. This ensures that only the appropriate page is displayed, resulting in a more efficient and streamlined user experience.

## Recommended page, page container and tab usage

[Page Container](https://docs.uipath.com/apps/automation-suite/latest/user-guide/tabs#tabs) controls allow you to reuse a page within another page. Continuously switching pages in a Page Container can cause high memory usage in the browser. The upper limit of page switch events which cause this high memory usage depends on the volume of RAM in your system.

[Tab](https://docs.uipath.com/apps/automation-suite/latest/user-guide/tabs#tabs) controls allow you to reuse a page in multiple tabs. Using the Tab control is more efficient in terms of memory usage than replicating tabs using Page Container controls.

The effect is compounded if you are using both Tabs and Page Containers which replicate the same page. We recommend you avoid replicating the same page excessively in Tabs or Page Containers. This can result in data duplication or unexpected behavior, since VB expressions in pages are statically defined.

Recommendations:

* Create separate copies of the same page when it is necessary to display the page more than once.
* Avoid replicating more than one instance of a page simultaneously in Tab and Page Container controls.