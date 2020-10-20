# Exercicse:
#    Given a binary tree, perform an in-order traversal both recursively and iteratively.
# Example:
#                                   0
#                                  /  \
#                                -5    8
#                               /  \  /  \
#                            -10  -3 5    9
# Solution:
#   -10, -5, -3, 0, 5, 8, 9


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return f"{{ {self.value}:  {{ left: {self.left}, right: {self.right}  }} }}"


def in_order_traversal_recursive(node):
    if node is None:
        return

    in_order_traversal_recursive(node.left)
    print(node.value)
    in_order_traversal_recursive(node.right)


def in_order_traversal_iterative(node):
    stack = []
    while node is not None or len(stack) > 0:
        if node is not None:
            stack.append(node)
            node = node.left

        else:
            node = stack.pop()
            print(node.value)
            node = node.right


if __name__ == "__main__":
    tree = Node(0, Node(-5, Node(-10), Node(-3)), Node(8, Node(5), Node(9)))
    print(tree)
    print("# recursive")
    in_order_traversal_recursive(tree)
    print("# iterative")
    in_order_traversal_iterative(tree)
