"""
File:    escape_velocity.py
Author:  Pooja Rajamanikandan
Date:    02/05/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will calculate the velocity required to escape
the gravitational pull of an object, starting a a specific radius.
"""

G = 6.67 * (10**-11)

body = input("What body are we launching from? ")

#scientific notation for mass
coeff_m = float(input("Enter the mass of the planet in scientific notation with the floating number first: "))
exp_m = int(input("What power of 10 is this? "))

#scientific notation for radius
#print(,end="")
coeff_r = float(input("Enter the coefficient of the scientific notation of the radius from the center of {}: ".format(body)))
exp_r = int(input("What power of 10 is this? "))

mass = coeff_m * (10**exp_m)
radius = coeff_r * (10**exp_r)

escape_velocity = ((2 * G * mass)/radius)**(1/2)

print("The escape velocity required for {} is {} m/s".format(body,round(escape_velocity,3)))

