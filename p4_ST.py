from unicodedata import category
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, shapiro
data = pd.read_csv(
    "CleanDB/top_movies_clean.csv").set_index("id").sort_values("score", 0, False)
data = data.loc[(data.budget > 10000) & (data.revenue > 10000)].head(1000)
stat, p = pearsonr(data.budget, data.revenue)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Las ganancias no suelen depender del presupuesto.')
else:
    print('Las ganancias suelen depender del presupuesto.')

stat, p = shapiro(data.score)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Las puntuaciones tienen una distribucion normal.')
else:
    print('Las puntuaciones no tienen una distribucion normal.')
data_aux = data.groupby(by=['score'])['score'].count()
data_aux.plot()
plt.title(
    "Puntuaciones mas comunes")
plt.xlabel("Puntuacion")
plt.ylabel("Cantidad")
plt.savefig("img/p4_scores.png")
plt.show()
plt.close()
print(data_aux)
