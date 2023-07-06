sequence = [int(x) for x in input().split(' ')]
sum_of_removals = 0

while len(sequence) > 0:
    index_removal = int(input())
    if len(sequence) == 1:
        removed = sequence.pop()
        sum_of_removals += removed
        break
    if index_removal < 0:
        index_removal = 0
        removed = sequence[index_removal]
        sequence.pop(0)
        if len(sequence) == 0:
            sum += removed
            break
        last_element = sequence[-1]
        sequence.insert(0, last_element)
        sequence.pop(-1)
        if len(sequence) == 0:
            sum += removed
            break
        sum_of_removals += removed

        for item in range(len(sequence)):
            if sequence[item] <= removed:
                sequence[item] += removed
            else:
                sequence[item] -= removed
    elif index_removal > len(sequence) - 1:
        index_removal = -1
        removed = sequence[index_removal]
        sequence.pop(index_removal)
        if len(sequence) == 0:
            sum_of_removals += removed
            break
        first_element = sequence[0]
        sequence.remove(first_element)
        sequence.append(first_element)
        sum_of_removals += removed

        for item in range(len(sequence)):
            if sequence[item] <= removed:
                sequence[item] += removed
            else:
                sequence[item] -= removed
    else:
        removed = sequence[index_removal]
        sequence.pop(index_removal)
        if len(sequence) == 0:
            break
        sum_of_removals += removed
        for item in range(len(sequence)):
            if sequence[item] <= removed:
                sequence[item] += removed
            else:
                sequence[item] -= removed

print(sum_of_removals)
