#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  1.0.0
"""
import operator
import random
import matplotlib.pyplot

'''
Step 1: Initialise parameters.
'''
print("Step 1: Initialise parameters.")
num_of_agents = 100
num_of_iterations = 20
rangey = 100
rangex = 50
deltarange = 10
random_seed = 0 # Try varying this to get different results.
print("num_of_agents", num_of_agents)
print("num_of_iterations", num_of_iterations)
print("rangey" ,rangey)
print("rangex", rangex)
print("deltarange", deltarange)
print("random_seed", random_seed)
random.seed(random_seed)

'''
Step 2: Initialise agents.
'''
print("Step 2: Initialise agents.")
agents = [] # Create a new empty list for coordinates. 
# Populate agents adding agents with random locations given the ranges
for i in range(num_of_agents):
    agents.append([random.randint(0,rangey),random.randint(0,rangex)])
# Print x, y locations of agents
for i in range(num_of_agents):
    #print(str(i), agents[i][0])
    print("agents[" + str(i) + "] y =", agents[i][0], "x =", agents[i][1])

'''
Step 3: Move each agent up to a small (deltarange) random amount in x and y 
directions num_of_iterations times. This implements a torus where agents moving 
off the bottom move onto the top and those moving off the left move onto the 
right and vice versa.
'''
print("Step 3: Move each agent up to a small (deltarange) random amount in",
      "x and y directions num_of_iterations times. This implements a torus", 
      "where agents moving off the bottom move onto the top and those moving",
      "off the left move onto the right and vice versa.")
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # Move y
        deltay = random.randint(-deltarange, deltarange)
        #print("deltay ", deltay)
        agents[i][0] = (agents[i][0] + deltay) % rangey
        # Move x
        deltax = random.randint(-deltarange, deltarange)
        #print("deltax ", deltax)
        agents[i][1] = (agents[i][1] + deltax) % rangex
# Print x, y locations
for i in range(num_of_agents):
    #print(str(i), agents[i][0])
    # str(i) is used to force i to be regarded as a string.
    print("agents[" + str(i) + "] y =", agents[i][0], "x =", agents[i][1])

'''
Step 4: Calculate, store and print out the element of agents with the 
largest and smallest first and second elements.
'''
print("Step 5: Calculate, store and print out the element of agents with the", 
      "largest and smallest first and second elements.")
maxy = max(agents, key=operator.itemgetter(0))
print("Element of agents with the largest first element", maxy)
miny = min(agents, key=operator.itemgetter(0))
print("Element of agents with the smallest first element", miny)
maxx = max(agents, key=operator.itemgetter(1))
print("Element of agents with the largest second element", maxx)
minx = min(agents, key=operator.itemgetter(1))
print("Element of agents with the smallest second element", minx)

'''
Step 5: Plot agents.
'''
print("Step 6: Plot agents.")
matplotlib.pyplot.ylim(0, rangex) # This is why I think it is odd axis order! 
matplotlib.pyplot.xlim(0, rangey)
# Plot all agents
print("Plot all agents black.")
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][0],agents[i][1], color='black')
# Plot agent with the maxy blue.
print("Plot agent with the maxy blue.")
matplotlib.pyplot.scatter(maxy[0], maxy[1], color='blue')
# Plot agent with the miny red.
print("Plot agent with the miny red.")
matplotlib.pyplot.scatter(miny[0], miny[1], color='red')
# Plot agent with the maxy blue.
print("Plot agent with the maxx pink.")
matplotlib.pyplot.scatter(maxx[0], maxx[1], color='pink')
# Plot agent with the miny red.
print("Plot agent with the minx green.")
matplotlib.pyplot.scatter(minx[0], minx[1], color='green')
matplotlib.pyplot.show()