import time
from os import system
import os
from datetime import datetime
from src.inject import inject
from src.notification import notification
def alarm():
    i = 0
    file = open("reminders\\reminder.rem", "w")
    file.write(f"date: {reminddate}\ntime: {remindtime}\nnote: {note}")
    system("clear || cls")
    print("Reminder is running...")
    while True:
        print(f"Time elapsed: {i}s", end = '\r')
        i = i+1
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%d/%m/%y")
        formatted_time = current_datetime.strftime("%H:%M")
        time.sleep(1)
        if formatted_date == reminddate and formatted_time == remindtime:
            notification("-- Reminder --", f"note: {note}\ncoded with love by github.com/infamouskoala", "src\\notification.mp3")
            print(f"{note}")
            input()
            break
        else:
            pass

def start():
    if startup == "y":
        path = os.path.abspath(__file__)
        inject(path)
        print("Added to autostart")
    elif startup == "n":
        print("You will have to run the script everytime u turn on ur pc.")

# CHOICES + SORTING

system("title Reminder Maker")
system("clear || cls")
print("""Welcome to Reminder Maker
This is integrated into your windows so that you can get windows pop up notifications when your reminder goes off
Date Layout: 00/00/00 (DD/MM/YY)
Time Layout: HH/MM (24hr)
""")
remindtime = input("Time of reminder (HH:MM):  ")
reminddate = input("Date of reminder (DD/MM/YY): ")
note = input("Note: ")
startup = input("Add file to startup (y/n)?")
startup = startup.lower()

if startup == "y":
    inject(os.path.abspath(__file__))
    print("File injected, Starting reminder now")
    time.sleep(3)
else:
    print("File not added to startup.")
    time.sleep(3)

alarm()