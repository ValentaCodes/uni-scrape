from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrape import scrape


def driver(url):
    """Navigates to next page"""
    page = {}
    options = Options()
    d = webdriver.Chrome(options=options)
    d.get(url)
    i = 1
    while True:
        page[f"Page {i}"] = scrape(d.current_url)
        i = i + 1
        if d.current_url == f"https://books.toscrape.com/catalogue/page-50.html":
            break
        next_li = d.find_element(By.CLASS_NAME, "next")
        next_link = next_li.find_element(By.TAG_NAME, "a")
        next_link.click()

    d.quit()
    return page
