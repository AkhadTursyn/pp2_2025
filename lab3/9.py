movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]


def is_above_5_5(movie):
    return movie['imdb'] > 5.5


def movies_above_5_5(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]


def movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]


def average_imdb(movies):
    return sum(movie['imdb'] for movie in movies) / len(movies)


def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    if category_movies:
        return average_imdb(category_movies)
    return 0



print("Is 'Usual Suspects' IMDB score above 5.5?", is_above_5_5(movies[0]))


print("\nMovies with IMDB score above 5.5:")
for movie in movies_above_5_5(movies):
    print(movie['name'])


category = "Romance"
print("\nMovies in category '" + category + "':")
for movie in movies_by_category(movies, category):
    print(movie['name'])

print("\nAverage IMDB score of all movies:", round(average_imdb(movies), 2))


category = "Romance"
print("\nAverage IMDB score of movies in category '" + category + "':", round(average_imdb_by_category(movies, category), 2))