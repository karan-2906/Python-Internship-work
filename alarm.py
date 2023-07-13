import datetime
# import clock as c
from playsound import playsound
alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minute: "))
alarmAm = input("am/pm: ")

if alarmAm=="pm":
    alarmHour+=12
while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        # c.time()
        print("Playing...")
        playsound("ring.mp3")
        break
