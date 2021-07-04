import sqlite3
connection = sqlite3.connect('tasks.db', check_same_thread=False)

cursor = connection.cursor()

cursor.execute(
    """ CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32)
    );"""
)

cursor.execute(
    """ CREATE TABLE tasks(
        taskid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        taskname VARCHAR(50) NOT NULL,
        taskstartdate INTEGER NOT NULL,
        taskduedate INTEGER DEFAULT "0" NOT NULL,
        userid INTEGER NOT NULL,
        FOREIGN KEY(userid) REFERENCES users(pk)
    );"""
)


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
