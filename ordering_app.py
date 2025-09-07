import tkinter
import tkinter.ttk
screen=tkinter.Tk()
screen.geometry("400x200")
screen .title("ordering app")

def ordering():
    result=""
    ps=str(choose.get())
    wo=str(combobox1.get())
    ao=int(combobox2.get())
    print("You got "+str(ao)+","+ps+","+wo)
    result=result+"You got "+str(ao)+","+ps+","+wo
    label4.config(text=result)


label1=tkinter.Label(screen,text="Welcome to pizza hut")
label2=tkinter.Label(screen,text="select your fav pizza:")
label3=tkinter.Label(screen,text="enter Quanity")
label4=tkinter.Label(screen,text="")

combobox1=tkinter.ttk.Combobox(screen)
pizza=["cheese","Ham","mushroom","4 cheese"]
combobox1["values"]=pizza
combobox2=tkinter.ttk.Combobox(screen)
number=[]
for i in range(1,11):
    number.append(i)
combobox2["values"]=number

choose=tkinter.StringVar()

r1=tkinter.Radiobutton(screen,text="S",variable=choose,value="small")
r2=tkinter.Radiobutton(screen,text="M",variable=choose,value="medium")
r3=tkinter.Radiobutton(screen,text="L",variable=choose,value="large")

button1=tkinter.Button(screen,text="Order",command=ordering)

label1.grid(row=1,column=2)
label2.grid(row=2,column=1)
label3.grid(row=3,column=1)
label4.grid(row=5,column=2)

combobox1.grid(row=2,column=2)
combobox2.grid(row=3,column=2)

r1.grid(row=2,column=3)
r2.grid(row=3,column=3)
r3.grid(row=4,column=3)

button1.grid(row=4,column=2)


screen.mainloop()