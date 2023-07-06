movie_name = input()
num_days = int(input())
num_tickets = int(input())
price_ticket = float(input())
percent_for_cinema = int(input())

profit_per_day = num_tickets * price_ticket
period_profit = num_days * profit_per_day
cinema_profit = period_profit *(percent_for_cinema/100)
personal_profit = period_profit - cinema_profit
print(f"The profit  from the movie {movie_name} is {period_profit:.2f} lv")