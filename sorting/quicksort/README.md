# Quick sort algorithm 🏃‍♂️ 💨

**Time complexity (average):** `O(n * log n)`

[Simple implementation in Python](./quicksort.py)

Quicksort is a [divide-and-conquer](../../DivideAndConquer) algorithm. The main idea is to select a
**pivot** and partition the other elements into two _sub-arrays_, which are dealt with as
_sub-problems_. These sub-arrays are sorted recursively.

It can be much faster than _merger sort_ or _heapsort_.

Quicksort is **comparison sort** - we can sort anything for which we can define a _less-than_
relation.

## How does it work?

### Base (simple) case

- Empty array
- Array with only one element

### Reducing the original problem

1. Select a _pivot_ element.
2. Partitioning - we want to find every element that is greater than _pivot_ and put it into one
   sub-array and we want to do the same with elements that are smaller than the _pivot_.

This way we have: _pivot_ element, sub-array with elements smaller than _pivot_ and sub-array of
elements grater than _pivot_.

Then next step is to recursively sort all sub-arrays.

Once the sub-arrays are sorted we can combine elements to obtain the final solution.

## Choice of pivot

Choosing a pivot is quite important with quicksort and can affect performance of your
implementation. It should not be just the leftmost element of the array. Try to pick the value under
the **middle index** or **median**.
