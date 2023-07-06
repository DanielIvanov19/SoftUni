rows, columns = [int(el) for el in input().split(', ')]

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

row_1 = 0
row_2 = 1
col_1 = 0
col_2 = 1

max_sum = 0

while row_2 < rows and col_2 < columns:
    current_sum = matrix[row_1][col_1] + matrix[row_1][col_2] + matrix[row_2][col_1] + matrix[row_2][col_2]
    if max_sum < current_sum:
        max_sum = current_sum
        max_elements = [[matrix[row_1][col_1], matrix[row_1][col_2]], [matrix[row_2][col_1], matrix[row_2][col_2]]]
    row_1 += 1
    row_2 += 1
    col_1 += 1
    col_2 += 1

max_matrix = [[int(el) for el in max_elements] for _ in range(2)]

print(max_matrix)

print(max_sum)

