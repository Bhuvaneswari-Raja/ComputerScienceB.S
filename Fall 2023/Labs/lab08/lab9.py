"""
File:    lab9.py
Author:  Pooja Rajamanikandan
Date:    11/02/2023
Section: 54
E-mail:  le64534@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""


def create_new_weird_2d_list(height, width, value):
    """
    Creates a 2d list where all values are initialized to the supplied value
    :param height: the amount of sublists
    :param width: the size of each sublist
    :param value: the value to initialize each item in the list
    :return: a 2d list
    """
    row = []
    mat = []

    for i in range(width):
        row.append(value)

    for i in range(height):
        mat.append(row)

    return mat


def create_new_not_weird_2d_list(height, width, value):
    """
    Creates a 2d list where all values are initialized to the supplied value
    :param height: the amount of sublists
    :param width: the size of each sublist
    :param value: the value to initialize each item in the list
    :return: a 2d list
    """
    # hint hint hint: make two nested for loops that utilize range()
    
    row = []

    for i in range(width):
        column = []
        for j in range(height):
            column.append(value)
            #print("Column",j,"=",column)
        row.append(column)
        #print("Row",i,"=",row)
    return row


if __name__ == '__main__':
    '''
    matrix = create_new_weird_2d_list(4, 4, 0)
    matrix[0][1] = 1
    matrix[2][3] = 2
    print(matrix)
    # I'm expecting [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0]]
    # but what do I get...?
    '''

    new_list = create_new_not_weird_2d_list(4, 4, 0)
    new_list[0][1] = 1
    new_list[2][3] = 2
    print(new_list)
    
