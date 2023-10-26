#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
File:        leap_year.py
Author:      Pooja Rajamanikandan
Date:        09/18/2023
Section:     50
E-mail:      le64534@umbc.edu
Description: In order to open the lock, the user has to input two numbers
    that have the sum of 36 and the correct switch combination 
"""


# In[8]:


first_num  = int(input("What is the first number in the combination lock? "))
second_num = int(input("What is the second number in the combination lock? "))
first_switch = input("What is the position of the first switch (up/down)? ")
second_switch = input("What is the position of the second switch (up/down)? ")
third_switch = input("What is the position of the third switch (up/down)? ")

sum = first_num + second_num
#locker_movement = True

if first_switch == "up" and (second_switch == "up" or third_switch == "up"):
    locker_movement = True    
elif second_switch == "up" and (first_switch == "up" or third_switch == "up"):
    locker_movement = True    
elif third_switch == "up" and (second_switch == "up" or first_switch == "up"):
    locker_movement = True    
else:
    locker_movement = False
    
if sum == 36 and locker_movement:
    print("The lock opens, you gain access to the treasure.")
elif sum == 36 or locker_movement:
    print("The lock clanks but does not open.")
else:
    print("The lock does not even budge, try again.")
    


# In[ ]:




