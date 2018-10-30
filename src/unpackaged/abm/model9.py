import agentframework9 as af
import random
#import operator
from sys import argv
import csv
import matplotlib
matplotlib.use('TkAgg') # Needs to be before any other matplotlb imports
#matplotlib.use('TkInter')
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import requests
import bs4
#import certifi
#import urllib.request
#from bs4 import BeautifulSoup as soup

'''
Step 1: Initialise parameters
'''
print(argv)
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
Step 2: Initialise GUI main window
'''
root = tkinter.Tk() # Main window.
root.wm_title("Model")

'''
Step 3: Get data from the web
'''
url = 'https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
td_zs = soup.find_all(attrs={"class" : "z"})
''' print test
#print(td_xs) 
for td in td_xs:
    print(td.text)
#print(td_ys)
#print(td_zs)
'''
''' Code exploration
#response = urllib.request.urlopen(url)
#response = urllib.request.urlopen(url, cafile=certifi.where())
#response = urllib.request.urlopen(url, data=None, cafile=None, capath=None, cadefault=False, context=None)
#data = response.read()      # a `bytes` object
#text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
# Getting elements by ID or other attributes:
table = soup.find(id="yxz")
tds = soup.find_all(attrs={"class" : "y"})
#Getting all elements of a specific tag:
trs = table.find_all('tr')
for tr in trs:
     # Do something with the "tr" variable. 
#Getting elements inside another and get their innerHTML:
tds = tr.find_all("td")
for td in tds:
    print (td.text) 
#All tags are lowercased during search
''' 

'''
Step 4: Initialise environment this will contain data about the spatial 
environment in which agents act.
'''
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
Step 5: Initialise agents.
'''
agents = []
# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    # Add 1 to random seed to get each agent initialised and moving differently
    random_seed += 1
    agents.append(af.Agent(environment, agents, random_seed, y, x))
'''
# Test getting another agent from an agent
print(agents[0].agents[1])
'''

carry_on = True

def update(frame_number):
    
    fig.clear()
    global carry_on
    
    # Process the agents in a randomish order.
    for j in range(num_of_iterations):
        if (j % 10 == 0):
            print("iteration", j)
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
            if (agents[i].store > 30):
                half_full_agent_count += 1
        if (half_full_agent_count == num_of_agents):
            carry_on = False
            print("stopping condition")
                
        # Stop randomly
        '''
        if random.random() < 0.1:
            carry_on = False
            print("stopping condition")
        '''
        
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety())
            #print(agents[i].getx(),agents[i].gety())

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
'''
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety())
'''

#matplotlib.pyplot.show()

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

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()



canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop() # Wait for interactions.