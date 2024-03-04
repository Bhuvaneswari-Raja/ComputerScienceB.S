"""
File:    list_reverse.py
Author:  Pooja Rajamanikandan
Date:    02/24/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: 
"""

if __name__ == "__main__":
    my_list = input("Enter a list separated by commas: ")
    temp_list = my_list.split(",")
    new_list = []

         
    for x in range(len(my_list.split(","))):
        new_list.append(temp_list.pop())

        for x in range(len(new_list)):        
            if "0" in new_list[x]:
                new_list.remove(new_list[x])
            elif "1" in new_list[x]:
                new_list.remove(new_list[x])
            elif "2" in new_list[x]:
                new_list.remove(new_list[x])
            elif "3" in new_list[x]:
                new_list.remove(new_list[x])
            elif "4" in new_list[x]:
                new_list.remove(new_list[x])
            elif "5" in new_list[x]:
                new_list.remove(new_list[x])
            elif "6" in new_list[x]:
                new_list.remove(new_list[x])
            elif "7" in new_list[x]:
                new_list.remove(new_list[x])
            elif "8" in new_list[x]:
                new_list.remove(new_list[x])
            elif "9" in new_list[x]:
                new_list.remove(new_list[x])
            
    if len(new_list) < 1:
        print("The new list was empty")
    else:
        print(", ".join(new_list))