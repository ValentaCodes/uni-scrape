# Week 1 checkpoint - Read a CSV file, parse and print each row
# Week 2 checkpoint - Fetch data from real webpage and pull data out of it
# Week 3 checkpoint - Clean data and store it in database

import csv
import requests
import pandas as pd
import sqlite3 as sql

from bs4 import BeautifulSoup

"""
Enter uni name
scaper should gather program information 
Parse data
categorize and data and save as a CSV file
"""

def parse_csv(filename):
    """
    Opens a CSV file and prints each row as a dictionary.
    """
    try:
        with open(filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except PermissionError:
        print(f"Permission denied: {filename}")
    except OSError as e:
        print(f"Error opening file {filename}: {e}")

def scrape_site():
    books = []
    r = requests.get("https://books.toscrape.com")
    soup = BeautifulSoup(r.content, "html.parser")

    products = soup.find_all("article", {"class": "product_pod"})
    for pod in products:
        titles = pod.find_all(title=True)
        prices = pod.find_all("p", {"class": "price_color"})
        price = prices.pop(0).text.strip('£').strip()
        title = titles.pop(0).attrs["title"].strip()
        books.append({"Title": title, "Price": float(price)})

    df = pd.DataFrame(books, columns=["Title", "Price"])
    df.sort_values(by=["Price"], ascending=True, inplace=True)
    df.to_csv("scrapedBooks.csv", index=False)

    save_to_db(df)

def save_to_db(df):
    conn = sql.connect("scrapedBooks.db")
    df.to_sql("scrapedBooks", conn, index=False, if_exists="replace")
    res = conn.execute("Select * from scrapedBooks")
    print(res.fetchall())
    conn.close()

def main():
    scrape_site()

if __name__ == "__main__":
    main()
