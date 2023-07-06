countries = input().split(", ")
capitals = input().split(", ")

capitals_of_countries = {countries[idx]: capitals[idx] for idx in range(len(capitals))}

for country, capital in capitals_of_countries.items():
    print(f"{country} -> {capital}")