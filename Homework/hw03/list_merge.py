#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
File: list_merge.py
Author: Pooja Rajamanikandan
Date: 09/26/2023
Lab Section: 50
Email:  le64534@umbc.edu
Description: merger two lists containing inputs from the user
"""


# In[14]:


list_size = int(input("How  many elements do you want in each list? "))
list_1 = []
list_2 = []
merged_list = [] 

for x in range(list_size):
    first_list_element = input("What do you want to put in the first list? ")
    list_1.append(first_list_element)

for x in range(list_size):
    second_list_element = input("What do you want to put in the second list? ")
    list_2.append(second_list_element)



for x in range(list_size):
    merged_list.append(list_1[x])    
    merged_list.append(list_2[x])    

print("The first list is: ",list_1)
print("The second list is: ",list_2)
print("The merged list is:  ",merged_list)  

