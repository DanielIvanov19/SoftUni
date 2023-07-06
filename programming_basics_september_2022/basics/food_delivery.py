chicken_menu = 10.35
fish_menu = 12.4
vegetarian_menu = 8.15
delivery = 2.5
chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())
menus_total = chicken_menus * chicken_menu + fish_menus * fish_menu + vegetarian_menus * vegetarian_menu
dessert_price = menus_total*20/100
total_price = menus_total + dessert_price + delivery
print(total_price)