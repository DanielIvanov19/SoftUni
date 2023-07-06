import sys

max_num = -sys.maxsize
input_line = input()
while input_line != "Stop":
    num = int(input_line)
    if num > max_num:
        max_num = num
    input_line = input()
print(max_num)