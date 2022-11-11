import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(
    "CleanDB/top_movies_clean.csv").set_index("id").sort_values("score", 0, False)
data1 = data.head(100)
data2 = data.tail(100)
plt.scatter(data1.budget, data1.revenue, color='blue', label='100 mejores')
plt.scatter(data2.budget, data2.revenue, color='red', label='100 peores')
plt.legend()
plt.title(
    "Relacion de la ganancia con respecto al presupuesto")
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.savefig("img/p3_scatter.png")
plt.show()
plt.close()
