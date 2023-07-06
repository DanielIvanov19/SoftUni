user_input = input().split(', ')
input_to_num_list = list(map(int, user_input))

positives = [pos for pos in input_to_num_list if pos >= 0]
negatives = [neg for neg in input_to_num_list if neg < 0]
evens = [even for even in input_to_num_list if even % 2 == 0]
odds = [odd for odd in input_to_num_list if odd % 2 != 0]

positives_to_str = list(map(str, positives))
negatives_to_str = list(map(str, negatives))
evens_to_str = list(map(str, evens))
odds_to_str = list(map(str, odds))

positives_string = ', '.join(positives_to_str)
negatives_string = ', '.join(negatives_to_str)
evens_string = ', '.join(evens_to_str)
odds_string = ', '.join(odds_to_str)

print("Positive: " + positives_string)
print("Negative: " + negatives_string)
print("Even: " + evens_string)
print("Odd: " + odds_string)
