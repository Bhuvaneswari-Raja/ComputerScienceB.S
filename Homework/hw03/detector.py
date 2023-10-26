"""
File: basel.py
Author: Pooja Rajamanikandan
Date: 09/26/2023
Lab Section: 50
Email:  le64534@umbc.edu
Description: check for diphthong in the word the user inputs
"""

if __name__ == '__main__':
    word = input("Tell me the word you wish to check for diphthongs: ")

    vowels = ["a","e","i","o","u","y"]
    dipthong_detector = 0
    
    ''''
    for x in word:
        if x in vowels:
            if word[word.index(x)+1] in vowels:
                if word[word.index(x)+1] == x:
                    dipthong_detector += 1
    '''
    for x in range(len(word)):
        if word[x] in vowels and word[x+1:x+2] in vowels:
            dipthong_detector += 1

    print("There are {} diphthongs in the string".format(dipthong_detector))