"""
File:    major.py
Author:  Pooja Rajamanikandan 
Date:    09/14/2023
Section: 50
E-mail:  le64534@umbc.edu
Description: compares strings for equivalence using if-else blocks 
"""

major_name = input("Please enter your major: ")

if(major_name == "CMSC" or  major_name == "CMPE"):
    print("You need to earn at least a B for CMSC 201 to count")

else:
    print("You need to earn at least a C for CMSC 201 to count")

