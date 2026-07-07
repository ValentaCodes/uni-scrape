import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape(url):
    """Scrapes books from website"""
    books = []
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")
    products = soup.find_all("article", {"class": "product_pod"})

    for pod in products:
        titles = pod.find_all(title=True)
        prices = pod.find_all("p", {"class": "price_color"})
        price = prices.pop(0).text.strip('£').strip()
        title = titles.pop(0).attrs["title"].strip()
        books.append(
            {"Title": title, "Price": float(price), "Scraped_Time": datetime.now().strftime("%m-%d-%y %H:%M:%S")})

    return books
