import sys

num_of_movies = int(input())

low_rating_movie_name = ''
low_rating = sys.maxsize
high_rating_movie_name = ''
max_rating = -sys.maxsize

sum_of_ratings = 0
for count in range(num_of_movies):
    name_of_movie = input()
    curr_movie_rating = float(input())

    sum_of_ratings += curr_movie_rating

    if curr_movie_rating > max_rating:
        max_rating = curr_movie_rating
        high_rating_movie_name = name_of_movie
    if curr_movie_rating < low_rating:
        low_rating = curr_movie_rating
        low_rating_movie_name = name_of_movie
avg_rating = sum_of_ratings / num_of_movies

print(f"{high_rating_movie_name} is with highest rating {max_rating}")
print(f"{low_rating_movie_name} is with lowest rating {low_rating}")
print(f"Average rating: {avg_rating:.1f}")