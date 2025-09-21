import tkinter
import tkinter.ttk
screen=tkinter.Tk()
screen.geometry("350x450")
screen .title("Color Changer")

def add():
    object=entry1.get()
    if object!="":
        listbox1.insert(tkinter.END,object)
        entry1.delete(0,tkinter.END)

def delete():
    index=listbox1.curselection()
    print(index)
    if index!=():
        listbox1.delete(index)

def change():
    index=listbox1.curselection()
    color=listbox1.get(index)
    screen.config(background=color)

    



listbox1=tkinter.Listbox(screen,width=20,height=10,font=("arial",20))

entry1=tkinter.Entry(screen)

button1=tkinter.Button(screen,text="DELETE",font=("arial",15),command=delete)
button2=tkinter.Button(screen,text="ADD",font=("arial",15),command=add)
button3=tkinter.Button(screen,text="CHANGE",font=("arial",15),command=change)



button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=2,column=2)

entry1.grid(row=2,column=1)

listbox1.grid(row=3,column=1,columnspan=2)

screen.mainloop()