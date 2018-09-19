import operator
import random
import matplotlib.pyplot

agents = [] # Create a new empty list for coordinates. 

agents.append([random.randint(0,99),random.randint(0,99)]) # Add y0,x0 to agents
agents.append([random.randint(0,99),random.randint(0,99)]) # Add y1,x1 to agents

print("agents[0][1]", agents[0][1])
print("agents[0][0]", agents[0][0])

print("agents[1][1]", agents[1][1])
print("agents[1][0]", agents[1][0])

distance = ((agents[0][1] - agents[1][1])**2 + (agents[0][0] - agents[1][0])**2)**0.5
print("distance "); print(distance)

print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
#matplotlib.pyplot.scatter(max(agents, key=operator.itemgetter(1)), color='red')
matplotlib.pyplot.show()