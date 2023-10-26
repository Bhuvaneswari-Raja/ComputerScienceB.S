def sum_list (numbers):
    """
    Sums a list of integers
    :param numbers: a list of integers
    :return: the sum of the integers in numbers
    """
    sum_of_list = 0
    for x in numbers:
        sum_of_list += x
    return sum_of_list

def get_string_lengths(strings):
    """
    Given a list of strings, return a list of integers representing
    the lengths of the input strings
    :param strings: a list of strings
    :return: a list of integers representing the lengths of the input strings
    """
    string_length_list = list()
    for x in strings:
        string_length_list.append(len(x))
    return string_length_list

def get_names():
    """
    Asks the user for a list of names
    :return: a list of strings for the names the user entered
    """
    user_name = input("Enter a name, STOP to stop: ")
    name_list = list()
    while user_name != "STOP":
        name_list.append(user_name)
        user_name = input("Enter a name, STOP to stop: ")
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

    list_of_len_kitties = get_string_lengths(kitties)
    sum_of_kitties = sum_list(list_of_len_kitties)
    print("sum of lengths of the string in kitties =",sum_of_kitties)

    # print the sum of the lengths of the strings in kitties

    puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]

    # prints the sum of the lengths of the strings in puppers
    list_of_len_puppers = get_string_lengths(puppers)
    sum_of_puppers = sum_list(list_of_len_puppers)
    print("sum of lengths of the string in puppers =",sum_of_puppers)
    
    list_names = get_names()
    sum_of_names = sum_list(get_string_lengths(list_names))
    print("sum of lengths of the string in names =",sum_of_names)