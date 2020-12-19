# Heaps

Heap is a tree-like data structure that satisfies a few properties:

- **Its shape must be complete.** This means that that, apart from the last one, it has to have all
  of the levels completely filled, and the last level has to have the left-most element filled.
- Heap's node must have all of its children either less than or equal to (_max-heap_) or greater
  than or equal to (_min-heap_).

Let's look at a few examples:

```
A)         a      B)         a
          / \               / \
        b     c            b   c
       / \                /
      d   e              d
     /
    f

C)         59     D)        2
          / \              / \
        41   52           3   14
       / \   /           / \
     30  2  20         33   9
```

A is not a valid heap. B is a valid heap. C is a so called **max-heap**, and D is a **min-heap**.

Notice in example D how the values are spread across the data structure. **See that it is possible
to have more than one element with the same value.** Heaps do not follow the rules of Binary Search
Trees.

⚠️ FYI: Here I'm focusing mainly on binary heaps.

## Operations on heaps

The main operations performed on heaps are:

- find-max (or find-min)
- insert
- remove-max (or remove-min)

Usually implementations of heaps will also have: methods responsible for creation of a heap (e.g.
_heapify_ an array), merging of heaps, heap's size calculation. Also _replace_, which pops an old
entry and pushed a new one. This is better than separate pop and push because

## Implementation

It is possible to implement a heap as a linked list. However, there is also an array based
implementation.

In the latter variant every element of a heap is an element of some array. We can determine the
index of any given element based on the parent node:

```
             (i)           : Parent Node
            /    \
           /      \
          /        \
    (2*i + 1)    (2*i + 2) : Children Node
```

The fact that we can represent a heap as a single array (or a single list) is guaranteed by the fact
that the underlying tree is **complete**.

Many languages have heaps implemented in their standard libraries. For instance Python has the
[`heapq`](https://docs.python.org/3/library/heapq.html) module which is a heap implementation of a
priority queue.

[Simple implementation in Python.](./simple_heap.py)

## Complexity

With the array based implementation we need an array or a list to hold all nodes and also some
constant space to hold information such as the heap's size. Thus, we could say that the space
complexity is `O(n)`.

The time complexity of _max-search_ (or _min-search_) is `O(1)`.

Operations _insert_ and _remove-max_ (or _remove-min_) have time complexity `O(log n)`.

|   a    |  Average   | Worst case |
| :----: | :--------: | :--------: |
| Space  |   `O(n)`   |   `O(n)`   |
| Search |   `O(n)`   |   `O(n)`   |
| Insert |   `O(1)`   | `O(log n)` |
| Remove | `O(log n)` | `O(log n)` |
|  Peek  |   `O(1)`   |   `O(1)`   |

### Building heap

Let's say that you have an _n_ element array and you want to create a heap out of it. Building a
heap by adding elements from such array, one element at a time would have a complexity of
`O(n * log n)`, as we would have to repeat the insertion `O(log n)` for _n_ elements.

There is however a faster method.
[Find it described here.](https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap)

## Applications

- Priority queues - Binary heaps are often used as implementations of priority queues. This is
  because it is very easy to retrieve the element with the _"highest priority"_.
- Heapsort
- Heaps allow us to quickly find the max an min elements of a collection.

You can find a real life application of a min-heap in the source code of `libuv`. It stores timers
in a heap data structure. See https://github.com/libuv/libuv/blob/v1.x/src/timer.c#L168 and
https://github.com/libuv/libuv/blob/v1.x/src/heap-inl.h#L67.

## Further reading 📚

- [Heap, Wikipedia](<https://en.wikipedia.org/wiki/Heap_(data_structure)>)
- [Binary Heap, Wikipedia](https://en.wikipedia.org/wiki/Binary_heap)
- [Learning to love heaps](https://medium.com/basecs/learning-to-love-heaps-cef2b273a238)
- [Binary Heap Implementation](https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html)
