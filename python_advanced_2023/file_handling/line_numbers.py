from string import punctuation

with open('files/text.txt', 'r') as file:
    text = file.readlines()

output_file = open('files/output.txt', 'w')


for i in range(len(text)):

    letters, punctuation_symbols = 0, 0

    for symbol in text[i]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punctuation_symbols += 1
    output_file.write(f"Line {i+1}: {''.join(text[i][:-1])} ({letters})({punctuation_symbols})\n")