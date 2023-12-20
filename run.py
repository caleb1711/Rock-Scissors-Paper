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
        score = 0
        
        
        """ Defines player input and checks game status"""

        while player not in options: 
            player = input("Enter a choice (rock, paper, scissors): ")

        print(f"player: {player}")
        print(f"computer: {computer}")

        if player == computer:
            print("It's a tie!")

        elif player == "rock" and computer == "scissors":
            print("You WIN!")
            
        elif player == "paper" and computer == "rock":
            print("You WIN!")

        elif player == "scissors" and computer == "paper":
            print("You WIN!")
            

        else:
            print("You Lost!")

        """ Options to continue or exit Game""" 
           
        if not input("Play again? (y/n): ").lower() == "y":
            running = False










