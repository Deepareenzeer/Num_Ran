import tkinter as tk
import tkinter.ttk as tt
from tkinter import *
from tkinter import ttk

Num = tk.Tk()
Num.geometry('390x250+750+300')
Num.title("Number")
Num.resizable(False,False)

def show_answer(num):
    current_text = Entr.get()
    new_text =  current_text + num
    Entr.delete(0,tk.END)
    Entr.insert(0,new_text)
  
Entr=ttk.Entry(Num)
Entr.place(x=15,y=30)

btn1=ttk.Button(Num,text='1',width=17,command=lambda num=str(1):show_answer(num)).place(x=15,y=85)
btn2=ttk.Button(Num,text='2',width=17,command=lambda num=str(2):show_answer(num)).place(x=140,y=85)
btn3=ttk.Button(Num,text='3',width=17,command=lambda num=str(3):show_answer(num)).place(x=260,y=85)
btn4=ttk.Button(Num,text='4',width=17,command=lambda num=str(4):show_answer(num)).place(x=15,y=120)
btn5=ttk.Button(Num,text='5',width=17,command=lambda num=str(5):show_answer(num)).place(x=140,y=120)
btn6=ttk.Button(Num,text='6',width=17,command=lambda num=str(6):show_answer(num)).place(x=260,y=120)
btn7=ttk.Button(Num,text='7',width=17,command=lambda num=str(7):show_answer(num)).place(x=15,y=155)
btn8=ttk.Button(Num,text='8',width=17,command=lambda num=str(8):show_answer(num)).place(x=140,y=155)
btn9=ttk.Button(Num,text='9',width=17,command=lambda num=str(9):show_answer(num)).place(x=260,y=155)
btn0=ttk.Button(Num,text='0',width=17,command=lambda num=str(0):show_answer(num)).place(x=15,y=190)

Num.mainloop()