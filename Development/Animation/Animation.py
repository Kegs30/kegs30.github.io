# -*- coding: utf-8 -*-
"""
Animation practical output

The code that follows builds on the "Communications.py" file

Additional code that follows has in part been modified from that of
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part8/index.html
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part8/examples/animatedmodel.py
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part8/examples/animatedmodel2.py
"""

import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframeworkanimate
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

# Variables to animate the model.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

ax.set_autoscale_on(False)

# Make the agents.
# Addition of environment as argument for Agent class to allow interaction between agents and environment.
# Addition of agents as argument for Agent class to allow agents to interact with each other.
for i in range(num_of_agents):
    agents.append(agentframeworkanimate.Agent(environment, agents))


carry_on = True

# Creating model animation.
def update(frame_number):
    fig.clear()
    global carry_on    

# Move the agents and store what they eat
    for j in range(num_of_iterations):
        # Shuffle function used to randomise the order agents are processed with each iteration.
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
        # Stopping condition for animation when all agents have 100 in their store.
        if agents[i].store == 100:
            carry_on = False
            print("Stopping condition met")

    # Generate scatterplot of agents after model iterations.
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
# Generator function to stop animation.
# Will stop animation after 10 iterations unless carry_on variable is set to False.
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 100) & (carry_on):
        yield a
        a = a + 1        

# Animation will run until generator function condition is met
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()

        
# Writing the final environment to a text file.
with open("out.txt", "w", newline="") as finalenviron:
    writer = csv.writer(finalenviron, delimiter=",")
    for row in environment:
        writer.writerow(row)
