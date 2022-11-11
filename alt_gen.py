import pandas as pd
import json
from types import SimpleNamespace
import ast


def get_genre(row):
    row.genres = ast.literal_eval(row.genres)[0]
    return row


data = pd.read_csv("CleanDB/top_movies_clean.csv")
data = data.set_index("id").sort_values("id")
data = data.apply(get_genre, axis="columns")
data.to_csv("./CleanDB/top_movies_clean_alt.csv")
print(data)
