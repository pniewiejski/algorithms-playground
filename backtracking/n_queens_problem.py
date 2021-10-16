from typing import List
from pprint import pprint


def n_queens(size: int) -> List[List[int]]:
    solutions = []
    solve(size, 0, [], solutions)
    return solutions


def solve(size: int, row: int, row_placement: List[int], solutions: List[List[int]]) -> None:
    # row_placement is a list of row indices where queens are located, where each entry of
    # row_placement is associated with a column
    if row == size:
        # We've exhausted one "decision path" - we've went through all rows and did not backtrack,
        # thus we have found one of the solutions
        return solutions.append(row_placement.copy())  # copy, do not add references as they are volatile
    else:
        for row_index in range(size):
            row_placement.append(row_index)  # next "solution candidate"
            if is_valid(row_placement):  # validate a "solution candidate"
                solve(size, row + 1, row_placement, solutions)  # travel further through the decision space
            row_placement.pop()  # Backtrack


def is_valid(row_placement: List[int]) -> bool:
    last_column = len(row_placement) - 1
    for column_index in range(last_column):
        diff = abs(row_placement[last_column] - row_placement[column_index])
        if diff == 0 or diff == last_column - column_index:
            # Queens cannot be in the same row or column - diff == 0
            # And also there cannot be two queens on the same diagonal - diff == current_column - column_index
            return False
    return True


def print_solution(solution: List[int]):
    # Create an empty chess board
    def make_row(length):
        return [" "] * length

    size = len(solution)
    board = [make_row(size) for _ in range(size)]

    for column, row in enumerate(solution):
        board[column][row] = "$"  # mark queen's position
    pprint(board)


if __name__ == "__main__":
    solutions = n_queens(4)
    print(f"Found {len(solutions)} solutions")
    for index, solution in enumerate(solutions):
        print(f"Solution no. {index + 1}:")
        print(solution)
        print_solution(solution)
