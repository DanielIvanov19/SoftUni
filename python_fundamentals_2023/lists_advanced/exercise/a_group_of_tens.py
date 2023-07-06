numbers_str = input().split(', ')
numbers_to_int = list(map(int, numbers_str))
max_num = max(numbers_to_int)
boundary = 10
while len(numbers_to_int) > 0:
    filtered = list(filter(lambda x: x <= boundary, numbers_to_int))
    for sorted_num in filtered:
        numbers_to_int.remove(sorted_num)
    print(f"Group of {boundary}'s: {filtered}")

    boundary += 10

