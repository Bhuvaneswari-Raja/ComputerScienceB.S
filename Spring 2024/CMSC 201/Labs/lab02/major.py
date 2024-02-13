"""
File:    major.py
Author:  Pooja Rajamanikandan 
Date:    02/12/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: compares strings for equivalence using if-else blocks 
"""

major = input("Please enter your major: ")

if major.upper() == "CMSC" or  major.upper() == "CMPE":
    print("You need to earn at least a B for CMSC 201 to count")

else:
    print("You need to earn at least a C for CMSC 201 to count")

