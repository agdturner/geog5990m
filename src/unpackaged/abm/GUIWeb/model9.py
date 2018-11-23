#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  0.1.0

This model is run from a GUI in which there is a run menu.
When you run this code it is expected that a window will appear on your 
computer screen. To run the model, find this window and select run from the
menu bar.
"""
import agentframework9 as af
import random
#import operator
from sys import argv
import csv
import matplotlib
matplotlib.use('TkAgg') # Needs to be before any other matplotlb imports
#matplotlib.use('TkInter')
import matplotlib.pyplot as pyplot
import matplotlib.animation as anim
import tkinter
import requests
import bs4
#import certifi
#import urllib.request
#from bs4 import BeautifulSoup as soup
#import sys
import os

"""
Step 1: Initialise parameters
"""
print("Step 1: Initialise parameters")
print("argv", argv)
if len(argv) < 6:
    num_of_agents = 10
    num_of_iterations = 20
    neighbourhood = 20
    random_seed = 0
    agent_store = 90
    print("argv does not contain the expected number of arguments")
    print("len(argv)", len(argv))
    print("expected len(argv) 5")
    print("expecting:")
    print("argv[1] as a integer number for num_of_agents")
    print("argv[2] as a integer number for num_of_iterations")
    print("argv[3] as a integer number for neighbourhood")
    print("argv[4] as a integer number for random_seed for setting the random seed")
    print("argv[5] as a integer number for between 0 and 100. This is the level that if all agents stores reach, the program ends.")
else:
    # set parameters from argv
    num_of_agents = int(argv[1])
    num_of_iterations = int(argv[2])
    neighbourhood = int(argv[3])
    random_seed = int(argv[4])
    agent_store = int(argv[5])
print("num_of_agents", str(num_of_agents))
print("num_of_iterations", str(num_of_iterations))
print("neighbourhood", str(neighbourhood))
print("random_seed", str(random_seed))
random.seed(random_seed)

"""
Step 2: Initialise GUI main window.
"""
print("Step 2: Initialise GUI main window")
root = tkinter.Tk() # Main window.
root.wm_title("Model")

"""
Step 3: Get data from the web.
"""
print("Step 3: Get data from the web.")
url = 'https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
td_zs = soup.find_all(attrs={"class" : "z"})
# Note that there is a new range in the data read in and agents are only 
# initialise in the first 100 by 100 npart of enviroement
""" print test
#print(td_xs) 
for td in td_xs:
    print(td.text)
#print(td_ys)
#print(td_zs)
"""
""" Code exploration
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
""" 

"""
Step 4: Initialise environment this will contain data about the spatial 
environment in which agents act.
"""
print("Step 4: Initialise environment this will contain data about the",
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

"""
Step 5: Initialise agents.
"""
print("Step 5: Initialise agents.")
agents = []
# Make the agents.
for i in range(num_of_agents):
    j = i
    while (i > len(td_ys)): # ensure we don't fall off the end of the array
        j -= len(td_ys)
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    # Add 1 to random seed to get each agent initialised and moving differently
    random_seed += 1000
    agents.append(af.Agent(environment, agents, random_seed, y, x))

"""
Step 6: Initialise the GUI
"""
print("Step 6: Initialising GUI.")
# Set up the figure and loop variables.
fig = pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
init = True
halted = False
rerunid = 0
total_ite = 0;
print("A GUI window should appear. Please select \"Run Model\" from the \"Model\" menu to run the model.")

"""
Step 7: Animate acting agents.
"""
def update(frame_number):
    """
    Updates the display in the animation.
    """
    global carry_on
    global init
    global halted
    global rerunid
    if (init == True):
        print("Step 7: Animate acting agents.")
        print("Start .", end='')
        init = False
    else:
        if (halted):
            rerunid += 1
            print("Continuing", rerunid, end='')
            halted = False
        else:
            print(" .", end='')
        
    fig.clear()
    """
    Clear the figure
    """
   
    # Process the agents in a randomish order.
    if (carry_on):
        # Shuffle agents
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        # Stop if all agents have more than agent_store store
        half_full_agent_count = 0
        for i in range(num_of_agents):
            if (agents[i].store > agent_store):
                half_full_agent_count += 1
        if (half_full_agent_count == num_of_agents):
            carry_on = False
            print(" all agent stores are greater than", agent_store, "run ended after ", end='')
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
    """
    A halting function for the animation.
    """
    a = 0
    global carry_on
    global halted
    global total_ite
    while  (a < num_of_iterations) & (carry_on): 
        yield a			#: Returns control and waits next call.
        a = a + 1
        total_ite += 1
    halted = True
    if (a == num_of_iterations):
        print(" run stopped after", total_ite, "iterations.")
    else:
        print(total_ite, "iterations.")
        exiting()
    
#animation = anim.FuncAnimation(fig, update, interval=1)
#animation = anim.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = anim.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
animation = anim.FuncAnimation(fig, update, frames=gen_function, repeat=False)
"""
Create animated plot. Continues to update the plot until stopping criteria is 
met.
"""

#pyplot.show()
#"""Display the plot."""
def run():
    global animation
    animation = anim.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    #canvas.show()
    canvas.draw()

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
#model_menu.add_command(label="Exit", command=root.quit)
#model_menu.add_command(label="Destroy", command=root.destroy)
"""
Since overriding the WM_DELETE_WINDOW protocol the preceding (now commented) 
two commented lines of code are no longer needed.
"""

# The process is quit as well as destroying the main window (root) on exit
def exiting():
    """
    Write output files and exits killing the GUI window.
    """
    if halted == False:
        print(" run stopped after", total_ite, "iterations.")
    
    '''
    Step 8: Write out the environment to the file dataout.csv.
    '''
    print("Step 8: Write out the environment to the file dataout.csv.")
    file = os.path.join(outputdatadir, 'dataout.csv')
    with open(file, 'w', newline='') as f2:
        writer = csv.writer(f2, delimiter=' ')
        for row in environment:
            writer.writerow(row)
    
    '''
    Step 9: Calculate total amount stored by all the agents and append this to the
    file dataout2.txt.
    '''
    print("Step 9: Calculate total amount stored by all the agents and append",
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
    print("Step 10: End Program.")
    #print("we're here")
    root.quit()
    root.destroy()
    #sys.exit(0)

root.protocol('WM_DELETE_WINDOW', exiting) 

tkinter.mainloop() # Wait for interactions.

print("Thank you for running the model.")