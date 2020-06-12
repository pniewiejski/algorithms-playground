# Task:
#     You are given a string containing '(', ')', '{', '}', '[' and ']',
#     check if the input string is valid. 

#     An input string is valid if:
#     * Open brackets are closed by the same type of brackets.
#     * Open brackets are closed in the correct order.

from collections import deque

OPENING_BRACKETS = ['(', '[', '{']
ALLOWED_CLOSING = {
    ')': ['(', '}', ']'],
    ']': ['[', '}', ')'],
    '}': ['{', ']', ')']
}


def validate_brackets(string):
    stack = deque()
    for symbol in string:
        if symbol in OPENING_BRACKETS:
            stack.append(symbol)
        else:
            bracket = stack.pop()
            if bracket == ALLOWED_CLOSING[symbol]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(validate_brackets("[()({})]"))  # Expect True
    print(validate_brackets("[(())({})]{"))  # Expect False
    print(validate_brackets("[(()({})]{}"))  # Expect False
