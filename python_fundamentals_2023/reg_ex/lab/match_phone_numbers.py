import re

pattern = r"\+359 2 \d{3} d{4}\b|\+359-2-\d{3}-\d{4}\b"
text = input()

# regex_pattern = re.compile(pattern) -> lower time  consumption
# numbers = regex_pattern.findall(text)

numbers = re.findall(pattern, text)

print(*numbers, sep=', ')
