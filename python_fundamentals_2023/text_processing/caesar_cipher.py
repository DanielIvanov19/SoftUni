text = input()
result = ''
for each in text:
    new_ascii = ord(each) + 3
    new_char = chr(new_ascii)
    result += new_char

print(result)