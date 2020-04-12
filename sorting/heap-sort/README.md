# Heapsort

Heapsort is a comparison based sorting algorithm. Like _selection sort_, **heapsort** will divide
the array into to parts: the already sorted sub-array and the unsorted sub-array. Whereas on every
iteration _selection sort_ preformed linear scan of the unsorted sub-array, the **heapsort** will
keep the unsorted part in a **heap data structure**. This ensures quick lookup time for the largest
element.

**Heapsort is not a stable sort algorithm**.

## How does it work?

1. Build a _max-heap_ from the data you want to sort. In other words, "heapify" the input array.
2. The max value should be at the root of the heap tree.

Let's say that we want to sort the following array:

```
array = [4, 20, 1, 15, 7, 5]
```

We create a _max-heap_. Right after turning the array into heap it would look like:

```
           4
          / \
        20   1
       / \   /
     15  7  5
```

Then we would have to transform it into a proper _max-heap_.

```
           20
          /  \
        15    5
       / \   /
      7  4  1
```

Now we can remove the max element and insert it into the "already sorted" sub-array.

This neat animation from _Wikipedia_ provides a good visualization:
![Heapsort GIF](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)

## Complexity

|                 |    Complexity     |
| :-------------: | :---------------: |
| Worst-case time |  `O(n * log n)`   |
| Best-case time  |  `O(n * log n)`   |
|      Space      | `O(1)` (in-place) |

On average _quicksort_ algorithm will perform better than heapsort. However, heapsort has much
better worst-case time complexity (For quicksort it's `O(n^2)`).

## Further reading 📚

- [Heapify all the things](https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82)
- [heapsort, Wikipedia](https://en.wikipedia.org/wiki/Heapsort)
