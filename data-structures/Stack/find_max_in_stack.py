# Task:
#    Implement a stack which has a max() method, which finds the max value on stack.
#
#    This is a tricky task because stacks do not give us
#    this kind of operation straight out of the box.
#    We will have to somehow store the information about max value.
#    We will have to _cache_ the max value. Keep in mind, that this solution
#    will have to be push and pop save. This means that we want the max opperation 
#    to have O(1) time complexity regardless of the history of pushes and pops.
#    This is why simply adding additional field to Stack class (e.g. self.max_value) won't
#    work here. Because in some cases (when we pop the max value) then we'd have to perform
#    a search over the whole stack. 
#
#    One way to achieve it would be to annotate each element in the stack
#    with the max value. This way we are sure that we're getting O(1) time complexity
#    However this has a O(n) space complexity because we have to annotate every element on stack.
#    In case where we have a lot of repeated values this is unnecessary. We would waste lots of space.
#
#    What we can create an additional stack which purpose is only to hold the max values.
#    This way we get the O(1) time complexity but we also improve
#    the space complexity in the optimistic case.

# There is a very nice explanation of this problem on YouTube:
# https://www.youtube.com/watch?v=nGwn8_-6e7w

from collections import deque
from dataclasses import dataclass

class Stack:
    def __init__(self):
        self._stack = deque()

    def __str__(self):
        return f"{self._stack}"
    
    def push(self, value):
        self._stack.append(value)
    
    def pop(self):
        return self._stack.pop()

    def top(self):
        if self._stack:
            return self._stack[-1]
        return None

@dataclass 
class MaxCacheEntry:
    value: int
    count: int

    def increment_count(self):
        self.count += 1

    def decrement_count(self):
        self.count -= 1

class StackMax:

    def __init__(self):
        self._stack = Stack()
        self._max_cache = Stack()

    def __str__(self):
        return f"Stack: {self._stack}, max: {self._max_cache}"

    def pop(self):
        current_max = self._max_cache.top()
        if current_max:
            current_max.decrement_count()
            if current_max.count < 1:
                self._max_cache.pop()
        
        return self._stack.pop()

    def push(self, value):
        self._stack.push(value)
        current_max = self.max()
        if not current_max or current_max < value:
            self._max_cache.push(MaxCacheEntry(value=value, count=1))
        elif current_max == value:
            self._max_cache.top().increment_count()

    def max(self):
        cache_top = self._max_cache.top()
        if cache_top:
            return cache_top.value
        return None

if __name__ == "__main__":
    stack = StackMax()
    print("Pushing")
    stack.push(2)
    stack.push(2)
    stack.push(1)
    stack.push(4)
    stack.push(5)
    stack.push(5)
    stack.push(3)
    print("Current stack")
    print(stack)
    print(f"Stack's max: {stack.max()}")
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print("Current stack")
    print(stack)