def print_favorite_numbers(who, favorites):
    """
    :param who: this is a string, representing a person in our dictionary
    :param favorites: the favorite numbers dictionary
    :return: None
    """
    print(favorites[who])
    #pass


def add_favorite_number(who, number, favorites):
    """
    :param who: add "who" to the dictionary if they're not already there and give them a blank list
            otherwise, add the number to their favorites list if the number isn't already in someone's list.
    :param number: the number to add
    :param favorites: the favorites dictionary
    :return: None (dictionaries are mutable, so you don't need to return it to modify it)
    """
    if who not in favorites:
        favorites[who] = list()
        favorites[who].append(number)
        print(number, "added to",who+"'s favourites")

    elif who in favorites:        
        if number in favorites[who]:
            print(number, "was found in",who+"'s favourites")
        else:
            #favorites[who] = list()
            favorites[who].append(number)
            print(number, "added to",who+"'s favourites")
        

    #pass


if __name__ == '__main__':
    favorites = {}
    in_string = input('What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ')

    while in_string.strip().lower() != 'quit':
        if in_string.strip().lower().startswith('print favorite numbers for'):
            print_favorite_numbers(in_string.strip().split()[-1], favorites)

        if len(in_string.split()) == 2:
            who, num = in_string.split(" ")
            #temp = in_string.split(" ")
            #print(who)
            num = int(num)
            add_favorite_number(who, num, favorites)

        #print(favorites)
        in_string = input('What do you want to do (add favorite number), or quit? ')
