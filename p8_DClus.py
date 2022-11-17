import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import numpy as np
from functools import reduce
from sklearn.cluster import KMeans

data = pd.read_csv("CleanDB/top_movies_clean.csv")
data = pd.DataFrame(data, columns=['score', 'popularity'])
kmeans = KMeans(n_clusters=3).fit(data)
centroids = kmeans.cluster_centers_
print(centroids)
plt.scatter(data['score'], data['popularity'],
            c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.title("Puntuacion de las peliculas mas populares")
plt.ylabel("Popularidad")
plt.xlabel("Puntuacion")

plt.savefig("img/p8_clustering")
plt.show()
plt.close()
