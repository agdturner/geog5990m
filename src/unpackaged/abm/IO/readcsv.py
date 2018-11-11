# -*- coding: utf-8 -*-
import csv
import matplotlib
import os

environment = []

# Initialise data dir
dir = os.getcwd()
print(dir)
parent = os.path.dirname(dir)
parent = os.path.dirname(parent)
parent = os.path.dirname(parent)
basedir = os.path.dirname(parent)
print(basedir)
datadir = os.path.join(basedir, 'data')
print(datadir)
inputdatadir = os.path.join(datadir, 'input')
print(inputdatadir)

# Open file and read.
file = os.path.join(inputdatadir, 'in.txt')
f = open(file, newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    for value in row: # A list of value
        rowlist.append(value)
        #print(value)
    environment.append(rowlist)
f.close()

# Plot environment.
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()