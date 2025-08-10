import tkinter
import random
screen=tkinter.Tk()
screen.geometry("400x350")
screen.title("Rock,paper,scissors shoot!")
score=0
Cscore=0



def choose(item):
    global score,Cscore
    options=("rock","paper","scissors")
    Citem=random.choice(options)
    label5.config(text="you seleted:"+item)
    label7.config(text="computer seleted:"+Citem)
    if item==Citem:
        label2.config(text="it is a draw :(")

    if item=="rock" and Citem=="scissors" or item=="paper" and Citem=="rock" or item=="scissors" and Citem=="paper":
        label2.config(text="Player Won!!!",fg="Green")
        score=score+1
        label6.config(text="Player Score: "+ str(score))
        
    if Citem=="rock" and item=="scissors" or Citem=="paper" and item=="rock" or Citem=="scissors" and item=="paper":
        label2.config(text="Player lost!!!",fg="Red")
        Cscore=Cscore+1
        label8.config(text="Computer Score: "+ str(Cscore))

label1=tkinter.Label(screen,text="Rock paper scissors")
label2=tkinter.Label(screen,text="")
label3=tkinter.Label(screen,text="Your Options:")
label4=tkinter.Label(screen,text="Score:")
label5=tkinter.Label(screen,text="You Seleted:")
label6=tkinter.Label(screen,text="Player Score:")
label7=tkinter.Label(screen,text="Computer Seleted:")
label8=tkinter.Label(screen,text="Computer Score:")

button1=tkinter.Button(screen,text="Rock",command=lambda:choose("rock"))
button2=tkinter.Button(screen,text="Paper",command=lambda:choose("paper"))
button3=tkinter.Button(screen,text="Scissor",command=lambda:choose("scissors"))



label1.grid(row=1,column=1,columnspan=4)
label2.grid(row=2,column=1,columnspan=4)
label3.grid(row=3,column=1)
label4.grid(row=5,column=1)
label5.grid(row=6,column=2)

label6.grid(row=6,column=3)
label7.grid(row=7,column=2)
label8.grid(row=7,column=3)

button1.grid(row=4,column=2)
button2.grid(row=4,column=3)
button3.grid(row=4,column=4)


screen.mainloop()