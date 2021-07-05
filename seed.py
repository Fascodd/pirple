import sqlite3
db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
db_cursor = db_connection.cursor()
db_cursor.execute(

    """ SELECT taskid 
    FROM tasks 
    WHERE "data" >= date('now', '-1 days') AND  datetime(1092941466, 'unixepoch', 'localtime');"""
)
tasks = db_cursor.fetchall()
db_connection.commit()
db_cursor.close()
db_connection.close()
print(len(tasks))
