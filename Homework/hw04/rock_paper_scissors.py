#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""
File:    rock_paper_scissors.py
Author:  Pooja Rajamanikandan
Date:    10/02/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: This program implements a game of rock, paper, scissors
    against the user and computer
"""


# In[ ]:


import sys from random import choice, seed
if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":
    
    
    user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")
    choice_list = ["rock","paper","scissors"]
    
    
    while user_choice != "stop":
        computer_choice =  choice(choice_list)
        
        #checks invalid input
        if user_choice not in choice_list:
            print("You need to select rock, paper or scissors")
            user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")
            
        #checks for a tie
        if user_choice == computer_choice:
            print("Both",user_choice,",It's a tie")
            user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")
        
        #checks against computer_choice if user_choice is rock
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Paper covers rock, you lose")
            elif computer_choice == "scissors":
                print("Rock crushes scissors, you win.")
            user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")
        
        #checks against computer_choice if user_choice is paper
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock, you win")
            elif computer_choice == "scissors":
                print("Scissors cuts paper, you lose")
            user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")
        
        #checks against computer_choice if user_choice is scissors
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Rock crushes scissors, you lose.")
            elif computer_choice == "paper":
                print("Scissors cuts paper, you win")
            user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")



# In[ ]:




