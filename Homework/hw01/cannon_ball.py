
"""
File:    cannon_ball.py
Author:  Pooja Rajamanikandan 
Date:    09/12/2023
Section: 50
E-mail:  le64534@umbc.edu
Description: Ask the user for an initial velocity and angle in which 
    they wil fire the cannon, and caluate the distance a 
    cannon ball travels.
"""

import math

intial_velocity = int(input("Enter the initial velocity (V0): "))
angle_degree = int(input("Enter the angle that you will fire the cannon: "))

radian = angle_degree * (math.pi / 180)
travel_distance = ((intial_velocity**2) * math.sin(2 * radian)) / 9.8

print(f"The distance the cannon ball will travel is {travel_distance} meters")
