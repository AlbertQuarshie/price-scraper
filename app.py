import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://books.toscrape.com/"
response=requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")


books = soup.find_all("article", class_="product_pod")

data =[]

for book in books[:10]:
    title = book.h3.a["title"]
    price = float(book.find("p", class_="price_color").text.replace("Â£", ""))

    data.append({
        "Title": title,
        "Price_GBP": price
    })

rate_api = "https://api.exchangerate-api.com/v4/latest/GBP"
rate = requests.get(rate_api).json()["rates"]["KES"]

for item in data:
    item["Price_KES"] = round(item["Price_GBP"] * rate, 2)

df = pd.DataFrame(data)

print(df)

df.to_csv("books.csv", index=False)