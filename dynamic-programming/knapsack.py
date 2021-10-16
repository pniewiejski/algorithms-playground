# This is a simple solution to a discrete knapsack problem using dynamic programming

from pprint import pprint

ITEMS = [
    { "name": "tablet", "price": 1500, "weight": 1},
    { "name": "stereo", "price": 3000, "weight": 4},
    { "name": "computer", "price": 2000, "weight": 3},
]

MAX_BACKPACK_WEIGHT = 4

# This is the 2D matrix (list of lists) that is used to track solutions of sub-problems
# additional row and column with zeros is allocated for the base case (0kg max weight, no stolen items)
memorized_solutions = [[0 for _ in range(MAX_BACKPACK_WEIGHT + 1)] for _ in range(len(ITEMS) + 1)]

def get_item(item_number): return ITEMS[item_number - 1]
def get_item_value(item_number): return get_item(item_number)["price"]
def get_item_weight(item_number): return get_item(item_number)["weight"]
def get_item_name(item_number): return get_item(item_number)["name"]

for item_number in range(1, len(ITEMS) + 1):
    for max_bagpack_weight in range(1, MAX_BACKPACK_WEIGHT + 1):
        if max_bagpack_weight < get_item_weight(item_number):
            previous_max = memorized_solutions[item_number - 1][max_bagpack_weight]

            memorized_solutions[item_number][max_bagpack_weight] = previous_max
        else:
           previous_max = memorized_solutions[item_number - 1][max_bagpack_weight]
           current_item_value = get_item_value(item_number)
           value_of_remaining_space = memorized_solutions[item_number - 1][max_bagpack_weight - get_item_weight(item_number)] 

           memorized_solutions[item_number][max_bagpack_weight] = max(previous_max, current_item_value + value_of_remaining_space)
    print(f"{item_number}: Result after checking {get_item_name(item_number)}")
    pprint(memorized_solutions)

print("-------------------")
print("Final solution grid")
pprint(memorized_solutions)

