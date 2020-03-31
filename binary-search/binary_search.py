def binary_search(array, searched_value):
    """
    Returns the index at which a `searched_value` exists in the `array`
    and `None` in case where `searched_value` is not in the `array`.
    """
    lower = 0
    upper = len(array) - 1

    while lower < upper:
        middle_index = lower + (upper - lower) // 2
        middle_value = array[middle_index]

        if middle_value == searched_value:
            return middle_index
        elif middle_value > searched_value:
            upper = middle_index - 1
        else:
            lower = middle_index + 1
    
    return None

def binary_search_recursive(array, searched_value):
    def helper(upper, lower):
        if lower > upper:
            return None
        
        middle_index = lower + (upper - lower) // 2
        middle_value = array[middle_index]

        if middle_value == searched_value:
            return middle_index
        elif middle_value > searched_value:
            return helper(middle_index - 1, lower)
        else:
            return helper(upper, middle_index + 1)
    
    return helper(len(array) - 1, 0)

if __name__ == "__main__":
    print(binary_search([1, 2, 4, 7, 9, 11, 13], 11))
    print(binary_search_recursive([1, 2, 4, 7, 9, 11, 13], 11))