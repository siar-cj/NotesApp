import os
import sys
import datetime
from tkinter import *
import ctypes
import tkinter as tk
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def window(note,dayy,hourr,minutee,filename):
    def plus():
        _ = int(cont_text.get())
        cont_text.set("")
        cont_text.insert(END, str(_ + 1))
    def minus():
        _ = int(cont_text.get())
        cont_text.set("")
        cont_text.insert(END, str(_ - 1 if _ != 1 else 0))
    t = Tk()
    t.resizable(False, False)
    t.geometry(f"300x200+{int(screensize[0]/2)-150}+{int(screensize[1]/2)-200}")
    t.title("Remind Me Later")


    class Lotfi(tk.Text):
        def __init__(self, master=None, **kwargs):
            self.var = tk.StringVar()
            tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
            self.old_value = ''
            self.var.trace("w", self.check)
            self.get, self.set = self.var.get, self.var.set

        def check(self, *args):
            if self.get() == "":
                self.set("")
            elif self.get().isdigit():
                self.old_value = self.get()
            else:
                self.set(self.old_value)
    cont_text = Lotfi(t,width=30)
    cont_text.insert(END, '5')
    Label(t,text=note[:335],wraplength=295).place(x = 0,y = 0)

    Label(t,text="Remind me").place(x=82,y=128)
    Label(t,text="minutes later!").place(x=180,y=128)
    cont_text.place(x = 150,y = 130,width=30,height=17)
    Button(t,text="+",command=plus).place(x=150,y=115,width=20,height=17)
    Button(t,text="-",command=minus).place(x=150,y=147,width=20,height=17)

    def later():
        currentDT = datetime.datetime.now()
        name = f"reminders/{str(pluss(int(cont_text.get()),currentDT.day,currentDT.hour,currentDT.minute)[0])}-{str(pluss(int(cont_text.get()),currentDT.day,currentDT.hour,currentDT.minute)[1])}-{str(pluss(int(cont_text.get()),currentDT.day,currentDT.hour,currentDT.minute)[2])}-{filename.split('-')[-2]}.txt"
        os.rename("reminders/" + filename, name)
        t.quit()

    def ok():
        os.remove(f"reminders/{filename}")
        t.destroy()

    Button(t,text="Later",command=later).place(x=230,y=160,width=60,height=30)
    Button(t,text="OK",command=ok).place(x=10,y=160,width=60,height=30)

    t.mainloop()
    if filename in os.listdir("reminders/"):
        os.remove(f"reminders/{filename}")


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



args = sys.argv
window(args[1],args[2],args[3],args[4],args[5])