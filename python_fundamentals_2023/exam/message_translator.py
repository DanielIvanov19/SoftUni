import re

n_strings = int(input())
pattern = r"^\!([A-Z][a-z]{2,})\!:(\[[A-Za-z]+\])"
p = re.compile(r"^\!([A-Z][a-z]{2,})\!:\[([A-Za-z]+)\]")


def is_valid(input_string):
    matches = re.findall(pattern, input_string)
    if not matches:
        print("The message is invalid")
    else:
        first_word = p.match(input_string).group(1)
        second_word = p.match(input_string).group(2)
        string_out = first_word + ": "
        for chr in second_word:
            string_out += str(ord(chr)) + " "
        string_out = string_out.rstrip(" ")
        print(string_out)


for _ in range(n_strings):
    line = input()

    is_valid(line)
