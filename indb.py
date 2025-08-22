from product import Movies

def generate_movies():
    list_movies = []

    for i in range(10):
        m = Movies(title = f"Filme {i + 1}", year = 1990 + i)
        list_movies.append(m)

    return list_movies