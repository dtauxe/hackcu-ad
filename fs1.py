import numpy as np
from sympy.abc import t,s
from sympy import exp,symbols,pi
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
        coef = eval(ss0[0])
    else:
        coef = 1
    ss1 = expr.split("(",1)
    inside = ss1[-1]
    realDeal = inside.split(")",1)[0]
    moreReal = eval(realDeal)
    freq = moreReal.as_coeff_Mul()[0]
    print(freq,ss1)
    return [coef,freq]

#sin/cos handler
def sinusoid(expr):
    s1 = expr.split("*",1)
    #0.5 coef for sin & cos --> just consider magnitude
    if ('sin' not in s1[0] or 'cos' not in s1[0]):
        coef = eval(s1[0])*0.5
    else:
        coef = 0.5
    #chop up the input and get w0!
    s0 = expr.split("(",1)[-1]
    #splitPatrn = '(\+|-)*\)'
    splitPatrn = '(\+|\-)\d*\)'
    itsReal = re.split(splitPatrn,s0)
    reality = eval(itsReal[0])
    #print("PRINTING REALITY\n")
    freq = reality.as_coeff_Mul()[0]
    print (coef,freq)
    return [coef,freq]          #need to plot +/- of coef

#general periodic functions - plot how many coef? integrate each coef
#have user enter data of 1 period, return coef/freq array, should work for
#sinusoid/exponential, beware of defsult assumption
#for piecewise functions enter p in front
def general(expr,period=2*pi,bounds=[0,2*pi]):
    
    return [coef,freq]

fxn = input("Function: ")
period = 2*pi
[coef,freq] = general(fxn,period)

#stem([coef],[freq],'-')
# pl.xlabel('Time (n)')
# pl.ylabel('x[n]')
pl.show()

#iterate thru all components of input
# component = re.split("[+-]",fxn)        #fix this
# for i in range(0,len(component)):
#     print(component[i])
