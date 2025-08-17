import tkinter
import time
screen=tkinter.Tk()
screen.geometry("300x200")
screen.title("Timer")
hour=tkinter.StringVar()
mins=tkinter.StringVar()
sec=tkinter.StringVar()

hour.set("00")
mins.set("00")
sec.set("00")

def start():
    H=int(entry1.get())
    M=int(entry2.get())
    S=int(entry3.get())
    TS=H*3600+M*60+S
    
    while TS>0:
        TS=TS-1
        print(TS)
        h=TS//3600
        m=TS%3600//60
        s=TS%60
        hour.set(h)
        mins.set(m)
        sec.set(s)
        screen.update()
        time.sleep(1)

entry1=tkinter.Entry(screen,textvariable=hour,font=("arial",20,"bold"),width=5)
entry2=tkinter.Entry(screen,textvariable=mins,font=("arial",20,"bold"),width=5)
entry3=tkinter.Entry(screen,textvariable=sec,font=("arial",20,"bold"),width=5)

button1=tkinter.Button(screen,text="Start Timer",command=start)

entry1.grid(row=1,column=2)
entry2.grid(row=1,column=3)
entry3.grid(row=1,column=4)

button1.grid(row=2,column=3)

screen.mainloop()