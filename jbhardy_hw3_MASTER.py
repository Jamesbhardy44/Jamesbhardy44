# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:40:23 2021

@author: James Hardy
CS_521 Assignment 3
Master 
"""


#3.2.1
#------------------------------------------------------------------
#initialization:
 
    
Min_range = 2
Max_range = 130
    
#MAIN LIST FOR PROGRAM:
a = list(range(Min_range, Max_range))

#print(a)

#------------------------------------------------------------------
#count all even numbers
even_a = list(range(2, 131, 2))
even_a_len = len(even_a)
#print(f'There are {even_a_len} even numbers within list a')

#------------------------------------------------------------------
#count all odd numbers
odd_a = list(range(3, 131, 2))
odd_a_len = len(odd_a)
#print(f'There are {odd_a_len} odd numbers within list a')


#print(odd_a)
#print(even_a)

#------------------------------------------------------------------        
# counts the squares of an integer within the list:
  
squares_count = 0
for i in a: 
   squares_count+=1
   squared_i = i**2
   #print(f'{i} squared: {squared_i}, index: {squares_count}')
 

#------------------------------------------------------------------
#counts the number of cubes within the list:         

cubes_count = 0
for i in a: 
   cubes_count+=1
   cubed_i = i**3
  # print(f'{i} cubed: {cubed_i}, index: {cubes_count}')

#PRINTING SECTION:
#------------------------------------------------------------------        

str1 = F"Checking numbers from {Min_range} to {Max_range}"
str1.title()  
print(str1.title())  
print(f"Odd ({odd_a_len}):  {Min_range} to ... {Max_range}")
print(f"Even ({even_a_len}): {Min_range} to ... {Max_range}")
#Does not meet requirements *************************
print(f"Square ({squares_count}):  {squared_i} {Min_range} to ... {Max_range}")
print(f'Cube ({cubes_count}): {cubed_i}')
#*****************************************************





#3.4.2 ------------------------------------------------------------


#Initialization:   
X = 'nyc'
y = len(X)
z = X[0]
w = X[1]
q = X[2]
#print(y)
#Declaration of X:
print(f"My 3 character string is: {X}")
#Conditional Logic to determine that the string X is odd:
if y % 2 == 0:
    print(f'ERROR: {X} has an even char length; this does not meet requirements')
elif y % 2 == 1:
    print(f"{X} has an odd char length.")
    print(f"{X} is {y} characters long")
    print(f"{w} is the middle character of {X}!")
    print(f"{z} is the string up to but not including the middle char!")
    print(f"{q} is the string immediately following the middle char to the end!")
    
 #3.4.3-----------------------------------------------------------------------
import string 
result = string.punctuation 
print(result)

str = input(">$ Please enter a sentence!: ")
lower_count= 0
upper_count = 0
digit_count = 0
punct_count = 0

#methods called: isupper(), islower(), isdigit(), punct checked string.punct
for i in str:
   if i.isupper():
       lower_count+=1
   elif i.islower():
       upper_count+=1
   elif i.isdigit():
       digit_count+=1
   elif i in string.punctuation:
       punct_count+=1
      
#PRINTING SECTION:
str_1 = f'#Upper #Lower #Digits #Punct '.title()
print(str_1) 
print("-----------------------------")     
print(f'{lower_count} |    {upper_count} |   {digit_count}  |  {punct_count}') 

#---------------------------------------------------------------------------

#3.4.4 -- Prompts user to enter three digit whole number 
#such that digits are in ascending order and without duplicates. 
#valid ex: 123 and 489
#invalid ex: 133 and 174


#does not catch duplicates or non sequential numbers at this time. 

int_input = []
x, y, z = input(">$ Please enter a 3 digit number in order; no repeats: ")
w = x + y + z
print(x, y, z, 'was entered into', int_input, 'list')
while len(int_input) != len(set(int_input)):
    int_input.pop()
    print('Duplicate detected. Try again!:')                
else:
    user_input = int_input.append(w)
    print('unique values: Valid.Adding to list.')
    print(int_input)
  
    
    

#----------------------------------------------------------------------------


#3.6.5----------- manually create a text file 
# files
import os
#path declared as variable
my_dir = 'C:/Users/Administrator/OneDrive/Documents/python'
# in the below lines, change the directory name to one on your computer
current_dir = os.getcwd()  # check working directory
os.chdir('C:/Users/Administrator/OneDrive/Documents/python')  # change it

#-------------------------------------------------
import os
current_dir = os.getcwd() 

os.listdir(current_dir)
#manually create a text file
f = open("example 1.py", "w+")
#rename to txt:
os.rename('example 1.py', 'Assignment3_file.txt')
#shows files in current dir
for filename in os.listdir(current_dir):
    if filename.endswith(('.txt', '.csv')):
        print(filename)
          
my_dir = 'C:/Users/Administrator/OneDrive/Documents/python'   
my_file = "Assignment3_file.txt"      
#with a single sentence of 20 words
#Initialization for control of writing:
Allowed_total_len = 20
Words_per_line = 5
num_lines = 5
num_words = 0
#re-assignment of var f to new filename with writing permission
f = open("Assignment3_file.txt", "w+")
#for loop writes to file:
for i in range(4):
    f.write("This is line number %d\r\n" % (i+1))
    f.truncate()  
#read file and check contents    
with open("Assignment3_file.txt", 'r') as my_file:
    data = my_file.read()
if data != 84:
    print("file is not correct size.")    
elif data == 84:
    print("file is correct size")      
      
f.close()

#3.14.6---------------------------------------------------------------


f = open("CH_14_EXC.txt", "w+")
       #--------------
a = [(), (), (), ()]
       #-------------
f.write("John Smith, 1, 3.5")
f.write("Dave Jenkins, 1, 3.7")
f.write("Bill Bob, 1, 3.5")
f.write("Chester Stephens, 1, 2.5")
f.truncate()  
#Check file and store line by line data into a collection. 

with open("CH_14_EXC.txt", 'r') as my_file:
  #data = my_file.read()
 a = my_file.readlines()
 print(a)

f.close()
