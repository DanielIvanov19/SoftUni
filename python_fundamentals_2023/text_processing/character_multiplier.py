names = input().split()

first_name = names[0]
second_name = names[1]

min_length = min(len(first_name), len(second_name))

result = 0
for idx in range(min_length):
    first_chr = first_name[idx]
    second_chr = second_name[idx]
    result += ord(first_chr) * ord(second_chr)

result += sum([ord(char) for char in first_name[min_length::]])
result += sum([ord(char) for char in second_name[min_length::]])

print(result)
