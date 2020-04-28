import random
import operator
import matplotlib.pyplot
import agentframeworkagents

"""
Agents! practical output

The code that follows has in part been modified from that of 
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part5/index.html
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part5/2.html
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part5/3.html
"""

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

# Testing Agent class by creating single agent.
# Expected outcome of print statement is two random integer values between 0 and 99.
a = agentframeworkagents.Agent()
print(a.y, a.x)

# Testing move method with single agent.
# Expected outcome of print statement is two integer values that have changed by 1 from original value.
a.move()
print(a.y, a.x)

# Setting initial parameters
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframeworkagents.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

# Generate scatterplot of agents after model iterations.
# The following code was provided by Dr Andy Turner
# from https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part5/index.html
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# Calling the distance function to calculate distance between all agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
