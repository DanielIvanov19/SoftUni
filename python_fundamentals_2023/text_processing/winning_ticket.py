def get_char_best_result(half, character):
    best_result = 0
    current = 0
    for ch in half:
        if ch == character:
            current += 1
        else:
            best_result = max(best_result, current)
            current = 0
    return max(best_result, current)


tickets = [ticket.strip() for ticket in input().split(', ')]
symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    left_part = ticket[:10]
    right_part = ticket[10:]

    best_res = 0
    best_symbol = ''

    for symbol in symbols:
        left_part_score = get_char_best_result(left_part, symbol)
        right_part_score = get_char_best_result(right_part, symbol)
        overall_res = min(left_part_score, right_part_score)

        if overall_res > best_res:
            best_res = overall_res
            best_symbol = symbol

    is_winning = best_res >= 6
    is_jackpot = is_winning and best_res == 10
    if is_winning:
        print(f'ticket "{ticket}" - {best_res}{best_symbol}')
    elif is_jackpot:
        print(f'ticket "{ticket}" - {best_res}{best_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - no match')


