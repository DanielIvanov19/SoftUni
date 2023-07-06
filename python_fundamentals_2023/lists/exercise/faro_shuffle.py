import random
cards_list = input().split(" ")
count_shuffles = int(input())

for _ in range(count_shuffles):
    first_half = []
    second_half = []
    for idx in range(1, len(cards_list) - 1):
        card = cards_list[idx]
        if idx < len(cards_list) / 2:
            first_half.append(card)
        else:
            second_half.append(card)
    shuffled = []
    first_part_idx = 0
    second_part_idx = 0
    for idx in range(len(first_half) * 2):
        if idx % 2 == 0:
            shuffled.append(second_half[second_part_idx])
            second_part_idx += 1
        else:
            shuffled.append(first_half[first_part_idx])
            first_part_idx += 1

        cards_list = [cards_list[0]] + shuffled + [cards_list[-1]]
print(cards_list)


#first_half = []
#first_half.extend(cards_list[1:len(cards_list)//2])
#second_half = []
#second_half.extend(cards_list[len(cards_list)//2:len(cards_list) - 1])
# ace two three four five six

# for i in range(0, count_shuffles - 1):
#    card = random(cards_list[1], cards_list[len(cards_list)//2])
#    cards_list.remove(card)
#    first_half.append(card)
