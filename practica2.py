import pandas as pd
data = pd.read_csv("CleanDB/top_movies_clean.csv")
data = data.sort_values("score", 0, False)
data = data.head(100)
AvBudget = data.budget.mean()
DesvBudget = data.budget.std()
MaxBudget = data.budget.max()
MaxMovie = data[data.budget == MaxBudget].title
AvScore = data.score.mean()
DesvScore = data.score.std()
print("El presupuesto promedio de las  mejores 100 peliculas es: " + str(int(AvBudget)))
print("Con una desviacion estandar de: " + str(DesvBudget))
print("La pelicula con mayor presupuesto de estas es: " +
      str(MaxMovie.iloc[0]) + " con " + str(MaxBudget))
print("La puntuacion promedio de las peliculas es: " + str(AvScore))
print("Con una desviacion estandar de: " + str(DesvScore))
