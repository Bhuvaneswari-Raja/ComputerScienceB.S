"""
File:    will_it_float.py
Author:  Pooja Rajamanikandan
Date:    02/12/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will determine if the object entered by the user will 
    sink, float, or have neutral buoyancy.
"""

race = input("Which race are you? (human/dwarf/elf/maiar/hobbit) ")

if race.lower() == "human":
    answer = input("Are you the King of Gondor? ")
    if answer.lower() == "yes":
        print("You are Aragorn son of Arathorn")
    else:
        frodo = input("Did you try to take the ring from Frodo? ")
        if frodo.lower() == "yes":
            print("You are Boromir, poor guy...")
        else:
            print("Theoden")
elif race.lower() == "elf":
    answer = input()
    if answer.lower() == "yes":
        print()
    else:
        print
elif race.lower() == "maiar":
    answer = input
    if answer.lower() == "good":
        print
    if answer.lower() == "evil":
        answer = input
        if answer.lower() == "yes":
            print 
        else:
            print
elif race.lower() == "hobbit ":
    print
elif race.lower() == "dwarf":
    print
else:
    print("You are an Orc, sorry about that")
