from tkinter import *
from tkinter.ttk import Combobox

import finalProj

# FigureCanvasTkAgg: create the library needed for canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Import the modules needed for drawing
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy as sym
plt.style.use('ggplot')

x = sym.Symbol('x')
arr = np.linspace(0, 4*math.pi, 100)

root = Tk()
canvas = Canvas(root, width = 800, height = 400)
canvas.pack()

coefficient = 0
trigonometry = None
power = 0
start = 0
n = 0

def setup_label():
    label1 = Label(root, text='Taylor Series Generator')
    label1.config(font=('Arial', 20))
    canvas.create_window(400, 50, window=label1)

    label2 = Label(root, text="Coefficient")
    canvas.create_window(250, 90, window=label2)

    label3 = Label(root, text="Trigonometry")
    canvas.create_window(250, 110, window=label3)

    label4 = Label(root, text="Power")
    canvas.create_window(250, 130, window=label4)

    label5 = Label(root, text="Start")
    canvas.create_window(250, 150, window=label5)

    label6 = Label(root, text="Number of Polynomials")
    canvas.create_window(250, 170, window=label6)

def get_input():
    global coefficient_input
    global combo_box
    global power_input
    global start_input
    global n_input
    global my_label

    global coefficient
    global trigonometry
    global power
    global start
    global n

    coefficient = int(coefficient_input.get())
    trigonometry = str(combo_box.get())
    power = int(power_input.get())
    start = int(start_input.get())
    n = int(n_input.get())

    if power == 1:
        my_label = Label(root, text="f(x) = " + trigonometry + "(" + str(coefficient) + "x" + ")"
        , font=('Arial', 12, "bold"))
        canvas.create_window(400, 200, window=my_label)
    else:
        my_label = Label(root, text="f(x) = " + trigonometry + "(" + str(coefficient) + "*x**" + str(power) + ")"
        , font=('Arial', 12, "bold"))
        canvas.create_window(400, 200, window=my_label)
        

def check_taylor(coef, trigo, power):
    global x

    if(trigo == "sin"):
        tay = sym.sin(coef*x**power)
    elif(trigo == "cos"):
        tay = sym.cos(coef*x**power)
    elif(trigo == "tan"):
        tay = sym.tan(coef*x**power)
    elif(trigo == "cosec"):
        tay = sym.csc(coef*x**power)
    elif(trigo == "sec"):
        tay = sym.sec(coef*x**power)
    elif(trigo == "cot"):
        tay = sym.cot(coef*x**power)
    elif(trigo == "arcsin"):
        tay = sym.asin(coef*x**power) 
    elif(trigo == "arccos"):
        tay = sym.acos(coef*x**power)
    else:
        tay = sym.atan(coef*x**power)   
    return tay                                

def plot_taylor(tay, arr, start, n):
    global x
    global graph

    tayl = finalProj.taylor(tay, arr, start, n)
    y = sym.lambdify(x, tay)

    fig = Figure(figsize=(4, 3), dpi=100)
    ax = fig.add_subplot(111)
    if power == 1:
        ax.set_title(f"f(x) = {trigonometry}({coefficient}x)")
    else:
        ax.set_title(f"f(x) = {trigonometry}({coefficient}$x^{power}$)")
    ax.plot(arr, y(arr), label="Original")
    ax.plot(arr, tayl, label="Taylor")
    ax.set_ylim([-10,10])

    graph = FigureCanvasTkAgg(fig, root) 
    graph.get_tk_widget().pack(fill=BOTH, expand=0)

def clear_all():
    my_label.destroy()
    coefficient_input.delete(0, END)
    power_input.delete(0, END)
    start_input.delete(0, END)
    n_input.delete(0, END)
    graph.get_tk_widget().pack_forget()

coefficient_input = Entry(root)
canvas.create_window(400, 90, window= coefficient_input)

choices_variable = StringVar(root)
user_choices = ("sin", "cos", "tan", "cosec", "sec", "cot", "arcsin", "arccos", "arctan")
choices_variable.set(user_choices[0])

combo_box = Combobox(root, textvariable=choices_variable, values=user_choices)
canvas.create_window(400, 110, window=combo_box)

power_input = Entry(root)
canvas.create_window(400, 130, window=power_input)

start_input = Entry(root)
canvas.create_window(400, 150, window=start_input)

n_input = Entry(root)
canvas.create_window(400, 170, window=n_input)

button1 = Button(root, text="  Submit  ", command=get_input, bg='#ff996e', fg='white', font=('Arial', 11, 'bold'), activebackground="#ffd97a")
canvas.create_window(400, 240, window=button1)

button2 = Button(root, text="  Show Graph  ", command=lambda:[check_taylor(coefficient, trigonometry, power),
                    plot_taylor(check_taylor(coefficient, trigonometry, power), arr, start, n)], 
                    bg='#b280f2', font=('Arial', 11, 'bold'), fg='white', activebackground="#f071a3"
                )
canvas.create_window(400, 280, window=button2)

button3 = Button(root, text="  Clear Graph  ", command=clear_all, bg='#6d71ed', font=('Arial', 11, 'bold'), fg='white', activebackground="#5ed6ba")
canvas.create_window(400, 320, window=button3)


setup_label()
root.title("Taylor Series")
root.mainloop()