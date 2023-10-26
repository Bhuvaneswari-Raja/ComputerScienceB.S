#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
File:    pascal.py
Author:  Pooja Rajamanikandan
Date:    10/16/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: This program takes a list, and computes the next level of 
    Pascal's triangle based on the previous level
"""


# In[ ]:


def next_level(level):
    new_list = [1]
    
    for x in range(1,len(level)):
        # Makes sure index doesn't go out of bounds 
        if x+1 > len(level):
            return new_list
        new_list.append(level[x-1] + level[x])
    # Sets the last index to 1    
    new_list.append(1)
        
    return new_list
    
    
if __name__ == "__main__":
    in_string = input('What values do you want to run next_level on(w/)? ')
while in_string != '':
    values = []
    for x in in_string.strip():
        values.append(int(x))
        #print(values)
    print(next_level(values))
    in_string = input('What values do you want to run next_level on? ')


# In[ ]:




