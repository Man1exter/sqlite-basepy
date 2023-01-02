import sqlite3

database = sqlite3.connect("client_base.db")
cursor = database.cursor()


database.commit()
database.close()