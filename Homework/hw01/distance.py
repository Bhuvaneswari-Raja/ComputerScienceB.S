#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
File:    distance.py
Author:  Pooja Rajamanikandan 
Date:    09/12/2023
Section: 50
E-mail:  le64534@umbc.edu
Description: Ask the user questions for two points, then calucalting the
    distance between those points using the distance formula
"""


# In[4]:


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = ((x2 - x1)**2)**1/2 + ((y2 - y1)**2)**1/2

print("The distance between ({}, {}) and ({}, {}) is".format(x1,y1,x2,y2), distance)


# In[ ]:




