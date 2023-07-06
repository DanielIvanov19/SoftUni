rows, cols = [int(el) for el in input().split(', ')]
matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(', ')]
    matrix.append(inner_list)

max_sum = float('-inf')

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        curr_el = matrix[row_index][col_index]
        el_below = matrix[row_index + 1][col_index]
        next_el = matrix[row_index][col_index + 1]
        diagonal_el = matrix[row_index + 1][col_index + 1]
        sum_elements = curr_el + el_below + next_el + diagonal_el

        if max_sum < sum_elements:
            max_sum = sum_elements
            sub_matrix = [[curr_el, next_el], [el_below, diagonal_el]]


print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)