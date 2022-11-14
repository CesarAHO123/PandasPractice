from unicodedata import category
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm
data = pd.read_csv(
    "CleanDB/top_movies_clean.csv")
#data = data.loc[(data.budget > 10000) & (data.revenue > 10000)]
data_test = data.groupby(['genre', 'score'])[
    'budget'].aggregate(pd.DataFrame.sum)
data_test = data_test.to_frame()
data_test.reset_index(inplace=True)
data_test.set_index("score", inplace=True)
data_test.reset_index(inplace=True)
data_test = data_test.drop(['score'], axis=1)
data_aux = ols("budget ~ genre", data=data_test).fit()
print(data_test)
table = sm.stats.anova_lm(data_aux, typ=2)
if table["PR(>F)"][0] < 0.005:
    print("Hay diferencia en el dinero dado a cada genero")
else:
    print("No hay diferencias en el dinero dado a cada genero")
print(table)
