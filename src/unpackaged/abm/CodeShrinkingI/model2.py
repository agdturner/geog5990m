#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  1.0.0
"""
import operator
import random
import matplotlib.pyplot

'''
Step 1: Set the random seed.
'''
print("Step 1: Set the random seed.")
random_seed = 0
print("random_seed", random_seed)
random.seed(random_seed)

'''
Step 2: Create agents list.
'''
print("Step 2: Create agents list.")
agents = [] # Create a new empty list for coordinates. 
agents.append([random.randint(0,99),random.randint(0,99)]) # Add y0,x0 to agents
agents.append([random.randint(0,99),random.randint(0,99)]) # Add y1,x1 to agents
# Print out details of agents[0] and agents[1]
print("agents[0][1]", agents[0][1])
print("agents[0][0]", agents[0][0])
print("agents[1][1]", agents[1][1])
print("agents[1][0]", agents[1][0])

'''
Step 3: Calculate distance between agents[0] and agents[1].
'''
print("Step 3: Calculate distance between agents[0] and agents[1].")
distance = ((agents[0][1] - agents[1][1])**2 + (agents[0][0] - agents[1][0])**2)**0.5
print("distance "); print(distance)

'''
Step 4: Calculate, store and print out the element of agents with the largest second element.
'''
print("Calculate, store and print out the element of agents with the largest second element.")
m = max(agents, key=operator.itemgetter(1))
print("Element of agents with the largest second element", m)

'''
Step 5: Plot agents.
'''
print("Step 5: Plot agents.")
matplotlib.pyplot.ylim(0, 99) # Limit the y of the plot
matplotlib.pyplot.xlim(0, 99) # Limit the x of the plot
matplotlib.pyplot.scatter(agents[0][1],agents[0][0]) # Plot agent[0] a random colour
matplotlib.pyplot.scatter(agents[1][1],agents[1][0]) # Plot agent[1] a random colour
print("Agents with the largest second element plotted in red.")
matplotlib.pyplot.scatter(m[1],m[0], color='red')
#matplotlib.pyplot.scatter(max(agents, key=operator.itemgetter(1)), color='red')
matplotlib.pyplot.show()