#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  1.0.0

Holds a basic Agent class. Agents have a location in a 2D plane represented by 
a raster environment which is shared as is a list of all other agents with all 
other agents in the environment.
"""
import random

class Agent():
    
    #def __init__(self, environment):
    def __init__(self, environment, agents, random_seed, x, y):
        """
        Initialises an agent.
        
        Postional arguments:
        environment -- the raster environment to be shared with all agents.
        agents -- a reference to all agents in environmet
        random_seed -- a number used to initialise the random seed for this 
        agent
        x -- the x axis locational coordinate for this agent.
        y -- the y axis locational coordinate for this agent.
        """
        self.environment = environment
        self.agents = agents
        self.store = 0
        # Find out the size of environment inside the agents
        self.width = len(environment);
        self.height = len(environment[0])
        # Seed random so that the same results are attained each time
        #print("random_seed", random_seed)
        if (random_seed == None):
            random.seed(0) # defaul random seed to 0
        else:
            random.seed(random_seed)
        if (x == None):
            self._x = random.randint(0,self.width)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,self.height)
        else:
            self._y = y
        random.randint(0,self.width)
        #print("x", self._x)
        #print("y", self._y)
      
    def move(self):
        """
        Moves an agent though there is a 1 in 3 chance of not moving in either 
        the x or y direction.
        """
        if random.random() >= 1/float(3):
            if random.random() < 0.5:
                self._x = (self._x + 1) % self.width
            else:
                self._x = (self._x - 1) % self.width
        if random.random() >= 1/float(3):
            if random.random() < 0.5:
                self._y = (self._y + 1) % self.height
            else:
                self._y = (self._y - 1) % self.height
    
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    @property
    def y(self):
        """I'm the 'y' property."""
        return self._y
    
    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def hi(self):
        """
        Prints the Agent location of an agent to std.out
        """
        #print("Agent location: x =", self._x, "y =", self._y)
        print(self)
        
    def __str__(self):
        """
        Returns:
        A description of the agent detailing it's location and store.
        """
        return "Location x = " + str(self._x) + ", y = " + str(self._y) + ", store = " + str(self.store)
        
    def eat(self):
        """
        Agent eats/removes some of environemnt. If their store gets to be 
        greater than 100, then 50% of it is dumped into the environment.
        """
        # If more than 10 get 10
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            # Store what is left
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
        #print(str(self.store))
        if self.store > 100:
            self.environment[self._y][self._x] = self.environment[self._y][self._x] + 50
            #print(str(self))
            self.store = 50
            #print(str(self))
            #self.__str__.__call__
            #print("Location x =", self._x, "y =", self._y, "store =", str(self.store))
            
    def share_with_neighbours(self, neighbourhood):
        """
        Agent shares some of store with neighbours.
        
        Postional arguments:
        neighbourhood -- the distance within which agents share an instance of this Agent class
        """
        #print(neighbourhood)
        for agent in self.agents:
            # Don't share with self for speed (not that it matters much)
            if(self != agent):
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    #print("sharing " + str(dist) + " " + str(ave))
 
    def distance_between(self, agent):
        """
        Calculate and return the distance between self and agent.
        
        Postional arguments:
        agent -- an instance of this Agent class
        
        Returns: Number
        The distance between self and agent.
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
   
        
        
    