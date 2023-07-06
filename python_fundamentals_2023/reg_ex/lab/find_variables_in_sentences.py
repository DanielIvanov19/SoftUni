import re

pattern = r'\b_([A-Za-z\d]+)\b'

line = input()
matches = re.findall(pattern, line)

print(','.join(matches))
