---
title: "Useful VB functions"
visible: true
slug: "useful-vb-functions"
---

This page contains VB expressions that you may find useful while building your app.

We grouped several of these functions in a [public app](https://alpha.uipath.com/appdevtest/apps_/default/run/production/2b514bff-2c40-4e9d-a87b-5fa64e21729a/d5edbd5b-1a41-4aca-8df3-652190d0d4ae/ID20cd26edc66248dabc82c528b541e38e/public?el=vb), so you can try out them out and see how they behave.

## VB function: Where

The `Where()` function returns a zero-based array containing a subset of a string array based on a specified filter criteria.

Assume you have a variable called `words` defined as `List(Of String) = {"apple", "banana", "cherry", "date"}`.

To get the list of words that contain the letter "a", apply the `Where()` function as follows:

```
words.Where(Function(w) w.Contains("a")).ToList()
```

The output is `{"apple", "banana", "date"}`.

## VB function: Select

The `Select()` function creates a new array that contains the results of applying a lambda expression to each element in the source array.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To get the list of numbers multiplied by themselves, apply the `Select()` function as follows:

```
numbers.Select(Function(n) n * n).ToArray()
```

The output is `{1, 4, 9, 16, 25}`.

## VB function: Aggregate

The `Aggregate()` function performs calculations over all the elements in an array and returns a single value. This function can be useful in aggregating multiple values inside a column.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To get the sum of all the numbers in the array, apply the Aggregate() function as follows:

```
Dim sum = numbers.Aggregate(Function(acc, n) acc + n)
```

The output is `15`.

## VB function: Group By

The `GroupBy()` function groups elements in a sequence by a key selector function.

Assume you have a variable called `words` defined as `String() = {"apple", "banana", "cherry", "date"}`.

To group the words by the first letter, which is the key selector function, apply the `GroupBy()` function as follows:

```
words.GroupBy(Function(w) w(0))
```

The output is `{ {"a", "apple", "date"}, {"b", "banana"}, {"c", "cherry"} }`.

## VB function: Order By

The `OrderBy()` and `OrderByDescending()` functions sort elements in a sequence based on a key selector function.

Assume you have a variable called `words` defined as `String() = {"apple", "banana", "cherry", "date"}`.

To order the words by their length, which is the key selector function, apply the `OrderBy()` function as follows:

```
words.OrderBy(Function(w) w.Length).ToArray()
```

The output is `{"date", "apple", "cherry", "banana"}`.

## VB function: Join

The `Join()` function combines elements in two sequences based on a key selector function.

Assume you have two variables:

* `names` defined as `String() = {"John", "Jane", "Joe"}`
* `ages` defined as `Integer() = {25, 30, 35}`

To combine the elements in the first sequence with the elements in the second sequence, apply the `Join()` function as follows:

```
names.Join(ages, Function(name) name(0), Function(age) age Mod 10, Function(name, age) $"{name}: {age}")
```

The output is `{"John: 25", "Jane: 30", "Joe: 35"}`.

## VB function: First

The `First()` function returns the first element in a sequence that satisfies a specified condition.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To get the first even number in the sequence, apply the `First()` function as follows:

```
numbers.First(Function(n) n Mod 2 = 0)
```

The output is `2`.

## VB function: First Or Default

The `FirstOrDefault()` function returns the first element, or a default value if no element satisfies the condition.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To get the first odd number in the sequence, apply the `FirstOrDefault()` function as follows:

```
numbers.FirstOrDefault(Function(n) n Mod 2 = 1)
```

The output is `1`.

## VB function: Last

The `Last()` function returns the last element in a sequence that satisfies a specified condition.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To get the first even number in the sequence, apply the `last()` function as follows:

```
numbers.Last(Function(n) n Mod 2 = 0)
```

The output is `4`.

## VB function: Last Or Default

The `LastOrDefault()` function returns the last element, or a default value if no element satisfies the condition.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To get the first odd number in the sequence, apply the `FirstOrDefault()` function as follows:

```
numbers.LastOrDefault(Function(n) n Mod 2 = 1)
```

The output is `5`.

## VB function: Skip

The `Skip()` function skips a specified number of elements in a sequence.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To skip the first two elements in the sequence, apply the `Skip()` function as follows:

```
numbers.Skip(2).ToArray()
```

The output is `{3, 4, 5}`.

## VB function: Skip While

The `SkipWhile()` function skips elements until a condition is no longer satisfied.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To skip the numbers which are lower than 3, apply the `SkipWhile()` function as follows:

```
numbers.SkipWhile(Function(n) n < 3).ToArray()
```

The output is `{3, 4, 5}`.

## VB function: Take

The `Take()` function returns a specified number of elements from the start of a sequence.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To get the first three elements in the sequence, apply the `Take()` function as follows:

```
numbers.Take(3).ToArray()
```

The output is `{1, 2, 3}`.

## VB function: Take While

The `TakeWhile()` returns elements until a condition is no longer satisfied.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To get the numbers which are lower than 4, apply the `TakeWhile()` function as follows:

```
numbers.TakeWhile(Function(n) n < 4).ToArray()
```

The output is `{1, 2, 3}`.

## VB function: Any

The `Any()` function returns `true` if any element in a sequence satisfies a specified condition.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To find out if at least one number in the sequence is even, apply the `Any()` function as follows:

```
numbers.Any(Function(n) n Mod 2 = 0)
```

The output is `true`.

## VB function: All

The `All()` returns `true` if all elements in a sequence satisfy a specified condition.

Assume you have a variable called `numbers` defined as `Integer() = {1, 2, 3, 4, 5}`.

To find out if all the numbers in the sequence are positive, apply the `All()` function as follows:

```
numbers.All(Function(n) n > 0)
```

The output is `true`.

## VB function: Add item to list

The list function `AddItemToList()` adds a new item to an existing list.

Assume you want to manipulate the records in an **Edit Grid** control with data from a process integration, using the **Set Value** rule. The item to set is `Processes.ALLDATATYPES.out_genericList`.

To add an item to the generic list, assign it the following value:

```
AddItemToList(Processes.ALLDATATYPES.out_genericList, MainPage.EditGrid.NewItem)
```

## VB function: Delete item from list

The list function `DeleteItemFromList()` deletes items from an existing list.

Assume you want to manipulate the records in an **Edit Grid** control with data from a process integration, using the **Set Value** rule. The item to set is `Processes.ALLDATATYPES.out_genericList`.

To delete an item from the generic list, assign it the following value:

```
DeleteItemFromList(Processes.ALLDATATYPES.out_genericList, MainPage.EditGrid.RowIndex)
```

## VB function: Update list item at index

The list function `UpdateListItemAtIndex()` updates items in an existing list.

Assume you want to manipulate the records in an **Edit Grid** control with data from a process integration, using the **Set Value** rule. The item to set is `Processes.ALLDATATYPES.out_genericList`.

To update an item in the generic list, assign it the following value:

```
UpdateListItemAtIndex(Processes.ALLDATATYPES.out_genericList, MainPage.EditGrid.RowIndex, MainPage.EditGrid.SelectedItem)
```