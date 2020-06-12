def heapsort(array):
    # we begin from the last element because that's where
    # the highest value element will be after we sort the array;
    # We are sorting from the smallest to the largest value.
    last_element_index = len(array) - 1

    build_maxheap(array)  # Build a max heap
    # Now the element array[0] is the largest value in the array

    while last_element_index > 0:
        # append the largest element in the unsorted sub-array (our heap)
        # to the "already sorted" sub-array
        swap(array, 0, last_element_index)

        # "Repear the heap" (unsorted sub-array)
        heapify(array, 0, last_element_index)

        # Decrement the size of the unsorted sub-array
        last_element_index -= 1

    return array


def build_maxheap(array):
    index = len(array) // 2 - 1

    while index >= 0:
        heapify(array, index, len(array))
        index -= 1


def heapify(heap, begin_index, max_index):
    while begin_index < max_index:
        index = begin_index

        left_child = 2 * index + 1
        right_child = left_child + 1

        if left_child < max_index and heap[left_child] > heap[index]:
            index = left_child

        if right_child < max_index and heap[right_child] > heap[index]:
            index = right_child

        if index == begin_index:
            return

        swap(heap, begin_index, index)
        begin_index = index


def swap(array, begin_index, end_index):
    array[begin_index], array[end_index] = array[end_index], array[begin_index]


if __name__ == "__main__":
    print(heapsort([3, 4, 1, 1, 34, 11]))
