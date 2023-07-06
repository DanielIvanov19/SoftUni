def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids, naughty_kids = [], []
    result = []

    def place_kid():
        """if a kid is found, place it in a certain list"""
        if len(kids) == 1:
            nice_kids.append(kids[0][1]) if type_kid == 'Nice' else naughty_kids.append(
                kids[0][1])  # .extend() = .append(*)
            santa_list.remove(*kids)

    for kid_data in args:
        number = int(kid_data.split('-')[0])
        type_kid = kid_data.split('-')[1]
        kids = [info for info in santa_list if info[0] == number]
        place_kid()

    for name, type_kid in kwargs.items():
        kids = [info for info in santa_list if info[1] == name]
        place_kid()

    if nice_kids:
        result.append(f"Nice: {', '.join(nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(naughty_kids)}")
    if santa_list:
        result.append(f"Not found: {', '.join(k[1] for k in santa_list)}")

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
