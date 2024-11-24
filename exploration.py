import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns

# Conexão ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movielens"]

# Carregar dados
movies = pd.DataFrame(list(db["movies"].find()))
ratings = pd.DataFrame(list(db["ratings"].find()))

# Análise básica
print("Resumo dos Ratings:")
print(ratings.describe())

# Distribuição dos ratings
sns.histplot(ratings["rating"], bins=10, kde=True)
plt.title("Distribuição de Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequência")
plt.show()

# Popularidade de gêneros
movies["genres"] = movies["genres"].str.split("|")
genres_exploded = movies.explode("genres")
top_genres = genres_exploded["genres"].value_counts()

plt.figure(figsize=(10, 5))
sns.barplot(x=top_genres.index, y=top_genres.values)
plt.title("Gêneros mais Populares")
plt.xlabel("Gêneros")
plt.ylabel("Número de Filmes")
plt.xticks(rotation=45)
plt.show()
