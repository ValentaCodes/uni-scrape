# Week 1 checkpoint - Read a CSV file, parse and print each row
# Week 2 checkpoint - Fetch data from real webpage and pull data out of it
# Week 3 checkpoint - Clean data and store it in database

from transform import transform
from driver import driver
"""
Enter uni name
scaper should gather program information 
Parse data
categorize and data and save as a CSV file
"""

def main():
    url = "https://books.toscrape.com/"

    books = driver(url)
    transform(books)
    # load(data_frame)


if __name__ == "__main__":
    main()
