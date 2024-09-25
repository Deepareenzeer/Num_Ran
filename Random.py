import tkinter as tk
import tkinter.ttk as tt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

Num = tk.Tk()
Num.geometry('390x250+765+400')
Num.title("Random")
Num.resizable(False,False)
count= 0
def show_answer(num):
        global count
        count +=1
        ran=random.randint(1,10)
        current_text = Entr.get()
        new_text =  current_text + num
        Entr.delete(0,tk.END)
        Entr.insert(0,new_text)
        number = int(num)
        if number > ran :
            messagebox.showerror("High",f"{number} มากเกินไป") 
            Entr.delete(0,tk.END)
        elif number < ran :
            messagebox.showerror("Low",f"{number} น้อยเกินไป") 
            Entr.delete(0,tk.END)
        elif number == ran :
            messagebox.showinfo("Correct",f"{number} ถูกต้อง")
            Entr.delete(0,tk.END)
            messagebox.showinfo("showinfo",f"คุณใช้ทั้งหมด {count}") 
            count = 0
            
Entr=ttk.Entry(Num)
Entr.place(x=15,y=30)

btn1=ttk.Button(Num,text='1',width=17,command=lambda num=str(1):show_answer(num)).place(x=15,y=85)
btn2=ttk.Button(Num,text='2',width=17,command=lambda num=str(2):show_answer(num)).place(x=138,y=85)
btn3=ttk.Button(Num,text='3',width=17,command=lambda num=str(3):show_answer(num)).place(x=260,y=85)
btn4=ttk.Button(Num,text='4',width=17,command=lambda num=str(4):show_answer(num)).place(x=15,y=120)
btn5=ttk.Button(Num,text='5',width=17,command=lambda num=str(5):show_answer(num)).place(x=138,y=120)
btn6=ttk.Button(Num,text='6',width=17,command=lambda num=str(6):show_answer(num)).place(x=260,y=120)
btn7=ttk.Button(Num,text='7',width=17,command=lambda num=str(7):show_answer(num)).place(x=15,y=155)
btn8=ttk.Button(Num,text='8',width=17,command=lambda num=str(8):show_answer(num)).place(x=138,y=155)
btn9=ttk.Button(Num,text='9',width=17,command=lambda num=str(9):show_answer(num)).place(x=260,y=155)
btn0=ttk.Button(Num,text='0',width=17,command=lambda num=str(0):show_answer(num)).place(x=15,y=190)

Num.mainloop()