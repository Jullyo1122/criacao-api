from fastapi import FastAPI
from json_db import JsonDB
from product import Movies

app = FastAPI()

productDB = JsonDB(path='./data/product.json')
@app.get("/")
def get_movies():
    filmes = productDB.read()
    return { "Filmes" : filmes }
@app.post("/")
def create_movies(product: Movies):

    productDB.insert(product)

    return { "Status" : "Inserted" }

