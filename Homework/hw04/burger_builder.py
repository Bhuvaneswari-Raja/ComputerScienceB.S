#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
File:    burger_builder.py
Author:  Pooja Rajamanikandan
Date:    10/02/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: build a hamburger or cheeseburger using the User input.
    Print out all the condiments in the burger and diplays if it was
    n-number of cheeseburger or hamburger.
"""


# In[ ]:


if __name__ == "__main__":
    bun = input("What do you want to add? ")
    condiment_list = list()
    cheese_counter = 0
    burger_counter = 0
    
    while bun != "bottom bun":
        print("You must start with the bottom bun!")
        bun = input("What do you want to add? ")
            
    while bun.lower() == "bottom bun":
        condiments = input("What do you want to add? ")
        #adds all condiements to the list except for top bun, cheese, and burger 
        if condiments != "cheese" and condiments != "top bun" and condiments != "burger":
            condiment_list.append(condiments)
        
        #counts the number of cheese
        if condiments.lower() == "cheese":
            cheese_counter += 1
        #counts the number of burger 
        if condiments.lower() == "burger":
            burger_counter += 1
        #sets the bun to top bun
        if condiments == "top bun":
            bun = "top bun"
            
    if cheese_counter > 0:
        print("You have created a {}-cheeseburger with the condiments: ".format(cheese_counter))
        for x in condiment_list:
            print(x,end=", ")
    else:
        print("You have created a {} -hamburger with the condiments: ".format(burger_counter))
        for x in condiment_list:
            print(x,end=", ")
        


# In[ ]:




