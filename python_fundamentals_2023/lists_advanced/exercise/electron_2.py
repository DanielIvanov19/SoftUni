number_of_electrons = int(input())
result = []
while number_of_electrons > 0:
    n = len(result) + 1
    electrons_needed = min(2 * (n ** 2), number_of_electrons)
    result.append(electrons_needed)
    number_of_electrons -= electrons_needed
print(result)