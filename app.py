import requests
from bs4 import BeautifulSoup
from pandas import pd

url ="https://books.toscrape.com/"
response=requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")


books = soup.find_all("article", class_="product_pod")

data =[]

for book in books[:10]:
    title = book.h3.a["title"]
    price = float(book.find("p", class_="price_color").text.replace("£", ""))

    data.append({
        "Title": title,
        "Price_GBP": price
    })
