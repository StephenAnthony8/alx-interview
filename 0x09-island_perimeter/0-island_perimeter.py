#!/usr/bin/python3
""" 0-island_perimeter: calculates 2D matrix blocks perimeter """


def island_perimeter(grid=[]):
    """
    returns the perimeter of the island described in grid
    """

    # add blocks surrounding the cell that are zero
    # check only blocks that are 1s,
    # check above, left, right & below

    count = 0

    for x in range(len(grid)):
        x_axis = grid[x]
        for y in range(len(x_axis)):
            # check only blocks that are 1s
            if (x_axis[y] == 1):
                # check above
                if (x > 0) and (grid[x - 1][y] != 1):
                    count += 1
                # check below
                if (x < len(grid) - 1) and (grid[x + 1][y] != 1):
                    count += 1

                # check right
                if (y > 0) and (x_axis[y - 1] != 1):
                    count += 1

                # check left
                if (y < len(x_axis) - 1 and (x_axis[y + 1] != 1)):
                    count += 1
    return (count)
