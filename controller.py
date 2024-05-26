import sqlite3
from datetime import datetime


class SQLiteController():
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
    
    
    def close(self):
        self.connection.close()
        

    def add_task(self, task_name, task_text, user_id, deadline=None):
        sql = "insert into Tasks(TaskName, TaskText, Deadline, CreationDate, LooserID) values (?, ?, ?, ?, ?)"
        self.cursor.execute(sql, 
            (task_name, task_text, deadline, datetime.today().strftime('%Y-%m-%d'), user_id))
        self.connection.commit()
        
    
    def close_task(self, task_id):
        sql = "update Tasks set complete = 1 where ID = ?"
        self.cursor.execute(sql, (task_id,))
        self.connection.commit()

dbcontroller = SQLiteController('Enquar')
dbcontroller.close_task(1)
dbcontroller.close()
