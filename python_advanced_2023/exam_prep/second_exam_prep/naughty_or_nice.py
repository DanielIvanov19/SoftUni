def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []
    result = []
    for command in args:
        number = int(command.split('-')[0])
        kid_type = command.split('-')[1]
        count_kid_occurrences = 0

        if kid_type == 'Naughty':
            index_of_found_kid = 0
            kid_name = ''
            for kid in santa_list:
                if kid[0] == number:
                    kid_name = kid[1]
                    index_of_found_kid = santa_list.index(kid)
                    count_kid_occurrences += 1
            if count_kid_occurrences > 1:
                continue
            else:
                santa_list.pop(index_of_found_kid)
                naughty.append(kid_name)
        elif kid_type == 'Nice':
            index_of_found_kid = 0
            kid_name = ''
            for kid in santa_list:
                if kid[0] == number:
                    kid_name = kid[1]
                    index_of_found_kid = santa_list.index(kid)
                    count_kid_occurrences += 1
            if count_kid_occurrences > 1:
                continue
            else:
                santa_list.pop(index_of_found_kid)
                nice.append(kid_name)
        if santa_list:
            [not_found.append(k[1]) for k in santa_list]

    result.append(f"Nice: {', '.join(nice)}")
    result.append(f"Naughty: {', '.join(naughty)}")
    result.append(f"Not found: {', '.join(not_found)}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
