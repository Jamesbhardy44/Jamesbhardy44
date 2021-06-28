# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:51:33 2021

@author: James Hardy
@class: CS_521 Information Structures in Python
@assignment 4 Master doc:
"""

#4.7.1: Find the sum of list range 1-10 inc; no loops. 
#list comprehension x for x in list x if list is even 
X_list = list(range(1, 11))
sum_even_X_list = sum(list(range(2,11,2)))
sum_odd_X_list = sum(list(range(1,11,2)))
print(f"Evaluating the numbers in: {X_list}")
print(f"Even: {sum_even_X_list}")
print(f"Odd: {sum_odd_X_list}")

#-----------------------------------------------------------------
#4.7.2 given constant list of int; make new list 
#same number of elements as original such that 
#each int in new list is sum of its nearest neighbors and itself 
#from original list. 

X_LIST = [1,2,3,4,5]

#
def Add_Neighbors(X_list):
    "adds the neighbors of a list and appends to new list"
    y_list = []
    y_list.append(X_list[0] + X_list[1])
    x = 1
    while x < len(X_list) - 1:
        y_list.append(X_list[x - 1] + X_list[x] + X_list[x + 1])
        x += 1
    y_list.append(X_list[x - 1] + X_list[x])
    print(f"Input List:{X_list}")
    #only the list
    return y_list


z = Add_Neighbors(X_list) 
print(f'Sum of neighbors and itself: {z}')
#--------------------------------------------------------------
#4.9.3   create dictionary if list len is equal.--------------------------
a = 0
b = 0
First_names = ['Karl', 'John', 'Kobe', 'Michael']
Last_names = ['Malone', 'Stockton', 'Bryant', 'Jordon']
#uncomment to try unmatched sized lists:
#Last_names = ['Smith', 'Stockton', 'Fields', 'Johnson', 'fifth-wheel']

#use zip to create the dict
#------------------------------------------------------------------
def Check_Length(a, b):
    "checks length of input lists. if same; creates dictionary"
    a=len(First_names)
    b=len(Last_names)
    if a > b or b > a:
        print("Error: list sizes do not match! Aborting zip...")
    else:
        c = dict(zip(First_names, Last_names))
        return c
        
#------------------------------------------------------------------
Check_Length(First_names, Last_names)
print("List sizes match! zipping.......")
print(f'First Names: {First_names}')
print(f'Last Names: {Last_names}')
print(f'new zipped dictionary:',Check_Length(a,b))

#------------------------------------------------------------------


#4.9.4 using my_dict = {a':15, 'c':18, 'b':20}
#print all keys, values, key  value pairs, 
#key value pairs in asc order of key
#key value pairs in desc order of value

my_dict = {'a':15, 'c': 18, 'b': 20}
key_list = []
val_list = []
#print all keys:
for key in my_dict:
    key_list.append(key)
    
print(f'Keys: {key_list}')
  
#print all values:
for value in my_dict.values():
    val_list.append(value)
    
print(f'values: {val_list}')    

#print all key value pairs:
print(f'key value pairs: {my_dict}')    

#print key value pairs in asc order of key: (a, b, c)
sorted_by_keys = sorted(my_dict)
for i in sorted_by_keys:
    print(f'in asc order of key: {i}, value: {my_dict[i]}')

#print key value pairs in desc order of value: (20, 18, 15)
print('In reverse order of values:')
print(sorted(my_dict.items(), reverse = True, \
             key = lambda kv:(kv[1], kv[0])))   
    
   
    

#----------------------------------------------------------------
#4.9.5

#create three functions with docstrings

#letter_count()

#takes a string as its argument and returns a dictionary 
#of the letters as keys and frequency counts as values. 


#assign sentence of > 15 char into a string variable:
    
#used throughout:
    
B_str = "THISISASTRINGVAR"


#-----------------------------------------------------------------------------
def Letter_Count(B_str):
    "takes a string as arg and returns dict; letters =k, freq of letters = v"
    if __name__ == '__main__':
        #new empty dict to count letter frequency:
        dict_1 = {}
        #for loop to iterate through and check letter frequency
        for i in B_str:
            if i in dict_1:
                dict_1[i] += 1
            else:
                dict_1[i] = 1  
     #print output:     
    #print(f'The string being analyzed is B_str: {B_str}') 
    #print(f'{dict_1}') 
    return dict_1

#-------------------------------------------------------------------------
Letter_Count(B_str)
#need print statement that describes dict of letter count
print(f'Letter Count: {Letter_Count(B_str)}')
    
#largest value of the values
#most_common_letter()



def Most_Common_Letter(B_str):
    "Counts the most common letter in given string"
    if __name__ == '__main__':
        #calls previous function to get dictionary:
        u = Letter_Count(B_str)
        #iterable type; 
        u.values()
        #print(u.values())
        #convert to list, and put back into u var
        u_vals = list(u.values())
        sorted(u_vals)
        #sorted just changes the current representation
        #print(sorted(u_vals, reverse = True))
        #first val in this list is largest
        #get max value from u_vals:
        mcl = sorted(u_vals, reverse = True)[0]
        h = []
        for k, v in u.items():
            if v == mcl:
               h.append(k)
               
        #print(h)  
        #join to make list into string
        #RETURN STATEMENT WITH STRING NOT LIST
        j = ''
        k = j.join(h) 
        #print(k)
        return k
            


#-------------------------------------------------------------------------
Most_Common_Letter(B_str)
print(f' The most common letter(s) is/are: {Most_Common_Letter(B_str)}')
#function returns string most common letter
#----------------------------------------------------------------------
#string_count_histogram()
#takes string as arg; returns list of unique letters; 
#each letter repeated as it is in string;
#This new list will be printed 1 element per line like a histogram
#this function should call Letter_Counts()

def String_Count_Histogram(B_str):
    "returns a histogram of letter frequency in given string"
    if __name__ == '__main__':
        #call previous function to get our dictionary:
        t = Letter_Count(B_str)         
        hist = []
        #for i in B_str:
             #hist[i] = hist.get(i, 0) + 1
        for k, v in t.items():
            n = k*v
            hist.append(n)
    return hist
        
        
     
    #print letter the number of times it appears         
String_Count_Histogram(B_str) 
print(f'Histogram: {String_Count_Histogram(B_str)}')               
#print statement that pulls return statement of the function. 
#4.9.6--------------------------------------------------------

#-----------------------------------------------------------------
#simplified:

x = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "-", ".",]
y = ['zero',"one", 'two', 'three', 'four', 'five', 'six', \
           'seven', 'eight', 'nine', "ten", "negative", "point" ]
#create dictionary of x and y:
z = dict(zip(x,y))
print(z)
print(z.items())
print(z.keys())
print(z.values())
#-------------------------------------------------------------------

#start loop:----------------------------------------------------------
import string
l = string.punctuation 
print(l)
#remove minus sign and decimal point from punctuation list:
l.remove('-')
l.remove('.')
l = list(l)

#test cases:
    #1 - regular valid number   -works
    #2 - minus sign and decimal point     -works
    #3 - invalid input = alpha or comma   - works
#debugging: space bar makes loop go forever

res = []
done = False
#initiate loop; do until conditions met
while not done:
        u_i = str(input("$> Please enter a number:"))
        print(f' Checking...........')
        h = str.isspace(u_i)
        for i, e in enumerate(u_i):
              if (i in l) or  (u_i.isalpha()) or (',' in u_i) or (u_i in z.values()):
                  print('*Error: Invalid input. *(no commas/words allowed!) Try again:')
                  break
              else:
                  if e in z.keys():
                      print(f'working.... value {e} found. validation passed.')
                      g = z[e]
                      res.append(g)
                      print('added to list!')
                      done = True 
                      #print('loop will now terminate...... Thank you!')
print(f' Your Number: {u_i}')
print(f' As Text: {res}')           
            
#------------------------------------------------------------------------------
some_stuff =0
done = False
while not done:
    if(some_stuff):
        done = True
        
        
#-------------------------------------------------------------------------




