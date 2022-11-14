import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
data = pd.read_csv(
    "CleanDB/top_movies_clean.csv").set_index("id")
text = " ".join(key for key in data.keywords)
text = text.replace("[", "")
text = text.replace("'", "")
text = text.replace("]", "")
text = text.replace(",", "")
wc_test = WordCloud(max_words=100,
                    background_color="white").generate(text)
plt.imshow(wc_test, interpolation="bilinear")
plt.axis('off')
plt.title("Descriptores mas usados en las peliculas")
plt.savefig("img/p9_textanalysis")
plt.show()
