import sqlite3
import sys

from Create_db import create_db
import subprocess

try:
    create_db()


    conn = sqlite3.connect('Reminder.db')
    curr = conn.cursor()

    message = input('What Should it say--:\n')

    date = input('Date (dd/mm/yyyy format)--:\n')

    time = input('Time (hr/min/sec format) --:\n')

    new_data = ("""INSERT INTO Remind_Me (Message, Date, Time)
    
        VALUES ('{}','{}','{}');""".format(message, date, time))

    curr.execute(new_data)
    conn.commit()
    conn.close()

except sqlite3.OperationalError :

    conn = sqlite3.connect('Reminder.db')
    curr = conn.cursor()

    message = input('What Should it say--:\n')

    date = input(' Date (dd/mm/yyyy format) --:\n')

    time = input('Time (hr/min/sec format) --:\n')

    new_data = ("""INSERT INTO Remind_Me (Message, Date, Time)

            VALUES ('{}','{}','{}');""".format(message, date, time))

    curr.execute(new_data)
    conn.commit()
    conn.close()
    print("Reminder Set")

cmd = "Reminder.py"
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
sys.exit()



