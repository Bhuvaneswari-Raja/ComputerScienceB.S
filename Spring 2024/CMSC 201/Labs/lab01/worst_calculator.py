"""
File:         worst_calculator.py
Author:       Pooja Rajamanikandan
Date:         02/05/2024
Section:      16
E-mail:       le64534@umbc.edu
Description:  The program makes the worst calculator ever
"""

integer_1 = int(input("Enter integer 1: "))
integer_2 = int(input("Enter integer 2: "))
float_1 = float(input("Enter float 1: "))
float_2 = float(input("Enter float 2: "))
float_3 = float(input("Enter float 3: "))

sum = integer_1 + integer_2
product = float_1 * float_2 * float_3

print("The sum of the integers {} and {} is {}".format(integer_1,integer_2,sum))
print("The product of the floats {},{},{}, is {}".format(float_1,float_2,float_3,product))