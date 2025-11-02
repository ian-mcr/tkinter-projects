import tkinter
from tkinter.colorchooser import askcolor
screen=tkinter.Tk()
screen.geometry("550x600")
screen.title("Color Paint")
pencolor="black"
pensize=1
eraseron=False
oldx=None
oldy=None


def draw(event):
    global oldx,oldy,pensize,eraseron,pencolor
    pensize=scale1.get()
    if eraseron==False:
        drawingcolor=pencolor
    else:
        drawingcolor="white"
    if oldx and oldy:
        canvas1.create_line(oldx,oldy,event.x,event.y,width=pensize,fill=drawingcolor,smooth=True,capstyle=tkinter.ROUND)
    oldx=event.x
    oldy=event.y

def reset(event):
    global oldx,oldy
    oldx=None
    oldy=None

def color():
    global pencolor
    pencolor=askcolor()[1]

def rubber():
    global eraseron
    eraseron=True

def pen():
    global eraseron
    eraseron=False

    


button1=tkinter.Button(screen,text="pen",command=pen)
button2=tkinter.Button(screen,text="colour",command=color)
button3=tkinter.Button(screen,text="eraser",command=rubber)

scale1=tkinter.Scale(screen,from_=1,to=10,orient="horizontal")

canvas1=tkinter.Canvas(screen,width=550,height=600,bg="white")

canvas1.bind("<B1-Motion>",draw)
canvas1.bind("<ButtonRelease-1>",reset)

button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)
scale1.grid(row=1,column=4)
canvas1.grid(row=2,column=1,columnspan=4)

screen.mainloop()