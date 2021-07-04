import sqlite3
connection = sqlite3.connect('tasks.db', check_same_thread=False)

cursor = connection.cursor()

cursor.execute(
    """ CREATE TABLE admins(
        adminid INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32),
        userid INTEGER NOT NULL,
        FOREIGN KEY(userid) REFERENCES users(pk)
    );"""
)
connection.commit()
cursor.close()
connection.close()
