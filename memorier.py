import tkinter
import tkinter.filedialog
import tkinter.ttk
screen=tkinter.Tk()
screen.geometry("350x450")
screen .title("memorier")

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

def save():
    file1=tkinter.filedialog.asksaveasfile()
    if file1!=None:
        for item in listbox1.get(0,tkinter.END):
            print(item,file=file1)
            listbox1.delete(0,tkinter.END)

def open():
    OpenFile=tkinter.filedialog.askopenfile()
    if OpenFile!=None:
        listbox1.delete(0,tkinter.END)
        data=OpenFile.readlines()
        for item in data:
            listbox1.insert(tkinter.END,item)

    




button1=tkinter.Button(screen,text="OPEN",font=("arial",15),command=open)
button2=tkinter.Button(screen,text="DELETE",font=("arial",15),command=delete)
button3=tkinter.Button(screen,text="SAVE",font=("arial",15),command=save)
button4=tkinter.Button(screen,text="ADD",font=("arial",15),command=add)

entry1=tkinter.Entry(screen)
listbox1=tkinter.Listbox(screen,width=20,height=10,font=("arial",20))


entry1.grid(row=2,column=1,columnspan=2)

listbox1.grid(row=3,column=1,columnspan=3)

button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)
button4.grid(row=2,column=3)


screen.mainloop()