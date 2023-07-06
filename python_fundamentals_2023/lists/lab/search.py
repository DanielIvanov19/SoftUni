n = int(input())
word = input()
all_strings = []
strings_containing_word = []
for _ in range(n):
    current_input = input()
    if word in current_input:
        strings_containing_word.append(word)
    all_strings.append(current_input)
print(all_strings)
print(strings_containing_word)