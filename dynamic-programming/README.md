# Dynamic programming

Dynamic programming is a method of solving problems by breaking them down into sub-problems in a
recursive manner.

In order to use dynamic programming a problem has to have the following qualities:

- [Optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure) - _"a problem is said
  to have optimal substructure if an optimal solution can be constructed from optimal solutions of
  its sub-problems._"
- [Overlapping sub-problems](https://en.wikipedia.org/wiki/Overlapping_subproblems) - \_" is said to
  have overlapping sub-problems if the problem can be broken down into sub-problems which are reused
  several times or a recursive algorithm for the problem solves the same subproblem over and over
  rather than always generating new sub-problems."

See
[further explanation on Wikipedia. 📚](https://en.wikipedia.org/wiki/Dynamic_programming#Computer_programming)

If we're dealing with a problem that has optimal substructure but non-overlapping sub-problems then
we're dealing with the _divide and conquer_ method.

## Algorithms that use dynamic programming:

- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm),
  [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm),
  [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm)
- Dynamic programming can be used to improve performance of solutions that use recursion by
  memoizing solutions of sub-problems. For instance we could improve the performance of recursive
  calculation of Fibonacci sequence by storing partial solutions. **This reduces the time complexity
  by increasing the space complexity.**
- Solving the problem of longest common subsequence
- Solving the (discrete) Knapsack problem (dyskretny problem plecakowy)
- It's often used in place of greedy algorithms (algorytmy zachłanne)

## Knapsack problem

Imagine that you are a thief trying to rob a store. You have a backpack that can hold a maximum of 4
kilograms of stolen goods. Your goal is to maximize to value of stolen goods.

You walki into a store where on a shelf there are:

- A stereo set that costs 3000$ and weighs 4g
- A computer for 2000$, 3kg
- A tablet for 1500$, 1kg

What's the best combination to steal?

### Simple solution

The simples solution would be to try every possible combination. This is however very ineffective.
Time complexity is `O(2^n)` where n is a number of items. In our case we'd have to go only through 8
options but it's clear to see that this number would grow very quickly if the shore had more items
to sell.

### Using dynamic programming

Following a simple implementation in [knapsack.py](./knapsack.py) we can see how the solution grid
evolves:

```
1: Result after checking tablet
[[0, 0, 0, 0, 0], [0, 1500, 1500, 1500, 1500], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
2: Result after checking stereo
[[0, 0, 0, 0, 0],
 [0, 1500, 1500, 1500, 1500],
 [0, 1500, 1500, 1500, 3000],
 [0, 0, 0, 0, 0]]
3: Result after checking computer
[[0, 0, 0, 0, 0],
 [0, 1500, 1500, 1500, 1500],
 [0, 1500, 1500, 1500, 3000],
 [0, 1500, 1500, 2000, 3500]]
-------------------
Final solution grid
[[0, 0, 0, 0, 0],
 [0, 1500, 1500, 1500, 1500],
 [0, 1500, 1500, 1500, 3000],
 [0, 1500, 1500, 2000, 3500]]
```

## Solving the problem of longest common subsequence

TODO
