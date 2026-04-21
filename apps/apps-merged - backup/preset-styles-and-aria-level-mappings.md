---
title: "Preset styles and aria-level mappings for the Header control"
visible: true
slug: "preset-styles-and-aria-level-mappings"
---

Aria-level roles allow screen readers to reliably interpret the structure of text in your app.

* Level 1 represents a top-level heading, typically the main title in a page.
* Level 2 represents a second-level heading, typically a sub-heading in a page.
* Level 3 represents a third-level heading.
* Level 4 represents large text.
* Level 5 represents normal-size text.
* Level 6 represents small text.

The following are the default preset styles and aria-levels for the **Header** controls:

```
headline1  : Level 1 
headline2  : Level 2 
headline3  : Level 3 
LargeText  : Level 4 
NormalText : Level 5 
SmallText  : Level 6
```

If you manually customize styling using the **Style** area in the **Properties** panel, the aria-level is set based on the font size:

```
>= 32px = Level 1 
>= 24px = Level 2 
>= 18px = Level 3 
>= 16px = Level 4 
>= 14px = Level 5 
<  14px = Level 6
```