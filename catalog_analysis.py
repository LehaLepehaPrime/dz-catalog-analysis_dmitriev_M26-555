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


if __name__ == "__main__":
    main()
