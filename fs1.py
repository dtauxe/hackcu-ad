import numpy as np
from sympy.abc import t,s
from sympy import exp,symbols
from matplotlib import pyplot as pl
from pylab import stem
import re

#POA: check 3 classes, return coefficients and freq positions

#exponential handler
def complexExp(expr):
    #expr gives parsed exp expression --> how to handle inputs w/o integral w0?
    #parse inside\
    ss0 = expr.split("*",1)
    if ('exp' not in ss0[0]):
        coef = ss0[0]
    else:
        coef = 1
    ss1 = expr.split("(",1)
    inside = ss1[-1]
    realDeal = inside.split(")",1)[0]
    moreReal = eval(realDeal)
    freq = moreReal.as_coeff_Mul()[0]
    print(freq,ss1)
    return [coef,freq]

fxn = input("Function: ")
[coef,freq] = complexExp(fxn)

stem([coef],[freq],'-')
# pl.xlabel('Time (n)')
# pl.ylabel('x[n]')
pl.show()

#iterate thru all components of input
# component = re.split("[+-]",fxn)        #fix this
# for i in range(0,len(component)):
#     print(component[i])
