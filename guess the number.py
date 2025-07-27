import tkinter
import random
import tkinter.messagebox 
screen=tkinter.Tk()
screen.geometry("300x300")
screen .title("GUESS THE NUMBER !!!")
number=random.randint(1,20)


def ok():
    name=entry1.get()
    tkinter.messagebox.showinfo("name","Hello "+name+",I'm thinking of a number between 1 and 20 can you guess it!!!")

def guess():
    numberGuess=int(entry2.get())
    name=entry1.get()
    if numberGuess==number:
        tkinter.messagebox.showinfo("guess the number","you got it RIGHT,good job "+name)
    if numberGuess>number:
        tkinter.messagebox.showinfo("guess the number","The REAL number is LOWER")
    if numberGuess<number:
        tkinter.messagebox.showinfo("guess the number","The REAL number is HIGHER")



label1=tkinter.Label(screen,text="WELCOME to are GAME!")
label2=tkinter.Label(screen,text="What is your name")
label3=tkinter.Label(screen,text="Take a guess")

button1=tkinter.Button(screen,text="OK",command=ok)
button2=tkinter.Button(screen,text="Guess",command=guess)

entry1=tkinter.Entry(screen)
entry2=tkinter.Entry(screen)


label1.grid(row=1,column=2)
label2.grid(row=2,column=1)
label3.grid(row=4,column=1)

entry1.grid(row=3,column=1)
entry2.grid(row=4,column=2)

button1.grid(row=3,column=3)
button2.grid(row=4,column=3)

def ok():
    name=entry1.get()
    tkinter.messagebox.showinfo("name","Hello"+name+"I'm thinking of a number between 1 and 20 can you guess it!!!")






screen.mainloop()