"""
File:    number_guesser.py
Author:  Pooja Rajamanikandan
Date:    02/24/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: 
"""
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1]) 


if __name__ == "__main__":
    rand_num = randint(1,100)
    print(rand_num)
    
    number = int(input("Guess a number between 1 and 100: "))

    counter = 1
    while number != rand_num:
        if number < rand_num:
            print("Your guess is too low")
        if number > rand_num:
            print("Your guess is too high")
        
        number = int(input("Guess a number between 1 and 100: "))
        counter += 1

    if number == rand_num:
        print("You guessed the value!")
        print(f"it took you {counter} steps")


