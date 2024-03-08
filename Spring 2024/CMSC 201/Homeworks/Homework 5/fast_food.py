"""
File:    fast_food.py
Author:  Pooja Rajamanikandan
Date:    03/04/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: 
"""

PRICES = [5,3,2.5,8.5,4]
EXIT_STRING = "place order"

def fast_food_receipt(order):
    total_cost = 0
    for x in range(len(order)):
        if "burger" in order[x] and "sandwich" in order[x]:
            total_cost += PRICES[0]
        elif order[x] == "fries":
            total_cost += PRICES[1]
        elif order[x] in ["coke","sprite","mountain dew"]:
            total_cost += PRICES[2]
        elif order[x] == "combo":
            total_cost += PRICES[3]
        else:
            total_cost += PRICES[4]
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
    

    min_count = burger
    if fries < min_count:
        min_count = fries
    if drink < min_count:
        min_count = drink

    combo_extra = ["combo" * min_count]

    extras = ["burger" for i in range(burger-len(com))] + \
        ["fries" for i in range(fries-len(com))] + \
            ["coke" for i in range(drink-len(com))]   
    



    #total = fast_food_receipt(order + com + extras)
    print("The total bill is",total)


