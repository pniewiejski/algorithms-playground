def insertion_sort(array):
    for index in range(1, len(array)):
        current_position = index
        current_value = array[index]

        while current_position > 0 and array[current_position - 1] > current_value:
            array[current_position] = array[current_position - 1]
            current_position -= 1

        array[current_position] = current_value
    
    return array

if __name__ == "__main__":
    print(insertion_sort([5,3,2,67,0,9]))