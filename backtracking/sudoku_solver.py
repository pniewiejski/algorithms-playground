import pprint
import itertools
from typing import List

# Example from Wikipedia https://en.wikipedia.org/wiki/Sudoku
# I use 0 to indicate an empty spot.
GAME = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# Solution
# [[5, 3, 4, 6, 7, 8, 9, 1, 2],
#  [6, 7, 2, 1, 9, 5, 3, 4, 8],
#  [1, 9, 8, 3, 4, 2, 5, 6, 7],
#  [8, 5, 9, 7, 6, 1, 4, 2, 3],
#  [4, 2, 6, 8, 5, 3, 7, 9, 1],
#  [7, 1, 3, 9, 2, 4, 8, 5, 6],
#  [9, 6, 1, 5, 3, 7, 2, 8, 4],
#  [2, 8, 7, 4, 1, 9, 6, 3, 5],
#  [3, 4, 5, 2, 8, 6, 1, 7, 9]]


class SudokuGame:
    def __init__(self, board: List[List[int]]):
        self._board = board

    def __str__(self):
        return self._board.__str__()

    def get_value_at(self, row: int, column: int) -> int:
        return self._board[row][column]

    def set_value_at(self, row: int, column: int, value: int):
        self._board[row][column] = value

    def is_solved(self) -> bool:
        return self._compute_task_size() == 0

    def print_board(self) -> None:
        pprint.pprint(self._board)

    def _compute_task_size(self) -> int:
        return list(itertools.chain.from_iterable(self._board)).count(0)


class SudokuSolver: 
    def __init__(self, game: list):
        self._game = SudokuGame(game)

    def is_possible(self, row: int, column: int, value: int) -> bool:
        # check row - the same value cannot appear in the same row twice
        for i in range(9):
            if self._game.get_value_at(row, i) == value:
                return False
        # check column - the same value cannot appear in the same column twice
        for i in range(9):
            if self._game.get_value_at(i, column) == value:
                return False
        # check neighbors - Sudoku board is divided into 9 sub-squares.
        # The same value cannot appear twice in one sub-square.
        x0 = (row // 3) * 3 # find row, column indices of the beginning of the sub-square
        y0 = (column // 3) * 3
        for i in range(3):
            for j in range(3):
                if self._game.get_value_at(x0 + i, y0 + j) == value:
                    return False
        return True

    def solve(self) -> SudokuGame:
        self._solve()
        return self._game

    def _solve(self) -> bool:
        for row in range(9):
            for column in range(9):
                # we want to operate only on elements that we haven't found solution yet
                if self._game.get_value_at(row, column) == 0:
                    for value_to_check in range(1, 10):
                        if self.is_possible(row, column, value_to_check):
                            self._game.set_value_at(row, column, value_to_check)
                            if self._solve():
                                return True
                            self._game.set_value_at(row, column, 0)  # backtrack
                    return False
        if self._game.is_solved():
            return True

        return False


if __name__ == "__main__":
    solver = SudokuSolver(GAME)
    solution = solver.solve()
    solution.print_board()
