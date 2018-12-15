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

c.execute("""
    INSERT INTO book 
    VALUES ('Inventing Japan', 10, '0812972864')
""")

c.execute("""
    INSERT INTO book 
    VALUES ('Origins of Political Order', 12, '0374533229')
""")

# can't run `fetch` methods twice in a row
# i.e. can't do `fetchone()` then `fetchall()`
# once records have been fetched, they're unavailable to be fetched again
c.execute("""SELECT * FROM book""")
print(c.fetchall())  # returns list of tuples

# save transaction
conn.commit()
conn.close()
