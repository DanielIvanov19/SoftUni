team_A_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

sent_off_string = input()
sent_off_list = sent_off_string.split(" ")

count_team_A = len(team_A_list)
count_team_B = len(team_B_list)
length = len(sent_off_list)
if "A-" in sent_off_string or "B-" in sent_off_string:
    for i in sent_off_list:
        if i[0] == "A":
            num = int(i[2:])
            if num in team_A_list:
                team_A_list.remove(num)
                if len(team_A_list) < 7:
                    break
            else:
                continue
        elif i[0] == "B":
            num = int(i[2:])
            if num in team_B_list:
                team_B_list.remove(num)
                if len(team_B_list) < 7:
                    break
            else:
                continue
print(f"Team A - {len(team_A_list)}; Team B - {len(team_B_list)}")
if len(team_A_list) < 7 or len(team_B_list) < 7:
    print("Game was terminated")

# card_args = card.split("-")
# team = card_args[0]
# pl_num = card_args[1]
