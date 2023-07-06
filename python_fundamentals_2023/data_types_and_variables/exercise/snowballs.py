import array

n = int(input())
snowball_dict = {}
quality_arr = array.array('d')
best_snowball = float('-inf')
output = ""
for i in range(0, n):
    weight_snowball = int(input())
    time_snowball = int(input())
    quality = int(input())

    value = (weight_snowball // time_snowball) ** quality
    if value > best_snowball:
        best_snowball = value
        output = f"{weight_snowball} : {time_snowball} = {value} ({quality})"
print(output)

