# Created by PyCharm.
# User: madmul
# Date: 10/05/2018
# Time: 09:01 PM

from Puzzle import Puzzle, astarFormula


def main():
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
    puzzle_board = [[3, 4, 8], [5, None, 6], [7, 1, 2]]
    puzzle = Puzzle(puzzle_board, None)
    depth = 100
    astarFormula(puzzle, goal, depth)


if __name__ == "__main__":
    main()