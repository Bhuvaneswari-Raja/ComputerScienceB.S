#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""
File:    mad_py_lib.py
Author:  Pooja Rajamanikandan 
Date:    09/12/2023
Section: 50
E-mail:  le64534@umbc.edu
Description: MadLib using a poem
"""


# In[3]:


place_noun = input("What is a place name?")
noun_1 = input("Give an example of a noun. ")
noun_2 = input("Give an example of another noun. ")
familial_relation = input("Give an example of a familial relation. ")
name = input("Give an example of a person's name. ")
noun_3 = input("Give yet another noun. ")


print("There once was a man from",place_noun)
print("Who kept all his {} in a {}.".format(noun_1,noun_2))
print("   But his {}, name {},".format(familial_relation,name))
print("   Ran away with a {}".format(noun_3))
print("And as for the {}, {}.".format(noun_2, place_noun))


# In[ ]:




