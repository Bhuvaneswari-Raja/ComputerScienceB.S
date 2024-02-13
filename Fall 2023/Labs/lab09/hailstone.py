"""
File: hailstone.py
Author: Pooja Rajamanikandan	
Date: 11/09/2023
Section: 54
E-mail: le64534@umbc.edu
Description: This file contains python code that implements the "flight"
  of a hailstone, following the HOTPO rules (also known as the Collatz
  Conjecture), recursively
"""

# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE

def flight(height):
    """
    recursively calculates the path of a hailstone
    :param height: the height of the hailstone
    :return: a recursive call, which at the end returns the number
        of "steps"taken for the hailstone to reach a height of 1
    """

    #### BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0
    if height <= 0:
        print("Invalid height of",height)
        return 0

    # stops when it reachs height of 1 (the ground)

    #### RECURSIVE CASES:
    # if the current height is even, divide it by 2

    # if the current height is odd, multiply it by 3, then add 1
    else:
        if height == 1:
            print("Height of",height)
            return 0
        if height % 2 == 0:
            print("Height of",height)
            return flight(int(height / 2))+1

        if height % 2 != 0:
            print("Height of",height)
            return flight(int((height*3) +1)) +1
            
if __name__ == "__main__":

    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    start_height = int(input(msg))

    # recursive call goes here
    steps = flight(start_height)

    print("\nIt took", steps, "steps to hit the ground.")
    print("Thank you for using the Hailstone Simulator!\n")

