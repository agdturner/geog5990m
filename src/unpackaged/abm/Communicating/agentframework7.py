#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  1.0.0
"""
import random

class Agent():
    
    #def __init__(self, environment):
    def __init__(self, environment, agents, random_seed):
        self.environment = environment
        self.agents = agents
        self.store = 0
        # Find out the size of environment inside the agents
        self.width = len(environment);
        self.height = len(environment[0])
        #print("width", self.width)
        #print("height", self.height)
        # Seed random so that the same results are attained each time
        #print("random_seed", random_seed)
        random.seed(random_seed)
        self._x = random.randint(0,self.width)
        self._y = random.randint(0,self.height)
        #self._x = random.randint(0,99)
        #self._y = random.randint(0,99)
        #print("x", self._x)
        #print("y", self._y)
    
    '''
    def __init__ (self):
        pass
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
    '''
    
    '''    
    def __init__ (self, x, y):
        pass
        self.x = x
        self.y = y
    '''
    
    def move(self):
        '''
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        '''
        if random.random() < 0.5:
            self._x = (self._x + 1) % self.width
        else:
            self._x = (self._x - 1) % self.width
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
        print("Hello world I am at x =", self._x, "y =", self._y)
        
    def __str__(self):
        return "Location x = " + str(self._x) + ", y = " + str(self._y) + ", store = " + str(self.store)
        
    def eat(self):
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
            self.environment[self._y][self._x] = self.environment[self._y][self._x] + 100
            #print(str(self))
            self.store = 0
            #print(str(self))
            #self.__str__.__call__
            #print("Location x =", self._x, "y =", self._y, "store =", str(self.store))
            
    def share_with_neighbours(self, neighbourhood):
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
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
   
        
        
    