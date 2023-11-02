"""
File:         icecream.py
Author:       Pooja Rajamanikandan
Date:         09/28/2023
Section:      54
E-mail:       le64534@umbc.edu
Description:  The program will interate through a list of ice cream 
    flavours and print which topping go well with that flavour. It will
    also display a special message for strawberry ice cream
"""
if __name__ == "__main__":
    ice_cream_flavor = ["vanilla", "strawberry", "chocolate"]
    toppings = ["caramel", "marshmallow", "gummi bears","cherries"]
    
    for x in ice_cream_flavor:
        print(x)
    print("---------------------------")
    for x in ice_cream_flavor:
        if x == "strawberry":
            print(x,"is fine on its own!")
        else:
            for y in toppings:
                print(x,"is tasty with",y)