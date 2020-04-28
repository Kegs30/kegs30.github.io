# -*- coding: utf-8 -*-
"""
Sheep and Wolves Model

Variation of an agent based model
Imports an environment in the form of a text file
Creates one set of agents (sheep) that interact with the environment
Creates a separate set of agents (wolves) that interact with the sheep

Output is modified environment as a text file
"""

import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import tkinter


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
num_of_sheep = 10
num_of_wolves = 5
num_of_iterations = 10
neighbourhood = 20
lamb_distance = 8
hunting_distance = 10
sheep = []
wolves = []


# Variables to create the matplotlib window for the animation.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

ax.set_autoscale_on(False)


# Make the agents.
# Addition of environment as argument for Agent class to allow interaction between agents and environment.
# Addition of agents as argument for Agent class to allow agents to interact with each other.
for i in range(num_of_sheep):
    sheep.append(agentframework.Agent(environment, sheep))
    
# Make the wolves.
# Use of environment and agents as arguments to allow interactions.
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolves(environment, sheep, wolves))

# Setting carry_on variable for gen_function below.
carry_on = True

# Creating model animation.
def update(frame_number):
    """Determines the code that should be run for each frame of the matplotlib animation.
    
    Return:
    None
    """
    fig.clear()
    global carry_on
  

# Loops for running the behaviour and interactions of the agents.
# Print statements used for testing.
    for j in range(num_of_iterations):
        # Shuffle function used to randomise the order sheep are processed with each iteration.
        random.shuffle(sheep)
        print("Number of sheep is " + str(len(sheep)))
    
        # Interactions if more than 1 sheep. 
        if len(sheep) > 1:
            for i in range(len(sheep)-1):
                sheep[i].move()
                sheep[i].eat()
                sheep[i].share_with_neighbours(neighbourhood)
                sheep[i].lambing(lamb_distance)
                if sheep[i].lambing(lamb_distance) == "Lamb":
                    sheep.append(agentframework.Agent(environment, sheep))
                    print("Sheep added")
                    print(len(sheep))
                    print("Sheep moved")
            # Wolf movements and interactions.
            for k in range(num_of_wolves):
                wolves[k].move()
                wolves[k].hunting(hunting_distance, sheep)
                if wolves[k].hunting(hunting_distance, sheep) == "Hunted":
                    del(sheep[0])
                    print("Sheep eaten")
                    print(len(sheep))
            # Stopping condition for animation if all sheep are eaten.
            if len(sheep) == 0:
                carry_on = False
                print("All sheep have been eaten")
                break
            # Stopping condition for animation if number of sheep is greater than or equal to 100.
            if len(sheep) >= 100:
                carry_on = False
                print("100 or more sheep in the field!")
                break
        else:
            for i in range(1):
                sheep[i].move()
                sheep[i].eat()
            # Wolf movements and interactions.
            for k in range(num_of_wolves):
                wolves[k].move()
                wolves[k].hunting(hunting_distance, sheep)
                if wolves[k].hunting(hunting_distance, sheep) == "Hunted":
                    del(sheep[0])
                    print("Sheep eaten")
                    print(len(sheep))
            # Stopping condition for animation if all sheep are eaten.
            if len(sheep) == 0:
                carry_on = False
                print("All sheep have been eaten")
                break
            break
        break
    
    
            
            
    # Generate scatterplot of sheep and wolves after model iterations.
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)   

    for i in range(len(sheep)):
        matplotlib.pyplot.scatter(sheep[i].x, sheep[i].y, color='white')
        matplotlib.pyplot.imshow(environment) 
    for j in range(num_of_wolves):
        matplotlib.pyplot.scatter(wolves[j].x, wolves[j].y, color='black')
        matplotlib.pyplot.imshow(environment) 

        
# Generator function to stop animation.
# Will stop animation after 10 iterations unless carry_on variable is set to False.
def gen_function():
    """Determines stopping condition of model
    
    Returns:
    integer value of a
    
    Code is altered from that at https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part8/examples/animatedmodel2.py
    """
    a = 1
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a = a + 1        


# Function to run model.
def run():
    """Determines how animation should be run
    
    Returns:
    None
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
# Writing the altered environment to a comma delimited text file.
def write():
    """Writes the altered environment variable as a comma delimited text file.
    
    Returns:
    None
    """
    with open("out.txt", "w", newline="") as finalenviron:
        writer = csv.writer(finalenviron, delimiter=",")
        for row in environment:
            writer.writerow(row)
    print("Output written")
    
# GUI.
# Contains canvas for animation and buttons to run and end the model.
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.grid(column = 0, columnspan = 10, row = 0)

quit_button = tkinter.Button(root, text ="End model", command=root.destroy).grid(column = 9, row = 1)
run_button = tkinter.Button(root, text = "Run model", command=run).grid(column = 0, row = 1)
write_button = tkinter.Button(root, text = "Write output", command=write).grid(column = 4, row = 1)

tkinter.mainloop()


