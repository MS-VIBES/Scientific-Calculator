# IMPORTING THE REQUIRED LIBRARIES.
from tkinter import *
import math
import tkinter.messagebox

#SETTING THE WINDOW LAYOUT.
root=Tk()
root.geometry("650x400+300+300")
root.iconbitmap(True,"calc icon.ico")
root.title("Scientific Calculator")

#ADDING THE LOGIC

#ROW-1


def pi():
    if display.get()=='0':
        display.delete(0,END)
        pos=len(display.get())
        display.insert(pos,str(math.pi))

def fact():
    try:
        ans=int(display.get())
        ans=math.factorial(ans)
        display.delete(0,END)
        display.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror('error')

def sin():
    try:
        si=float(display.get())
        si=math.sin(math.radians(si))
        display.delete(0,END)
        display.insert(0,str(si))
    except Exception:
        tkinter.messagebox.showerror(("error"))

def cos():
    try:
        cs=float(display.get())
        cs=math.cos(math.radians(cs))
        display.delete(0,END)
        display.insert(0,str(cs))
    except Exception:
        tkinter.messagebox.showerror(("error"))

def tan():
    try:
        tn=float(display.get())
        tn=math.tan(math.radians(tn))
        display.delete(0,END)
        display.insert(0,str(tn))
    except Exception:
        tkinter.messagebox.showerror(("error"))

def btn_1():
    if display.get()=='0':
        display.delete(0,END)
        pos=len(display.get())
    display.insert(pos,'1')


def btn_1():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'1')


def btn_2():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'2')

def btn_3():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'3')

def btn_add():
    pos=len(display.get())
    display.insert(pos,'+')

    #row-2

def btn_e():
    if display.get=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,str(math.e))

def sqrt():
    try:
        ans=int(display.get())
        ans=math.sqrt(ans)
        display.delete(0,END)
        display.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("value Error! check your operator and operand")

def asin():
    try:
        asn=float(display.get())
        asn=math.asin(math.radians(asn))
        display.delete(0,END)
        display.insert(0,str(asn))
    except Exception:
        tkinter.messagebox.showerror(("error"))

def acos():
    try:
        acs=float(display.get())
        acs=math.acos(math.radians(acs))
        display.delete(0,END)
        display.insert(0,str(acs))
    except Exception:
        tkinter.messagebox.showerror(("error"))

def atan():
    try:
        atn=float(display.get())
        atn=math.atan(math.radians(atn))
        display.delete(0,END)
        display.insert(0,str(atn))
    except Exception:
        tkinter.messagebox.showerror(("error"))
    
def btn_4():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'4')

def btn_5():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'5')

def btn_6():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'6')
        
def btn_minus():
    pos=len(display.get())
    display.insert(pos,'-')

    #row-3

def radian():
    try:
        rad=display.get()
        rad=math.radians(rad)
        display.delete(0,END)
        display.insert(0,rad)
    except Exception:
        tkinter.messagebox.showerror("value Error! check your operator and operand")

def round():
    try:
        rnd=display.get()
        rnd=math.round(rnd)
        display.delete(0,END)
        display.insert(0,rnd)
    except Exception:
        tkinter.messagebox.showerror("value Error! check your operator and operand")

def logn():
    try:
        ln=float(display.get())
        ln=math.log(ln)
        display.delete(0,END)
        display.insert(0,str(ln))
    except  Exception:
        tkinter.messagebox.showerror("value Error! Check your operator & operand")
        
def log():
    try:
        lg=int(display.get())
        lg=math.log10(lg)
        display.delete(0,END)
        display.insert(0,str(lg))
    except  Exception:
        tkinter.messagebox.showerror("value Error! Check your operator & operand")

def pow():
    pos=len(display.get())
    display.insert(pos,'**')

def btn_7():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'7')

def btn_8():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'8')

def btn_9():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'9')

def btn_multiply():
    pos=len(display.get())
    display.insert(pos,'*')

#row-4

def modulus():
    pos=len(display.get())
    display.insert(pos,'%')

def btn_brckR():
    pos=len(display.get())
    display.insert(pos,')')

def btn_brckL():
    pos=len(display.get())
    display.insert(pos,'(')

def btn_dot():
    pos=len(display.get())
    display.insert(pos,'.')

def clr():
    pos=len(display.get())
    display.delete(0,END)
    display.insert(pos,'0')

def backspc():
    pos=len(display.get())
    entry=str(display.get())
    if entry=="":
        display.insert(0,'0')
    elif entry==" ":
        display.insert(0,"0")
    elif entry=="0":
        pass
    else:
        display.delete(0,END)
        display.insert(0,entry[0:pos-1])


def btn_0():
    if display.get()=='0':
        display.delete(0,END)
    pos=len(display.get())
    display.insert(pos,'0')

def eq():
    try:
        ans=display.get()
        ans=eval(ans)
        display.delete(0,END)
        display.insert(0,ans)
    except Exception:
         tkinter.messagebox.showerror("value Error! Check your operator & operand")

def btn_divide():
    pos=len(display.get())
    display.insert(pos,'/')



