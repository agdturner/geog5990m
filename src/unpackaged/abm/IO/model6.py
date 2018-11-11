#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  1.0.0
"""
import csv
import matplotlib
import agentframework6 as af
import matplotlib.pyplot
import os

'''
Step 1: Initialise parameters.
'''
print("Step 1: Initialise parameters.")
num_of_agents = 10
num_of_iterations = 1000
print("num_of_agents",num_of_agents)
print("num_of_iterations",num_of_iterations)

'''
Step 2: Initialise environment this will contain data about the spatial 
environment in which agents act.
'''
print("Step 2: Initialise environment this will contain data about the",
      "spatial environment in which agents act.")
environment = []
# Initialise data dir
dir = os.getcwd()
#print(dir)
parent = os.path.dirname(dir)
print(parent)
parent = os.path.dirname(parent)
parent = os.path.dirname(parent)
basedir = os.path.dirname(parent)
#print(basedir)
datadir = os.path.join(basedir, 'data')
#print(datadir)
inputdatadir = os.path.join(datadir, 'input')
#print(inputdatadir)
outputdatadir = os.path.join(datadir, 'output')
#print(outputdatadir)
# Open file and read.
file = os.path.join(inputdatadir, 'in.txt')
# read csv into environment
''' This way works BUT see below...
f = open(file, newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    for value in row: # A list of values
        rowlist.append(value)
        #print(value)
    environment.append(rowlist)
f.close()
'''
# The following way is better as:
# The 'with' keyword sets up a Context Manager, which temporarily deals with 
# how the code runs. This closes the file automatically when the clause is 
# left. 
with open(file, newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
            #print(value)
        environment.append(rowlist)

'''
Step 3: Initialise agents.
'''
print("Step 3: Initialise agents.")
agents = []
# Make the agents.
for i in range(num_of_agents):
    agents.append(af.Agent(environment))

'''
Step 4: Agents act.
'''
print("Step 4: Agents act.")
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
'''
Step 5: Plot Agents on Environment.
'''
print("Step 5: Plot Agents on Environment.")
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety())
matplotlib.pyplot.show()
        
'''
Step 5: Write out the environment to the file dataout.csv.
'''
print("Step 5: Write out the environment to the file dataout.csv.")
file = os.path.join(outputdatadir, 'dataout.csv')
'''  This way works BUT see below...
f2 = open(file, 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environment: 
    writer.writerow(row) # List of values.
f2.close() 
'''
# The following way is better as:
# The 'with' keyword sets up a Context Manager, which temporarily deals with 
# how the code runs. This closes the file automatically when the clause is 
# left. 
with open(file, 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=' ')
    for row in environment:
        writer.writerow(row)
        '''
        for value in row:
            print(value)
            #writer.write(value)
        '''

'''
Step 6: Calculate total amount stored by all the agents and append this to the
file dataout2.txt.
'''
print("Step 6: Calculate total amount stored by all the agents and append",
      "this to the file dataout2.txt.")
total = 0
for a in agents:
    total += a.store
    #print(total)
# Append total to dataout2.txt
file = os.path.join(outputdatadir, 'dataout2.txt')
with open(file, "a") as f3:
    f3.write(str(total) + "\n")
    #f3.write("\n")
    f3.flush  
f3.close