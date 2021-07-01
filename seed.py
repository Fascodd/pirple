import sqlite3
connection = sqlite3.connect('tasks.db', check_same_thread=False)

cursor = connection.cursor()

cursor.execute(""" 
INSERT INTO tasks 
(taskname,taskcreatedate,taskstartdate,taskduedate,taskcompletedate,userid)
 VALUES 
 ("task2","2","2","2","2","4")
;""")

connection.commit()
cursor.close()
connection.close()
