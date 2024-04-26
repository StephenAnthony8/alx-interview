def pascal_triangle(n):
    rtn_list = []

    cell = []
    while (n != 0):
        len_c = len(cell)
        if len_c == 0:
            cell.append(1)
        else:
            next_cell = []

            next_cell.append(1)

            """ for x in range(len_c - 1): """
            [next_cell.append(cell[x] + cell[x + 1]) for x in range(len_c - 1)]

            next_cell.append(1)

            cell = next_cell
        rtn_list.append(cell)
        n -= 1
    return rtn_list
