#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
File:    checkerboard.py
Author:  Pooja Rajamanikandan
Date:    10/16/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: The program will draw a checkerboard pattern using the symbols the user inputs
"""


# In[16]:


def checkerboard(size, symbol_1, symbol_2):
    switch = 1
    #Outer loop for the columns 
    for c in range(size):
        #Inner loop for the rows
        for r in range(size):
            #Alternates between the symbols
            if switch == 1:
                print(symbol_1,end="")
                switch = 2
            elif switch == 2:
                print(symbol_2,end="")
                switch = 1
        print()

if __name__ == "__main__":
    size = int(input("What size do you want? "))
    symbols = input("What symbols do you want? ")
    
    temp_list = symbols.split()
    checkerboard(size, temp_list[0], temp_list[1])
    


# In[4]:


for x in range(1,3+1):
    print(x)


# In[ ]:




