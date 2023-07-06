import math


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line_length = pow((x2 - x1), 2) + pow((y2 - y1), 2)
    second_line_length = pow((x4 - x3), 2) + pow((y4 - y3), 2)
    if first_line_length == second_line_length:
        x2_int = int(x2)
        y2_int = int(y2)
        x1_int = int(x1)
        y1_int = int(y1)
        return f'({math.floor(x2_int)}, {math.floor(y2_int)})({math.floor(x1_int)}, {math.floor(y1_int)})'
    elif first_line_length > second_line_length:
        x2_int = int(x2)
        y2_int = int(y2)
        x1_int = int(x1)
        y1_int = int(y1)
        return f'({math.floor(x2_int)}, {math.floor(y2_int)})({math.floor(x1_int)}, {math.floor(y1_int)})'
    elif first_line_length < second_line_length:
        x4_int = int(x4)
        y4_int = int(y4)
        x3_int = int(x3)
        y3_int = int(y3)
        return f'({math.floor(x4_int)}, {math.floor(y4_int)})({math.floor(x3_int)}, {math.floor(y3_int)})'


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

result = longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)
print(result)
