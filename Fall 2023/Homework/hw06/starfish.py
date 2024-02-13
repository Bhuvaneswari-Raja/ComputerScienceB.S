"""
File:    starfish.py
Author:  Pooja Rajamanikandan
Date:    11/06/2023
Section: YOUR DISCUSSION SECTION NUMBER
E-mail:  le64534@umbc.edu
Description: 
"""

def starfish(leg_list, generations):
    if generations <= 0:
        return leg_list
    else:
        temp_list =[]
        for x in range(len(leg_list)):
            if leg_list[x] != 5:
                leg_list[x] += 1
            else:
                leg_list.remove(leg_list[x])
                leg_list.insert(x,[1,1,1,1,1])
        return (starfish(flatten_list(leg_list), generations-1))

            
def flatten_list(leg_list):
    final_list = []
    for sub in leg_list:
        if type(sub) == list:
            for x in sub:
                final_list.append(x)
        else:
            final_list.append(sub)
    return final_list

def count_starfish(leg_list):
   leg_counts = {1:0, 2:0, 3:0, 4:0, 5:0}
   for x in leg_list:
       leg_counts[x] += 1


   return leg_counts



if __name__ == '__main__':
    print(count_starfish(starfish([1, 2, 3, 4, 5], 3)))
    print(count_starfish(starfish([2, 4, 5], 10)))
    print(count_starfish(starfish([5, 5, 5], 1)))
    print(count_starfish(starfish([1], 20)))
    print(count_starfish(starfish([5, 5, 5, 5, 5], 5)))