numbers = [int(x) for x in input().split()]

count_remove = int(input())
for _ in range(count_remove):
    num_remove = min(numbers)
    numbers.remove(num_remove)
for idx in range(len(numbers)):
    num = numbers[idx]
    if idx == len(numbers) - 1:
        print(num)
    else:
        print(num, end=', ')

#num_to_str = [str(x) for ]
#for _ in range(count_remove):
#    min = float('inf')
#    for num in numbers:
#        if num < min:
#            min = num