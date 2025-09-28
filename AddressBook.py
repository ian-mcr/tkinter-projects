import tkinter
screen=tkinter.Tk()
screen.geometry("500x500")
screen.title("Address Book")

label1=tkinter.Label(text="My Address Book",font=("arial",15))
label2=tkinter.Label(text="Name:",font=("arial",15))
label3=tkinter.Label(text="Address:",font=("arial",15))
label4=tkinter.Label(text="Mobile:",font=("arial",15))
label5=tkinter.Label(text="Email:",font=("arial",15))
label6=tkinter.Label(text="Birthday",font=("arial",15))

entry1=tkinter.Entry()
entry2=tkinter.Entry()
entry3=tkinter.Entry()
entry4=tkinter.Entry()
entry5=tkinter.Entry()

button1=tkinter.Button(text="Open",font=("arial",15))
button2=tkinter.Button(text="Edit",font=("arial",15))
button3=tkinter.Button(text="Delete",font=("arial",15))
button4=tkinter.Button(text="update/add",font=("arial",15))
button5=tkinter.Button(text="save",font=("arial",15))

listbox1=tkinter.Listbox(width=25,height=10,font=("arial",15))

label1.grid(row=1,column=2)
label2.grid(row=2,column=3)
label3.grid(row=3,column=3)
label4.grid(row=4,column=3)
label5.grid(row=5,column=3)
label6.grid(row=6,column=3)

entry1.grid(row=2,column=4)
entry2.grid(row=3,column=4)
entry3.grid(row=4,column=4)
entry4.grid(row=5,column=4)
entry5.grid(row=6,column=4)

button1.grid(row=1,column=3)
button2.grid(row=7,column=1)
button3.grid(row=7,column=2)
button4.grid(row=7,column=4)
button5.grid(row=8,column=2,)

listbox1.grid(row=2,rowspan=5,column=1,columnspan=2)

screen.mainloop()