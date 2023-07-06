from string import ascii_lowercase

strings = input().split()
total_result = 0
for substring in strings:
    first_letter = substring[0]
    last_letter = substring[-1]
    number = int(substring[1:len(substring) - 1])

    first_letter_alphabetical_pos = ascii_lowercase.index(first_letter.lower()) + 1
    if first_letter.isupper():
        number /= first_letter_alphabetical_pos
    else:
        number *= first_letter_alphabetical_pos

    last_letter_alphabetical_pos = ascii_lowercase.index(last_letter.lower()) + 1

    if last_letter.isupper():
        number -= last_letter_alphabetical_pos
    else:
        number += last_letter_alphabetical_pos

    total_result += number

print(f'{total_result:.2f}')
