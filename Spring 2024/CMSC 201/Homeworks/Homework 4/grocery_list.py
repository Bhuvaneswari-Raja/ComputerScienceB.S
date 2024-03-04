"""
File:    grocery_list.py
Author:  Pooja Rajamanikandan
Date:    02/24/2024
Section: 
E-mail:  le64534@umbc.edu
Description: 
"""
ESSENTIAL = ["eggs","butter","bread","milk"]
if __name__ == "__main__":
    item = input("What do you pick up in the store? (quit to exit) ")
    grocery_list = []

    while item != "quit":
        grocery_list.append(item)
        item = input("What do you pick up in the store? (quit to exit) ")

    missing_items = []
    for x in ESSENTIAL:
        if x not in grocery_list:
            missing_items.append(x)

    if len(missing_items) == 0:
        print("You have everything you need.")
        print("You bought",", ".join(grocery_list))
        
    else:
        print("You still need ",", ".join(missing_items))
        print("You bought",", ".join(grocery_list))
              