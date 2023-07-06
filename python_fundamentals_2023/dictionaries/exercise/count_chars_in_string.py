word = input()

occurencies = {}

for bukva in word:
    if bukva == " ":
        continue
    if bukva not in occurencies:
        occurencies[bukva] = 1
    else:
        occurencies[bukva] += 1

for bukva, occurence in occurencies.items():
    print(f"{bukva} -> {occurence}")
