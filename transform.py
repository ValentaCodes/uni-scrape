import pandas as pd

def transform(books):
    """Transforms books into dataframe and creates a CSV file"""
    df = pd.DataFrame(books)
    df.to_csv('books.csv')
    return df