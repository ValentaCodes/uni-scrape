import requests
from bs4 import BeautifulSoup
from datetime import datetime
def scrape():
    books = []
    r = requests.get("https://books.toscrape.com")
    soup = BeautifulSoup(r.content, "html.parser")

    products = soup.find_all("article", {"class": "product_pod"})
    for pod in products:
        titles = pod.find_all(title=True)
        prices = pod.find_all("p", {"class": "price_color"})
        price = prices.pop(0).text.strip('£').strip()
        title = titles.pop(0).attrs["title"].strip()
        books.append({"Title": title, "Price": float(price), "Scraped_Time": datetime.now().strftime("%m-%d-%y %H:%M:%S")})

    print("Scraping complete!")

    return books
