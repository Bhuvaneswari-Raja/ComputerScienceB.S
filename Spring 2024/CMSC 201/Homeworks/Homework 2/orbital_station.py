"""
File:    orbital_station.py
Author:  Pooja Rajamanikandan
Date:    02/13/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will ask the user if they want to control 'rotation speed' or 'station radius'
     and determine which equation to use based on user's choice.
"""

control = input("Would you like to control \"rotation speed\" or \"station radius\"?")

if control.lower() == "rotation speed":
    radius = float(input("What is the radius of the station? "))
    
    rotation_speed = (60/(2 * 3.14)) * ((9.8/radius)**(1/2))
    
    print(F"The rotation speed is {rotation_speed} rpm")

if control.lower() == "station radius":
    rpm = float(input("What speed in rpm do you want the station to rotate? "))
        
    station_radius =  9.8 / (((2 * 3.14 * rpm)/60)**2)
    print(f"The station radius is {station_radius} meters")