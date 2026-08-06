import pandas as pd


def transform(row_of_books):
    """Transforms books into dataframe and creates a CSV file"""
    df = pd.DataFrame(row_of_books)
    df.to_csv('books.csv', index_label='Book ID')
    return df
