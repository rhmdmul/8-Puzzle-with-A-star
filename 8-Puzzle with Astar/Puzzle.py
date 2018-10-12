# Created by PyCharm.
# User: madmul
# Date: 10/05/2018
# Time: 08:44 PM

from copy import deepcopy


class Puzzle:
    def __init__(self, start, parent):
        self.table = start
        self.root = parent
        self.f_star = 0
        self.man_dist = 0
        self.wrong_amount = 0


def getFValue(open_list):
    f = open_list[0].f_star
    index = 0
    for i, item in enumerate(open_list):
        if i == 0:
            continue
        if item.f_star < f:
            f = item.f_star
            index = i
    # print("Index di GBF : ",index)
    # print("Open List : ",open_list[index])
    # print("F Value : ",f)
    return index, open_list[index]


def getNone(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return i, j


def manhattanDistance(board, goal):
    man_dist = 0
    for i in range(3):
        for j in range(3):
            pav = board[i][j]
            if pav is not None:
                for i_goal in range(3):
                    for j_goal in range(3):
                        if pav == goal[i_goal][j_goal]:
                            man_dist += abs(i - i_goal) + abs(j - j_goal)
    return man_dist


def neighborsNode(puzzle):
    table = puzzle.table
    list_of_neighbors = []
    x, y = getNone(table)
    if x > 0:
        new_table = deepcopy(table)
        new_table[x][y] = new_table[x - 1][y]
        new_table[x - 1][y] = None
        node = Puzzle(new_table, puzzle)
        list_of_neighbors.append(node)
    if y > 0:
        new_table = deepcopy(table)
        new_table[x][y] = new_table[x][y - 1]
        new_table[x][y - 1] = None
        node = Puzzle(new_table, puzzle)
        list_of_neighbors.append(node)
    if x < 2:
        new_table = deepcopy(table)
        new_table[x][y] = new_table[x + 1][y]
        new_table[x + 1][y] = None
        node = Puzzle(new_table, puzzle)
        list_of_neighbors.append(node)
    if y < 2:
        new_board = deepcopy(table)
        new_board[x][y] = new_board[x][y + 1]
        new_board[x][y + 1] = None
        node = Puzzle(new_board, puzzle)
        list_of_neighbors.append(node)
    return list_of_neighbors


def astarFormula(puzzle, goal, depth):
    opened_list = []
    closed_list = []
    opened_list.append(puzzle)

    i = 0
    while opened_list:
        if depth is not None and i >= depth:
            print("Not found in this depth")
            break

        index, current = getFValue(opened_list)
        if isGoal(current.table, goal):
            print("Puzzle Solve!")
            output(current)
            return current

        print("Current Puzzle State")
        output(current)

        opened_list.pop(index)
        closed_list.append(current)

        # print("Open List :", open_list)
        # print("Close LIst : ",closed_list)

        neighbor_list = neighborsNode(current)
        for neighbor in neighbor_list:
            is_closed = False
            for i, closed in enumerate(closed_list):
                if closed.table == neighbor.table:
                    is_closed = True
                    break

            if not is_closed:
                is_open = False
                wrong_temp = current.wrong_amount + 1

                for j, opened in enumerate(opened_list):
                    if opened.table == neighbor.table:
                        is_open = True
                        if wrong_temp < opened_list[j].wrong_amount:
                            opened_list[j].wrong_amount = wrong_temp
                            opened_list[j].f_star = opened_list[j].wrong_amount + opened_list[j].man_dist
                            opened_list[j].root = current
                        break

                if not is_open:
                    neighbor.wrong_amount = wrong_temp
                    neighbor.man_dist = manhattanDistance(neighbor.table, goal)
                    neighbor.f_star = neighbor.wrong_amount + neighbor.man_dist
                    neighbor.parent = current
                    opened_list.append(neighbor)

        i += 1

    return None


def isGoal(board, goal):
    return board == goal


def output(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle.table[i][j] is not None:
                print(puzzle.table[i][j], end=' ')
            else:
                print(' ', end=' ')
        print("")
    print("-----------------")