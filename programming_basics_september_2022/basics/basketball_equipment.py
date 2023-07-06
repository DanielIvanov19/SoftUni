annual_price = int(input())
basketball_sneakers = annual_price - annual_price*40/100
basketball_kit = basketball_sneakers - basketball_sneakers*20/100
basketball = basketball_kit/4
basketball_accessories = basketball/5
total_price = annual_price + basketball_accessories + basketball + basketball_sneakers + basketball_kit
print(total_price)