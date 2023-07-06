import re

text = input()

# r - used to use a string as a raw string

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

results = re.findall(pattern, text)
# findall -> when we don't work with groups


# print(text[results.start(): results.end()])
print(*results)
