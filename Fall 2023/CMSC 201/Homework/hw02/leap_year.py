"""
File:        leap_year.py
Author:      Pooja Rajamanikandan
Date:        09/18/2023
Section:     50
E-mail:      le64534@umbc.edu
Description: Determines if the year the user inputs is a leap year
"""


year = int(input("Enter a year: "))

if year % 4 == 0:    
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    elif year % 400 == 0:
        print("It is a leap year")
else:
    print("It is not a leap year")