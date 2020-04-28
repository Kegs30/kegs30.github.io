# -*- coding: utf-8 -*-

"""
Input/Ouput practical output

The code that follows has in part been modified from that of
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part6/index.html
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part6/2.html
"""

import random
import operator
import matplotlib.pyplot
import agentframeworkIO
import csv

def distance_between(agents_row_a, agents_row_b):
    """Calculates the distance between agents using Pythagoras' theory

    Positional arguments:
    agents_row_a -- index position of agents list
    agents_row_b -- index position of agents list

    Returns:
    Distance between agents.
    """
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Reading the in.txt file to create the environment.
with open("in.txt", newline="") as raster:
    dataset = csv.reader(raster, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        
# Testing reading of data has worked.
# Expected outcome is plot with raster image.
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
            
# Setting initial parameters.
num_of_agents = 10
num_of_iterations = 10000
agents = []

# Make the agents.
# Addition of environment as argument for Agent class to allow interaction between agents and environment.
for i in range(num_of_agents):
    agents.append(agentframeworkIO.Agent(environment))
    
# Move the agents and store what they eat.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

# Testing the store for each agent works as expected.
# Expected outcome is in format "x = integer value, y = integer value, store value = integer value".
for i in range(num_of_agents):
   print(agents[i].__str__())

# Generate scatterplot of agents after model iterations.
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# Calling the distance function to calculate distance between all agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
        
# Writing the final environment to a comma delimited text file.
with open("out.txt", "w", newline="") as finalenviron:
    writer = csv.writer(finalenviron, delimiter=",")
    for row in environment:
        writer.writerow(row)
