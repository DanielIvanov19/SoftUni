init_sum = 0
input_line = input()

while input_line != "NoMoreMoney":
    current_sum = float(input_line)

    if current_sum >= 0:
        print(f"Increase: {current_sum}")
        init_sum += current_sum
    else:
        print("Invalid operation!")
        break

    input_line = input()

print(f"Total sum: {init_sum:.2f}")
