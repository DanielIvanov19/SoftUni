import re

pattern = r"(www\.[A-Za-z\d-]+(\.[a-z]+)+)"
links = []
while True:
    line = input()
    if not line:
        break

    matches = re.findall(pattern, line)

    links.extend([m[0] for m in matches])
    # gets the first element from several tuples

for link in links:
    print(link)
