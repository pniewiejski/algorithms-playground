# Given a collection of **distinct** integers return all possible permutations.
# Example:
#  {1, 2, 3} -> (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)

# In general the number of permutations is n!
# Time complexity of the solution will be O(n!) and space complexity O(n!)

# We want to use **backtracking**

def find_permutations(numbers):
    
    result = []

    def swap_numbers(a, b):
        numbers[a], numbers[b] = numbers[b], numbers[a]

    def permutations_helper(start):
        if start == len(numbers) - 1:
            # Don't append by reference as `numbers` array is always changing in this implementation
            result.append(numbers.copy())

        for index in range(start, len(numbers)):
            swap_numbers(start, index)
            permutations_helper(start + 1) 
            swap_numbers(start, index) # swap back
    
    permutations_helper(0)
    return result

if __name__ == "__main__":
    print(find_permutations([1, 2, 3]))
