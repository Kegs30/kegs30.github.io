# sheepwolves.github.io

## Contents

### Main Model
- sheep wolves model.py
- sheep wolves model Development.py
- agentframewor.py
- in.txt

### Development Work
In the Development folder:
- Agents!.py
- Agents! Development.py
- agentframeworkagents.py
- Input Output.py
- Input Output Development.py
- agentframeworkIO.py
- Communications.py
- Communications Development.py
- agentframeworkcomms.py
- Animation.py
- Animation Development.py
- agentframeworkanimate.py
- tkinter interface.py

### Auxilary Documents
- README document
- LICENSE document


## Outline
The software is an agent based model that takes an environment input and modifies it based on the interactions of several agents.

It is based on the interactions of sheep grazing and breeding in a landscape with their population controlled by wolves as predators.

The model first takes a raster text file (supplied by the University of Leeds) and creates an environment variable that can be displayed in a matplotlib window.

The model then generates a series of objects using the agentframework module and assigns them to the sheep and wolf lists.

The agentframework module contains the class Agent which contains the methods for the sheep agent creation and interactions. It also contains the subclass wolves which creates the wolf agents. The wolf agents have similar but slighlty different methods to the sheep agents and they are linked to the sheep agents to allow interactions.

Once the agents have been created, the model runs through the main behaviour and interactions. The behaviour of the sheep agents includes:
- moving across the environment
- eating the environment (or regurgitating if they have eaten too much)
- sharing their food with other sheep agents
- breeding with other sheep agents to generate new sheep
The last two behaviours are dependent on the distance between the sheep agents and therefore may not occur on every iteration.

The behaviour of the wolf agents includes:
- moving across the environment
- hunting and removing sheep agents
The hunting behaviour is dependent on the distance between the wolf and sheep agents and therefore may not occur on every iteration.

The model is set to run as a matplotlib animation. This will show the movement of the sheep and wolves and the impact on the environment. The sheep appear as white dots and the wolves as black dots.

The model will end once one of the following conditions is met:
- ten iterations of the sheep and wolf behaviour
- all the sheep have been eaten
- there are 100 or more sheep in the field

Once the model has run, a comma delimited text file called "out" can be saved in the working directory with the altered environment.


## How to run the model
Take copies of the "sheep wolves model.py", "agentframework.py" and "in.txt" files and save them to your working directory.

The program has been built and tested in Spyder. It has a tkinter graphic GUI so please ensure the tkinter option is selected as the Graphic backend before running the model. This can be found under Tools - Preferences - IPython Console - Graphics tab.

When the sheep wolves model is run, a tkinter window will appear with three buttons at the bottom of the screen. Select the "Run model" button to run the model - the matplotlib animation will appear in the window with comments on the state of the model in the console window. Once the model has run, you can select "Run model" to run the model again but using the outputs from the previous model as the starting point. When you wish to save the altered environment as an output, click "Write output". This will generate a comma delimited text file of the current environment in the working directory and call it "out.txt". Click "End model" to close the tkinter window. You may need to manually stop the IPython console at this point.


## Issues
In creating this program a number of issues were encountered:

### The creation of new sheep agents
I adapted the code used for sharing the stores with neighbouring sheep (sharing_with_neighbours method) to allow the sheep to breed and generate a new sheep agent when they were within a set distance of each other (see lambing method in agentframework module). However, I could not pass the arguments to add new sheep agents as part of the lambing method itself because the variables required by the __init__ method did not exist in the module.

To resolve this issue, I set the lambing method to return a string when the distance argument was met. The evaluation of this string is then included in the main model and sheep agents are added as necessary. I then adapted this method to create the hunting and prey distance methods for the wolf agents.

### The distance_between method included self comparisons
After implementing the lambing method, I found the number of sheep agents increased on every iteration of the model even when I changed the number of sheep agents to 1. This was due to the sheep agents measuring the distance from and to themselves as well as all the other sheep agents. 

To avoid cloning, I added in an extra condition to the lambing method to test whether the distance measured was greater than zero and less than the lambing distance. This prevented the distance measured from a sheep agent to itself generating a new sheep agent.

### The GUI development
Whilst I have managed to add a basic GUI to the program, I struggled to add further functionality. I attempted to add in scale bars to enable the user to set the initial paramters of the model. Unfortunately, I could not get the structure of this part of the program to work. This part of the GUI would need to be positioned at the beginning of the code but the other part with the animation needs to be at the end to allow the code to be parsed first. I attempted to add a separate GUI window to just set the parameters but then I struggled to create a command that would enable the main code to run afterwards. My code for the parameter settings GUI can be found in the Development folder entitled "tkinter interface.py".


## Development
The development of this program can be seen in the files in the development folder. The order they should be read in is:
	- Agents
	- I/O
	- Communicating
	- Animation

Each version of the model is built on the previous ones. Any file with "development" in the name will include the print statements used for testing various stages of the model. These are commented out of the final versions where relevant.

All the code was originally based on code developed by Dr Andy Turner of the University of Leeds for this course (https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/). Specific URLs for different files can be found in the introductory comments for each file.

Future development of this program is to establish a more functional GUI with tkinter interface for setting the initial parameters, such as the number of sheep and wolves. Please see "tkinter interface.py" in the development folder for mock up of anticipated GUI structure. This would involve restructuring the main part of the code as indicated in the Issues section above.

Further development would be to allow for environments to be eaten to nothing or with little resources originally. Development could also include changes to the speed of agents, different agents (such as rabbits) or an environment with mixed vegetation (e.g. grass, trees, scrubland).
 
