import pandas as pd

def transform(books):
    df = pd.DataFrame(books, columns=["Title", "Price", "Scraped_Time"])
    df.sort_values(by=["Price"], ascending=True, inplace=True)
    df.to_csv("books.csv", index=False)

    return df

