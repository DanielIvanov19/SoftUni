text = input()
result = text[0]

for char in text:
    if char == result[-1]:
        continue
    else:
        result += char

print(result)