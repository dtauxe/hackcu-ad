# For the plotting calculator thingy

import sympy as sp
import numpy as np
from numpy import e, pi
from sympy.integrals import laplace_transform as Laplace
from sympy.integrals import fourier_transform as Fourier
from sympy.integrals.transforms import inverse_laplace_transform as InvLaplace
from sympy.integrals.transforms import inverse_fourier_transform as InvFourier
from sympy.plotting import plot_parametric
from sympy import plot, Heaviside, sin, cos, tan, exp, re, im, symbols

# Class used for parsing inputs from the command line
class CmdLine:

    # Constructor
    def __init__(self):
        pass

    # Begin parsing commands
    def begin(self):
        # make some things have nicer names
        i = j = 1j
        u = Heaviside

        while (True):
            # Prompt for input
            cmd = input("--> ")
            if cmd == 'quit':
                break
            # Try to run the command
            try:
                exec(cmd)
            except Exception as e:
                print ("Error: " + str(e))

## MAIN for testing
if __name__ == '__main__':
    print ("Welcome to the calculator thingy!")
    print ("Type \"quit\" to quit")

    # We encapsulate this in a class to avoid putting things in the global namespace
    cmdParser = CmdLine()
    cmdParser.begin()
