"""
File:    how_deep.py
Author:  Pooja Rajamanikandan
Date:    11/06/2023
Section: YOUR DISCUSSION SECTION NUMBER
E-mail:  le64534@umbc.edu
Description: The program will find how deep a nested list is using recursion
"""
def how_deep(list_struct):
    if len(list_struct) == 0:
            return 1
    else:
            list_of_depths = []
            for sub_list in list_struct:
                list_of_depths.append(how_deep(sub_list))
            return max(list_of_depths) + 1



if __name__ == '__main__':
    print(how_deep([[[], [], [], [[[]]]], []]))
    print(how_deep([]))
    print(how_deep([[], []]))
    print(how_deep([[[]], [], [[]], [[[]]]]))
    print(how_deep([[[[], [[]], [[[]]], [[[[]]]]]]]))
    print(how_deep([[[], []], [], [[], []]]))
    