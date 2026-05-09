import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
df = pd.read_csv("quotes.csv")

#bar chart 
top_authors = df["Author"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_authors.plot(kind="bar")
plt.title("Top 10 Authors")
plt.xlabel("Authors")
plt.ylabel("No of Quotes")
plt.show()

#pie chart
df["Author"].value_counts().head(5).plot(kind="pie",autopct="%1.1f%%")
plt.title("Top 5 Authors")
plt.ylabel("")
plt.show()

#seaborn countplot
plt.figure(figsize=(10,5))
sns.countplot(y="Author",data=df,order=df["Author"].value_counts().iloc[:10].index)
plt.title("Most Frequent Authors")
plt.show()