import random

class Agent():
    
    #def __init__(self, environment):
    def __init__(self):
        self.store = 0
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
    
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
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
    
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
            print(str(self))
            self.store = 0
            print(str(self))
            #self.__str__.__call__
            #print("Location x =", self._x, "y =", self._y, "store =", str(self.store))
        
        
    