
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  1.0.0
"""
import agentframework5 as af
import matplotlib.pyplot

''' Scratch code just to get things working
# Create an agent from agentframework5 and print out some details of it.
a = af.Agent()
print(type(a)) #  Print the type of aTo check the class:
print(isinstance(a, af.Agent)) # Check if a is an af.Agent type
print(a)
print(a.x)
print(a.y)
a.hi()
a.move()
a.hi()
'''

def distance_between(a, b):
    """ A function to calculate the distance between agent a and agent b.
    Args:
        a: A list of two coordinates for orthoganol axes.
        b: A list of two coordinates for the same orthoganol axes as a.
    Returns:
        The straight line distance between the a and b in the an plane given 
        by two orthoganol axes.
    """
    distance = ((a.getx() - b.getx())**2 + (a.gety() - b.gety())**2)**0.5
    ##print("distance =", str(distance))
    return distance

'''
Step 1: Inititlise parameters.
'''
print("Step 1: Inititlise parameters.")
num_of_agents = 10
num_of_iterations = 100


'''
Step 2. Initialise agents.
'''
print("Step 2. Initialise agents.")
agents = []
# Make the agents.
for i in range(num_of_agents):
    agents.append(af.Agent())

'''
Step 3. Move agents.
'''
print("Step 3. Move agents.")
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        
'''
Step 4. Plot agents.
'''
print("Step 4: Plot agents.")
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
matplotlib.pyplot.show()

'''
Step 5. Calculate distances between agents.
'''
print("Step 5. Calculate distances between agents.")
max_distance = 0;
for a in agents:
     for b in agents:
         distance = distance_between(a, b)
         if (distance > max_distance):
             max_distance = distance
print("Maximum distance between agents", max_distance)