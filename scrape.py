import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape(url):
    """Scrapes books from website"""
    data = [] # starting storage for data
    r = requests.get(url) # creates request to get given url

    soup = BeautifulSoup(r.content, "html.parser") #instantiate soup object
    products = soup.find_all("article", {"class": "product_pod"}) #create product soup

    # iterate through all found products and create item data, appends to data list
    for item in products:
        titles = item.find_all(title=True)
        prices = item.find_all("p", {"class": "price_color"})
        price = prices.pop(0).text.strip('£').strip()
        title = titles.pop(0).attrs["title"].strip()
        data.append(
            {"Title": title, "Price": float(price), "Scraped_Time": datetime.now().strftime("%m-%d-%y %H:%M:%S")})
    return data
