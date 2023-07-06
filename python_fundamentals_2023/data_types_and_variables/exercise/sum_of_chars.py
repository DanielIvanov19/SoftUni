n = int(input())
ascii_sum = 0
for i in range(0, n):
    char = input()
    ascii_sum += ord(char)
print(f"The sum equals: {ascii_sum}")
