factor = int(input())
count = int(input())

num_list = []

for i in range(0, count):
    n = (i + 1) * factor
    num_list.append(n)
print(num_list)