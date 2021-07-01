import sqlite3
from sqlite3.dbapi2 import Cursor, connect


def signup(username, password):
    db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        """ SELECT * FROM users WHERE username = '{username}';""".format(username=username))
    existingUser = db_cursor.fetchone()
    if existingUser is None:
        db_cursor.execute(
            """ INSERT INTO users(username,password) VALUES ('{username}','{password}')  ;""".format(username=username, password=password))
        db_connection.commit()
        db_cursor.close()
        db_connection.close()
    else:
        return('User already exists')
    return 'Account created'


def login():
    return


def verify_pw(username):
    db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    if user_exists(username):
        db_cursor.execute(
            """ SELECT password FROM users WHERE username = '{username}';"""
            .format(username=username))
        db_password = db_cursor.fetchone()[0]
        db_connection.commit()
        db_cursor.close()
        db_connection.close()
        return db_password
    else:
        return'Username/Password is not correctly entered'


def user_exists(username):
    db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        """ SELECT * FROM users WHERE username = '{username}';""".format(username=username))
    db_user = db_cursor.fetchone()
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    if db_user is None:
        return False
    else:
        return True


def get_user_id(username):
    db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        """ SELECT pk FROM users WHERE username = '{username}';""".format(username=username))
    db_user_id = db_cursor.fetchone()[0]
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return db_user_id


def get_tasks(username):
    db_user_id = get_user_id(username)
    db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    db_cursor.execute("""
    SELECT * FROM tasks WHERE userid = '{db_user_id}'
    ;""".format(db_user_id=db_user_id))
    tasks = db_cursor.fetchall()
    return tasks


def remove_task(task_id):
    db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        """ DELETE FROM tasks WHERE taskid = '{task_id}' ;""".format(task_id=task_id))
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return


def update_task(task_id, taskname, taskstartdate, taskduedate):
    db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        """ UPDATE tasks SET taskname = '{taskname}' , taskstartdate = '{taskstartdate}',taskduedate = '{taskduedate}'
        WHERE taskid = '{task_id}' ;""".format(task_id=task_id, taskname=taskname, taskstartdate=taskstartdate, taskduedate=taskduedate))
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return


def add_task(username, task_name, task_startdate, task_duedate):
    db_user_id = get_user_id(username)
    db_connection = sqlite3.connect('tasks.db', check_same_thread=False)
    db_cursor = db_connection.cursor()
    db_cursor.execute(""" 
    INSERT INTO tasks (taskname,taskstartdate,taskduedate,userid)
     VALUES ('{task_name}','{task_startdate}','{task_duedate}','{db_user_id}')
    ;""".format(username=username, task_name=task_name,
                task_startdate=task_startdate, task_duedate=task_duedate, db_user_id=db_user_id))
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    return