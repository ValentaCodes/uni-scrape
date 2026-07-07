import sqlite3 as sql

def load(df):
    conn = sql.connect("books.db")
    df.to_sql("books", conn, index=False, if_exists="replace")
    conn.commit()
    conn.close()
    print("Books saved to database!")