"""
File:    lock_and_key.py
Author:  Pooja Rajamanikandan
Date:    10/16/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: The program will calculate the sum of key cuts and lock pinning and determine if 
    they are within a range to open up
"""
def lock_and_key(key_cuts, lock_pinning, minimum):
    # Makes sure both list are equal
    while len(key_cuts) != len(lock_pinning):
        if len(key_cuts) > len(lock_pinning):
            key_cuts.pop()
        if len(key_cuts) < len(lock_pinning):
            lock_pinning.pop()
    counter = 0
    
    for x in range(len(key_cuts)):
        if abs((key_cuts[x] + lock_pinning[x]) - 6) < minimum:
            counter += 1
            #print("sum =",abs((key_cuts[x] + lock_pinning[x]) - 6))
    # Determines if locked or unlocked
    if counter == len(key_cuts):
        print("Unlocked")
    else:
        print("Still Locked")
            
    
    
if __name__ == "__main__":
      
    lock_and_key([2.1, 3.5, 2.7], [4.1, 2.5, 3.2], 0.25)
    lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2], 0.25)
    lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2, 3.2], 0.25)