def words_sorting(*words):
    total_sum_dict = 0
    words_dict = {word: sum(map(ord, word)) for word in words}

    # for value in words_dict.values():
    #    total_sum_dict += value
    # print(total_sum_dict)

    if sum(words_dict.values()) % 2 == 0:
        return '\n'.join([f'{w} - {s}' for w, s in sorted(words_dict.items(), key=lambda x: x[0])])
    return '\n'.join([f'{w} - {s}' for w, s in sorted(words_dict.items(), key=lambda x: -x[1])])


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    )
)