# -*- coding: utf-8 -*-
"""
agentframework module to accompany the Agents! script

Contains:
classes 
    Agent() -- methods for creation of agents and interactions
    
methods
    __init__() -- initialises agents and links to environment
    move() -- moves agents

Property attributes for self.x and self.y variables
"""

import random

class Agent():
    """Provides methods for creating agents and defining their interactions"""
    
    def __init__(self):
        """Creation of agent
    
        Returns:
        random integer value between 0 and 99 assigned to x
        random integer value between 0 and 99 assigned to y
        """
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)


# Moving the agents.       
    def move(self):
        """Moves agents based on random number generation

        Returns:
        integer value of the modulus of 100 after original value has been increased or decreased by one
        """
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
        if random.random() <0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            

# Setting the properties for x.            
    def getx(self):
        return self._x
    
    def setx(self, value):
        self._x = value
        
    def delx(self):
        del self._x
        
    x = property(getx, setx, delx, "I'm the 'x' property.")
    
# Setting the properties for y.
    def gety(self):
        return self._y
    
    def sety(self, value):
        self._y - value
        
    def dely(self):
        del self._y
            
    y = property(gety, sety, dely, "I'm the 'y' property.")
