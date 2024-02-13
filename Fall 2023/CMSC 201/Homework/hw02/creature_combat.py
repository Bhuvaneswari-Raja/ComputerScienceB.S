"""
File:        creature_combat.py
Author:      Pooja Rajamanikandan
Date:        09/18/2023
Section:     50
E-mail:      le64534@umbc.edu
Description: Combat between two creatures will if one of the creature 
    wins or they both die or they both die
"""
creature_1_name = input("What is the name of the first creature? ")
creature_1_power = int(input("What is the power of the first creature? "))
creature_1_toughness = int(input("What is the toughness of the first creature? "))
creature_2_name = input("What is the name of the second creature? ")
creature_2_power = int(input("What is the power of the second creature? "))
creature_2_toughness = int(input("What is the toughness of the second creature? "))

#calculates the final toughness of both creature
creature_1_stat = creature_1_toughness - creature_2_power
creature_2_stat = creature_2_toughness - creature_1_power

print("The first creature now has ({}, {})".format(creature_1_power, creature_1_stat))
print("The second creature now has ({}, {})".format(creature_2_power, creature_2_stat))

#determines which creatures dies or survies 
if creature_1_stat <= 0 and creature_2_stat <= 0:
    print("Both creatures die in mutual combat")
elif creature_1_stat > creature_2_stat:
    print("{} has died, {} wins".format(creature_2_name,creature_1_name))
elif creature_1_stat < creature_2_stat:
    print("{} has died, {} wins".format(creature_1_name,creature_2_name))
else:
    print("Both creatures live to fight another day")