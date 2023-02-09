import datetime
import os
import time
import ctypes
import subprocess
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def window(note,day,hour,minute,filename):
    subprocess.Popen(["python.exe", "reminder_window.py"] + [note,day,hour,minute,filename])

def pluss(p,day,hour,minute):
    x1 = day*1440 + hour*60 + minute
    r = x1
    x1 += p
    d = int(x1/1440)*1440
    x1 -= d

    h = int(x1/60)*60
    x1 -= h
    h = int(h/60)
    m = x1
    d = int(d / 1440)
    return [d,h,m,r]



run = True
viewed_files = []
while run:

    currentDT = datetime.datetime.now()
    for i in os.listdir("reminders/"):
        if i not in viewed_files:
            r = i.split("-")
            with open(f"reminders/{i}") as file:
                note = file.read()
            day = r[0]
            hour = r[1]
            minute = r[2]
            if pluss(0,currentDT.day,currentDT.hour,currentDT.minute)[3] >= pluss(0,int(day),int(hour),int(minute))[3]:
                viewed_files.append(i)
                window(note, day, hour, minute,i)
                time.sleep(1)
    time.sleep(1)
