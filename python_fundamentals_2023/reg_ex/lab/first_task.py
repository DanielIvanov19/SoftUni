import re

result = []


while True:
    line = input()
    if not line:
        break
    # ways for escaping the "\" : r-for regex before the string or \\
    matches = re.findall(r"[0-9]+", line)
    result.extend(matches)

print(' '.join(result))
