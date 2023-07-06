year = int(input())
year_to_str = str(year)
while len(year_to_str) != len(set(year_to_str)):
    year += 1
    year_to_str = str(year)
print(year)