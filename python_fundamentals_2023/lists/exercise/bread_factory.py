init_energy = 100
init_coins = 100
working_day_events = input().split("|")
events_handled = 0
events_list = []
for day in working_day_events:
    event_args = day.split("-")
    event = event_args[0]
    number = int(event_args[1])
    events_list.append(event)
    if event == "rest":
        if init_energy + number > 100:
            extra_energy = 100 - init_energy
            init_energy = 100
            print(f"You gained {extra_energy} energy.")
            print(f"Current energy: {init_energy}.")
        else:
            init_energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {init_energy}.")
        events_handled += 1
    elif event == "order":
        if init_energy >= 30:
            print(f"You earned {number} coins.")
            init_coins += number
            init_energy -= 30
            events_handled += 1
        else:
            print("You had to rest!")
            init_energy += 50
            continue
    else:
        if init_coins >= number:
            print(f"You bought {event}.")
            init_coins -= number
            events_handled += 1
        elif init_coins < number:
            print(f"Closed! Cannot afford {event}.")
            break
if len(events_list) == events_handled:
    print("Day completed!")
    print(f"Coins: {init_coins}")
    print(f"Energy: {init_energy}")
