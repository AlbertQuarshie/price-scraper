import requests
from bs4 import BeautifulSoup
from pandas import pd

url ="https://books.toscrape.com/"
response=requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
