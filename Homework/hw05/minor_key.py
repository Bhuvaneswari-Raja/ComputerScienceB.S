"""
File:    minor_key.py
Author:  Pooja Rajamanikandan
Date:    10/16/2023
Section: 54
E-mail:  le64534@umbc.edu
Description: This program will determine the harmonic minor scale for the note the user inputs
"""

MUSICAL_NOTES = ['C', 'D\u266d', 'D', 'E\u266d', 'E', 'F', 'G\u266d', 'G', 'A\u266d', 'A', 'B\u266d', 'B']
MINOR_SCALE_STEPS = [2, 1, 2, 2, 1, 3, 1]
EXIT_STRING = "quit"

#Set starting note to match the propre musical notation
def set_note(note):
    new_note = ""
    if note[2:] == "flat":
        new_note = note[0]+"\u266d"
    else:
        new_note = note
    print(new_note)
    return new_note  

#Determines the starting index of the note
def set_index(note):
    #print("----------------------------")
    index = 0
    while note != MUSICAL_NOTES[index]:
        index += 1
    print("Index =",index)
    return index

#Determines the note in the minor scale
def set_minor_scale(index):
    minor_notes = []
    
    for x in MINOR_SCALE_STEPS:
        if index >= len(MUSICAL_NOTES):
            index = index % 12
            
        minor_notes.append(MUSICAL_NOTES[index])
        index += x
    return minor_notes

if __name__ == "__main__":
    starting_note = input("Enter a starting note: ")
    note = set_note(starting_note)
    
    if note not in MUSICAL_NOTES:
        print("There is no starting note",note)
        starting_note = input("Enter a starting note: ")
        note = set_note(starting_note)

    
    while starting_note != EXIT_STRING:
        starting_index = set_index(note)

        minor_scale = set_minor_scale(starting_index)
        minor_scale.append(note)
        for x in minor_scale:
            print(x,end = " ")
            
        starting_note = input("\nEnter a starting note: ")
        note = set_note(starting_note)