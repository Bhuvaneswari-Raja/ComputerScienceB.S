"""
File:        leap_year.py
Author:      Pooja Rajamanikandan
Date:        09/18/2023
Section:     50
E-mail:      le64534@umbc.edu
Description: Ask the user for a numerical day in September 2023 and
    tell them what day of the week it was 
"""
num_date = int(input("What day of September 2023 is it? "))

if num_date == 1 or num_date == 21:
    suffix = "st"
elif num_date == 2 or num_date == 22:
    suffix = "nd"
elif num_date == 3 or num_date == 23:
    suffix = "rd"
else:
    suffix = "th"

if num_date == 1 or num_date == 8 or num_date == 15 or num_date == 22 or num_date == 29:
    print("September {}".format(num_date)+ suffix +" is a Friday")
elif num_date == 2 or num_date == 9 or num_date == 16 or num_date == 21 or num_date == 28:
    print("September {}".format(num_date)+ suffix +" is a Saturday")
elif num_date == 3 or num_date == 10 or num_date == 17 or num_date == 24:
    print("September {}".format(num_date)+ suffix +" is a Sunday")
elif num_date == 4 or num_date == 11 or num_date == 18 or num_date == 25:
    print("September {}".format(num_date)+ suffix +" is a Monday")
elif num_date == 5 or num_date == 12 or num_date == 19 or num_date == 26:
    print("September {}".format(num_date)+ suffix +" is a Tuesday")
elif num_date == 6 or num_date == 13 or num_date == 20 or num_date == 27:
    print("September {}".format(num_date)+ suffix +" is a Wednesday")
elif num_date == 7 or num_date == 14 or num_date == 21 or num_date == 28:
    print("September {}".format(num_date)+ suffix +" is a Thursday")
else:
    print("That day",num_date,"is out of range, you must enter a number between 1 and 30")


print(16,"th")


num_date = int(input("What day of September 2023 is it? "))

print("What is happening?  ",num_date == 2 or 9 )
print(num_date)