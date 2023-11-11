"""
File:    ab_equality.py
Author:  Pooja Rajamanikandan
Date:    11/06/2023
Section: YOUR DISCUSSION SECTION NUMBER
E-mail:  le64534@umbc.edu
Description: The program outputs trings of a's and b's of length n so 
    that the number of a's and b's are equal. 
"""

def ab_equal(n, k, current):
   
    if n == 0 and  k != 0:
        return ""
    elif k == 0 and n == 0:
        print(current)
    else:    
        ab_equal(n - 1, k+1, current + 'a')
        ab_equal(n - 1, k-1, current + 'b')    
'''
        for x in current:
            if x == "a":
                k += 1
            if x == "b":
                k -= 1
        '''
        #print("K =",k)
        #print("CURRENT =",current)
    


if __name__ == '__main__':
    length = int(input("What lenght do you want to run? "))
    ab_equal(length,0,"")