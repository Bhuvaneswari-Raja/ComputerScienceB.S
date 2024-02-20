"""
File:    which_month_2.py
Author:  Pooja Rajamanikandan
Date:    02/19/2024
Section: 
E-mail:  le64534@umbc.edu
Description:  The program will ask the user how may months in the future they to go from the intial month and 
  determines the final month.
"""
MONTHS = ["December","January","February","March","April","May","June","July","August","September","October","November"]

if __name__ == "__main__":
    
    month_now = int(input("What month are we starting in (enter as an int) "))

    if month_now < 1 or month_now > 12:
        print("That is not a month between 1 and 12.")
    else:
      month_future = int(input("How many months in the future should we go? "))
      final = (month_now + month_future) % 12

      print(f"The month will be {MONTHS[final]}")