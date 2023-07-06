number_of_electrons = int(input())
position = 1
electrons_needed = 2 * (position * position)
shells_list = []
while number_of_electrons > 0:
    if electrons_needed <= number_of_electrons:
        number_of_electrons -= electrons_needed
        shells_list.append(electrons_needed)
        position += 1
    else:
        last_one = electrons_needed - number_of_electrons
        shells_list.append(last_one)
        number_of_electrons -= last_one
print(shells_list)