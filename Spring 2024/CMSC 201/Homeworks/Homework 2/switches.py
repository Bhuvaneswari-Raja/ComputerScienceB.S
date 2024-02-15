"""
File:    switches.py
Author:  Pooja Rajamanikandan
Date:    02/13/2024
Section: 16
E-mail:  le64534@umbc.edu
Description:  The program will implement a RPG that has a puzzle to be solved. In the game 
  the user will try to open a door with two knobs and a switch.
"""

first_knob = int(input("What is the position of the first knob? (Enter 1-12) "))

  
second_knob = int(input("What is the position of the second knob? (Enter 1-12) "))


switch_position = str(input("What is the position of the switch? (Enter up or down) "))


if first_knob < 1 or 12 < first_knob:
  print("Knob 1 needs to be set to 1 - 12")
elif second_knob < 1 or 12 < second_knob:
  print("Knob 2 needs to be set to 1 - 12")
elif switch_position.lower() != "up" and switch_position.lower() != "down":
  print("Switch need to be UP or DOWN")  
else:
  if first_knob % 2 == 0 and second_knob % 2 == 1 and switch_position.lower() == "up":
    print("The door opens, you get all the loot.")
  elif (first_knob % 2 == 0 or second_knob % 2 == 1) or switch_position.lower() == "down":
    print("The door clanks but does not open, try again.")
  else:
    print("The handle doesn't budge.")