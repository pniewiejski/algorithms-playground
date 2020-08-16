# Problem:
#     You are given a list of **sorted** singly linked lists.
#     The task is to merge this list into one singly linked list where items are sorted.
#

from typing import List

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value} -> " + str(self.next)

def merge(lists: List[Node]) -> Node:
    """Brute force solution. Time: O(n * log n)"""
    elements = []
    for node in lists: # append all elements from all lists to an array
        while node:
            elements.append(node.value)
            node = node.next

    merged = None
    merged_tail = None
    for element in sorted(elements):
        if not merged:
            merged = merged_tail = Node(element, None)
        else:
            merged_tail.next = Node(element, None)
            merged_tail = merged_tail.next

    return merged


def merge_k_linked_lists(lists: List[Node]) -> Node:
    """This is a better solution with time O(n)"""
    head = cursor = Node(None, None) # A dummy root

    while any(node is not None for node in lists):
        min_val, min_val_idx = min((head.value, idx) for idx, head in enumerate(lists) if head is not None)
        lists[min_val_idx] = lists[min_val_idx].next
        cursor.next = Node(min_val, None)
        cursor = cursor.next

    head = head.next # drop the dummy head
    return head

if __name__ == "__main__":
    lists = [
        Node(0, Node(1, Node(3, None))),
        Node(1, Node(4, Node(5, None))),
        Node(1, Node(2, Node(7, None)))
    ]

    print(merge(lists))
    print(merge_k_linked_lists(lists))

# A small performance test. We want to merge two large linked lists.
    import time
    h_a = c_a = Node(1)
    h_b = c_b = Node(1)
    for a in range(10000):
        c_a.next = Node(a)
        c_a = c_a.next
    for b in range(-100, 10000):
        c_b.next = Node(b)
        c_b = c_b.next
    lists = [
        h_a, h_b
    ]
    brute_force_start = time.time()
    for i in range(1000): merge(lists)
    brute_force_end = time.time()
    start = time.time()
    for i in range(1000): merge_k_linked_lists(lists)
    end = time.time()
    print(f"Brute force: {brute_force_end - brute_force_start}; Solution no. 2: {end - start}")
