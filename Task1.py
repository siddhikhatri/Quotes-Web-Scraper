# requests are used to open a website and get the data from websites
import requests

# pandas stores and organizes data
import pandas as pd

# BeautifulSoup is used to read and understand HTML
from bs4 import BeautifulSoup

# create empty list
quotes_list = []

# pagination loop
for page in range(1, 11):

    # dynamic URL
    url = f"http://quotes.toscrape.com/page/{page}/"

    print("Scraping Page:", page)

    # download website HTML
    getData = requests.get(url)

    # convert HTML into readable format
    soup = BeautifulSoup(getData.text, "html.parser")

    # extract complete quote blocks
    quotes = soup.find_all("div", class_="quote")

    # loop through each quote block
    for q in quotes:

        # extract quote text
        quote_text = q.find("span", class_="text").text.strip()

        # extract author name
        author_name = q.find("small", class_="author").text.strip()

        # extract tags
        tag_name = q.find("meta", class_="keywords")["content"]

        # print output
        print(quote_text)
        print("Author:", author_name)
        print("Tags:", tag_name)
        print()

        # store data
        quotes_list.append({
            "Quote": quote_text,
            "Author": author_name,
            "Tags": tag_name,
            "Page": page
        })

# create dataframe
df = pd.DataFrame(quotes_list)

# save csv properly
df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")

print("Dataset created successfully")