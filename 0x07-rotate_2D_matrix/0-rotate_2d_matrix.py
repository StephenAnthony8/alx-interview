#!/usr/bin/python3
"2D matrix rotation module"


def rotate_2d_matrix(matrix=[]):
    """ Rotates a 2D matrix by 90 degrees """

    copy_list = [[y for y in x] for x in matrix]

    inner_list_len = len(matrix[0])

    for x in range(0, inner_list_len):
        for y in range(0, inner_list_len):

            matrix[y][(inner_list_len - 1) - x] = copy_list[x][y]
