"""
File: basel.py
Author: Pooja Rajamanikandan
Date: 09/26/2023
Lab Section: 54
Email:  le64534@umbc.edu
Description: calculates the approximation for the number the 
    user inputs
"""
if __name__ == '__main__':
    sum_ending_point = int(input("What is the number of terms you want to sum? "))

    approximation_sum = 0
    for x in range(sum_ending_point):
        x +=1 
        approximation_sum += (1/x**2)
        
    print("The approximation for",sum_ending_point,"terms is",approximation_sum)
