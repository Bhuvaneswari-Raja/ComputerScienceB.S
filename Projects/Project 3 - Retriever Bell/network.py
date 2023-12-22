"""
File:    network.py
Author:  Pooja Rajamanikandan
Date:    11/29/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: The program implements connection servers for phonecalls using switchboard
    and area codes.
"""

import csv

HYPHEN = "-"
QUIT = 'quit'
SWITCH_CONNECT = 'switch-connect'
SWITCH_ADD = 'switch-add'
PHONE_ADD = 'phone-add'
NETWORK_SAVE = 'network-save'
NETWORK_LOAD = 'network-load'
START_CALL = 'start-call'
END_CALL = 'end-call'
DISPLAY = 'display'

MAX_PHONE_LINES = 3  # Maximum number of calls allowed on a single trunk line


class Switchboard:
    def __init__(self, area_code):
        self.area_code = area_code
        self.connected_switchboards = set()
        self.local_numbers = {}

    def add_local_number(self, number):
        self.local_numbers[number] = {'in_use': False, 'trunk_lines_used': 0}


def connect_switchboards(switchboards, area_1, area_2):
    """
    Connect two switchboards.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    - area_1 (int): Area code of the first switchboard.
    - area_2 (int): Area code of the second switchboard.
    """
    switchboard_1 = switchboards.get(area_1)
    switchboard_2 = switchboards.get(area_2)

    if switchboard_1 and switchboard_2:
        switchboard_1.connected_switchboards.add(area_2)
        switchboard_2.connected_switchboards.add(area_1)
        print(f"Switchboards {area_1} and {area_2} are now connected.")
    else:
        print(f"Error: Switchboards {area_1} or {area_2} do not exist.")


def add_switchboard(switchboards, area_code):
    """
    Add a new switchboard.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    - area_code (int): Area code of the new switchboard.
    """
    if area_code not in switchboards:
        switchboards[area_code] = Switchboard(area_code)
        print(f"Switchboard with area code {area_code} added.")
    else:
        print(f"Error: Switchboard with area code {area_code} already exists.")


def add_phone(switchboards, area_code, phone_number):
    """
    Add a new phone to a switchboard.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    - area_code (int): Area code of the switchboard.
    - phone_number (int): Phone number to be added.
    """
    switchboard = switchboards.get(area_code)
    if switchboard:
        switchboard.add_local_number(phone_number)
        print(f"Phone with number {area_code}-{phone_number} added.")
    else:
        print(f"Error: Switchboard with area code {area_code} does not exist.")


def save_network(switchboards, file_name):
    """
    Save the network configuration to a CSV file.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    - file_name (str): Name of the CSV file to save.
    """
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["area_code", "connected_switchboards", "numbers"])
        
        for switchboard in switchboards.values():
            local_numbers = list(switchboard.local_numbers.keys())
            connected_switchboards = list(switchboard.connected_switchboards)
            
            writer.writerow({"area_code": switchboard.area_code, "connected_switchboards": connected_switchboards, "numbers": local_numbers})
    
    print(f"Network saved to {file_name}.")


def load_network(file_name):
    """
    Load a network configuration from a CSV file.

    Parameters:
    - file_name (str): Name of the CSV file to load.

    Returns:
    - dict: Dictionary containing switchboards loaded from the file.
    """
    switchboards_from_file = {}
    
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            area_code = int(row["area_code"])
            
            connected_switchboards = [int(switchboard) for switchboard in row["connected_switchboards"].split(",")]
            numbers = [int(num) for num in row["numbers"].split(",")]
            
            switchboard = Switchboard(area_code)
            switchboard.connected_switchboards = connected_switchboards
            switchboard.local_numbers = {num: {"in_use": False, "trunk_lines_used": 0} for num in numbers}
            
            switchboards_from_file[area_code] = switchboard          

    return switchboards_from_file


def start_call(switchboards, start_area, start_number, end_area, end_number):
    """
    Initiate a call between two phones.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    - start_area (int): Area code of the calling phone.
    - start_number (int): Phone number of the calling phone.
    - end_area (int): Area code of the receiving phone.
    - end_number (int): Phone number of the receiving phone.
    """
    start_phone = f"{start_area}-{start_number}"
    end_phone = f"{end_area}-{end_number}"

    switchboard_start = switchboards.get(start_area)
    switchboard_end = switchboards.get(end_area)

    if switchboard_start and switchboard_end:
        # Perform a recursive check for connection
        if can_connect(switchboards, start_area, start_number, end_area, end_number):
            print(f"{start_phone} and {end_phone} are now connected.")
            switchboard_start.local_numbers[start_number]['in_use'] = True
            switchboard_end.local_numbers[end_number]['in_use'] = True

            # Increment trunk lines used along the path
            increment_trunk_lines_used(switchboards, start_area, start_number, end_area, end_number)
        else:
            print(f"{start_phone} and {end_phone} were not connected.")
    else:
        print(f"Error: Invalid switchboards {start_area} or {end_area}.")


