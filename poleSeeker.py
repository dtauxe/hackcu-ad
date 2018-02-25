#pl.ylabel(r'$x_{n}$') - TEX stuff
from numpy import inf,pi,cos,sin,heaviside
from sympy import fourier_transform,plot,exp,symbols,Heaviside
from sympy.abc import t,s
import numpy as np
from matplotlib import pyplot as pl
from pylab import stem,linspace
import re

def poleSeeker(fxn):
    pattern0 = 'u\[-(\d*\*)?n'
    pattern1 = 'u\[(\d*\*)?n'
    pattern2 = '(\d*)(\.)(\d*)\*\*'
    #small error checking
    if (re.search(pattern0,fxn) and re.search(pattern1,fxn)):
        print("Ya messed up real bad")
    if (re.search(pattern0,fxn)):
        roc = False
    elif (re.search(pattern1,fxn)):
        roc = True
    else:
        print("ya done messed up")
    #searching for z-trans pole
    m = re.search(pattern2,fxn)
    pole = eval(m.group(1)+m.group(2)+m.group(3))
    return [pole,roc]

def polePlotZ(pole,roc):
    #roc var for insided/outsided!!!
    pl.title('ROC Z-Transform')
    pl.axes(projection='polar')

    # Plot a circle with radius 2 using polar form
    rads = np.arange(0, (2*np.pi), 0.01)

    for radian in rads:
        plot.polar(radian,pole,'o')
    # theta = 0
    # ax = pl.subplot(111,projection='polar')
    # ax.plot(theta,pole,'b')
    # ax.set_rmax(pole*2)
    # ax.grid(True)
    # pl.show()

fxn = input("Enter function: ")
[thePole,roc] = poleSeeker(fxn)
polePlotZ(thePole,roc)

# vectSize = 15
# n,u = symbols('n,u')
# yvect = np.zeros(vectSize)
# for n in range(0,vectSize):
#     exec("f = " + fxn)
#     print(f)
#     yvect[n] = f
# stem(yvect,'-.')
# pl.suptitle('Z-Transform x[n]')
# pl.xlabel('Time (n)')
# pl.ylabel('x[n]')
# pl.show()
