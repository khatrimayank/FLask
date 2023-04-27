import sqlite3

conn = sqlite3.connect("books.sqlite")

cursor = conn.cursor()

sql_query = """ CREATE TABLE if not exists book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""

cursor.execute('''DROP TABLE  book''')

cursor.execute(sql_query)
