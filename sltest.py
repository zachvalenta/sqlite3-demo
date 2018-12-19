# based on DB-API (PEP 249)
import sqlite3

# connnect (and create `.db` file if it doesn't already exist)
conn = sqlite3.connect('test.db')

# this allows us to run SQL
c = conn.cursor()

# docstrings are a thing using sqlite3
c.execute(""" 
    CREATE TABLE book 
    (name text, price int, isbn text)
""")

# let's pretend this is user input we need to save
books = [
    {
        'name': 'Origins of Political Order',
        'price': 10.00,
        'isbn': '0374533229',
    },
    {
        'name': 'Political Order and Political Decay',
        'price': 10.00,
        'isbn': '0374535620',
    }
]

# use question marks to validate input
c.execute("""
    INSERT INTO book 
    VALUES (?, ?, ?)
""", (books[0]['name'], books[0]['price'], books[0]['isbn']))

c.execute("""
    INSERT INTO book 
    VALUES (?, ?, ?)
""", (books[0]['name'], books[0]['price'], books[0]['isbn']))

# can't run `fetch` methods twice in a row
# i.e. can't do `fetchone()` then `fetchall()`
# once records have been fetched, they're unavailable to be fetched again
c.execute("""SELECT * FROM book""")
print(c.fetchall())  # returns list of tuples

# save transaction
conn.commit()
conn.close()
