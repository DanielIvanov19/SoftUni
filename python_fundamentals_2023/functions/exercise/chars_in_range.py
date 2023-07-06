def get_chars_in_range(start, end):
    first = ord(start)
    last = ord(end)
    result = []
    for char in range(first + 1, last):
        result.append((chr(char)))
    return result


start_char = input()
end_char = input()
result_chars = get_chars_in_range(start_char, end_char)
print(' '.join(result_chars))
