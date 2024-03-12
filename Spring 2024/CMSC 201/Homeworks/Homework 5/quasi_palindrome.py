"""
File:    quasi_palindrome.py
Author:  Pooja Rajamanikandan
Date:    03/04/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program checks if a word is a palindrome based on the number errors allowed
"""
EXIT_STRING = "quit"

def quasi_palindrome(word, errors):
    length = len(word)
    errors = int(errors)
    
    if word == word[::-1]:
        return True
    if errors == 0:
        return False
    
    for i in range(length // 2): #interates over the half of the word
        if word[i] != word[length - i - 1]: #compares the characters at the beginning and end of the word to see if they match
            if errors <= 0: 
                return False
            errors -= 1
    
    return True 

    
    

if __name__ == "__main__":
    pal_word = input("What word do you want to check? ")
    while pal_word != EXIT_STRING:    
        error_allowed = input("How many errors do you want to allow? ")

        if quasi_palindrome(pal_word,error_allowed):
            print(f"It was a {error_allowed}-quasi-palindrome!")
        else:
            print(f"It was not {error_allowed}-quasi-palindrome!")

        pal_word = input("What word do you want to check? ")
