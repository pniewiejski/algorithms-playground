# Quick sort algorithm 🏃‍♂️ 💨

**Time complexity (average):** `O(n * log n)`

[Simple implementation in Python](./quicksort.py)

Quicksort is a [divide-and-conquer](../../DivideAndConquer.md) algorithm. The main idea is to select
a **pivot** and partition the other elements into two _sub-arrays_, which are dealt with as
_sub-problems_. These sub-arrays are sorted recursively.

It can be much faster than _merge sort_ or _heapsort_.

Quicksort is **comparison sort** - we can sort anything for which we can define a _less-than_
relation.

> There is one notable difference between quicksort and merge sort and it is the fact that quicksort
> is an **unstable** sorting algorithm. **It means that it does not guarantee that the order of
> elements that have the same value will be preserved.**

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

The complexity of quicksort in a pessimistic case is `O(n^2)`. It depends on the choice of pivot. In
general, we can worse performance if we choose pivot that is far from the median value.

Average time for a list that is sorted or almost-sorted is also going to be `O(n^2)`. **This is why
it is not advised to use quicksort on nearly-sorted arrays.**

## When to use quicksort? 🤔

- You don't care about stability (order of items with the same value is not significant)
- Data that you sort is not _"almost-sorted"_.
- You don't want to use external memory.

It is possible to run quicksort in a parallelised fashion (_parallel quicksort_). You can run each
partition as a separate parallel task.

## Further reading

- [Pivoting To Understand Quicksort [Part 1]](https://medium.com/basecs/pivoting-to-understand-quicksort-part-1-75178dfb9313)
- [Pivoting To Understand Quicksort [Part 2]](https://medium.com/basecs/pivoting-to-understand-quicksort-part-1-75178dfb9313)
- [Wikipedia](https://en.wikipedia.org/wiki/Quicksort)
