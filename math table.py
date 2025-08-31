import tkinter
import tkinter.ttk
screen=tkinter.Tk()
screen.geometry("400x590")
screen .title("")


def table():
    result=""
    multiples=choose.get()
    number=int(combobox1.get())
    for i in range(multiples):
        answer=number*i
        print(str(number)+"x"+str(i)+"="+str(answer))
        result=result+str(number)+"x"+str(i)+"="+str(answer)+"\n"
    label3.config(text=result)

label1=tkinter.Label(screen,text="Mathematicl Table")
label2=tkinter.Label(screen,text="Number and Range")
label3=tkinter.Label(screen,text="")

button1=tkinter.Button(screen,text="Generate",command=table)

combobox1=tkinter.ttk.Combobox(screen)
numbers=[]
for i in range(1,101):
    numbers.append(i)
combobox1["values"]=numbers

choose=tkinter.IntVar()


r1=tkinter.Radiobutton(screen,text="10",variable=choose,value=11)
r2=tkinter.Radiobutton(screen,text="20",variable=choose,value=21)
r3=tkinter.Radiobutton(screen,text="30",variable=choose,value=31)

label1.grid(row=1,column=2)
label2.grid(row=2,column=1)
label3.grid(row=6,column=2)

combobox1.grid(row=2,column=2)

r1.grid(row=2,column=3)
r2.grid(row=3,column=3)
r3.grid(row=4,column=3)

button1.grid(row=5,column=2)


screen.mainloop()