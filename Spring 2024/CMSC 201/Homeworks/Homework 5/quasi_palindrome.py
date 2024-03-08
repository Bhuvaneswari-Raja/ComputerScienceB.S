"""
File:    quasi_palindrome.py
Author:  Pooja Rajamanikandan
Date:    03/04/2024
Section: 
E-mail:  le64534@umbc.edu
Description: 
"""
EXIT_STRING = "quit"

def quasi_palindrome(word,errors):
    if word[::-1] == word:
        return True
    

if __name__ == "__main__":
    pal_word = input
    error_allowed = input
    while pal_word != EXIT_STRING:
        result = quasi_palindrome(pal_word,error_allowed)
        
        if result:
            print()
        else:
            print()
