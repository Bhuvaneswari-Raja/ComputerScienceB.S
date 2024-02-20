"""
File:    draw_a_square.py
Author:  Pooja Rajamanikandan
Date:    02/19/2024
Section: 16
E-mail:  le64534@umbc.edu
Description:  The program will draw a square using dimensions given by the user 
"""

if __name__ == "__main__":
    rows_vertical = int(input("How many rows (vertical) do you want? "))
    rows_horizontal = int(input("How many rows (horizontal) do you want? "))

    print("*"*rows_horizontal)
    for x in range(rows_vertical-2):
        print("*",end=" "*(rows_horizontal-2))
        print("*")
    print("*"*rows_horizontal)

    





