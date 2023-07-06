width = int(input())
length = int(input())
height = int(input())
sum_boxes = 0
volume = width * length * height
input_line = input()

while input_line != "Done":
    boxes = int(input_line)

    sum_boxes += boxes
    if sum_boxes > volume:
        break
    input_line = input()

diff = abs(sum_boxes - volume)
if sum_boxes > volume:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")