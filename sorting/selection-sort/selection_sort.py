def swap(array: list, origin: int, destination: int):
    tmp = array[origin]
    array[origin] = array[destination]
    array[destination] = tmp


def find_smallest(array: list) -> int:
    index_smallest = 0

    for i in range(1, len(array)):
        if array[i] < array[index_smallest]:
            index_smallest = i
    return index_smallest


def selection_sort(array: list) -> list:
    sorted_index = 0
    for i in range(len(array)):
        array_subset = array[i:]
        smallest_unsorted_index = find_smallest(array_subset)
        swap(array, smallest_unsorted_index + sorted_index, sorted_index)
        sorted_index += 1

    return array


if __name__ == "__main__":
    print(selection_sort([3, 4, 5, 2, 1]))
