# Import sqlite3 module
import sqlite3
try:
    # Create the database
    create = sqlite3.connect('example.db')
    print("\nDatabase created and connected to SQLite.")

    table = create.cursor()

    # Create table
    table.execute('''CREATE TABLE stocks
                   (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    table.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Create a query to request for version
    print(sqlite3.version)

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if create:
        create.close()
        print("\nThe SQLite connection is closed.")
    # Close Just be sure any changes have been committed or they will be lost.

