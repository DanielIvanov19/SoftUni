import re

user_input = input().lower()
target = input().lower()

# f to use placeholder in the regex, r for the regex
matches = re.findall(rf'\b{target}\b', user_input)

print(len(matches))