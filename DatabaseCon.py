import sqlite3


class DatabaseNew():
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS newUserDetails(account_no TEXT UNIQUE,name TEXT,contact TEXT,
        email TEXT, password NUMERIC,balance TEXT) """)
        self.con.commit()

    def insert(self, account, name, contact, email, password):
        self.cur.execute("insert into newUserDetails VALUES(?,?,?,?,?,0)", (account, name, contact, email, password))
        self.con.commit()

    def fetch(self, account, password):
        self.cur.execute("SELECT * from newUserDetails WHERE account_no = ? AND password =?", (account, password))
        rows = self.cur.fetchall()

        return rows

    def fetchonee(self, account, password):
        self.cur.execute("SELECT * from newUserDetails WHERE account_no = ? AND password =?", (account, password))
        rows = self.cur.fetchone()

        return rows

    def seleck(self):
        self.cur.execute("SELECT * FROM newUserDetails ")
        row = self.cur.fetchall()
        print(row)

    def updateData(self, balance, account):
        self.cur.execute("UPDATE newUserDetails SET balance=? WHERE account_no=?", (balance, account))
        self.con.commit()
