import pandas as pd
from pymongo import MongoClient

# Conexão ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movielens"]

# Carregar arquivos CSV
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Inserir dados no MongoDB
movies_collection = db["movies"]
ratings_collection = db["ratings"]

movies_collection.insert_many(movies.to_dict("records"))
ratings_collection.insert_many(ratings.to_dict("records"))

print("Dados carregados no MongoDB com sucesso!")
