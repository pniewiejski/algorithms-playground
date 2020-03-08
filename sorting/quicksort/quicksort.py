# This is a very simple and definitely not the best implementation
# of quicksort algorithm
# However, it shows the idea of pivot and sub-arrays very nicely

def quicksort(array):
    if len(array) < 2:
        return array
        
    pivot_index = int(len(array) / 2)  # selecting pivot
    pivot = array[pivot_index]
    array.pop(pivot_index) # remove pivot from array

    less = [i for i in array if i <= pivot]
    greater = [i for i in array if i > pivot]

    return quicksort(less) + [ pivot ] + quicksort(greater)

if __name__ == "__main__":
    print(quicksort([3, 4, 6, 1, 0, -24, 1]))