# This is the file that connects the database!
# Let's import sqlite3
import sqlite3

# - Connection to the database
class Database(object):
    def __init__(self):
        conn = sqlite3.connect("database.db")
        self.conn = conn
        self.cursor = self.conn.cursor()
        # Make sure that the database is created!
        self.create_database()
    def create_database(self):
        # Creating the Database
        self.cursor.execute('''CREATE TABLE 
IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    money INTEGER,
    topay INTEGER
);
        ''')
    def execute(self, instruction):
        # Execute the instruction passed
        self.cursor.execute(instruction)
    def close(self):
        # Close the database
        self.conn.close()