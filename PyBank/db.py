# This is the file that connects the database!
# Let's import sqlite3
import sqlite3

# - Connection to the database
class Database(object):
    def __init__(self):
        conn = sqlite3.connect("database.db")
        self.conn = conn
        self.cursor = self.conn.cursor()
    def execute(self, instruction):
        # Execute the instruction passed
        self.cursor.execute(instruction)
    def close(self):
        # Close the database
        self.conn.close()