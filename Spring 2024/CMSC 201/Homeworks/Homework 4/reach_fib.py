"""
File:    reach_fib.py
Author:  Pooja Rajamanikandan
Date:    02/24/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: 
"""

if __name__ == "__main__":
    fib_seq = [1,1]
    num = int(input("What number should we exceed? "))
    if num == 1:
        print(f"F{0} = {fib_seq[-1]} which is greater than or equal to {num}")
    else:
        while fib_seq[-1] < num:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
        print(f"F{len(fib_seq)-1} = {fib_seq[-1]} which is greater than or equal to {num}")