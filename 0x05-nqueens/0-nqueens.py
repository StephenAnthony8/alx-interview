#!/usr/bin/python3
""" Backtracking algorithm implementation """
import sys


class Nqueen:
    """
    Class Object: Queen object containing all attacking cells
    """
    def __init__(self, coordinates, val):
        x, y = coordinates
        self.xy = [
            f"[{0 + m}, {(y - x) + m}]" for m in range(val) if (
                0 <= 0 + m < val and 0 <= (y - x + m) < val
            )
            ]
        self.neg_xy = [
            f"[{0 + m}, {(y + x) - m}]" for m in range(val) if (
                0 <= 0 + m < val and 0 <= (y + x - m) < val
            )
            ]
        self.vert = [f"[{x}, {0 + m}]" for m in range(val)]
        self.horizontal = [f"[{0 + m}, {y}]" for m in range(val)]

    def occupied_cells(self):
        """ total cells occupied by an attacking queen """
        my_set = self.xy + self.neg_xy + self.vert + self.horizontal

        return (set(my_set))


def N_checker(board, val, cells, original=True, node=None):
    """
    Checks for cells that can fit in {val} amount of queens
    """
    if (original is True):
        storage = []

    # copy return list
    check = False

    for x in board:
        current_cells = cells.copy()
        current_cells.append(eval(x))
        remaining_cells = board.difference(
            Nqueen(eval(x), val).occupied_cells()
            )
        if len(remaining_cells) > 0:
            check = N_checker(remaining_cells, val, current_cells, False, x)

            if (check is not False) and original is False:
                check.sort()
                return check
            elif (check is not False) and original is True:
                if (check not in storage):
                    storage.append(check)

        elif len(current_cells) == val:
            return (current_cells)
    if (original is True):
        storage.sort()
        return storage
    return (False)


def Nqueens(val):
    """ Creates board and prints queen cells """

    board = set()
    [[board.add(f"[{x}, {y}]")for y in range(val)] for x in range(val)]

    values = N_checker(board, val, [], True,  None)

    [print(x) for x in values]


def main():
    """ Sanitization of input and initializaiton point """
    N = None
    if len(sys.argv) == 2:
        try:
            N = int(sys.argv[1])
        except Exception:
            sys.exit("N must be a number")

        if (N >= 4):
            Nqueens(N)
        else:
            sys.exit("N must be at least 4")

    else:
        sys.exit("Usage: nqueens N")


if __name__ == "__main__":
    main()
