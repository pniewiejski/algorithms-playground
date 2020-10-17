# Exercise:
#   Given a sorted array, convert it into a binary search tree.
#
#   For example, consider an array: [-10, -5, -3, 0, 5, 8, 9]
#   When transformed into a BST:
#                                   0
#                                  /  \
#                                -5    8
#                               /  \  /  \
#                            -10  -3 5    9


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f"{{ {self.value}:  {{ left: {self.left}, right: {{ {self.right} }} }}"


def array_2_bst(array):
    def find_middle_idx(start_idx, end_idx):
        return start_idx + (end_idx - start_idx) // 2

    def _array_2_bst(start_idx, end_idx):
        # Base case
        if start_idx == end_idx:
            return array[start_idx]
        if start_idx > end_idx:
            return None

        middle_idx = find_middle_idx(start_idx, end_idx)
        node = Node(array[middle_idx])
        node.left = _array_2_bst(start_idx, middle_idx - 1)
        node.right = _array_2_bst(middle_idx + 1, end_idx)

        return node

    return _array_2_bst(0, len(array) - 1)


if __name__ == "__main__":
    sorted_array = [-10, -3, 0, 5, 9]
    bst = array_2_bst(sorted_array)
    print(sorted_array)
    print(bst)
