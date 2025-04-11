from tkinter import *
import random
from tkinter import messagebox
w=Tk()
w.title('Jumbled Word Game')
w.geometry('500x500+1720+320')
words=['fractions','train','truck','river','ferrari','dubai','airport','math','mattress','poland']
jumbled=[]
score=0
number=0
for i in words:
    jumbled.append(''.join(random.sample(i,len(i))))
indexpo=random.randint(0,len(words)-1)
def awnsr():
    global indexpo,number,score
    number+=1
    if E.get()==words[indexpo]:
        messagebox.showinfo('Correct!','That is correct!')
        score+=1
    else:
        messagebox.showerror('WRONG','Wrong awnser')
    S.config(text=f'Score: {score}/{number}')
    WODR()
def WODR():
    reset()
    wordl.config(text=jumbled[indexpo])
def reset():
    global words,indexpo
    indexpo=random.randint(0,len(words)-1)
    E.delete(0,END)
Title=Label(w,text='Jumbled Word Game',font=('Normal',30))
wordl=Label(w,font=('Normal',20))
E=Entry(w,font=('Normal',20))
B1=Button(w,text='Submit',font=('Normal',20),command=awnsr)
B2=Button(w,text='Reset',font=('Normal',20),command=WODR)
S=Label(w,font=('Italic',7),text='Score:')
I=Label(w,font=('Italic',7),text='!!!spell in all lowercase!!!')
Title.pack(pady=5)
wordl.pack(pady=30)
E.pack(pady=10)
B1.pack(pady=20)
B2.pack(pady=10)
S.pack(pady=30)
I.pack(pady=4)
mainloop()