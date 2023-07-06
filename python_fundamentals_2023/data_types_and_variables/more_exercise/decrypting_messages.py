key = int(input())
lines = int(input())
message = ""
for i in range(1, lines + 1):
    letter = input()
    order = ord(letter)
    string_g = chr(order + key)
    message += string_g
print(message)
