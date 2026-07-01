# Books ETL Pipeline

A Python ETL pipeline that scrapes book data from [books.toscrape.com](https://books.toscrape.com), cleans it with pandas, and stores it in both CSV and SQLite formats.

Built as a portfolio project for data governance and analytics engineering roles.

## What It Does

1. **Extract** — Fetches the books.toscrape.com homepage and parses the first page listings
2. **Transform** — Pulls title and price from each listing, casts price to float, sorts by price ascending using pandas
3. **Load** — Writes the cleaned data to `books.csv` and a `books` table in `books.db`

## Stack

- `requests` — HTTP fetching
- `beautifulsoup4` — HTML parsing
- `pandas` — data cleaning and transformation
- `sqlite3` — local database storage (built into Python)

## Setup

```bash
pip install requests beautifulsoup4 pandas
```

## Run

```bash
python main.py
```

Outputs:
- `books.csv` — flat file export
- `books.db` — SQLite database with a `books` table

## Project Structure

```
web-scraping-project/
├── data_dictionary.md
├── main.py
├── README.md
├── load.py
├── scrape.py
├── transform.py
├── scrape.py
├── scrapedBooks.csv  # CSV output
└── scrapedBooks.db   # SQLite output
```

## Data Dictionary

| Column | Type    | Source                        | Notes                          |
|--------|---------|-------------------------------|--------------------------------|
| Title  | string  | `<article>` title attribute   | Full book title, whitespace stripped |
| Price  | float   | `.price_color` paragraph text | GBP value, £ symbol removed    |
|Scraped Time | datetime | system settings | format: "mm-dd-yy hh-mm-ss"|
