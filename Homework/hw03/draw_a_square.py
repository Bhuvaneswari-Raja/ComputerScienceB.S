#!/usr/bin/env python
# coding: utf-8

# In[6]:


"""
File: draw_a_square.py
Author: Pooja Rajamanikandan
Date: 09/26/2023
Lab Section: 54
Email:  le64534@umbc.edu
Description:  This program will ask the user for a size and then draw a 
    square using stars.
"""


# In[7]:


if __name__ == "__main__":
    square_size = int(input("What is the size of the square that we want to draw? "))
    
    for x in range(square_size):
        x += 1
        if x == 1 or x == square_size:
            print("*"*square_size)
        else:
            print("*",end="")
            print(" "*(square_size-2)+"*")

