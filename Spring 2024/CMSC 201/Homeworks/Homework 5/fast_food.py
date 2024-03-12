"""
File:    fast_food.py
Author:  Pooja Rajamanikandan
Date:    03/04/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program implements a function that returns the total cost of a food order.
"""

EXIT_STRING = "place order"

def fast_food_receipt(order):
    total_cost = 0
    
    for x in range(len(order)):

        if "burger" in order[x] or "sandwich" in order[x]:
            total_cost += 5.0
        elif order[x] == "fries":
            total_cost += 3.0
        elif order[x] in ["coke","sprite","mountain dew"]:
            total_cost += 2.5
        elif order[x] == "combo":
            total_cost += 8.5
        else:
            total_cost += 4.0
        

    return total_cost

if __name__ == "__main__":
    item = input("What would you like to order? ")
    order = []
    burger, fries, drink = 0,0,0

    while item != EXIT_STRING:
        if "burger" in item or "sandwich" in item:
            burger += 1
        elif item == "fries":
            fries += 1
        elif item in ["coke","sprite","mountain dew"]:
            drink += 1
        else:
            order.append(item)
    
        item = input("What would you like to order? ")
    
    # the maximum number of combos needed
    min_count = 0
    if burger <= fries and burger <= drink:
        min_count = burger
    elif fries <= burger and fries <= drink:
        min_count = fries
    else:
        min_count = drink 

    # calculates the number combos and add it to a list
    combos = ["combo" for i in range(min_count)]

    # calcultes any extras from the combos and add all of them to a list
    extras = ["burger" for i in range(burger-min_count)] + \
        ["fries" for i in range(fries-min_count)] + \
            ["coke" for i in range(drink-min_count)]   
    

    #combines the number of combos, extras from the combos and any addtional and is paased as a parameter
    total = fast_food_receipt(order + combos + extras)
    print("The total bill is",total)


