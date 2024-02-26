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
    list_a = []
    list_b = []
    while user_input != "quit":
        if user_input.split(" ")[0] == "add":
            if user_input.split(" ")[1].upper() == "A":
                list_a.append(user_input.split(" ")[-1])
            if user_input.split(" ")[1].upper() == "B":
                list_b.append(user_input.split(" ")[-1])

        elif user_input.split(" ")[0] == "remove":
            if user_input.split(" ")[1].upper() == "A":
                if user_input.split(" ")[-1] not in list_a:
                    print("Item not in Bin")
                    user_input = input()

                else:
                    list_a.remove(user_input.split(" ")[-1])

            if user_input.split(" ")[1].upper() == "B":
                if user_input.split(" ")[-1] not in list_b:
                    print("Item not in Bin")
                    user_input = input()
                else:
                    list_b.remove(user_input.split(" ")[-1])

        elif user_input.split(" ")[0] == "display":
            if user_input.split(" ")[1].upper() == "A":
                print("Bin A Contents:",list_a)
            if user_input.split(" ")[1].upper() == "B":
                print("Bin B Contents:",list_a)

        elif user_input.split(" ")[0] == "transfer":
            if user_input.split(" ")[1].upper() == "A":
                list_b.append(list_a.pop(0))
            if user_input.split(" ")[1].upper() == "B":
                list_a.append(list_b.pop(0))

        user_input = input()
