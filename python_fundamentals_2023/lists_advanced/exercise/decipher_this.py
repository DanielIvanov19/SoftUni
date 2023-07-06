message = input().split(' ')
deciphered_message = []
for word in message:
    first_letter = chr(int(word[0:1]))
    second_letter = word[-1]
    last_letter = word[2]
    word.replace(word[1], '')
    word.replace(word[0], first_letter)
    word.replace(word[1], second_letter)
    word.replace(word[-1], last_letter)
    deciphered_message.append(word)
deciphered_to_str = ' '.join(deciphered_message)
print(deciphered_to_str)
