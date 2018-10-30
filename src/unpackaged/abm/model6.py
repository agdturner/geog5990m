import csv
import matplotlib
import agentframework6 as af
#import random
#import operator
import matplotlib.pyplot

environment = []
 
# read csv into environment
'''
f = open('in.txt', newline='') 
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
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
            #print(value)
        environment.append(rowlist)

'''
def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a.getx() - agents_row_b.getx()))**2) + 
     ((agents_row_a.gety() - agents_row_b.gety())**2))**0.5
'''
'''
def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a.x() - agents_row_b.x()))**2) + 
     ((agents_row_a.y() - agents_row_b.y())**2))**0.5
'''

num_of_agents = 10
num_of_iterations = 1000
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(af.Agent(environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety())
matplotlib.pyplot.show()

'''
for agents_row_a in agents:
     for agents_row_b in agents:
         distance = distance_between(agents_row_a, agents_row_b) 
'''
        
# Write out the environment as a file
'''
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environment: 
    writer.writerow(row) # List of values.
f2.close() 
'''
with open('dataout.csv', 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=' ')
    for row in environment:
        writer.writerow(row)
        '''
        for value in row:
            print(value)
            #writer.write(value)
        '''
        
# Calculate total amount stored by all the agents
total = 0
for a in agents:
    total += a.store
    #print(total)

# Append total to dataout2.txt
with open("dataout2.txt", "a") as f3:
    f3.write(str(total) + "\n")
    #f3.write("\n")
    f3.flush  
f3.close