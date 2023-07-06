first_sequence = input().split(', ')
second_sequence = input().split(', ')
which_are_in = []

for substr in first_sequence:
    for str in second_sequence:
        if substr in str:
            which_are_in.append(substr)
            break
print(which_are_in)
