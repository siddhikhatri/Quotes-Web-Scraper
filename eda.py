import matplotlib.pyplot as plt
import pandas as pd

#load dataset
df = pd.read_csv("quotes.csv")

#read first 5 rows
print(df.head())


#data structure shape,info,columns

#dataset information
print(df.info())

#shape of dataset
print("Database Shape : ",df.shape)

#column names
print("Columns : ",df.columns)

#check duplicate rows
print("Duplicate Rows : ",df.duplicated().sum())

#total quotes
print("Total Quotes : ",len(df))

#unique authors 
print("Unique Authors : ",df["Author"].unique())

#top authors
print("\n Top Authors : ")
print(df["Author"].value_counts().head(10))

#visualization
df["Author"].value_counts().head(10).plot(kind="bar")

plt.xlabel("Authors")
plt.ylabel("No Of Quotes")
plt.title("Top 10 Authors")
plt.show()