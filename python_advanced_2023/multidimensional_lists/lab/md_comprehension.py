rows, cols = [int(el) for el in input().split(', ')]

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

# flattening

matrix_2 = [[1, 2, 3], [4, 5, 6]]
matrix_3 = ((1, 2, 3), (4, 5, 6))

flatten = tuple([el for list_el in matrix_3 for el in list_el])

# for list_el in matrix:
#    flatten.extend()


for row_index in range(len(matrix_2)):
    for col_index in range(len(matrix_2[row_index])):
        current_el = matrix_2[row_index][col_index]
        flatten.append(current_el)
print(flatten)

