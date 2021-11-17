import datetime
from plyer import notification

import sqlite3
from Delete_db import delete_db

try:
    conn = sqlite3.connect('Reminder.db')
    cur = conn.cursor()

    '''Query all rows in the Remind_ME table
       :param conn: the Connection object
       :return:
       '''
    curr = conn.cursor()
    curr.execute('''Select Message FROM Remind_ME ''')
    messages = curr.fetchone()
    for message in messages:
        msg = message

    curr.execute('''Select Date FROM Remind_ME ''')
    Date = curr.fetchone()
    for dete in Date:
        date = dete

    curr.execute('''Select Time FROM Remind_ME ''')
    Time = curr.fetchone()
    for time in Time:
        tym = time

    conn.close()

    delete_db()

    while True:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        det = datetime.date.today()
        d2 = det.strftime("%d/%m/%Y")
        if strTime == tym and d2 == dete:
            notification.notify(
                title="This is a Reminder",
                message=msg,
                app_icon="D:\\College\\Projects\\Reminder\\Reminder.ico",
                timeout=30
            )
            break

except TypeError:
    print("No Reminder Set")
