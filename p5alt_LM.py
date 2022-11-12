from unicodedata import category
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm
data = pd.read_csv(
    "CleanDB/top_movies_clean.csv").set_index("id").sort_values("score", 0, False)
data = data.loc[(data.budget > 10000) & (data.revenue > 10000)].head(1000)
dt = data.loc[:, ['score', 'vote_count']]
data_aux = ols('score ~ vote_count', data=dt).fit()
table = sm.stats.anova_lm(data_aux, typ=2)
if table["PR(>F)"][0] < 0.005:
    print("hay diferencias")
else:
    print("No hay diferencias")
print(table)
