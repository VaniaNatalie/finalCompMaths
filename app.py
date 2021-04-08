
from tkinter import *
from tkinter.ttk import Combobox
from sympy.core.sympify import sympify
from sympy.parsing.sympy_parser import parse_expr

from tkinter.messagebox import showerror
from finalProj import *

# FigureCanvasTkAgg: create the library needed for canvas
# NavigationToolbar2Tk: create the library required by the toolbar
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

# Implement the default Matplotlib key bindings (shortcut key required modules)
from matplotlib.backend_bases import key_press_handler

# Import the modules needed for drawing
from matplotlib.figure import Figure
import numpy as np

class Page(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.choices_variable = StringVar(window)
        self.user_choices = ("sin", "cos", "tan", "sec", "cot", "arcsin", "arccos", "arctan")
        self.choices_variable.set(self.user_choices[0])

        self.function_label = Label(window, text="Function", font=('calibre', 10))
        self.entry = Entry(window, textvariable=self.get_user_in, font=('calibre', 10))
        self.function_label.grid(row=1,column=0)
        self.entry.grid(row=1,column=1)


        self.combo_box = Combobox(window, textvariable=self.choices_variable, values=self.user_choices)
        self.combo_box.place(x=60, y=150)
        self.combo_box.grid(row=0, column=1)

        self.btn = Button(window, text="Submit", command=self.get)
        self.btn.grid(row=2,column=1)

        self.button1 = Button(window, text="Show Graph",
                            command=lambda: TaylorSeries(Page(window)))
        self.button1.grid(row=3, column=1)


    def get_value(self):
        self.val = self.combo_box.get()
        return self.val

    def get_user_in(self):
        self.user_input = self.change_operations(self.entry.get())
        #self.user_input = self.entry.get()
        return self.user_input

    def get(self):
        self.my_label = Label(window, text="f(x) = " + self.get_value() + "(" + self.get_user_in() + ")")
        self.my_label.grid(row=4, column=1)

    def change_operations(self, equation):
        return equation.replace("x", "*x")


class TaylorSeries(Page):
    def __init__(self, parent):
        super().__init__(parent)
        self.taylor_1 = self.combo_box.get()
        self.y_value_1 = self.entry

        self.user_input_1 = int(self.y_value_1[0])
        self.user_input_2 = x
        self.y_value = self.user_input_1 * self.user_input_2

        self.tay, self.y = self.check_function(self.taylor_1, self.y_value)

        # Canvas size and resolution
        fig = Figure(figsize=(5,5), dpi=100)

        ax = fig.add_subplot(111)
        ax.plot(arr, self.y(arr))
        ax.plot(arr, self.tay)
        ax.set_title (f"Taylor Series f(x) = {self.taylor_1}({self.y_value_1})", fontsize=16)
        ax.set_ylabel("Y", fontsize=14)
        ax.set_xlabel("X", fontsize=14)

        self.canvas = FigureCanvasTkAgg(fig, master=window)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.draw()
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()

    def check_function(self, value, user_input):
        if value == "sin":
            self.tay = taylor(sym.sin(user_input), arr, 0, 5)
            # Inserting the original graph
            self.y = sym.lambdify(x, sym.sin(user_input))
        elif value == "cos":
            self.tay = taylor(sym.cos(user_input), arr, 0, 5)
            # Inserting the original graph
            self.y = sym.lambdify(x, sym.cos(user_input))
        elif value == "tan":
            self.tay = taylor(sym.tan(user_input), arr, 0, 5)
            # Inserting the original graph
            self.y = sym.lambdify(x, sym.tan(user_input))
        elif value == "sec":
            self.tay = taylor(sym.sec(user_input), arr, 0, 5)
            # Inserting the original graph
            self.y = sym.lambdify(x, sym.sec(user_input))
        elif value == "cot":
            self.tay = taylor(sym.cot(user_input), arr, 0, 5)
            # Inserting the original graph
            self.y = sym.lambdify(x, sym.cot(user_input))
        elif value == "arcsin":
            self.tay = taylor(sym.asin(user_input), arr, 0, 5)
            # Inserting the original graph
            self.y = sym.lambdify(x, sym.asin(user_input))
        elif value == "arccos":
            self.tay = taylor(sym.acos(user_input), arr, 0, 5)
            # Inserting the original graph
            self.y = sym.lambdify(x, sym.acos(user_input))
        elif value == "arctan":
            self.tay = taylor(sym.atan(user_input), arr, 0, 5)
            # Inserting the original graph
            self.y = sym.lambdify(x, sym.atan(user_input))
        return (self.tay, self.y)



if __name__ == "__main__":

    # Instantiate a root window 
    window = Tk()
    window.geometry("600x400")
    window.wm_title("Taylor Series")
    x = Page(window)

    
    x.mainloop()