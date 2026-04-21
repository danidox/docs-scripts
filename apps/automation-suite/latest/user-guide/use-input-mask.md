---
title: "Use Input Mask"
visible: true
slug: "use-input-mask"
---

## Overview

You can guide your users enter data correctly into a **Textbox** control by using the **Input Mask** property.

![docs image](/images/apps/apps-docs-image-321150-9bb7dd80.webp)

To learn more on how to use this property, check the examples below.

To learn more about **Textbox** control properties, check the [Textbox](https://docs.uipath.com/apps/automation-suite/latest/user-guide/textbox#textbox) page.

:::note
* When the **Accept** property is not configured in the example, the default vale is `\d` (digits).
* If you restrict characters using `[\A-H]`, these will be enforced as capital letters. If you want to use lower case letters, you need to configure them as `[\A-Ha-h]`.
:::

## Date and time form

To configure an input mask for a date-time field, use the example below. This example only changes the values for the `d`, `m`, `y`, and `h` characters, and keep the `/`, `space`, and `:` in place.

1. Add `dd/mm/yyyy hh:mm` in the **Input mask** property.
2. Add `dmyh` in the **Mask char.** property.

   ![docs image](/images/apps/apps-docs-image-128975-91954c03.webp)

## Telephone number

To configure an input mask for a telephone number field, use the example below. This example only changes the values for the `_` character and keeps the `+1`, `(`, `)`, `-`, and `space` in place.

1. Add `+1 (___) ___-____` in the **Input mask** property.
2. Add `_` in the **Mask char.** property.
   :::tip
   You can also use REGEX validation in addition to **Input Mask** to allow phone numbers with optional country code, optional special characters and whitespace.
   :::

   ![docs image](/images/apps/apps-docs-image-128979-9b4fd4d4.webp)

## Invoice

To configure an input mask for an invoice field with a post-pended `-INV`, use the example below. This example only changes the values for the `*` character and keeps the post-pended `-INV` in place.

1. Add `***-INV** in the **Input Mask** property.
2. Add `*` in the **Mask char.** property.

   ![docs image](/images/apps/apps-docs-image-128985-e4c11e3d.webp)

## MAC Address

To configure an input mask for a MAC address field, use the example below. This example only changes the values for the `X` character and keeps the `:` character in place. This will also accept only digits and characters between `A` and `H`.

1. Add `XX:XX:XX:XX:XX:XX` in the **Input Mask** property.
2. Add `-` in the **Mask char.** property.
3. Add `[\dA-H]` in the **Accept** property.

   ![docs image](/images/apps/apps-docs-image-128989-cd1cfeda.webp)

## Alphanumeric

To configure an input mask for an alphanumeric field that only accepts characters from `A` to `Z` and digits, use the example below. This example only changes the values for the `_` character and keeps the `-` character in place. This will also accept only digits and characters between `A` and `Z`.

1. Add `__-__-__-____` in the **Input Mask** property.
2. Add `_` in the **Mask char.** property.
3. Add `[\dA-Z]` in the **Accept** property.

   ![docs image](/images/apps/apps-docs-image-128993-bb862191.webp)

## Credit card

To configure an input mask for a credit card field, use the example below. This example only changes the values for the `?` character and keeps the `space` character in place. This will also accept only digits.

1. Add `???? ???? ???? ????` in the **Input Mask** property.
2. Add `?` in the **Mask char.** property.
3. Add `[\d]` in the **Accept** property.
   :::tip
   You can also use REGEX validation in addition to **Input Mask** for specific cards (for example, MasterCard or Visa).
   :::

   ![docs image](/images/apps/apps-docs-image-128997-025e70c9.webp)

## Currency

To configure an input mask for a currency field, use the example below. This example only changes the values for the `_` character and keeps the `&` and `.` characters in place. This will also accept only values between `0000.01` and `9999.99`.

1. Add `$____.__` in the **Input Mask** property.
2. Add `_` in the **Mask char.** property.

   ![docs image](/images/apps/apps-docs-image-129001-fe5fc5e1.webp)