# Floyd's Tortoise and Hare algorithm 🐢 🐇

[Find Floyd's Tortoise and Hare algorithm on Wikipedia.](https://en.wikipedia.org/wiki/Cycle_detection)

Cycle detection algorithm. Originally designed by
[Robert W. Floyd](https://en.wikipedia.org/wiki/Robert_W._Floyd). This algorithm allows us to detect
cycles in sequences of values coming from an
[iterated function](https://en.wikipedia.org/wiki/Iterated_function), which is a function that maps
a set to itself, and is obtained by a composition of another function _f_ with itself a number of
times.

```
f: X -> X
```

**The idea is to move two pointers at different speeds through the sequence of values until both are
pointing to equal values.**

We have to pointers, one (tortoise) at `x_i` and the other (hare) at `x_{2i}`. At each step we are
increasing `i` by one, which effectively moves _tortoise_ one step forward and _hare_ two steps
forward. Then we compare values to which _tortoise_ and _hare_ are pointing.

There is a cycle if for any `i >= u` and `k >= 0`

```
x_i = x_{i + u*l}
```

where `l` is the length of the loop to be found and `u` is the index of the first element of the
cycle.

[See an example implementation in Python.](./tortoise-and-hare.py)

## Time and memory complexity

**TLDR:** The time complexity of this algorithm is linear: `O(n)`. The space complexity of this
algorithm is constant: `O(1)`.

> If we are accessing the sequence by storing and copying pointers, function evaluations, and
> equality tests, it qualifies as a pointer algorithm. The algorithm uses `O(l + u)` operations of
> these types, and `O(1)` storage space.

## Example problem

Given an array `nums` containing `n + 1` integers where these integers are between `1` and `n`
(inclusive), prove that at least one duplicate number must exist.

> Answer is related with the
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
