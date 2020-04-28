# -*- coding: utf-8 -*-
"""
Mock up of GUI interface for sheep wolves model.

Includes a tkinter window with scale bars to set initial parameters.
"""

import tkinter

settings = tkinter.Tk()
settings.wm_title("Parameters for model")

sheep_label = tkinter.Label(settings, text = "Number of Sheep:", pady = 5).grid(column = 0, row = 0, sticky = "S")
wolf_label = tkinter.Label(settings, text = "Number of Wolves:").grid(column = 0, row = 1, pady = 5, sticky = "S")

# Scale bars used to set initital parameters for model.
sheep_scale = tkinter.Scale(settings, from_ = 1, to = 10, orient = "horizontal", length = 150, variable = num_of_agents).grid(column = 1, row = 0, sticky = "W")
wolf_scale = tkinter.Scale(settings, from_ = 0, to = 5, orient = "horizontal", length = 75, variable = num_of_wolves).grid(column = 1, row = 1, sticky = "W")

# Button to run model once scale bars have been set.
# Would include a command function to run the model when initiated.
run_model = tkinter.Button(settings, text = "Run model").grid(column = 1, row = 2)

settings.mainloop()