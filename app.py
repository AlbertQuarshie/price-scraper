import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from tabulate import tabulate

#User inputs currency code (In Caps)
currency = input("Enter currency (e.g. KES, USD, EUR): ").upper()


# Source Website
url ="https://books.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error accessing website:", e)
    exit()

soup = BeautifulSoup(response.text,"html.parser")


books = soup.find_all("article", class_="product_pod")

data =[]

# 10 books are scrapped
for book in books[:10]:
    try:
        title = book.h3.a["title"]
        price = float(book.find("p", class_="price_color").text.replace("Â£", ""))

        data.append({
            "Title": title,
            "Price_GBP": price
    })
    
    except Exception as e:
        print("Error reading product")

# Initialization of exchange rate api to load in GBP as normal
try:
    rate_api = "https://api.exchangerate-api.com/v4/latest/GBP"
    rate_response = requests.get(rate_api)
    rate_response.raise_for_status()

    rate = rate_response.json()["rates"][currency]

except KeyError:
    print("Invalid currency code.")
    exit()

except requests.exceptions.RequestException as e:
    print("Error accessing currency API:", e)
    exit()
#Timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for item in data:
    item["Price_{currency}"] = round(item["Price_GBP"] * rate, 2)
    item["Timestamp"]= timestamp

df = pd.DataFrame(data)

#Tabulating data in the terminal
print(tabulate(df, headers="keys", tablefmt="grid"))

#Converting output to csv file
df.to_csv("books.csv", index=False)

#Confirmation message
print("\nData saved to books.csv")