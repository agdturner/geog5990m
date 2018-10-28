# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:07:41 2018

@author: geoagdt
"""
import csv
import matplotlib

environment = []
 
#f = open('data.csv', newline='') 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    for value in row: # A list of value
        rowlist.append(value)
        #print(value)
    environment.append(rowlist)
f.close()

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() 