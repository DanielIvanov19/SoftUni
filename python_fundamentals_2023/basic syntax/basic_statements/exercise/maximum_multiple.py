divisor = int(input())

boundary = int(input())

result = 0
for num in range(boundary, 0, - 1):
    if num % divisor == 0:
        print(num)
        break
#max_num = boundary - boundary % divisor
#print(max_num)