# Divide and Conquer ⚔️

The **divide-and-conquer** paradigm breaks the original problem into sub-problems, which can be
solved on their own, and then combines solutions for these sub-problems to find a solution of the
original problem.

Divide-and-conquer is usually implemented using recursion.

When looking for a solution we want to:

1. Define the base problem. This should be the simplest case.
2. Divide and reduce the problem until the base problem is reached.

Examples of algorithms that use divide-and-conquer approach:

- FFT (Fast Fourier Transform)
- [Quicksort](./sorting/quicksort/README.md)
- [Merge sort](./sorting/merge-sort/README.md)
- The Euclidean algorithm

## Advantages

- It allows us to solve difficult problems by breaking them down into simple sub-problems.
- **Parallelism** - these algorithms can be executed on a multi-processor machine.

## Potential issues

- Stack size - you have to mind the stack size when implementing solutions based on recursion.
  Alternatively you can think about using some explicit data structure (eg. stack, queue) to
  implement divide-and-conquer in a non-recursive way. This approach is also the standard solution
  in programming languages that do not provide support for recursive procedures.
- **Sharing repeated sub-problems** - In some cases you may end up with the recursive process doing
  the same sub-problem many times over. In such cases it might be beneficial to identify and store
  solutions to these sub-problems. This is known as **memorization**. You can look up **dynamic
  programming** for more information.

## Example

For example, let's look at **the Euclidean algorithm**. This algorithm will allow us to find _the
greatest common divisor_ of two numbers. Read more
[here](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm).

The idea here is that, if we have two integers `a` and `b`, we know that:

- `GCD(a, 0) = a`
- `GCD(b, 0) = b` This is because the greatest common divisor of some integer and zero is that
  integer. So this is our simple case.

If we can present `a` in a form of

```
a = b * r + c
```

where `r` and `c` are some integers, and `b != 0`, then

```
GCD(a,b) = GCD(b, r)
```

This is our second step - we have defined our _sub-problem_.

```python
def euclidean_algorithm(a, b):
    # We are looking for the greatest common divisor
    # What will be our simple case?
    # When we have two numbers - a & b, if one of them is 0,
    # then the second is their greatest common divisor!
    if b == 0:
        return a
    else:
        return euclidean_algorithm(b, a % b)
```

---

The thing about divide-and-conquer is that we can apply it to problems that we would normally solve
iteratively with a loop. If I gave a list of integers

```python
nums = [4, 8, 1]
```

and asked you to add all elements you could do it with a simple loop. However, you can also approach
this by dividing the original problem to sub-problems:

```python
sum_nums([4, 8, 1])
# original problem comes down to:
4 + sum_nums([8, 1])
```
