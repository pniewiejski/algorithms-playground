# Insertion sort algorithm

[Wikipedia page](https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort)
[Checkout also Khan Academy article](https://en.wikipedia.org/wiki/Insertion_sort)

**Time complexity: O(n^2)**

[Example implementation in python](./insertion_sort.py)

Insertion sort builds the final array one element at the time. Thus it can work "online", meaning
that it can sort a list as it receives it.

Considerably less efficient than eg. _quicksort_, _heapsort_ or _merge sort_. (But in practice
better than other `O(n^2)` sorting algorithms like for instance _selection sort_.) Notice that this
algorithm will be more efficient if the input data was previously "pre-sorted".