def can_connect(switchboards, start_area, start_number, end_area, end_number, visited=None):
    """
    Recursive function to check if a call can be established between two phones.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    - start_area (int): Area code of the starting phone.
    - start_number (int): Phone number of the starting phone.
    - end_area (int): Area code of the destination phone.
    - end_number (int): Phone number of the destination phone.
    - visited (set): Set of visited phones to avoid infinite recursion.

    Returns:
    - bool: True if a call can be established, False otherwise.
    """
    if visited is None:
        visited = set()

    phone = f"{start_area}-{start_number}"

    if phone in visited:
        return False

    visited.add(phone)

    switchboard = switchboards.get(start_area)
    if not switchboard or switchboard.local_numbers[start_number]['in_use']:
        return False

    if start_area == end_area:
        return True

    for neighbor_area in switchboard.connected_switchboards:
        if can_connect(switchboards, neighbor_area, start_number, end_area, end_number, visited):
            return True

    return False


def increment_trunk_lines_used(switchboards, start_area, start_number, end_area, end_number):
    """
    Recursive function to increment trunk lines used along the path.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    - start_area (int): Area code of the starting phone.
    - start_number (int): Phone number of the starting phone.
    - end_area (int): Area code of the destination phone.
    - end_number (int): Phone number of the destination phone.
    """
    phone = f"{start_area}-{start_number}"

    switchboard = switchboards.get(start_area)
    if switchboard:
        switchboard.local_numbers[start_number]['trunk_lines_used'] += 1

        if start_area != end_area:
            for neighbor_area in switchboard.connected_switchboards:
                increment_trunk_lines_used(switchboards, neighbor_area, start_number, end_area, end_number)


def end_call(switchboards, start_area, start_number):
    """
    End a call.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    - start_area (int): Area code of the phone ending the call.
    - start_number (int): Phone number of the phone ending the call.
    """
    phone = f"{start_area}-{start_number}"
    switchboard = switchboards.get(start_area)

    if switchboard and switchboard.local_numbers.get(start_number):
        switchboard.local_numbers[start_number]['in_use'] = False
        print(f"{phone} hung up. Connection terminated.")
    else:
        print(f"Unable to disconnect. {phone} is not in a call.")


def display(switchboards):
    """
    Display the current network configuration.

    Parameters:
    - switchboards (dict): Dictionary containing switchboards.
    """
    for area_code, switchboard in switchboards.items():
        print(f"Switchboard with area code: {area_code}")
        print("    Trunk lines are:")
        for connected_area in switchboard.connected_switchboards:
            print(f"      Trunk line connection to: {connected_area}")

        print("    Local phone numbers are:")
        for number, data in switchboard.local_numbers.items():
            state = f"connected to {data['in_use']}" if data['in_use'] else "not in use"
            print(f"      Phone with number: {number} is {state}. Trunk lines used: {data['trunk_lines_used']}")

        print()


def start_network():
    switchboards = {}
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
            area_1 = int(split_command[1])
            area_2 = int(split_command[2])
            connect_switchboards(switchboards, area_1, area_2)
        elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
            add_switchboard(switchboards, int(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:
            number_parts = split_command[1].split('-')
            area_code = int(number_parts[0])
            phone_number = int(''.join(number_parts[1:]))
            add_phone(switchboards, area_code, phone_number)
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_SAVE:
            save_network(switchboards, split_command[1])
            print('Network saved to {}.'.format(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_LOAD:
            switchboards = load_network(split_command[1])
            print('Network loaded from {}.'.format(split_command[1]))
        elif len(split_command) == 3 and split_command[0].lower() == START_CALL:
            src_number_parts = split_command[1].split(HYPHEN)
            src_area_code = int(src_number_parts[0])
            src_number = int(''.join(src_number_parts[1:]))

            dest_number_parts = split_command[2].split(HYPHEN)
            dest_area_code = int(dest_number_parts[0])
            dest_number = int(''.join(dest_number_parts[1:]))
            start_call(switchboards, src_area_code, src_number, dest_area_code, dest_number)

        elif len(split_command) == 2 and split_command[0].lower() == END_CALL:
            number_parts = split_command[1].split(HYPHEN)
            area_code = int(number_parts[0])
            number = int(''.join(number_parts[1:]))
            end_call(switchboards, area_code, number)

        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            display(switchboards)

        s = input('Enter command: ')

if __name__ == '__main__':
    start_network()
