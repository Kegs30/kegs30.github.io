# -*- coding: utf-8 -*-
"""
agentframework module to accompany the sheep wolves model script

Contains:
classes 
    Agent() -- methods for creation of agents and interactions
    
methods
    __init__() -- initialises agents and links to environment
    move() -- moves agents
    eat() -- determines interaction with environment
    __str__() -- overwrites the str() method to provide location and store details
    distance_between() -- calculates distance between agents
    share_with_neighbours() -- averages agents stores if distance between them is less than neighbourhood parameter
    lambing() -- creates new agents if distance between agents is less than lambing_distance parameter

Property attributes for self.x and self.y variables

subclass
    Wolves() -- methods for creation of wolf agents and interactions
    
methods
    __init__() -- initialises agents and links to environment
    move() -- moves agents
    prey_distance() -- calculates distance between agents
    hunting() -- removes agents if distance between agents is less than pre_distance parameter
    
Property attributes for self.x and self.y variables

This code is built upon the "agentframeworkanimate.py" file.
"""

import random

# Creating class for agents.
class Agent():
    """Provides methods for creating agents and defining their interactions"""
    
    def __init__(self, environment, agents):
        """Creation of agent

        Positional arguments:
        environment -- list of integers (no default set)
        agents -- list of objects (no default set)
    
        Returns:
        random integer value between 0 and 99 assigned to x
        random integer value between 0 and 99 assigned to y
        links list of agents to environment variable
        0 assigned to store variable of each agent
        links agent to list of agents
        """
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents

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

        
# Distance between agents method.
    def distance_between(self, agent):
        """Calculates the distance between agents using Pythagoras' theory
        Use of if statement to default calculations against self to 100

        Positional arguments:
        agent -- list of objects (no default set)

        Returns:
        integer value of distance
        """ 
        #if (self.x == agent.x) and (self.y == agent.y):
            #return 100
        #else:
        return (((self.x - agent.x) ** 2) + ((self.y - agent.y) ** 2)) ** 0.5
        
# Share with neighbours method. 
# Print statements for testing
    def share_with_neighbours(self, neighbourhood):
        """Splits value of agent's store if agents are within neighbourhood distance
        
        Positional arguments:
        neighbourhood -- integer value (no default set)
        
        Returns:
        None
        """
        for agent in self.agents:
            distance = self.distance_between(agent)
            if (distance > 0) and (distance <= neighbourhood):
                #print("Under 20")
                #print(distance)
                #print(self.x, self.y)
                #print(agent.x, agent.y)
                total_store = self.store + agent.store
                average = total_store / 2
                self.store = average
                agent.store = average    
            #else:
                #print("Over 20")
                #print(distance)
                
# Lambing method.
    def lambing(self, lamb_distance):
        """Generates new agent (sheep) when agents are within lamb distance
        
        Positional arguments:
        lamb_distance -- integer value (no default set)
        
        Returns:
        Boolean
        """
        for agent in self.agents:
            distance = self.distance_between(agent)
            if (distance > 0) and (distance <= lamb_distance):
                return "Lamb"

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
    
# Wolves subclass.
class Wolves(Agent):
    """Subclass of Agent class"""
    
    def __init__(self, environment, agents, wolves):
        """Creation of wolf agents
        
        Positional arguments:
        environment -- list of integers (no default set)
        agents -- list of objects (no default set)
        wolves -- list of objects (no default set)
    
        Returns:
        random integer value between 0 and 99 assigned to x
        random integer value between 0 and 99 assigned to y
        links list of wolves to environment variable
        links wolf to list of agents
        links wolf to list of wolves
        """
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.wolves = wolves
        
# Moving the wolves.
    def move(self):
        """Moves wolves based on random number generation

        Returns:
        integer value of the modulus of 100 after the original value has been increased or decreased by five
        """
        if random.random() < 0.5:
            self._x = (self._x + 5) % 100
        else:
            self._x = (self._x - 5) % 100
            
        if random.random() <0.5:
            self._y = (self._y + 5) % 100
        else:
            self._y = (self._y - 5) % 100
            
# Prey distance.
    def prey_distance(self, agent):
        """Calculates the distance between wolf and agent using Pythagoras' theory
        
        Positional arguments:
        agent -- list of objects (no default set)
        
        Returns:
        integer value of distance
        """
        return (((self.x - agent.x) ** 2) + ((self.y - agent.y) ** 2)) ** 0.5
    
# Hunting method,
    def hunting(self, hunting_distance, agents):
        """Removes an agent (sheep) if wolf is within hunting_distance
        
        Positional arguments:
        hunting_distance - integer value (no default set)
        
        Returns:
        Boolean
        """
        for agent in agents:
            wolf_distance = self.prey_distance(agent)
            if wolf_distance <= hunting_distance:
                return "Hunted"
        
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
