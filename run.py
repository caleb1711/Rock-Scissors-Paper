# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


"""set the Game's optoins"""

options = ("rock", "paper", "scissors")
running = True


"""computer chooses randomly between the options"""
while running:
    
        player = None
        computer = random.choice(options)

