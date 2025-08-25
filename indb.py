from product import Movies
import json

def generate_movies():
    f = open ('./data/product.json')
    data = json.loads(f.read())
    f.close()
    return data