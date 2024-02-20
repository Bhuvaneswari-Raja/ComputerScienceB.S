"""
File:    windows_95.py
Author:  Pooja Rajamanikandan
Date:    02/19/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will analyze a windows 95 key entered by the user and determine is it is valid or not.
"""
if __name__ == "__main__":

    user_key = input("Enter the key: ")

    if "-" not in user_key:
        print("The code is not accepted")
    else:
        key = user_key.split("-")
        sum = 0

        for x in key[1]:
            sum += int(x)

        if int(key[0]) % 111 != 0 and sum % 7 == 0:
            print("Code Accepted!")
        else:
            print("The code is not accepted")


