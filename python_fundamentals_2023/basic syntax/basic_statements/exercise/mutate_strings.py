first_string = input()
second_string = input()
transform_string = ""

for idx in range(len(first_string)):
    if first_string[idx] == second_string[idx]:
        continue
    transform_string = second_string[:idx + 1] + first_string[idx + 1:]
    print(transform_string)
