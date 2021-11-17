import sqlite3

def create_db ():
    conn = sqlite3.connect('Reminder.db')
    curr = conn.cursor()

    sql_command = """
    
    CREATE TABLE Remind_ME( 
    
    Message TEXT PRIMARY KEY,   
    
    Date VARCHAR(50) ,
    
    TIME VARCHAR(50));"""


    curr.execute(sql_command)
    conn.commit()

    conn.close()
