# Exercise:
#     Given a binary tree, determine whether it is a valid
#     Binary Search Tree.

#     Let's recall what are the conditions that a BST has to fulfill.

#     Value of each node must be greater than the values in every node
#     in the left sub-tree and less than all values in the right sub-tree.

#     Think of an example:
#     A) This is NOT a valid BST as 4 is smaller than 6
#             6
#            / \
#           1   4
#              / \
#             2   7
#     B) This is NOT a valid BST as 4 is smaller than 5
#             5
#            / \
#           1   6
#              / \
#             4   7
#     C) This is NOT a valid BST as 7 is greater than 6
#             5
#            / \
#           2   6
#              / \
#             7   9
#     D) This is a VALID BST
#             4
#            / \
#           2   7
#              / \
#             5   9
#
# As you might have noticed the decision if the tree is valid or not
# cannot be based only by comparing the value of each node with
# the values of its children.
# We also need information the is coming from the parent.

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def is_valid_bst(node: Node) -> bool:
    # In this implementation we will need to visit every node twice.
    # Thus, the time complexity of this implementation is O(n)

    # The space complexity here will be related with the size of the callstack.
    # This is because we are using recursive calls.
    # In this implementation we're making a call of is_valid_util for every sub-tree.
    # So in case of a balanced tree the space complexity will be O(log n),
    # however in the worst case it will be O(n)
    def is_valid_util(node, lower, upper):
        if node is  None: # base case
            return True

        if node.value <= lower or node.value >= upper:
            return False

        if not is_valid_util(node.right, node.value, upper):
            return False

        if not is_valid_util(node.left, lower, node.value):
            return False
        
        return True
    
    return is_valid_util(node, float('-inf'), float('inf'))

if __name__ == "__main__":

    # Example B
    root = Node(5)
    root.right = Node(6)
    root.left = Node(1)
    root.right.right = Node(7)
    root.right.left = Node(4)

    print("Is B a valid BST? - {}".format(is_valid_bst(root)))

    # Example C
    root = Node(5)
    root.right = Node(6)
    root.left = Node(2)
    root.right.right = Node(9)
    root.right.left = Node(7)

    print("Is C a valid BST? - {}".format(is_valid_bst(root)))

    # Example D
    root = Node(4)
    root.right = Node(7)
    root.left = Node(2)
    root.right.right = Node(9)
    root.right.left = Node(6)

    print("Is D a valid BST? - {}".format(is_valid_bst(root)))

