even_list = []
odd_list = []
negative_list = []
positive_list = []

n = int(input())

for _ in range(n):
    curr_num = int(input())
    if curr_num >= 0:
        positive_list.append(curr_num)
    else:
        negative_list.append(curr_num)
    if curr_num % 2 == 0:
        even_list.append(curr_num)
    else:
        odd_list.append(curr_num)
command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "positive":
    print(positive_list)
elif command == "negative":
    print(negative_list)
