# Merge sort algorithm

This is another algorithm based on the idea of [divide-and-conquer](../../DivideAndConquer.md).

**Time complexity (average)** - `O(n * log n)`

[Example implementation in python](./merge_sort.py)

The basic steps are:

1. **Divide** the unordered array into two two sub-arrays. This is done by finding the middle index.
   **The basic case** here, will be a array of one element (which is always sorted 😉).
2. **Conquer** - Recursively sort sub-arrays.
3. **Combine** - Merge two sorted sub-arrays into one ordered array which is the result.

![Merge sort visualization, source Wikipedia](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

The problem that is to be understood here is **merging**. Provided that we have two sorted arrays,
how do we merge them together to create one ordered array.

## Merging

Merging of two sorted lists can be achieved in a linear time and linear space.

Also check out:

- [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
- [Khan academy](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort_)
