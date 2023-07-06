import re

pattern = r"\s([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-za-z][A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)"

text = input()

matches = re.findall(pattern, text)
print('\n'.join(groups[0] for groups in matches))
