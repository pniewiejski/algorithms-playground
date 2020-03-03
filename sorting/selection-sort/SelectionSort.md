# Selection sort algorithm

[See the Wikipedia page on selection sort.](https://en.wikipedia.org/wiki/Selection_sort)

[Simple implementation in python. 🐍](./selection_sort.py)

**Time complexity is O(n^2).** Because of that this algorithm is not very efficient on large arrays.

The main idea is that we divide the list (array) into two parts:

- sorted sublist which is built up from left ot right. Initially it's empty
- unsorted sublist

Algorithm works by finding the smallest element of the unsorted sublist and then appends it to the
sorted sublist.

### Complexity

We are scanning `n` elements and then taking `(n - 1)` comparisons, and then swapping their
position. The next step will require scanning of the remaining `(n - 1)` elements and so on. In other
words, the number of comparisons could be described as:

```
(n - 1) + (n - 2) + ... + 1 = \sum_{i=1}^{n-1} i = \frac{n^2 - n}{2}
```

This basically comes down to the complexity of **O(n^2)**.

a sorted sublist of items which is built up from left to right at the front (left) of the list and a
sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted
sublist is empty and the unsorted sublist is the entire input list.
