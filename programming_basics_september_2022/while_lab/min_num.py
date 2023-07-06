import sys

min_num = sys.maxsize
input_line = input()
while input_line != "Stop":
    num = int(input_line)
    if num < min_num:
        min_num = num
    input_line = input()
print(min_num)