"""
File:    basel.py
Author:  Pooja Rajamanikandan
Date:    02/19/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will calculate the approximation for the number from user input
"""
if __name__ == "__main__":
    
    num_of_sums = int(input("What is the number of terms you want to sum? "))
    sum = 0

    for x in range(1,num_of_sums+1):
        sum += 1 / (x**2)

    print(f"The approximation for {num_of_sums} terms is {sum}")