"""
File:    factor_me.py
Author:  Pooja Rajamanikandan
Date:    10/02/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: The program wil factor a number into prime factors less than 50
"""

if __name__ == "__main__":
    
    list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
    user_num = int(input("Enter a number to factor: "))
    
    
    #Iterates through the list of primes
    for x in list_of_primes:
        #checks if the number is factorable with prime less than 50 
        if user_num % x == 0:
            print("\nThis part of the number couldn't be factored with primes less than 50:",user_num) 
    
    #If the number is factorable with prime less than 50, outputs all the factors 
    for x in range(len(list_of_primes)):
        while user_num % list_of_primes[x] != 0:
            if user_num % list_of_primes[-1] != 0:
                print("We didn't find any factors")
                print("This part of the number couldn't be factored with \nprimes less than 50:")