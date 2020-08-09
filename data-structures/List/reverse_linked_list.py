class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value} -> " + str(self.next)


def reverse(head):
    previous = None
    current = head

    while current is not None:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp

    return previous


if __name__ == "__main__":
    linked_list = Node(1, Node(2, Node(3, Node(4))))
    print(linked_list)

    print(reverse(linked_list))
