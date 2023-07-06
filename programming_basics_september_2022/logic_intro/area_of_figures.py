import math

figure = input()

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
elif figure == "circle":
    radius = float(input())
    area = radius * radius * math.pi
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = side * height / 2

print(f"{area:.3f}")