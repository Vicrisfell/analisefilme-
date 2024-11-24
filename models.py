from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# Conexão ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movielens"]

# Carregar dados
movies = pd.DataFrame(list(db["movies"].find()))
ratings = pd.DataFrame(list(db["ratings"].find()))

# Preparar dados
data = ratings.merge(movies, left_on="movieId", right_on="movieId", how="inner")
data["genres"] = data["genres"].str.split("|")
data = data.explode("genres")
data = pd.get_dummies(data, columns=["genres"], prefix="genre")

X = data.drop(columns=["rating", "_id", "title", "movieId", "userId", "timestamp"])
y = data["rating"]

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelos

## Árvore de Decisão
def decision_tree_model():
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Acurácia Árvore de Decisão:", accuracy_score(y_test, y_pred))

## Naive Bayes
def naive_bayes_model():
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    y_pred = nb.predict(X_test)
    print("Acurácia Naive Bayes:", accuracy_score(y_test, y_pred))

## Rede Neural
def neural_network_model():
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(1, activation="linear")
    ])
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.fit(X_train_scaled, y_train, epochs=10, batch_size=32)
    mse, mae = model.evaluate(X_test_scaled, y_test)
    print("MSE Rede Neural:", mse)

# Executar modelos
decision_tree_model()
naive_bayes_model()
neural_network_model()
