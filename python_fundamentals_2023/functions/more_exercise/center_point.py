x_1 = float(input())
y_1 = float(input())

x_2 = float(input())
y_2 = float(input())


def center_point(x1, x2, y1, y2):
    distance_1 = pow(x1, 2) + pow(y1, 2)
    distance_2 = pow(x2, 2) + pow(y2, 2)

    if distance_1 == distance_2:
        return f'({int(x1)}, {int(y1)})'
    elif distance_1 < distance_2:
        return f'({int(x1)}, {int(y1)})'
    elif distance_2 < distance_1:
        return f'({int(x2)}, {int(y2)})'


result = center_point(x_1, x_2, y_1, y_2)
print(result)
