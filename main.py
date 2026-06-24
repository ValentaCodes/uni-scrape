# Week 1 checkpoint - Read a CSV file, parse and print each row
# Week 2 checkpoint - Fetch data from real webpage and pull data out of it

import csv
from bs4 import BeautifulSoup

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

def scrape_site(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    print(soup.prettify())

def main():
    file_path = input("Enter file location: ").strip()
    if not file_path:
        print("No file path provided.")
        return
    parse_csv(file_path)

if __name__ == "__main__":
    main()
