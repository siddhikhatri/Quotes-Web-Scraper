import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("quotes.csv")

# sentiment function
def get_sentiment(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    else:
        return "Neutral"

# apply sentiment analysis
df["Sentiment"] = df["Quote"].apply(get_sentiment)

# show results
print(df[["Quote", "Sentiment"]].head(10))

# count sentiments
print(df["Sentiment"].value_counts())

# visualization
df["Sentiment"].value_counts().plot(kind="bar")

plt.title("Sentiment Analysis Results")
plt.xlabel("Sentiment")
plt.ylabel("Count")
df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")
plt.show()