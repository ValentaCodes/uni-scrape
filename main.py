# Week 1 checkpoint - Read a CSV file, parse and print each row
# Week 2 checkpoint - Fetch data from real webpage and pull data out of it
# Week 3 checkpoint - Clean data and store it in database

import csv
from scrape import scrape
from transform import transform
from load import load
"""
Enter uni name
scaper should gather program information 
Parse data
categorize and data and save as a CSV file
"""

def main():
    books = scrape()
    data_frame = transform(books)
    load(data_frame)


if __name__ == "__main__":
    main()
