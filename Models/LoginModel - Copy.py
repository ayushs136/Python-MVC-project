import sqlite3
import bcrypt


class LoginModel:
    def __init__(self):
        self.connection = sqlite3.connect('Models/geeks.db')
        self.cur = self.connection.cursor()

    def check_user(self, Username, Password, data):
        user = self.cur.execute("SELECT * FROM geeks WHERE Username=?", (Username,))
        if Username:
            hashed = self.cur.fetchone()[3]
            if user:
                if bcrypt.checkpw(Password.encode(), hashed):
                    return user
            else:
                return "error"
        else:
            return "error"
