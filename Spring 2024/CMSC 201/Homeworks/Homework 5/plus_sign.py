"""
File:    plus_sign.py
Author:  Pooja Rajamanikandan
Date:    03/04/2024
Section: 16
E-mail:  le64534@umbc.edu
Description: The program implements a function to check if the is plus sign by in a randomly generated 2-d list
"""
import random

def generate_grid(m, n, seed=0):
   if seed:
       random.seed(seed)
   return [[random.choice(['.', '*']) for _ in range(n)] for _ in range(m)]

def display_grid(the_grid):
   for row in the_grid:
       print(' '.join(row))

def is_plus_there(my_grid):
   for r in range(len(my_grid)-2): # disregards the last two rows of the grid
      for c in range(1,len(my_grid[r])-1): #considers only the 1 index value and the second to last index value

         if my_grid[r][c] == "*":
            if my_grid[r+1][c] == "*" and my_grid[r+2][c] == "*": # checks the 2 columns 
               if my_grid[r+1][c-1] == "*" and my_grid[r+1][c+1] == "*": #checks the 2 index values rows of the same row
                  return True 
   
   return False
               
            
               

if __name__ == '__main__':
   numbers = input('Enter the dimensions (and optionally the seed): ').split()
   x = int(numbers[0])
   y = int(numbers[1])
   the_seed = int(numbers[2])
   a_grid = generate_grid(x, y, the_seed)  
   display_grid(a_grid)

   print(is_plus_there(a_grid))

   