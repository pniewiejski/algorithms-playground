# Backtracking

Backtracking is an approach (algorithm) for finding all or some solutions to a computational problem
(usually a
[constraint satisfaction problems](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem),
e.g. Sudoku). Such algorithm will incrementally build _"potential solutions" (candidates)_ and when
it decides that a _candidate_ is not valid (meaning that a _candidate_ cannot be completed to a
valid solution), it _backtracks_, meaning that it effectively drops such _candidate_.

> Backtracking can be applied only for problems which admit the concept of a "partial candidate
> solution" and a relatively quick test of whether it can possibly be completed to a valid solution.
> It is useless, for example, for locating a given value in an unordered table.
>
> _source: Wikipedia_

To paraphrase, the idea behind backtracking, is that a backtracking algorithm generates _"potential
solutions" (candidates)_, but whenever it checks that a certain _"candidate"_ is not a valid
solution, it _backtracks_, meaning it goes back to the point where it can make another decision.

What's important to understand is that we can use backtracking in problems where a solution can be
built i a _"step by step"_ approach.

When solving a problem using backtracking you have to figure out three elements:

🗺 **Choice** - Define a _decision space_ from which you can choose _"solution candidates"_. What is
going to be the choice that you are going to make at each step of the algorithm.

👮‍♂️ **Constraints** - Define which elements of the _decision space_ are "valid".

🥇 **Goal** - Define the end result. What are you trying to accomplish. You can think of it as a
base case in a recursion problem.

## Example problems

### Sudoku

We can use backtracking to solve [sudoku](https://en.wikipedia.org/wiki/Sudoku).

In a brute force solution we would have to generate every possible "solution candidate" and then
validate it. In this case we would generate a great number of such "potential solutions" which do
not even make sense.

Using backtracking we can limit the number of operations that we'd need to perform. In other words
we'd like to direct the recursion so that when we know that there is no chance that a certain
partial "potential solution" is valid, we do not want to follow that decision path and spend more
time on that particular "potential solution". **We want to backtrack** 😉.

[Example implementation in Python 🐍](./sudoku_solver.py)

### Eight queens puzzle 👸

The [eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) tries to find a placing
of eight queens (chess piece) on a eight by eight chess board, such that no two queens threated each
other (No two queens share a row, a column or a diagonal).

Problem can be generalizes to _n_ queens on a _n_ by _n_ chess board.

[Example implementation in Python 🐍](./n_queens_problem.py)

### Find all...

- [Find all permutations of a collection of integers](./permutations.py)

## Further reading 📚

- [Backtracking, Wikipedia](https://en.wikipedia.org/wiki/Backtracking)
- [The Backtracking Blueprint](https://www.youtube.com/watch?v=Zq4upTEaQyM)
- [Backtracking explained](https://medium.com/@andreaiacono/backtracking-explained-7450d6ef9e1a)
