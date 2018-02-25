#!/bin/python

from CmdLine import CmdLine

## MAIN
if __name__ == '__main__':
    print ("Welcome to the calculator thingy!")
    print ("Type \"quit\" to quit")

    # We encapsulate this in a class to avoid putting things in the global namespace
    cmdParser = CmdLine()
    cmdParser.begin()
