from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrape import scrape


def driver(url):
    """Navigates to next page"""
    books = []
    options = Options()
    d = webdriver.Chrome(options=options)
    d.get(url)

    while True:
        books.append(scrape(d.current_url))

        if d.current_url == "https://books.toscrape.com/catalogue/page-50.html":
            break

        next_li = d.find_element(By.CLASS_NAME, "next")
        next_link = next_li.find_element(By.TAG_NAME, "a")
        next_link.click()

    d.quit()
    return books
