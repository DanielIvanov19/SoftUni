sequence_of_numbers = [int(x) for x in input().split(" ")]

middle = len(sequence_of_numbers) // 2

left_racer_time = 0
right_racer_time = 0
index_of_i = 0
for i in sequence_of_numbers:
    if index_of_i < middle:
        if i == 0:
            left_racer_time = left_racer_time * 0.8
        else:
            left_racer_time += i
    elif index_of_i > middle:
        if i == 0:
            right_racer_time = right_racer_time * 0.8
        else:
            right_racer_time += i
    index_of_i += 1
if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
elif right_racer_time < left_racer_time:
    print(f"The winner is right with total time: {right_racer_time:.1f}")