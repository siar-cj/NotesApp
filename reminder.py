import subprocess
import os

def run_background():
    global process
    process = subprocess.Popen(["python.exe", "_background.py",])

def kill_background():
    process.kill()

def add_background_note(note,day,hour,minute):
    file_name = f"{day}-{hour}-{minute}"
    file = open(f"reminders/{day}-{hour}-{minute}-{len([i for i in os.listdir('reminders/') if file_name in i])}-.txt", "w+",encoding="utf-8")
    file.write(note)
    file.close()

