# -*- coding: utf-8 -*-
"""
Communication practical output

The code that follows is built upon the "Input Output.py" file.

Additional code that follows has in part been modified from that of
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part7/index.html
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part7/2.html
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part7/3.html
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part7/4.html
"""

import random
import operator
import matplotlib.pyplot
import agentframeworkcomms
import csv


# Reading the in.txt file to create the environment.
with open("in.txt", newline="") as raster:
    dataset = csv.reader(raster, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
 
                   
# Setting initial parameters.
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


# Make the agents.
# Addition of environment as argument for Agent class to allow interaction between agents and environment.
# Addition of agents as argument for Agent class to allow agents to interact with each other.
for i in range(num_of_agents):
    agents.append(agentframeworkcomms.Agent(environment, agents))
    
# Creating test instance of agent class.
a = agentframeworkcomms.Agent(environment,agents)

# Testing instance assigned to a can access other agents in the agents list.
# Expected outcome is integer values for y and x assigned to a and a different set of values for the 6th index located agent.
print(a.y, a.x)
print(a.agents[6].y, a.agents[6].x)
      

# Move the agents and store what they eat.
# Print statements included in share_with_neighbours method in agentframeworkcomms module for testing purposes.
for j in range(num_of_iterations):
    # Shuffle function used to randomise the order agents are processed with each iteration.
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        

# Generate scatterplot of agents after model iterations.
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

        
# Writing the final environment to a comma delimited text file.
with open("out.txt", "w", newline="") as finalenviron:
    writer = csv.writer(finalenviron, delimiter=",")
    for row in environment:
        writer.writerow(row)
