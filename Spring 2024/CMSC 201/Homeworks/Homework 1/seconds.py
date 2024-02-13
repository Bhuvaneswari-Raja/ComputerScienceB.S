"""
File:    seconds.py
Author:  Pooja Rajamanikandan
Date:    02/05/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will ask the user how much time has and converst into just seconds.
"""

days = int(input("How many days have elapsed? "))
hours = int(input("How many additional hours have elapsed? "))
minutes = int(input("How many additional minutes have elapsed? "))
seconds = int(input("How many additional seconds have elapsed? "))

total = (86400 * days) + (3600 * hours) + (60 * minutes) + seconds

print("The total amount of time elapsed is {} seconds".format(total))