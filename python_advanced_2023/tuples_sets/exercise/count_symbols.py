word = input()

for char in sorted(set(word)):
    print(f"{char}: {word.count(char)} time/s")

# occurrences = {}
# for letter in input():
#    occurrences[letter] = occurrences.get(letter, 0) + 1
#
# for letter, occurrence in sorted(occurrences.items()):
#   print(f'{letter}: {occurrence} time/s')
