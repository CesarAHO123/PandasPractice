import pandas as pd
import json
from types import SimpleNamespace

data = pd.read_csv("CleanDB/top_movies_clean.csv")
data = data.head(100)


def get_genres(row):
    aux = []
    aux2 = str(row.genres)
    aux2 = aux2.replace('[', '')
    aux2 = aux2.replace(']', '')
    aux2 = aux2.replace('},', '}},')
    aux3 = aux2.split("},")
    for genre in aux3:
        x = json.loads(genre, object_hook=lambda d: SimpleNamespace(**d))
        aux.append(x.name)
    row.genres = aux
    return row


data = pd.read_csv("top_movies.csv")
data = data.drop(columns=["homepage", "production_countries",
                 "production_companies", "spoken_languages", "status", "original_title", "overview"])
data = data.dropna().set_index("id").sort_values("id")
data = data.loc[(data.budget > 10000) & (data.revenue > 100) &
                (data.genres != "[]") & (data.keywords != "[]")]
data = data.rename(columns={"vote_average": "score"})
data = data.apply(get_genres, axis="columns")
data.to_csv("./CleanDB/top_movies_clean.csv")
print(data)
