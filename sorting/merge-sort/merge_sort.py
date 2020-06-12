def merge(a, b):
    merged = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            merged.append(a[0])
            a.pop(0)
        else:
            merged.append(b[0])
            b.pop(0)
    # At this point either a or b is empty
    merged += a + b

    return merged


def merge_sort(array):
    if len(array) < 2:  # base case
        return array

    middle_index = len(array) // 2
    left = array[:middle_index]
    right = array[middle_index:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


if __name__ == "__main__":
    print(merge([0, 1, 2], [1, 2, 5]))
    print(merge_sort([4, 3, 5, 0, 2, 1, -2, 9, 7]))
