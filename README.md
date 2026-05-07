# Price Scraper

## A. Contributor

- **Albert Junior Quarshie**

---

# B. Overview

- Price Scraper + Currency Converter is a simple Python application that scrapes product data from an e-commerce practice website and converts the product prices into another currency.

- The project uses web scraping techniques with BeautifulSoup and requests to collect product information, then integrates a free exchange rate API to perform currency conversion.

- The scraped and converted data is displayed in a table format using pandas and saved into a CSV file for future use.

---

# C. Installation

- Follow these steps to set up and run the project locally:

## 1. Clone the Repository

```bash
git clone https://github.com/AlbertQuarshie/price-scraper.git
cd price-scraper
```

## 2. Install Dependencies

- The project requires Python 3 or later.

```bash
pip install requests beautifulsoup4 pandas
```

## 3. Run the Application

```bash
python app.py
```

---

# D. Usage

## 1. Launch the Application

- Run the Python file from the terminal.

## 2. Scrape Product Data

- The application scrapes at least 10 book products from:

```text
https://books.toscrape.com/
```

## 3. Convert Prices

- Product prices in GBP are automatically converted into another currency (e.g., KES).

## 4. View Results

- The converted product data is:
  - Displayed in the terminal
  - Saved into a CSV file named:

```text
books.csv
```

---

# E. Features

## 1. Web Scraping

- Extracts product titles and prices from an online store using BeautifulSoup.

## 2. Currency Conversion

- Converts product prices using a free exchange rate API.

## 3. Data Storage

- Saves scraped and converted data into a CSV file using pandas.

## 4. Simple Table Display

- Displays product information in a readable tabular format.

## 5. Lightweight and Beginner Friendly

- Simple project structure with easy-to-understand Python code.

---

# F. Tech Stack

- **Programming Language:** Python 3
- **Web Scraping:** BeautifulSoup, requests
- **Data Handling:** pandas
- **Currency API:** ExchangeRate-API
- **Execution Environment:** Console / Terminal
