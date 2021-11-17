import sqlite3
def delete_db():
    conn= sqlite3.connect('Reminder.db')
    curr= conn.cursor()
    """
       Delete all rows in the Remind_ME table
       :param conn: Connection to the SQLite database
       :return:
       """
    sql = 'DELETE FROM Remind_ME'

    curr.execute(sql)
    conn.commit()

