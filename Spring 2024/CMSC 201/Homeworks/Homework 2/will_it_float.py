"""
File:    will_it_float.py
Author:  Pooja Rajamanikandan
Date:    02/12/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will determine if the object entered by the user will 
    sink, float, or have neutral buoyancy.
"""

object = input("What object are we putting in the water today? ")
object_weight = float(input("What is the weight of the object? "))
object_volume = float(input("What is the volume of the object? "))

density = object_weight / object_volume

if density > 1000:
    print(object,"will sink")
elif density < 1000:
    print(object,"will float")
elif density == 1000:
    print(object,"has neutral buoyancy")
