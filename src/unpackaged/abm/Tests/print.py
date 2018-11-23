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
        a1D.append(a2D)

print("Here 2")
#sys.stdout.flush()

'''
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(a2D)
matplotlib.pyplot.show()
'''
