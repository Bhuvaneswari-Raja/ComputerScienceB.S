"""
File:    mad_py_lib.py
Author:  Pooja Rajamanikandan
Date:    02/05/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will make mad-lib.
"""
name = str(input("Tell me your name: "))
noun = str(input("Tell me a subject/thing (noun): "))
adjective = str(input("Tell me an adjective: "))
verb = str(input("Tell me a verb: "))
another_noun = str(input("Tell me a noun: "))

print("Hello {}, we are going to have an amazing semester".format(name))
print("learning {}, it's going to be {} so don't".format(noun,adjective))
print("worry if you need to {} from a {}.".format(verb, another_noun))