# Week 1 checkpoint - Read a CSV file, parse and print each row
# Week 2 checkpoint - Fetch data from real webpage and pull data out of it
# Week 3 checkpoint - Clean data and store it in database

import csv
import requests
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
    r = requests.get("https://books.toscrape.com")
    soup = BeautifulSoup(r.content, "html.parser")

    products = soup.find_all("article", {"class": "product_pod"})
    for pod in products:
        titles = pod.find_all(title=True)
        prices = pod.find_all("p", {"class": "price_color"})
        for title in titles:
            print(title.text)
            for price in prices:
                print(price.text)
def main():
    scrape_site()

    # file_path = input("Enter file location: ").strip()
    # if not file_path:
    #     print("No file path provided.")
    #     return
    # parse_csv(file_path)

if __name__ == "__main__":
    main()
