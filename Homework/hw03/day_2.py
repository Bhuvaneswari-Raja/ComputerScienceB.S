#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
File: day_2.py
Author: Pooja Rajamanikandan
Date: 09/26/2023
Lab Section: 50
Email:  le64534@umbc.edu
Description: The program will determine the day of the week using at least 
    one listand modulus division
"""


# In[19]:


if __name__ == "__main__":
    num_date = int(input("What day of September 2023 is it? "))
    
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    

    if num_date == 1 or num_date == 21:
        suffix = "st"
    elif num_date == 2 or num_date == 22:
        suffix = "nd"
    elif num_date == 3 or num_date == 23:
        suffix = "rd"
    else:
        suffix = "th"
    

    if num_date % 7 == 1:
        print("September {}{} is a {}".format(num_date,suffix,days[4]))
    elif num_date % 7 == 2:
        print("September {}{} is a {}".format(num_date,suffix,days[5]))
    elif num_date % 7 == 3:
        print("September {}{} is a {}".format(num_date,suffix,days[6]))
    elif num_date % 7 == 4:
        print("September {}{} is a {}".format(num_date,suffix,days[0]))
    elif num_date % 7 == 5:
        print("September {}{} is a {}".format(num_date,suffix,days[1]))
    elif num_date % 7 == 6:
        print("September {}{} is a {}".format(num_date,suffix,days[2]))
    elif num_date % 7 == 0:
        print("September {}{} is a {}".format(num_date,suffix,days[3]))
    else:
        print("That day",num_date,"is out of range, you must enter a number between 1 and 30")



# In[15]:


4%7


# In[ ]:




