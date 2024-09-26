#!/usr/bin/python3
""" 0-island_perimeter: calculates 2D matrix blocks perimeter """


def island_perimeter(grid=[]):
    """
    returns the perimeter of the island described in grid
    """

    # add blocks surrounding the cell that are zero
    # check only blocks that are 1s,
    # check above, left, right & below

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Assume all land cells have 4 sides
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    # Deduct 2 for shared side with above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Deduct 2 for shared side with neighbor to the left
                    perimeter -= 2

    return perimeter
