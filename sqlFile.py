import sqlite3

# connection created
conn = sqlite3.connect('lite.db')

# cursor created
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER, price REAL)")

# inserting the data
cur.execute("INSERT INTO store VALUES('books', 100, 110.5)")
# cur.execute("DELETE FROM store where item = 'books'")

# changes made here will be submitted to the database by 
conn.commit()

# close the connection
conn.close()
