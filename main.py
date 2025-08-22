from fastapi import FastAPI

from indb import generate_movies

app = FastAPI()

filmes = generate_movies()
@app.get("/")
def get_movies():
    return { "Filmes" : filmes }
