# -*- coding: utf-8 -*-
"""
CS_521 Information Structures in Python
Assignment 2
Created on Thu Mar 25 09:12:56 2021

@author: James Hardy
"""
# 2.1.1: Prompts user to enter number. in one calc, take input +2*3-6/3. 
# Use if statement to check whether the input matches calculated value 
#print result of this check in descriptive message:
    
num_input = int(input(">$ Enter a number:"))
calc_one = (num_input + 2 * 3 - 6 / 3)
if calc_one != num_input:
    print(calc_one, "is calculated from: ", num_input)
else:
    print("Your number equals: ", num_input)
    
#2.1.2: Prompt user for input and then print that input as: 1. str, 2. int, 3. flt
user_input = input(">$ Enter some data here!")
user_str = str(user_input)
user_int = int(user_input)
user_flt = float(user_input)
print(user_str)
print(user_int)
print(user_flt)    
#ANSWER Q: what data types can be input that will print without generating ANY ERRORS?
"""
It appears that Integers will not cause an error message.(They can be easily converted to both other types).  
Strings will cause error message. 
Floats, interestingly, also cause error message.
"""

#2.1.3: Write a python program that asks the user to enter an integer(n) and compute the value of:
    #n+n*n+n*n*n+n*n*n*n = ?
#The program must then print the formula, replacing the 'n' variables with the user input, and the ? with the calc results.
#Numbers greater than 1000 must have a comma seperator. **Print using an F string or format() function.     


n = int(input(">$ Please enter an integer: "))
calc_val = n+n*n+n*n*n+n*n*n*n
print(f"The calculated answer is: {calc_val:,}")

# Write a 3 line program that 1: prompts for a number, 2: converts the input to an integer, and 3: prints the number 0 if even; 1 if odd
  
    
user_input = int(input(">$ Please enter a number: "))
print(1) if user_input % 2 == 0 else print(0)     
    
    
    
x = {"salmon": "fish", "orca": "whale"}  
y = x["fish"]  
print(y)
    
    
