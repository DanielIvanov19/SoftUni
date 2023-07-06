text = input()
digits = ''
letters = ''
others = ''

for charac in text:
    if charac.isalpha():
        letters += charac
    elif charac.isdigit():
        digits += charac
    else:
        others += charac

print(digits)
print(letters)
print(others)
