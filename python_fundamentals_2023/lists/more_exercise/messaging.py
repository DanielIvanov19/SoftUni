num_sequence = input().split(" ")

user_input = input()
message = ""
for i in num_sequence:
    index_of = 0
    for digit in i:
        index_of += int(digit)
    if index_of > len(user_input):
        index_of = index_of % len(user_input)
        message += user_input[index_of]
        user_input = user_input.replace(user_input[index_of], "")
    else:
        message += user_input[index_of]
        user_input = user_input.replace(user_input[index_of], "")
print(message)
