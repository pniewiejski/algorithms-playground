# Stacks

Stack is an _abstract data structure_ that is a collection of elements on which we can perform two
operations.

- `push`, which adds element to the collection
- `pop`, which removes element form the collection

Data on stack is stored in a **LIFO** (last in, first out) structure.

## Use cases

- Backtracking
- Syntax parsing - Some compilers use stacks to parse expressions.
- Managing memory - In some programming languages (like C) stacks are used to hold data that is
  local to a procedure. This can result in vulnerabilities and make space for exploits like _buffer
  overflow_. Java VM is also stack oriented.
- A very simple application for reversing a word 🤷‍♂️

Simple application of stack in a [bracket matching problem](./bracket_validation.py).

## Other sources 🔎

- [Stacks and overflows](https://medium.com/basecs/stacks-and-overflows-dbcf7854dc67)
