"""
File:    names.py
Author:  Pooja Rajamanikandan
Date:    03/11/2024
Section: 16
E-mail:  le64534@umbc.edu
Description:  YOUR DESCRIPTION GOES HERE AND HERE
              YOUR DESCRIPTION CONTINUED SOME MORE
"""


def sum_list(numbers):
    """
    Sums a list of integers
    :param numbers: a list of integers
    :return: the sum of the integers in numbers
    """
    sum = 0
    for x in range(len(numbers)):
        sum += numbers[x] 

    return sum


def get_string_lengths(strings):
    """
    Given a list of strings, return a list of integers representing
    the lengths of the input strings
    :param strings: a list of strings
    :return: a list of integers representing the lengths of the input strings
    """
    len_list = []

    for x in range(len(strings)):
        len_list.append(len(strings[x]))

    return len_list


def get_names():
    """
    Asks the user for a list of names
    :return: a list of strings for the names the user entered
    """
    name_list = []
    name = input("Enter a name, STOP to stop: ")
    while name != "STOP":
        name_list.append(name)
        name = input("Enter a name, STOP to stop: ")

    return name_list 


if __name__ == '__main__':
    kitties = [
        "Jules",
        "Stubby",
        "Tybalt",
        "Scooter",
        "KC",
        "Garfield",
        "Bucky"
    ]

    sum = sum_list(get_string_lengths(kitties))
    print(f"There are {sum} letters in kitties")
    # print the sum of the lengths of the strings in kitties

    puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]
    sum = sum_list(get_string_lengths(puppers))
    print(f"There are {sum} letters in puppers")

    names = get_names()

    sum = sum_list(get_string_lengths(names))
    print(f"There are {sum} letters in the names you entered")

    # prints the sum of the lengths of the strings in puppers

    # gets names from the user and reports how many letters are in all the names