import datetime
from datetime import date
from plyer import notification

if __name__ == "__main__":

    Message = input("What Should I Remind --:\n")
    remind_date = input("On what date should I remind\n(dd/MM/YYYY format)--:\n")
    remind_time = input("At what time should I remind\n(hrs:min:secs format) --:")
    while True:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        det = date.today()
        d2 = det.strftime("%d/%m/%Y")
        if strTime == remind_time and d2 == remind_date:
            notification.notify(
                title="This is a Reminder",
                message=Message,
                app_icon="D:\College\Projects\Reminder\Reminder.ico",
                timeout=30
            )
            print("Reminder Set")
            break
        else:
            pass



