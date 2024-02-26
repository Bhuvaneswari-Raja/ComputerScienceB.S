"""
File:         icecream.py
Author:       Pooja Rajamanikandan
Date:         02/26/2024
Section:      16
E-mail:       le64534@umbc.edu
Description:  The program will interate through a list of ice cream flavours and print which topping 
    go well with that flavour. It will also display a special message for strawberry ice cream
"""
if __name__ == "__main__":
    flavors = ["vanilla", "strawberry", "chocolate"]
    toppings = ["caramel", "marshmallow", "gummi bears"]
    
    for x in flavors:
        print(x)
    print("-------------------------")
    for x in flavors:
        for y in toppings:
            print(f"{x} is tasty with {y}")
    print("-------------------------")
    for x in flavors:
        if x == "strawberry":
            print(x,"is fine on its own!")
        else:
            for y in toppings:
                print(f"{x}is tasty with {y}")