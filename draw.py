from tkinter import *
from tkinter.colorchooser import askcolor
class Draw:
    def __init__(self):
        self.win=Tk()
        self.B1=Button(self.win,text='Pen',command=self.pen)
        self.B2=Button(self.win,text='Colour',command=self.pick)
        self.B3=Button(self.win,text='Eraser',command=self.erase)
        self.B4=Button(self.win,text='Clear',command=self.clear)
        self.S=Scale(self.win,from_=1,to=10,orient=HORIZONTAL)
        self.C=Canvas(self.win,bg='white',width=600,height=600)
        self.B1.grid(row=0,column=0)
        self.B2.grid(row=0,column=1)
        self.B3.grid(row=0,column=2)
        self.B4.grid(row=0,column=3)
        self.S.grid(row=0,column=4)
        self.C.grid(row=1,columnspan=5)
        self.imprint()
        self.win.mainloop()
    def imprint(self):
        self.x=None
        self.y=None
        self.thickness=self.S.get()
        self.colour='Black'
        self.activebutton=self.B1
        self.C.bind('<B1-Motion>',self.write)
        self.C.bind('<ButtonRelease-1>',self.reset)
    def active(self,B):
        self.activebutton.config(relief=RAISED)
        B.config(relief=SUNKEN)
        self.activebutton=B
    def pen(self):
        self.active(self.B1)
        if self.colour=='white':
            self.colour='black' 
        else:
            self.colour=self.colour
    def erase(self):
        self.active(self.B3)
        self.colour='white'
    def clear(self):
        self.C.delete('all')
    def pick(self):
        self.colour=askcolor(color=self.colour)[1]
    def write(self,e):
        self.thickness=self.S.get()
        if self.x and self.y:
            self.C.create_line(self.x,self.y,e.x,e.y,width=self.thickness,fill=self.colour)
        self.x=e.x
        self.y=e.y
    def reset(self,e):
        self.x=None
        self.y=None
Draw()