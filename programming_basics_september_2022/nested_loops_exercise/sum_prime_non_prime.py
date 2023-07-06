input_line = input()
sum_prime = 0
sum_non_prime = 0
while input_line != "stop":
    num = int(input_line)
    if num < 0:
        print("Number is negative.")
        input_line = input()
        continue
    count = 0

    for n in range(1, num + 1):
        if num % n == 0:
            count += 1
    if count == 2:
        sum_prime += num
    else:
        sum_non_prime += num
    input_line = input()
print(f"Sum of all prime number is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
