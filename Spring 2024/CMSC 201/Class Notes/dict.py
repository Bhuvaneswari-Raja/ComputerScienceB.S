def random_dict():
    the_dict = dict()
    the_key = input('Tell me the key: ')
    #the_value = input('Tell me the value: ')
    while the_key != 'quit':  
        the_value = input('Tell me the value: ')
        the_dict[the_key] = the_value
        the_key = input('Tell me the key: ')
    
    print(the_dict)
    return the_dict

def print_out_dict(the_dictionary):
   for key in the_dictionary:
       print("Key:", key, "Value:", the_dictionary[key])

if __name__ == '__main__':
   print_out_dict(random_dict())
