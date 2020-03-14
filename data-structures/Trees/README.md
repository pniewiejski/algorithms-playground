# Binary Search Trees 🌳

Trees allow us to represent hierarchical structures. A tree structure where each parent node has at
max two children is called **binary tree**.

## What are binary search trees?

Sometimes called _ordered binary trees_, binary search trees are a type of binary trees that satisfy
the following conditions:

🌴 Each node have two sub-trees which are usually called _left_ and _right_ sub-trees.

🌴 **Value of each node must be greater than the values in every node in the _left_ sub-tree and
less than all values in the _right_ sub-tree.**

## Complexity

|     Alg     |  Average   | Worst  |
| :---------: | :--------: | :----: |
|    Space    |   `O(n)`   | `O(n)` |
| Search time | `O(log n)` | `O(n)` |
| Insert time | `O(log n)` | `O(n)` |
| Delete time | `O(log n)` | `O(n)` |

## Searching

If you take a look at the rules that we use for creating a binary search tree, you can notice that
we are using here the idea of the **binary search**. Time complexity of searching of an element in a
binary search tree depends on the tree's height. Time complexity will also dement if a tree is
**balanced**. In case where a binary search tree is **unbalanced** it can look like more of a
_linked list_, instead of a tree. In such a case the time complexity can become `O(n)`.

```python
def search_bst(value, node):
    """
    Recursive implementation of BST search
    """
    if node is None or value = node.value:
        return node
    if value < node.value:
        search_bst(value, node.left)
    if value > node.value:
        search_bst(value, node.right)
```

```python
def search_bst(value, node):
    """
    Iterative implementation of BST search
    """
    current_node = node
    while node is not None:
        if value == current_node.value:
            return current_node
        if value < current_node.value:
            current_node = current_node.left
        if value > current_note:
            current_node = current_node.right
```

### Searching of the max and min element

You can easily implement searching of the max and min value. Notice that the minimal value should be
stored in the left-most leaf of the BST and the maximal value should be in the right-most leaf.

## Insertion

Insertion process looks similar to the search process. It is important to keep the order of
elements. In the simplest implementation, we want to find a node which will become the parent of the
node we want to insert. Then we will have to determine if it should be added to the left or right
sub-tree.

```python
def insert_bst(root, new_node):
    if root is None:
        root = new_node
    if root.value < new_node.value:
        if root.right is None:
            root.right = new_node
        else:
            insert_bst(root.right, new_node)
    if root.value > new_node.value:
        if root.left is None:
            root.left = new_node
        else:
            insert_bst(root.left, new_node)
```

## Deletion

There are a couple of cases to consider here:

1. Node we want to remove is a leaf. This is the easy case. We can just remove that node and set
   parent's pointer to `null`.
2. When we want to remove a parent with only one child. Then we remove the node and replace it with
   its child.
3. Deleting node with two children. This is the tricky case. In this case we will want to find a
   in-oder predecessor or successor and use it as a replacement. We copy the value of such node
   (let's call it node `B`) to the value slot of node we want to remove (node `A`). If `B` hasn't
   got any children we can simply remove `B`. If it has got children (eg. `C`), replace `B` with `C`
   at `B`'s parent (change pointer at `B`'s parent).

```python
def delete_node(root: Node, value) -> Node:
    def find_minimal(node):
        if node.left:
            return find_minimal(node.left)
        return node

    if root is None:
        return root

    if value < root.value:
        root.left = delete_node(root.left, value)

    elif value > root.value:
        root.right = delete_node(root.right, value)

    else: # root's value is the same as value to be removed

        # Cases for one or no children
        if root.left is None:
            tmp = root.right
            root = None
            return tmp
        elif root.right is None:
            tmp = root.left
            root = None
            return tmp
        # Case for two children
        tmp = find_minimal(root.right)
        root.value = tmp.value
        root.right = delete_node(root.right, tmp.value)
    return root
```

## Verification

You are given a binary tree. Determine if it is Binary Search Tree.

[This problem is described and solved here.](./validate_bst.py)

## [Self-balancing binary search tree](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)

This is a BST which automatically adjusts its structure to keep its height low. There are lots of
implementations of self-balancing BST. For instance [B-tree](https://en.wikipedia.org/wiki/B-tree).
