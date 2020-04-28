# -*- coding: utf-8 -*-
"""
agentframework module to accompany the I/O script

Contains:
classes 
    Agent() -- methods for creation of agents and interactions
    
methods
    __init__() -- initialises agents and links to environment
    move() -- moves agents
    eat() -- determines interaction with environment
    __str__() -- overwrites the str() method to provide location and store details

Property attributes for self.x and self.y variables

The code that follows has in part been modified from that of
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part6/index.html
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part6/2.html
"""

import random

# Creating class for agents.
class Agent():
    """Provides methods for creating agents and defining their interactions"""

    def __init__(self, environment):
        """Creation of agent

        Positional arguments:
        environment -- list of integers (no default set)
    
        Returns:
        random integer value between 0 and 99 assigned to x
        random integer value between 0 and 99 assigned to y
        links list of agents to environment variable
        0 assigned to store variable of each agent
        """
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.store = 0

# Moving the agents.      
    def move(self):
        """Moves agents based on random number generation

        Returns:
        integer value of the modulus of 100 after the original value has been increased or decreased by one
        """
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
        if random.random() <0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            
# Eat method for interacting with environment.
    def eat(self):
        """Alters value of environment at position of agent and individual agent store dependent on original environment list value and agent store value

        Returns:
        integer value of agent store
        """
        while self.store <= 100:
            if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 10
                self.store += 10
                return self.store
            else:
                self.store += self.environment[self.y][self.x]
                self.environment[self.y][self.x] = 0
                return self.store
        # Condition if store becomes greater than 100.
            self.environment[self.y][self.x] += self.store
            self.store = 0
            return self.store

# Overwriting str method to return agent position and store value when called.
    def __str__(self):
        """Overwrites str method to allow agent position and store value to be printed

        Returns:
        string of agent position
        string of agent store
        """
        return "x = " + str(self._x) + ", y = " + str(self._y) + ", store value = " + str(self.store)


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
