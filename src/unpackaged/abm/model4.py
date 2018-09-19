import operator
import random
import matplotlib.pyplot
import time

def distance_between(agents_row_a, agents_row_b):
    #distance = ((agents[0][1] - agents[1][1])**2 + (agents[0][0] - agents[1][0])**2)**0.5
    distance = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    print("distance =", str(distance))
    return distance
    
agents = [] # Create a new empty list for coordinates. 

num_of_agents = 10
num_of_iterations = 20
rangey = 100
rangex = 50
deltarange = 10

# Populate agents adding agents with random locations
for i in range(num_of_agents):
    agents.append([random.randint(0,rangey),random.randint(0,rangex)])

# Print x, y locations of agents
for i in range(num_of_agents):
    #print(str(i), agents[i][0])
    print("agents[" + str(i) + "] y =", agents[i][0], "x =", agents[i][1])

# Move each agent up to a small (deltarange) random amount in x and y 
# directions. This implements a torus where agents moving off the bottom
# move onto the top and those moving off the left move onto the right and
# vice versa.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # Move y
        deltay = random.randint(-deltarange,deltarange)
        #print("deltay ", deltay)
        agents[i][0] = (agents[i][0] + deltay) % rangey
        # Move x
        deltax = random.randint(-deltarange,deltarange)
        #print("deltax ", deltax)
        agents[i][1] = (agents[i][1] + deltax) % rangex

# Print x, y locations
for i in range(num_of_agents):
    #print(str(i), agents[i][0])
    print("agents[" + str(i) + "] y =", agents[i][0], "x =", agents[i][1])

# Calculate maximum and minimum distance between agents
# Time how long this takes to calculate
start = time.clock()
maxdistance = distance_between(agents[0], agents[1])
mindistance = maxdistance
for i in range(num_of_agents):
    #for j in range(num_of_agents):
    for j in range(i, num_of_agents):
        if (i != j):
            print("i=", i,"j=", j)
            distance = distance_between(agents[i], agents[j])
            maxdistance = max(maxdistance, distance)
            mindistance = min(mindistance, distance)
            #print("maxdistance=", maxdistance)
            #print("mindistance=", mindistance)
print("maxdistance=", maxdistance)
print("mindistance=", mindistance)            
end = time.clock()
print("time = " + str(end - start))

# Print agent with the max x
print(max(agents, key=operator.itemgetter(1)))
# Print agent with the max y
print(max(agents, key=operator.itemgetter(0)))

matplotlib.pyplot.ylim(0, rangey)
matplotlib.pyplot.xlim(0, rangex)
# Plot all agents
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
# Plot agent with the max y blue
m = max(agents, key=operator.itemgetter(0))
matplotlib.pyplot.scatter(m[1],m[0], color='blue')
# Plot agent with the max x red 
# (N.B. This may be the same agentas just plotted in blue!)
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()