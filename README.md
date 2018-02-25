# Signal Transform Plotter

This is a program to plot signals and their transforms.

WHAT'S IT DO?
=============
The idea is to provide an easy way to convert between signals and their Laplace/Fourier/Ztransforms.

# How to use

Simply enter a signal (or its transform) into the appropriate box and hit 'Enter' or the corresponding arrow button to transform the signal into its other representation and graph both (if available). One day, you will also be able to see some of the signal's properties in the lower left corner, but that is not implemented yet.

REQUIREMENTS
============
* Python3
* SymPy
* PyQt5

RUNNING
=======
Run it however you prefer to run Python3 programs, e.g.

    python3 main.py

Depending on your environment, you may be able to get away with:

    ./main.py

TODO
====
* Z-transform
* Plotting of discrete functions
* Pole-Zero plots for Laplace, Z transforms
* Signal properties (ROC, stability, causality)
