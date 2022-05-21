import sqlite3

DATABASE_NAME = "db_tekkom_0441.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn