class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value} -> " + str(self.next)

def reverse(head):
    previous = None
    current = head

    while current != None:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp

    return previous


if __name__ == "__main__":
    linked_list = Node(1)
    linked_list.next = Node(2)
    linked_list.next.next = Node(3)
    print(linked_list)

    print(reverse(linked_list))