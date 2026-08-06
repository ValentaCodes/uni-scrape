from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrape import scrape


# TODO: ADD ERROR Handling
# TODO: WRITE TESTS

def driver(url):
    """Navigates to next page"""
    books = {}
    # data = []
    options = Options()
    d = webdriver.Chrome(options=options)
    d.get(url)
    i = 1
    while True:
        page_scraped_data = scrape(d.current_url)  #Scrapes data from current page and stores it in this var as a list
        books[f"Page {i}"] = page_scraped_data
        i = i + 1  #increment page key
        if d.current_url == f"https://books.toscrape.com/catalogue/page-10.html":  #break when we reach the 50th page
            break
        next_li = d.find_element(By.CLASS_NAME, "next")
        next_btn = next_li.find_element(By.TAG_NAME, "a")
        next_btn.click()
    d.quit()  #quit driver object
    return books


def flatten_books(page):
    """Flattens books into list. Prepares list for SQL entry as rows"""
    all_books = []
    for page_name, book in page.items():
        all_books.extend(book)
    return all_books
