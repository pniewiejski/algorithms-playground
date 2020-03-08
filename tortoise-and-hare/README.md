# Floyd's Tortoise and Hare algorithm 🐢 🐇

[Find Floyd's Tortoise and Hare algorithm on Wikipedia.](https://en.wikipedia.org/wiki/Cycle_detection)

Cycle detection algorithm. Originally designed by
[Robert W. Floyd](https://en.wikipedia.org/wiki/Robert_W._Floyd). This algorithm allows us to detect
cycles in sequences of values coming from a **iterated function**, which is a function that maps
some set to itself.

```
f: X -> X
```

The idea is to move two pointers at different speeds through the sequence of values until both are
pointing to equal values.

We have to pointers, one (tortoise) at `x_i` and the other (hare) at `x_{2i}`. At each step we are
increasing `i` by one, which effectively moves tortoise one step forward and hare two steps forward.
Then we compare values to which tortoise and hare are pointing.

There is a cycle if for any `i >= u` and `k >= 0`

```
x_i = x_{i + u*l}
```

where `l` is the length of the loop to be found and `u` is the index of the first element of the
cycle.

[See an example implementation in Python.](./tortoise-and-hare.py)

## Time and memory complexity

**TLDR:** The time complexity of this algorithm is linear: O(n). The space complexity of this
algorithm is constant: O(1).

> If we are accessing the sequence by storing and copying pointers, function evaluations, and
> equality tests, it qualifies as a pointer algorithm. The algorithm uses O(l + u) operations of
> these types, and O(1) storage space.

## Example problem

Given an array `nums` containing `n + 1` integers where these integers are between `1` and `n`
(inclusive), prove that at least one duplicate number must exist.

> Answer seems obvious and is related with the
> [pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle).

```python
nums = [1, 4, 6, 2, 6, 3, 5]
# therefore allowed integers are a set of
# {1, 2, 3, 4, 5, 6}
def find_duplicates(nums):
    tortoise = nums[0]
    hare = nums[nums[0]]

    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]

    tortoise = 0
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return tortoise

```
