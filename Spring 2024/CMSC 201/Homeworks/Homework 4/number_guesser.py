"""
File:    number_guesser.py
Author:  Pooja Rajamanikandan
Date:    02/24/2024
Section: 
E-mail:  le64534@umbc.edu
Description: 
"""
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1]) 


if __name__ == "__main__":
    number = input()