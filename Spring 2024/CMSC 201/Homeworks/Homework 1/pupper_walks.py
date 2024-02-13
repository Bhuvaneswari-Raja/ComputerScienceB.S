"""
File:    pupper_walks.py
Author:  Pooja Rajamanikandan
Date:    02/05/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will calculate how long you walk Pupper each year.  
"""

real_name = input("What is pupper's real name? ")
walk_per_week = int(input("How many times per week do you walk pupper? "))
walk_in_miles = int(input("How long is the walk in miles? "))
time_for_mile = int(input("How many minutes does it take for you to walk a mile? "))

miles_walked = (walk_per_week * walk_in_miles) * 52
hours_walkes = (miles_walked * time_for_mile) / 60

print("Your dog's name is {}, and you have walked {} miles this year, in {} hours.".format(real_name,miles_walked,hours_walkes))
