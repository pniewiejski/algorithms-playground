# Binary Search 🕵️‍♂️

Binary search algorithm allows us to find a searched value in a sorted array. It works by comparing
the searched value with the value in the middle of the array. If the compared values are not equal
we eliminate the part of array which cannot contain the searched value. The algorithm continues
until we find the searched value or the reduced array is empty which means that the searched value
is not in the array. The principle of reducing the searched parts of the array works thanks to the
fact that the array is sorted.

Let's look at an example. Assume that we are searching for a value `4` in an array
`[1, 2, 4, 5, 8, 9, 11]`.

1. The middle element is `5`. `5` is not equal to `4`. In fact, `5` is greater than `4`. So now, we
   will only look for this part of the array that is on the left side of `5` - `[1, 2, 4]`
2. The middle element is `2`. `2` is not equal to `4`. `2` is less than `4`. So now, we will only
   look for this part of the array that is on the right side of `2` in the reduced table. In other
   words, it will be `[4]`
3. The middle (and only element) of the reduced array is `4`. **We found the searched element!**
   🍾🎊

This graphic form _Wikipedia_ provides a nice visual illustration of how the algorithm works.

![Binary search visualization](https://upload.wikimedia.org/wikipedia/commons/8/83/Binary_Search_Depiction.svg)

It is easy to deduce that the **time complexity** of binary search is logarithmic - `O(log n)`,
where `n` is the number of elements in the array.

When it comes to the **space complexity**, we could say that it is constant - `O(n)`. We require
three pointers which all take up a constant space. In case of the recursive implementation we should
also consider the stack size taken up be the recursive function calls.

Check this simple implementation in Python. This is the iterative implementation. Note that it is
also possible to implement binary search recursively.

```python
def binary_search(array, searched_value):
    lower = 0
    upper = len(array) - 1

    while lower < upper:
        middle_index = lower + (upper - lower) // 2
        middle_value = array[middle_index]

        if middle_value == searched_value:
            return middle_index
        elif middle_value > searched_value:
            upper = middle_index - 1
        else:
            lower = middle_index + 1

    return None
```

## Implementations vulnerability

There's a famous vulnerability of the binary search implementations. You can read a thorough
explanation in this
[Google AI blog post](https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html).

Basically it all comes down to how the _middle_ index is computed. In many implementations before
this bug was discovered it was done as follows:

```java
int middle = (low + high) / 2;
```

This becomes problematic for high values of `high` and `low` where the sum of the two numbers may
overflow. A safe way to implement this would be for example:

```java
int middle = low + (low + high) / 2;
```

## Further reading

- [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)
