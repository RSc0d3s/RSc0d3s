from _ast import Lambda
from tkinter import*
import tkinter.font as fnt

from themed_tkinter import widget

root = Tk()
root.title("Simple Calculator")
root.configure(bg="gray")

e = Entry(root, width=65, borderwidth=8)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

#define buttons

button_1 = Button(root, bg='#CCFFFF', text="1", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(1))
button_1.configure (borderwidth=8)
button_2 = Button(root, bg='#FFFFCC', text="2", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(2))
button_2.configure (borderwidth=8)
button_3 = Button(root, bg='#FFCCFF', text="3", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(3))
button_3.configure (borderwidth=8)
button_4 = Button(root, bg='#FFCCCC', text="4", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(4))
button_4.configure (borderwidth=8)
button_5 = Button(root, bg='#FFCC99',text="5", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(5))
button_5.configure (borderwidth=8)
button_6 = Button(root, bg='#FF99CC',text="6", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(6))
button_6.configure (borderwidth=8)
button_7 = Button(root, bg='#E57373', text="7", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(7))
button_7.configure (borderwidth=8)
button_8 = Button(root, bg='#FFEBEE', text="8", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(8))
button_8.configure (borderwidth=8)
button_9 = Button(root, bg='#F06292',text="9", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(9))
button_9.configure (borderwidth=8)
button_0 = Button(root, bg='#E1BEE7', text="0", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=40,pady=20, command=lambda: button_click(0))
button_0.configure (borderwidth=8)
button_add = Button(root, bg='#D2C4E9', text="+", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=39,pady=20, command=button_add)
button_add.configure (borderwidth=8)
button_equal = Button(root, bg='#C5CAE9', text="=", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=91,pady=20, command=button_equal)
button_equal.configure (borderwidth=8)
button_clear = Button(root, bg='#BBDEFB', text="Clear", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=183,pady=20, command=button_clear)
button_clear.configure (borderwidth=8)
button_subtract = Button(root, bg='#B3E5FC', text="-", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=41,pady=20, command=button_subtract)
button_subtract.configure (borderwidth=8)
button_multiply = Button(root, bg='#B2EBF2', text="*", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=39,pady=20, command=button_multiply)
button_multiply.configure (borderwidth=8)
button_divide = Button(root, bg='#B2DFDB', text="/", font=fnt.Font(family='Arial Bold', size=10, weight='bold'), padx=39,pady=20, command=button_divide)
button_divide.configure (borderwidth=8)

#put buttons on screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_clear.grid(row=5,column=0, columnspan=4)
button_equal.grid(row=4,column=1, columnspan=2)

button_add.grid(row=1,column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()
