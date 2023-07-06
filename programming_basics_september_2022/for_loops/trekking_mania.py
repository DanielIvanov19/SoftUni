num_of_groups = int(input())

c_musala = 0
c_montblanc = 0
c_kilimanjaro = 0
c_k2 = 0
c_everest = 0
people = 0

for _ in range(1, num_of_groups + 1):
    group_size = int(input())
    people += group_size
    if group_size <= 5:
        c_musala += group_size
    elif group_size <= 12:
        c_montblanc += group_size
    elif group_size <= 25:
        c_kilimanjaro += group_size
    elif group_size <= 40:
        c_k2 += group_size
    elif group_size >= 41:
        c_everest += group_size

musala_percentage = (c_musala / people) * 100
montblanc_percentage = (c_montblanc / people) * 100
kilimanjaro_percentage = (c_kilimanjaro / people) * 100
k2_percentage = (c_k2 / people) * 100
everest_percentage = (c_everest / people) * 100

print(f"{musala_percentage:.2f}%")
print(f"{montblanc_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
