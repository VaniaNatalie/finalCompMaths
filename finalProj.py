import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym

# Initializing X as a symbol to calculate differential 
x = sym.Symbol('x')

# Loop for differential
def differential(graph, loop):
    # Do differential corresponding to the loop in taylor func
    for i in range(loop):
        graph = sym.diff(graph)
    # Return the appropriate derviative to be processed in taylor
    return graph


def taylor(graph, arr, start, n):
    total = 0
   
    for i in range(n):
        f = sym.lambdify(x, differential(graph, i))
        # General taylor function, substitude x from differential with input array
        total = np.add(total, (f(start) * (arr - start)**i / math.factorial(i))) 
    return total

arr = np.linspace(0, 4*math.pi, 100) 


#tay = taylor(sym.sin(2*x), arr, 0, 5)
#Inserting the original graph
#y = sym.lambdify(x, sym.sin(2*x))
#plt.plot(arr, y(arr))
#plt.plot(arr, tay)
#plt.ylim([-10, 10])
#plt.show()

