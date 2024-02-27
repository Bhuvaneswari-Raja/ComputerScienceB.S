"""
File:    two_bins.py
Author:  Pooja Rajamanikandan
Date:    02/24/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: 
"""

if __name__ == "__main__":
    user_input = input()
    bin_a = []
    bin_b = []
    while user_input != "quit":
        if user_input.split(" ")[0] == "add":
            if user_input.split(" ")[1].upper() == "A":
                bin_a.append(user_input.split(" ")[-1])
            elif user_input.split(" ")[1].upper() == "B":
                bin_b.append(user_input.split(" ")[-1])
    
        elif user_input.split(" ")[0] == "remove":
            if user_input.split(" ")[1].upper() == "A":
                if user_input.split(" ")[-1] not in bin_a:
                    print("Item not in Bin, Try again")
                else:
                    bin_a.remove(user_input.split(" ")[-1])

            elif user_input.split(" ")[1].upper() == "B":
                if user_input.split(" ")[-1] not in bin_b:
                    print("Item not in Bin, Try again")
                else:
                    bin_b.remove(user_input.split(" ")[-1])

        elif user_input.split(" ")[0] == "display":
            if user_input.split(" ")[1].upper() == "A":
                print("Bin A Contents:",bin_a)
            if user_input.split(" ")[1].upper() == "B":
                print("Bin B Contents:",bin_b)
        
        elif user_input.split(" ")[0] == "transfer":
            if user_input.split(" ")[1].upper() == "A":
                if len(bin_a):
                    bin_b.append(bin_a.pop(0))
                else:
                    print("Bin A is empty, Try again")
            if user_input.split(" ")[1].upper() == "B":
                if len(bin_b):
                    bin_a.append(bin_b.pop(0))
                else:
                    print("Bin B is empty, Try again")

        user_input = input()

       
