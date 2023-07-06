import random

footballer = ["Lionel Messi", "Karim Benzema", "Olivier Giroud", "Erling Haaland", "Leroy Sane", "Raheem Sterling",
              "Harry Kane", "Victor Osimhen", "Mohammed Salah", "Romelu Lukaku", "Timo Werner"]
performance = ["scored a goal", "scored a brace", "scored a hat trick"]
stadium = ["home", "away"]
tournament = ["Champions League", "domestic league"]
additional_info = ["made 15 successful dribbles", "assisted once", "created 4 big chances for his team"]
rating = ["8.9", "8.1", "9.3", "8.7", "8.5"]

end_of_news = '"enough"'


def get_random_phrase(phrases):
    return random.choice(phrases)


print("Hello, this is the first info of today's sports news:")
command = input("Press [Enter] to continue.")
while command != "enough":
    print()
    rand_footballer = get_random_phrase(footballer)
    rand_performance = get_random_phrase(performance)
    rand_stadium = get_random_phrase(stadium)
    rand_tournament = get_random_phrase(tournament)
    rand_info = get_random_phrase(additional_info)
    rand_rating = get_random_phrase(rating)

    print(f"{rand_footballer} {rand_performance} in his {rand_stadium} game in the {rand_tournament}.\n"
          f"He also {rand_info}. His rating was {rand_rating}.")
    print()
    command = input(f"Press [Enter] for another sports performance / Type {end_of_news} to end the news session: ")

