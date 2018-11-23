# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:52:22 2018

@author: geoagdt
"""
import sys
import matplotlib
import matplotlib.pyplot

n = 100
a2D = []
v = 1

for i in range(n):
    a1D = []
    a2D.append(a1D)
    for j in range(n):
        #a1D.append(v)
        a1D.append(a2D) # This is a crazy line as we are appending the 2D array to itself and it breaks the plotting code.

print("Here")
sys.stdout.flush() # This forces the print buffer to flush.
# If we do not force the print buffer to flush the program hangs without printing "Here"

# If we comment out the matplotlib lines this program ends and flushes the print buffer.
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(a2D)
matplotlib.pyplot.show()

