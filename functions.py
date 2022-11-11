import json
from types import SimpleNamespace
import pandas as pd
data = pd.read_csv("CleanDB/top_movies_clean.csv")
data = data.head(100)
test = data.iloc[0]
test = str(test.genres)
test = test.replace('[', '')
test = test.replace(']', '')
test = test.replace('},', '}},')
abc = test.split("},")
aux = []

for i in abc:
    x = json.loads(i, object_hook=lambda d: SimpleNamespace(**d))
    aux.append(x.name)
print(aux)
