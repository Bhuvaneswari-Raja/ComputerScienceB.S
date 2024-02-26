"""
File:    reach_fib.py
Author:  Pooja Rajamanikandan
Date:    02/24/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: 

#1,1,2,3,5,8

if __name__ == "__main__":

    fib_sequence = 1
    counter = 1
    print(f"F{0} = {fib_sequence}")

    while fib_sequence <= 6:
            print(f"F{counter} = {fib_sequence}")
            counter += 1
            fib_sequence += ((fib_sequence) + (counter-1))

            
    num = int(input("What number should we exceed? "))

    

    if num <= 1:
        print(f"F{counter} = {fib_sequence} which is greater than or equal to {num}")
    else:  
        

    
        #print(f"F{counter} = {fib_sequence} which is greater than or equal to {num}")
"""


fib = 1
counter = 0
sequence = 0

for x in range(5):
    print(f"F{x} = {sequence}")
    sequence += (fib + counter) + sequence

    