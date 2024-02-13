"""
File:    derangements.py
Author:  Pooja Rajamanikandan
Date:    11/06/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: The program find Dn for n > 0, using a recursive fuction
"""

def derangement(n):
    if n == 0:
        return 1
    else:
        return n*derangement(n - 1) + (-1)**n


if __name__ == '__main__':
   '''
    test_num = int(input('What Dn do you want to compute? '))
    while test_num != -1:
        print(test_num, derangement(test_num))
        test_num = int(input('What Dn do you want to compute? '))
   '''
   for x in range(24):
       print(x, derangement(x))
       