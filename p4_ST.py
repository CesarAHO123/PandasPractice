from unicodedata import category
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("top_movies.csv").head(10)
data3 = data.plot(x='budget',
                  y='revenue', kind='scatter')
print(data[data.budget > 250000000])

# plt.show()
