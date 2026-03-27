def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new_row = []
        for i in row:
            i = i ** 2
            new_row.append(i)
        new.append(new_row)
    return new
