import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    ratings = [movie["rating"] for movie in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest_age = max(ages)
    newest_age = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))
    return oldest_age, newest_age, avg_age


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо" if rating < 5 else "средне"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = title.split()
    return " ".join(word[0].upper() + word[1:] for word in words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    normalized = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{normalized}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography


def above_average_ratings(movies):
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg
    }


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration_above_rating(movies, threshold=7):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > threshold)


def main():
    print("Этап 1")
    print(f"  Средняя оценка: {average_rating(movies)}")
    print(
        f"  Возрастной диапазон (старый, новый, средний): {catalog_age_stats(movies)}"
    )
    print(f"  155 минут в часах: {duration_in_hours(155)}")

    print("\nЭтап 2")
    for movie in movies:
        tier = rating_tier(movie["rating"])
        decade = decade_label(movie["year"])
        print(
            f"  {movie['title']:<25} rating = {movie['rating']:<4} "
            f"- {tier:<9} year = {movie['year']} - {decade}"
        )

    print("\nЭтап 3")
    print("Фильмы не в жанре comedy:")
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(f"    - {movie['title']}")

    print("Первый фильм с рейтингом > 9.0:")
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(f"    Найден: {movies[index]['title']} ({movies[index]['rating']})")
            break
        index += 1
    else:
        print("    Шедевров не найдено")

    print(f"Фильмов длиннее 120 минут: {count_long_movies(movies)}")

    print("\nЭтап 4")
    print(f"  normalize_title('silent hours') - {normalize_title('silent hours')}")
    print(
        f"  normalize_title('midnight in oslo') - {normalize_title('midnight in oslo')}"
    )
    print(f"  make_slug('Silent Hours') - {make_slug('Silent Hours')}")
    print("  format_report_line для всего каталога:")
    for movie in movies:
        print(f"    {format_report_line(movie)}")

    print("\nЭтап 5")
    print("  Названия по убыванию рейтинга:")
    for title in titles_sorted_by_rating(movies):
        print(f"    - {title}")
    print(f"  Топ-3: {top_n_by_rating(movies, 3)}")

    print("\nЭтап 6")
    print(f"  count_by_genre: {count_by_genre(movies)}")
    print("  actor_filmography:")
    for actor, titles in actor_filmography(movies).items():
        print(f"    {actor}: {titles}")
    print(f"  above_average_ratings: {above_average_ratings(movies)}")

    print("\nЭтап 7")
    print(f"  all_genres: {all_genres(movies)}")
    print(
        f"  common_actors(movies[0], movies[3]): {common_actors(movies[0], movies[3])}"
    )
    print(
        f"  genres_only_in_one(movies[5:6], movies[:5]): "
        f"{genres_only_in_one(movies[5:6], movies[:5])}"
    )

    print("\nЭтап 8 — итераторы и генераторы")
    print("  Фильмы с рейтингом ≥ 8.0 (ленивый генератор):")
    for movie in iter_high_rated(movies):
        print(f"    {format_report_line(movie)}")
    print(
        f"  Суммарная длительность фильмов с рейтингом > 7: "
        f"{total_duration_above_rating(movies)} мин"
    )


if __name__ == "__main__":
    main()
