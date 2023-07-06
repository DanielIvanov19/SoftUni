people = int(input())
nights = int(input())
transport_cards = int(input())
museum_tickets = int(input())

night_price = 20
card_price = 1.6
museum_ticket = 6

sum = ((nights * night_price + transport_cards * card_price + museum_tickets * museum_ticket) * people) * 1.25
print(f"{sum:.2f}")