"""
File:    which_month.py
Author:  Pooja Rajamanikandan
Date:    02/14/2024
Section: 16
E-mail:  le64534@umbc.edu
Description:  The program will ask the user how may months in the future they to go from the intial month and 
  determines the final month.
"""
month_now = int(input("What month are we starting in (enter as an int)"))
if month_now < 1 or month_now > 12:
  print("That is not a month between 1 and 12.")
  month_now = int(input("What month are we starting in (enter as an int)"))
  
month_future = int(input("How many months in the future should we go? "))

final_month = (month_now + month_future) % 12

if final_month == 1:
  print("The month wil be January")
elif final_month == 2:
  print("The month wil be February")
elif final_month == 3:
  print("The month wil be March")
elif final_month == 4:
  print("The month wil be April")
elif final_month == 5:
  print("The month wil be May")
elif final_month == 6:
  print("The month wil be June")
elif final_month == 7:
  print("The month wil be July")
elif final_month == 8:
  print("The month wil be August")
elif final_month == 9:
  print("The month wil be September")
elif final_month == 10:
  print("The month wil be October")
elif final_month == 11:
  print("The month wil be November")
elif final_month == 0:
  print("The month wil be December")