import re
pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z][a-z])\2(?<Year>\d{4})\b"
# with 2 we call the match of group 2

text = input()

# findall returns tuple
# finditer returns match objects

dates = re.finditer(pattern, text)

# date.groupdict() -> makes a dictionary if we have named the groups

for date in dates:
    date_data = date.groupdict()
    print(f"Day: {date_data['Day']}, Month: {date_data['Month']}, Year: {date_data['Year']}")
