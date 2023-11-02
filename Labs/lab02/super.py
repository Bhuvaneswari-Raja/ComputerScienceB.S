"""
File:    super .py
Author:  Pooja Rajamanikandan 
Date:    09/14/2023
Section: 50
E-mail:  le64534@umbc.edu
Description: Ask the user if they're a hero or a villian and print
 an response based on their response
"""

status = input("Are you a hero or a villain? ")

if status == "villain" :
    villain_name = input("What is your name? ")
    print(villain_name,"sounds pretty evil!")

if status == "hero" :
    people_saved = int(input("How many people have you saved? "))
    if people_saved <= 10:
        print("Go on more patrols! ")
    elif 10 < people_saved  and  people_saved < 100:
        print("Sounds like you're making a difference!")
    elif people_saved > 100:
        print("Wow, great job saving the city!")
        
    
