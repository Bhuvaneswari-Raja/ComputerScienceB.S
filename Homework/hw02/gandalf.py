#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
File:        gandalf.py
Author:      Pooja Rajamanikandan
Date:        09/18/2023
Section:     50
E-mail:      le64534@umbc.edu
Description: A guessing game to detremine which "Lord of the Rings" character the user is.
"""


# In[6]:


character_race = input("Which race are you? (human/dwarf/elf/maiar/hobbit) ")

if character_race.lower() == "human":
    king_of_gondor = input("Are you the King of Gondor?  ")
    
    if king_of_gondor.lower() == "yes":
        print("You are Aragorn son of Arathorn")
    else:
        ring = input("Did you try to take the ring from Frodo? ")
        if ring.lower() == "yes":
            print("You are Boromir")
        else:
            print("You are Theoden")

elif character_race.lower() == "elf":
    matrix = input("Were you in the matrix? ")
    if matrix.lower() == "yes":
        print("You're Elrond")
    else:
        print("You're Legolas")
        
elif character_race.lower() == "maiar":
    good_or_evil = input("Are you good or evil? ")
    
    if good_or_evil.lower() == "good":
        print("You are Gandalf")
    else:
        one_ring = input("Did you forge the One Ring? ")
        if one_ring.lower() == "yes":
            print("You are Sauron")
        else: 
            print("You are Saruman")
            
elif character_race.lower() == "hobbit":
    carry_ring = input("Do you carry the One Ring? ")
    if carry_ring.lower() == "yes":
        print("You are Fordo Baggins")
    else:
        hobbit_gardener = input("Are yoy a gardener? ")
        if hobbit_gardener.lower() == "yes":
            print("You're Samwise")
        else:
            print("You are either Merry or Pippin")
            
elif character_race.lower() == "dwarf":
    print("You are Gimil son of Gloin")

else:
    print("You are an Orc, sorry about that")

        


# In[ ]:





# In[ ]:




