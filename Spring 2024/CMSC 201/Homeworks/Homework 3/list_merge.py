"""
File:    list_merge.py
Author:  Pooja Rajamanikandan
Date:    02/19/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program will merger two lists containing inputs from the user
"""

if __name__ == "__main__":
    length = int(input("How  many elements do you want in each list? "))    
    
    list_one = []
    for x in range(length):
        list_one.append(input("What do you want to put in the first list? "))

    list_two = []
    for x in range(length):
        list_two.append(input("What do you want to put in the second list? "))

    merged_list = []
    for x in range(length):
        merged_list.append(list_one[x])
        merged_list.append(list_two[x])

    print("The first list is: ",list_one)
    print("The second list is: ",list_two)
    print("The merged list is: ",merged_list)