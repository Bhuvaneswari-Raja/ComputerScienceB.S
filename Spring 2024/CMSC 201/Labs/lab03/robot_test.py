"""
File:    robot_test.py
Author:  Pooja Rajamanikandan
Date:    02/19/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: 
"""

if __name__ == "__main__":
        
    user = input("Be you robot, or human? ")

    if user.lower() == "human":
        print("Humans must be destroyed!")
    if user.lower() == "robot":
        print("Administer the test!")
        print("Which of following would you prefer")
        print("A puppy\nA flower\nA data file")
        preference = input("Choose! ")
        
        if preference.lower() == "puppy":
            print("Get the intruder! Get the humanoid!")
        elif preference.lower() == "flower": 
            print("That is acceptable, pass on mechanical friend")
        elif preference.lower() == "data file":
            print("Very good, you are a robot of some esteem")