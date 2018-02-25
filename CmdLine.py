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
class CmdLine():

    # List of members to import and give names w/out prefix
    #imports = {'sympy': ['sin', 'cos', 'tan', 'exp', 'plot'],
    #        'np': ['e', 'pi']}

    # Constructor
    def __init__(self):
        pass

    # Plot the function
    #def plot(self, func):
    #    # TODO
    #    print ("Not yet done")

    # Begin parsing commands
    def begin(self):
        # make some things have nicer names
        i = j = 1j
        u = Heaviside
        #for prefix in self.imports:
        #    for member in self.imports[prefix]:
        #        exec(member + "=" + prefix + "." + member)

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

