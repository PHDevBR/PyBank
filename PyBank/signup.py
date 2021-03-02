# Import our Database
from dbfile import Database

class SignUp(object):
    def __init__(self):
        # Connect with database
        self.db = Database()
    def create_user(self, name, email, password):
        # SignUp new Users!
        self.name = name
        self.email = email
        self.password = password 
    def check_if_exists(self):
        self.db.execute("SELECT name FROM users;")
        for line in self.db.cursor.fetchall():
            if self.name == line:
                return False
            else:
                return True