#ADDING THE ENTRY BOX & CUSTOMISING IT ACCORDINGLY.
display=Entry(root,font="Verdana",fg="Black",bg="mistyrose",bd=4,justify=RIGHT)
display.insert(0,'0')
display.pack(expand=TRUE,fill=BOTH)


#ADDING THE BUTTONS
    # make the frame-1 for the buttons.
row1=Frame(root,bg="#000000")
row1.pack(expand=TRUE,fill=BOTH)

    #adding the buttons to the frame-1
PI_btn=Button(row1,text="π",font="segoe 18",relief=GROOVE,bd=0,command=pi,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
fact_btn=Button(row1,text="x!",font="segoe 18",relief=GROOVE,bd=0,command=fact,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
sin_btn=Button(row1,text="Sin",font="segoe 18",relief=GROOVE,bd=0,command=sin,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
cos_btn=Button(row1,text="Cos",font="segoe 18",relief=GROOVE,bd=0,command=cos,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
tan_btn=Button(row1,text="Tan",font="segoe 18",relief=GROOVE,bd=0,command=tan,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn1=Button(row1,text="1",font="segoe 23",relief=GROOVE,bd=0,command=btn_1,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn2=Button(row1,text="2",font="segoe 23",relief=GROOVE,bd=0,command=btn_2,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn3=Button(row1,text="3",font="segoe 23",relief=GROOVE,bd=0,command=btn_3,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn_plus=Button(row1,text="+",font="segoe 23",relief=GROOVE,bd=0,command=btn_add,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)

# make the frame-2 for the buttons.
row2=Frame(root,bg="#000000")
row2.pack(expand=TRUE,fill=BOTH)

    #adding the buttons to the frame-2
e_btn=Button(row2,text="e",font="segoe 18",relief=GROOVE,bd=0,command=btn_e,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
root_btn=Button(row2,text="√x",font="segoe 18",relief=GROOVE,bd=0,command=sqrt,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
negativesin_btn=Button(row2,text="Sin-1",font="segoe 18",relief=GROOVE,bd=0,command=asin,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
negativecos_btn=Button(row2,text="Cos-1",font="segoe 18",relief=GROOVE,bd=0,command=acos,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
negativetan_btn=Button(row2,text="Tan-1",font="segoe 18",relief=GROOVE,bd=0,command=atan,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn4=Button(row2,text="4",font="segoe 23",relief=GROOVE,bd=0,command=btn_4,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn5=Button(row2,text="5",font="segoe 23",relief=GROOVE,bd=0,command=btn_5,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn6=Button(row2,text="6",font="segoe 23",relief=GROOVE,bd=0,command=btn_6,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn_minus=Button(row2,text="-",font="segoe 23",relief=GROOVE,bd=0,command=btn_minus,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)

# make the frame-3 for the buttons.
row3=Frame(root,bg="#000000")
row3.pack(expand=TRUE,fill=BOTH)

    #adding the buttons to the frame-1
Rad_btn=Button(row3,text="Rad",font="segoe 18",relief=GROOVE,bd=0,command=radian,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
round_btn=Button(row3,text="round",font="segoe 18",relief=GROOVE,bd=0,command=round,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
lognatural_btn=Button(row3,text="ln",font="segoe 18",relief=GROOVE,bd=0,command=logn,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
log_btn=Button(row3,text="log",font="segoe 18",relief=GROOVE,bd=0,command=log,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
power_btn=Button(row3,text="pow",font="segoe 18",relief=GROOVE,bd=0,command=pow,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn7=Button(row3,text="7",font="segoe 23",relief=GROOVE,bd=0,command=btn_7,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn8=Button(row3,text="8",font="segoe 23",relief=GROOVE,bd=0,command=btn_8,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn9=Button(row3,text="9",font="segoe 23",relief=GROOVE,bd=0,command=btn_9,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn_mul=Button(row3,text="*",font="segoe 23",relief=GROOVE,bd=0,command=btn_multiply,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)

# make the frame-4 for the buttons.
row4=Frame(root,bg="#000000")
row4.pack(expand=TRUE,fill=BOTH)

    #adding the buttons to the frame-4
percentage_btn=Button(row4,text="%",font="segoe 18",relief=GROOVE,bd=0,command=modulus,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
bracketopen_btn=Button(row4,text="(",font="segoe 18",relief=GROOVE,bd=0,command=btn_brckL,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
bracketclose_btn=Button(row4,text=")",font="segoe 18",relief=GROOVE,bd=0,command=btn_brckR,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
dot_btn=Button(row4,text=".",font="segoe 18",relief=GROOVE,bd=0,command=btn_dot,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
clear_btn=Button(row4,text="C",font="segoe 18",relief=GROOVE,bd=0,command=clr,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
backspace_btn=Button(row4,text="bkspc",font="segoe 23",relief=GROOVE,bd=0,command=backspc,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn0=Button(row4,text="0",font="segoe 23",relief=GROOVE,bd=0,command=btn_0,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
equals_btn=Button(row4,text="=",font="segoe 23",relief=GROOVE,bd=0,command=eq,fg="white",bg="red").pack(side=LEFT,expand=TRUE,fill=BOTH)
division_btn=Button(row4,text="/",font="segoe 23",relief=GROOVE,bd=0,command=btn_divide,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)

 


#TERMINATING THE WINDOW.
root.mainloop()