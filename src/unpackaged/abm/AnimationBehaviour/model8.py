#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  1.0.0
"""
import csv
import agentframework7 as af
import random
import matplotlib.pyplot as pyplot
from sys import argv
import matplotlib.animation as anim
import os

'''
Step 1: Initialise parameters
'''
print("Step 1: Initialise parameters")
print("argv", argv)
if len(argv) < 5:
    num_of_agents = 10
    num_of_iterations = 100
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
    agents.append(af.Agent(environment, agents, random_seed))


'''
Step 4: Animate acting agents.
'''
print("Step 4: Animate acting agents.")
fig = pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

def update(frame_number):
    
    global carry_on  #Not actually needed as we're not assigning, but clearer
    
    # Clear fig
    fig.clear()
            
    # Process the agents in a randomish order.
    #for j in range(num_of_iterations):
    # The number of iterations is now controlled in the gen_function
    if True:
        if (carry_on):
            #if (j % 10 == 0):
            #    print("iteration", j)
            # Shuffle agents
            #agents = random.shuffle(agents)
            #random.shuffle(agents[, random.random()])
            random.shuffle(agents)
            for i in range(num_of_agents):
                agents[i].move()
                agents[i].eat()
                agents[i].share_with_neighbours(neighbourhood)
            # Stop if all agents have more than 50 store
            for i in range(num_of_agents):
                half_full_agent_count = 0
                if (agents[i].store > 50):
                    half_full_agent_count += 1
            if (half_full_agent_count == num_of_agents):
                carry_on = False
                print("stopping condition")
            ''' Stop randomly
            if random.random() < 0.1:
                carry_on = False
                print("stopping condition")
            '''
    # Plot            
    # Plot environment
    pyplot.xlim(0, len(environment))
    pyplot.ylim(0, len(environment[0]))
    pyplot.imshow(environment)
    # Plot sheep
    for i in range(num_of_agents):
        pyplot.scatter(agents[i].getx(),agents[i].gety(), color="grey")
        #print(agents[i].getx(),agents[i].gety())
    
       
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while  (a < num_of_iterations) & (carry_on): 
        yield a			#: Returns control and waits next call.
        a = a + 1
        
#animation = anim.FuncAnimation(fig, update, interval=1)
#animation = anim.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = anim.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
animation = anim.FuncAnimation(fig, update, frames=gen_function, repeat=False)
"""Create animated plot. Continues to update the plot until stopping criteria is met.""" 

pyplot.show()
"""Display the plot."""

'''
Step 5: Write out the environment to the file dataout.csv.
'''
print("Step 5: Write out the environment to the file dataout.csv.")
file = os.path.join(outputdatadir, 'dataout.csv')
with open(file, 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=' ')
    for row in environment:
        writer.writerow(row)

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