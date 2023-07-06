rage_message = ''

rage_input = input()
counter_alpha = 0
idx = 0
while idx < len(rage_input):
    element = rage_input[idx]
    if element.isdigit():
        first_idx_num = rage_input.index(element)
        if idx + 1 < len(rage_input):
            if rage_input[idx + 1].isdigit():
                number = int((element + rage_input[idx + 1]))
                rage_message += rage_input[counter_alpha:first_idx_num].upper() * number
                idx += 2
                counter_alpha += idx + 1
            else:
                number = int(element)
                rage_message += rage_input[counter_alpha:first_idx_num].upper() * number
                idx += 1
                counter_alpha = idx
        else:
            number = int(element)
            rage_message += rage_input[counter_alpha:first_idx_num].upper() * number
            idx += 1
    else:
        idx += 1

print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)
