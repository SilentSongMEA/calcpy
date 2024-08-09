from tkinter import *
root=Tk()
def center(window,width,height):
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenwidth()
    x=(screen_width//2)-(width//2)
    y=(screen_height//2)-(height//2)
    window.geometry(f'{Width}x{height}+{x}+{y}')
Width=400
height=500
center(root,Width,height)
e=StringVar()
def func1(num):
    e.set(e.get()+num)
def func2():
    e.set(eval(e.get()))

def func3(s):
    x=e.get()[-1]
    if x=="+" or x=="-" or x=="*" or x=="/":
        e.set(e.get()[:-1])
        e.set(e.get()+s)
    else:
        e.set(e.get()+s)

lbl1=Label(textvariable=e, font=("Times New Roman",16,"bold"),padx=10,pady=10,fg="blue",bg="#decaef")
lbl1.grid(columnspan=4)
btn1=Button(text="1", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('1'))
btn1.grid(row=1,column=0)

btn2=Button(text="2", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('2'))
btn2.grid(row=1,column=1)

btn3=Button(text="3", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('3'))
btn3.grid(row=1,column=2)

btnsum=Button(text="+", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func3('+'))
btnsum.grid(row=1,column=3)

btn4=Button(text="4", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('4'))
btn4.grid(row=2,column=0)

btn5=Button(text="5", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('5'))
btn5.grid(row=2,column=1)

btn6=Button(text="6", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('6'))
btn6.grid(row=2,column=2)

btnmin=Button(text="-", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func3('-'))
btnmin.grid(row=2,column=3)

btn7=Button(text="7", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('7'))
btn7.grid(row=3,column=0)

btn8=Button(text="8", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('8'))
btn8.grid(row=3,column=1)

btn9=Button(text="9", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('9'))
btn9.grid(row=3,column=2)

btnz=Button(text="*", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func3('*'))
btnz.grid(row=3,column=3)

btnclear=Button(text="c", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:e.set(''))
btnclear.grid(row=4,column=0)

btnzero=Button(text="0", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func1('0'))
btnzero.grid(row=4,column=1)

btnmosavi=Button(text="=", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=func2)
btnmosavi.grid(row=4,column=2)

btntaqsim=Button(text="/", font=("Times New Roman",14,"bold"),fg="#7b3eed",bg="#decaef",width=5,height=2,command=lambda:func3('/'))
btntaqsim.grid(row=4,column=3)


mainloop()
