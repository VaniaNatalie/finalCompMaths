from tkinter import *
from tkinter.ttk import Combobox
from sympy.core.sympify import sympify
from sympy.parsing.sympy_parser import parse_expr

from tkinter.messagebox import showerror
import taylor

# FigureCanvasTkAgg: create the library needed for canvas
# NavigationToolbar2Tk: create the library required by the toolbar
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

# Implement the default Matplotlib key bindings (shortcut key required modules)
from matplotlib.backend_bases import key_press_handler

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
root.geometry("250x200")

coefficient = 0
trigonometry = None
power = 0
start = 0
n = 0

def setup_label():
    label1 = Label(root, text="Coefficient")
    label1.grid(row=0, column=0)

    label2 = Label(root, text="Trigonometry")
    label2.grid(row=1, column=0) 

    label3 = Label(root, text="Power")
    label3.grid(row=2, column=0) 

    label4 = Label(root, text="Start")
    label4.grid(row=3, column=0)

    label5 = Label(root, text="n")
    label5.grid(row=4, column=0)

def get_input():
    global coefficient_input
    global combo_box
    global power_input
    global start_input
    global n_input

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

    my_label = Label(root, text="f(x) = " + trigonometry + "(" + str(coefficient) + "*x**" + str(power) + ")")
    my_label.grid(row=7, column=1)

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
    top = Toplevel()
    top.title("The Graph")
    global x
    tayl = taylor.taylor(tay, arr, start, n)
    y = sym.lambdify(x, tay)

    
    fig = Figure(figsize=(5,4))
    ax = fig.add_subplot(111)
    ax.plot(arr, y(arr), label="Original")
    ax.plot(arr, tayl, label="Taylor")
    ax.set_ylim([-10,10])
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=top)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   top)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

coefficient_input = Entry(root)
coefficient_input.grid(row=0, column=1)

choices_variable = StringVar(root)
user_choices = ("sin", "cos", "tan", "cosec", "sec", "cot", "arcsin", "arccos", "arctan")
choices_variable.set(user_choices[0])

combo_box = Combobox(root, textvariable=choices_variable, values=user_choices)
combo_box.grid(row=1, column=1)

power_input = Entry(root)
power_input.grid(row=2, column=1)

start_input = Entry(root)
start_input.grid(row=3, column=1)

n_input = Entry(root)
n_input.grid(row=4, column=1)

button1 = Button(root, text="Submit", command=get_input)
button1.grid(row=5, column=1)

button2 = Button(root, text="Show Graph", command=lambda:[check_taylor(coefficient, trigonometry, power),plot_taylor(check_taylor(coefficient, trigonometry, power), arr, start, n)])
button2.grid(row=6, column=1)

setup_label()
root.title("Taylor Series")
root.mainloop()