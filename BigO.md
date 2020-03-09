# Big O

We use the _"Big O"_ notation to represent a complexity of an algorithm, be it the time complexity
or the space complexity.

The _"Big O"_ should give us the idea how an algorithm will scale in relation to the size of input.

Not getting to far in to the underlying math, let's look at the following definition:

> `T(n)` is of `O(f(n))`, if for some `c > 0` and `n_0 > 0`:
>
> ![\forall n > n_0 \quad T(n) \leqslant c \cdot f(n)](<https://render.githubusercontent.com/render/math?math=%5Cforall%20n%20%3E%20n_0%20%5Cquad%20T(n)%20%5Cleqslant%20c%20%5Ccdot%20f(n)>)

- `n` is the size of input (some data set)
- `f(n)` is a function which performance we want to describe (our algorithm)
- `O(f(n))` will be the upper bound of resources required by `f(n)`

This means that if you were to graph `T(n)` and `f(n)`, curve described by `f(n)` be "under" the
curve described by `T(n)`.

---

We could name some typical classes of complexity:

- `O(n)` - Linear - A way to identify would be to check if you visit all nodes/items only once.

- `O(k)` - Constant - Algorithms which running time is independent form the input. Mathematical
  formulas are considered to have a constant time complexity.

- `O(log n)` - Logarithmic - eg. traversing a balanced binary tree.

- `O(n * log n)` - Superlinear - eg. quicksort, merge sort
- `O(n^2)` - Quadratic / Cubic / Polynomial - Easy way to detect is to check if you have a loop in a
  loop where in each of them you are iterating over the input data. Often brute force solutions have
  polynomial complexity. Let's say that you have two arrays of numbers and you want to find common
  elements and you do it be comparing each element from the first array with every element in the
  second array.

- `O(2^n)` - Exponential - eg. finding the number permutations of a given set; computing fibonacci
  sequence recursively, where when you try to find `fibonacci(n)` you will have to find solutions to
  two sub-problems `fibonacci(n-1)` and `fibonacci(n-2)`.

- `O(n!)` - Factorial - Think of the traveling salesman problem.

# What about Ω and Θ

Apart from the _"Big O"_ there is also a Ω and Θ.

Whereas the _"Big O"_ is used to represent the upper bound, the bin-Ω notation is used to represent
the lower bound. We can think of bin-Ω as of "the best case". We can think that a given algorithm
will take minimum the time described by the big-Ω.

The big-Θ notation is used to represent the _"tight bounds"_. You could think about big-Θ as a range
in which the true execution time is enclosed.

> For `n_0 > 0`, `c_1 > 0` and `c_2 > 0`:
>
> ![\forall n \geqslant n_0 \quad c_1 \cdot \ f(n) \leqslant T(n) \leqslant c_2 \cdot \ f(n)](<https://render.githubusercontent.com/render/math?math=%5Cforall%20n%20%5Cgeqslant%20n_0%20%5Cquad%20c_1%20%5Ccdot%20%5C%20f(n)%20%5Cleqslant%20T(n)%20%5Cleqslant%20c_2%20%5Ccdot%20%5C%20f(n)>)
