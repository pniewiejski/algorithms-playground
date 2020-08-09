class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value} -> " + str(self.next)


def remove_kth_entry(root: Node, k: int) -> Node:
    prev = None
    head = root
    if not root:
        print("Error: root cannot be None")

    if k == 0:
        print("Popping the first element. New root pointer will be returned")
        return head.next

    for i in range(k):
        prev = head
        head = head.next
        if not head:
            print(f"Error: Cannot remove the element with index {k} because it is out of range")
            return

    prev.next = head.next
    # free memory allocated for head
    return root


if __name__ == "__main__":
    linked_list = Node(1, Node(2, Node(3, Node(4))))
    print(linked_list)

    linked_list = remove_kth_entry(linked_list, 0)
    print(linked_list)
