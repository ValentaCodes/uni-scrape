from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrape import scrape
# TODO: ADD ERROR Handling
# TODO: WRITE TESTS

def driver(url):
    """Navigates to next page"""
    data = {}
    options = Options()
    d = webdriver.Chrome(options=options)
    d.get(url)
    i = 1
    while True:
        dirty_data = scrape(d.current_url)
        data[f"Page {i}"] = dirty_data
        i = i + 1
        if d.current_url == f"https://books.toscrape.com/catalogue/page-50.html":
            break
        next_li = d.find_element(By.CLASS_NAME, "next")
        next_btn = next_li.find_element(By.TAG_NAME, "a")
        next_btn.click()

    d.quit()
    return data


def flatten_books(page):
    """Flattens books into list. Prepares list for SQL entry"""
    all_books = []
    for page_name, books in page.items():
        all_books.extend(books)
    return all_books
