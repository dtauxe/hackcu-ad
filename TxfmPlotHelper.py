# Used by the window to calculate the transforms

import sympy as sp
import numpy as np
from numpy import e, pi
from sympy.integrals import laplace_transform as Laplace
from sympy.integrals import fourier_transform as Fourier
from sympy.integrals.transforms import inverse_laplace_transform as InvLaplace
from sympy.integrals.transforms import inverse_fourier_transform as InvFourier
from sympy import plot, Heaviside, sin, cos, tan, exp, re, im, symbols

u = Heaviside
I = j = 1j
t, n, s, z, w = symbols("t n s z w")

class TxfmPlotHelper:
    def __init__(self):
        pass

    # Calculate a transform
    def Transform(self, expr, txfm):
        if (txfm == 'Z'):
            raise Exception

        x = 'w' if txfm.endswith('Fourier') else 's' # Transformed unit
        f = eval(expr, globals(), locals())
        #print(f)
        if (txfm == 'Fourier' or txfm == 'Laplace'):
            F = eval(txfm+"(f, t, "+x+")", globals(), locals())
        elif (txfm == 'InvFourier' or txfm == 'InvLaplace'):
            F = eval(txfm+"(f, "+x+", t)", globals(), locals())
        return (f, F)

    # Generate a sympy plot
    def plot(self, expr, x):
        #f = eval(expr, globals(), locals())
        #if (x == 'w'): # Fourier - convert from f to w
            #f = f(w/(2*pi))
            #expr = str(expr).replace('w', "w/(2*pi)")
        return eval("plot("+str(expr)+",("+x+",-2*pi, 2*pi), show=False)", globals(), locals())
