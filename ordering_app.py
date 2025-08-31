import tkinter
import tkinter.ttk
screen=tkinter.Tk()
screen.geometry("400x500")
screen .title("ordering app")

label1=tkinter.Label(screen,text="Welcome to pizza hut")
label2=tkinter.Label(screen,text="select your fav pizza:")
label3=tkinter.Label(screen,text="enter Quanity")
label4=tkinter.Label(screen,text="")

combobox1=tkinter.ttk.Combobox(screen)
pizza=[0,1,2]
combobox2=tkinter.ttk.Combobox(screen)
number=[0,1,2,3,4,5,6,7]

choose=tkinter.IntVar()

r1=tkinter.Radiobutton(screen,text="S",variable=choose,value=10)
r2=tkinter.Radiobutton(screen,text="M",variable=choose,value=20)
r3=tkinter.Radiobutton(screen,text="L",variable=choose,value=30)

button1=tkinter.Button(screen,text="Order")

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