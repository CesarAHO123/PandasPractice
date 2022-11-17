import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import pandas_datareader.data as web
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
data = pd.read_csv("CleanDB/top_movies_clean.csv")
data.release_date = pd.to_datetime(data['release_date'], format='%Y-%m-%d')
data = data.loc[(data.release_date > pd.to_datetime(
    "1990-01-01", format='%Y-%m-%d'))]
data = data.sort_values("release_date")
data.index = pd.to_datetime(data['release_date'], format='%Y-%m-%d')
train = data[data.index < pd.to_datetime("2014-01-01", format='%Y-%m-%d')]
test = data[data.index > pd.to_datetime("2014-01-01", format='%Y-%m-%d')]
#plt.plot(data.index, data['budget'])
plt.plot(train.index, train["budget"], color="black", label='Entrenamiento')
plt.plot(test.index, test["budget"], color="red", label='Pruebas')
sns.set()

y = train['budget']
ARIMAmodel = ARIMA(y, order=(2, 2, 2))
ARIMAmodel = ARIMAmodel.fit()
y_pred = ARIMAmodel.get_forecast(len(test.index))
y_pred_df = y_pred.conf_int(alpha=0.05)
y_pred_df["Predictions"] = ARIMAmodel.predict(
    start=y_pred_df.index[0], end=y_pred_df.index[-1])
y_pred_df.index = test.index
y_pred_out = y_pred_df["Predictions"]
plt.plot(y_pred_out, color='Yellow', label='Predicciones')
#ARMAmodel = SARIMAX(y, order=(1, 0, 1))
#ARMAmodel = ARMAmodel.fit()
#y_pred = ARMAmodel.get_forecast(len(test.index))
#y_pred_df = y_pred.conf_int(alpha=0.05)
# y_pred_df["Predicciones"] = ARMAmodel.predict(
#    start=y_pred_df.index[0], end=y_pred_df.index[-1])
#y_pred_df.index = test.index
#y_pred_out = y_pred_df["Predicciones"]
#plt.plot(y_pred_out, color='green', label='Predicciones')
plt.legend()
plt.title('Presupuesto dado a las peliculas con los años')
plt.xlabel('Fecha de lanzamiento')
plt.ylabel('Presupuesto')
plt.xticks(rotation=45)
plt.savefig("img/p6_Forecasting.png")
plt.show()
plt.close()
