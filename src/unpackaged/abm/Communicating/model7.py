#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  1.0.0
"""
import csv
import matplotlib
import agentframework7
import random
#import operator
import matplotlib.pyplot
from sys import argv
import os

'''
Step 1: Initialise parameters
'''
print("Step 1: Initialise parameters")
print("argv", argv)
if len(argv) < 5:
    num_of_agents = 10
    num_of_iterations = 1000
    neighbourhood = 20
    random_seed = 0
    print("argv does not contain the expected number of arguments")
    print("len(argv)", len(argv))
    print("expected len(argv) 5")
    print("expecting:")
    print("argv[1] as a integer number for num_of_agents")
    print("argv[1] as a integer number for num_of_iterations")
    print("argv[1] as a integer number for neighbourhood")
    print("argv[1] as a integer number for random_seed for setting the random seed")
else:
    # set parameters from argv
    num_of_agents = int(argv[1])
    num_of_iterations = int(argv[2])
    neighbourhood = int(argv[3])
    random_seed = int(argv[4])
print("num_of_agents", str(num_of_agents))
print("num_of_iterations", str(num_of_iterations))
print("neighbourhood", str(neighbourhood))
print("random_seed", str(random_seed))
random.seed(random_seed)

'''
Step 2: Initialise environment this will contain data about the spatial 
environment in which agents act.
'''
print("Step 2: Initialise environment this will contain data about the",
      "spatial environment in which agents act.")
environment = []
# Initialise data dirs.
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
    # Add 1 to random seed to get each agent initialised and moving differently
    random_seed += 1
    agents.append(agentframework7.Agent(environment, agents, random_seed))
# Test getting another agent from an agent
print("Test getting another agent from an agent.")
print("agents[0].agents[1]", agents[0].agents[1])

'''
Step 4: Agents act.
'''
print("Step 4: Agents act.")
for j in range(num_of_iterations):
    if (j % 100 == 0):
        print("iteration", j)
    # Shuffle agents to process them in a randomish order.
    #agents = random.shuffle(agents)
    #random.shuffle(agents[, random.random()])
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

'''
Step 5: Plot agents on Environment.
'''
print("Step 5: Plot agents on Environment.")
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety())
matplotlib.pyplot.show()
   
'''
Step 6: Write out the environment to the file dataout.csv.
'''
print("Step 6: Write out the environment to the file dataout.csv.")
file = os.path.join(outputdatadir, 'dataout.csv')
with open(file, 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=' ')
    for row in environment:
        writer.writerow(row)

'''
Step 7: Calculate total amount stored by all the agents and append this to the
file dataout2.txt.
'''
print("Step 7: Calculate total amount stored by all the agents and append",
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