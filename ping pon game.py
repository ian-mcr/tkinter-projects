import tkinter
screen=tkinter.Tk()
screen.geometry("1000x800")
screen.title("Ping Pon Game")

canvas1=tkinter.Canvas(screen,width=1000,height=800,background="black")

canvas1.grid(row=0,column=0)

canvas1.create_line(500,0,500,800,fill="white",width=5)

canvas1.create_oval(400,300,600,500,outline="white",width=5)

class Ball():
    def __init__(self):
        self.pingball=canvas1.create_oval(475,375,525,425,fill="yellow")
        self.changeX=5
        self.changeY=5


class Paddel():
    def __init__(self,x1,y1,x2,y2,colour):
        canvas1.create_rectangle(x1,y1,x2,y2,fill=colour)
        self.changey=0

paddel1=Paddel(35,300,60,475,"orange")
paddel2=Paddel(965,300,940,475,"green")

ball1=Ball()


screen.mainloop()