import bcrypt
import sqlite3


class RegisterModel:
    def __init__(self):
        self.connection = sqlite3.connect('Models/geeks.db')
        self.cur = self.connection.cursor()

    def insert_user(self, Username, FullName, Email, Password):
        hashed = bcrypt.hashpw(Password.encode(), bcrypt.gensalt())
        # hashed  = Password
        self.cur.execute('CREATE TABLE IF NOT EXISTS geeks(Username TEXT, FullName TEXT, Email TEXT, Password BLOB)')
        id = self.cur.execute("INSERT INTO geeks(Username, FullName, Email, Password) VALUES (?,?,?,?)",
                              (Username, FullName, Email, hashed))
        self.connection.commit()




