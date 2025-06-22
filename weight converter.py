import tkinter
screen=tkinter.Tk()
screen.geometry("300x150")
screen.title("weight converter")
label=tkinter.Label(screen,text="enter the weight in kg",font=("Arial",10))
label1=tkinter.Label(screen,text="Grams")
label2=tkinter.Label(screen,text="Pounds")
label3=tkinter.Label(screen,text="Ounces")

number1=tkinter.Label(screen,text="")
number2=tkinter.Label(screen,text="")
number3=tkinter.Label(screen,text="")

entry=tkinter.Entry(screen,width=10)

def convert():
    weight=float(entry.get())
    grams=weight*1000
    pounds=weight*2.20462
    ounces=weight*35.274
    number1.config(text=grams)
    number2.config(text=pounds)
    number3.config(text=ounces)
    

button=tkinter.Button(screen,text="convert",command=convert)



label.grid(row=1,column=1)
entry.grid(row=1,column=2)
button.grid(row=1,column=3)
label1.grid(row=2,column=1)
label2.grid(row=2,column=2)
label3.grid(row=2,column=3)
number1.grid(row=3,column=1)
number2.grid(row=3,column=2)
number3.grid(row=3,column=3)



screen.mainloop()