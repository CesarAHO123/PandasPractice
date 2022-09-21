import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("top_movies.csv").head(500)
data3 = data.plot(x='budget',
                  y='revenue', kind='scatter')
plt.show()
