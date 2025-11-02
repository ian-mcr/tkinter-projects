import tkinter
screen=tkinter.Tk()
screen.geometry("1000x800")
screen.title("Ping Pon Game")

canvas1=tkinter.Canvas(screen,width=1000,height=800,background="black")

canvas1.grid(row=0,column=0)

canvas1.create_line(500,0,500,800,fill="white")

screen.mainloop()