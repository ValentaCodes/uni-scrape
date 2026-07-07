import pandas as pd

def transform(books):
    df = pd.DataFrame(books)
    df.to_csv("books.csv", index=False)
    return df