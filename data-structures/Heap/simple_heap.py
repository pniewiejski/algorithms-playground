# Simple implementation of binary heap
 
class BinaryMinHeap:
    def __init__(self):
        # In this implementation heap is represented as a list
        #         2
        #        / \      index: 0, 1, 2,   3, 4
        #       3   14   ===>   [2, 3, 14, 33, 9]
        #      / \
        #    33   9
        self._heap_list = []
        self._size = 0

    def __str__(self):
        return str(self._heap_list)

    def insert(self, value):
        # If the heap is represented by a list the simples way to
        # insert a new element is to simply append it.
        # Notice that it will guarantee that the underlying tree is complete!
        #
        # However, we will have to add some logic that will reorder the list, so that
        # structure of the heap satisfies all requirements.
        self._heap_list.append(value)
        self._size += 1
        self._percolate_up(self._size - 1)

    def _percolate_up(self, index):
        while index // 2:
            if self._heap_list[index] < self._heap_list[index // 2]:
                # Swap values
                # This is the "bubbling up" described in https://youtu.be/t0Cq6tVNRBA?t=50
                parent_index = index // 2
                parent_value = self._heap_list[parent_index]
                self._heap_list[parent_index] = self._heap_list[index]
                self._heap_list[index] = parent_value
            index = index // 2

    def _percolate_down(self, index):
        while (index * 2 + 1) < self._size:
            min_child_index = self._find_min_child(index)
            if self._heap_list[index] > self._heap_list[min_child_index]:
                # Swap values - "bubbling down"
                tmp = self._heap_list[index]
                self._heap_list[index] = self._heap_list[min_child_index]
                self._heap_list[min_child_index] = tmp
            index = min_child_index

    def _find_min_child(self, index):
        if index * 2 + 1 > self._size or self._size < 3:
            return index * 2 + 1 
        else:
            if self._heap_list[index * 2 + 1] < self._heap_list[index * 2 + 2]:
                return index * 2 + 1
            return index * 2 + 2

    def remove_min(self):
        removed = self._heap_list[0]
        self._heap_list[0] = self._heap_list[self._size - 1]
        self._size -= 1
        self._heap_list.pop()
        self._percolate_down(0)

        return removed

if __name__ == "__main__":
    heap = BinaryMinHeap()
    heap.insert(2)
    heap.insert(3)
    heap.insert(14)
    heap.insert(9)
    heap.insert(33)
    print(heap)
    heap.insert(4)
    print(heap)
    print(heap.remove_min())
    print(heap)
    print(heap.remove_min())
    print(heap.remove_min())
    print(heap.remove_min())
    print(heap.remove_min())
    print(heap.remove_min())
    print(heap)