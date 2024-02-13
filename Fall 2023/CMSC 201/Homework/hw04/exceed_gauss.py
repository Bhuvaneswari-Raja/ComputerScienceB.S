"""
File:    exceed_gauss.py
Author:  Pooja Rajamanikandan
Date:    10/02/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: The program calculates the Gauss sum of 1 to a number given 
    by the user.
"""
if __name__ == "__main__":
    
    gauss_range = int(input("What number do you want to test? "))
    gauss_sum = 0
    iterations = 0
    
    while gauss_sum <= gauss_range:
        #counts the number of iterations
        iterations += 1
        #calculates the sum
        gauss_sum += iterations
        
    print("After",iterations,"iterations, the gauss sum is",gauss_sum,"which exceeds (or is equal to) the number",gauss_range)