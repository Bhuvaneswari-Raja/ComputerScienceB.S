"""
File:    binary.py
Author:  Pooja Rajamanikandan
Date:    11/06/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: The program will use recursion to return a binary of the 
    decimal number the user inputs. 
"""

def determine_even_odd(num):
    if num % 2 == 0:
       return 0
    else:
       return 1

def binary(decimal):
   if decimal == 0:
      return 0
   else:
      return determine_even_odd(decimal) + 10 * binary(decimal // 2)
   
if __name__ == '__main__':
   dec_num = int(input("Tell me a number: "))

   while dec_num >= 0:
      print("0b"+str(binary(dec_num)), bin(dec_num)) 
      dec_num = int(input("Tell me a number: "))
