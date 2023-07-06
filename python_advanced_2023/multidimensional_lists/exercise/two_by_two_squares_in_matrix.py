rows, cols = [int(el) for el in input().split()]

matrix = [[str(el) for el in input().split()] for _ in range(rows)]

identical_two_by_twos = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        curr_el = matrix[row_index][col_index]
        el_below = matrix[row_index + 1][col_index]
        next_el = matrix[row_index][col_index + 1]
        diagonal_el = matrix[row_index + 1][col_index + 1]

        if curr_el == el_below == next_el == diagonal_el:
            identical_two_by_twos += 1

print(identical_two_by_twos)
