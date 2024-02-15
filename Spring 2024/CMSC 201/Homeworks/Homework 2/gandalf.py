"""
File:    will_it_float.py
Author:  Pooja Rajamanikandan
Date:    02/12/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: A guessing game to detremine which "Lord of the Rings" character the user is.
"""

race = input("Which race are you? (human/dwarf/elf/maiar/hobbit) ")

if race.lower() == "human":
    king_of_gondor = input("Are you the King of Gondor?  ")
    
    if king_of_gondor.lower() == "yes":
        print("You are Aragorn son of Arathorn")
    else:
        ring = input("Did you try to take the ring from Frodo? ")
        if ring.lower() == "yes":
            print("You are Boromir, poor guy...")
        else:
            print("You're probably Theoden")

elif race.lower() == "elf":
    matrix = input("Were you in the matrix? ")
    if matrix.lower() == "yes":
        print("You are Agent Smith, I mean... Elrond")
    else:
        print("You're Legolas")
        
elif race.lower() == "maiar":
    good_or_evil = input("Are you good or evil? ")
    
    if good_or_evil.lower() == "good":
        print("You are Gandalf")
    else:
        one_ring = input("Did you forge the One Ring? ")
        if one_ring.lower() == "yes":
            print("You are Sauron")
        else: 
            print("You are Saruman")
            
elif race.lower() == "hobbit":
    carry_ring = input("Do you carry the One Ring? ")
    if carry_ring.lower() == "yes":
        print("You are Fordo Baggins")
    else:
        hobbit_gardener = input("Are you a gardener? ")
        if hobbit_gardener.lower() == "yes":
            print("You're Samwise")
        else:
            print("You are either Merry or Pippin")
            
elif race.lower() == "dwarf":
    print("You are Gimil son of Gloin")

else:
    print("You are an Orc, sorry about that")