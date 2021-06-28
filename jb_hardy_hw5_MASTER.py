# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:37:25 2021

@author: James Hardy
@class CS_521 information structures in python
"""
#5.5.1---------------------------------------------------------------
#close but need to validate english, make sure print statements meet req. 

#divide and conquer

def Vc_Counter(u_i):
    "Counts vowels and consonants"
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ascii_vowels = "aeiouyAEIOUY"
    
    ascii_cons = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
   # vowel_count = 0
    #consonant_count = 0
    total_vowels = []
    total_consonants = []
    import string
    punct = [string.punctuation]
    #print(punct)
    punct_list = []   
    u_i = input('$> Please Enter a Sentence: >')
    for i in u_i:
        if i in ascii_vowels:
            total_vowels.append(i)
            vowel_count = len(total_vowels)
            #print(total_vowels)
        elif i in ascii_cons:
            total_consonants.append(i)
            consonant_count = len(total_consonants)
            #print(total_consonants)
    else:
           # c = dict(zip(total_vowels, total_consonants,))
            c = {f'{total_vowels}': f'{vowel_count}', \
                 f'{total_consonants}': f'{consonant_count}' }
           # y_dict = {k: v for k, v in x_dict.items() if v == 'cat'}
            #print(y_dict)
            #print(f' # vowels: {vowel_count} # consonants: {consonant_count}')
            return c   

def main():
   "execution control center of functions:"
   out= Vc_Counter(u_i)
   return out


if __name__ == "__main__":
    main()                   
     #(vowel_count, consonant_count)           
    #print(cons_res)
    #print(vowel_res)   
#----------------------------------------------------------------------------

#5.5.2---------------------------------------------


#lists for each range:
year = list(range(0, 2022))
["{:04d}".format(item) for item in year]
month = list(range(0, 13))
["{:02d}".format(item) for item in month]
day = list(range(0, 32))
["{:02d}".format(item) for item in day]
hour = list(range(0, 61))
["{:02d}".format(item) for item in hour]
minute = list(range(0, 61))
["{:02d}".format(item) for item in minute]
seconds = list(range(0, 61))
["{:02d}".format(item) for item in seconds]


#USE THIS TO CHECK MONTH LENGTH
#no leading zeros...
month_days_dict = {1: 31, 2: 28, 3:31, 4:30, 5:31, \
6: 30, 7: 31, 8: 31, 9: 30, 10 : 31, 11 : 30, 12: 31}
 #add leading zeros...   
leading_zero_k =["{:02d}".format(item) for item in month_days_dict.keys()]
j = dict(zip(leading_zero_k, month_days_dict.values()))
print(j)
    


#date = print(f"{month} : {day} : {year} : {hour} : {minute} : {seconds}")
#0123456789101112131415161718
#07/07/2021   12 : 3 1 : 5 9
#special char at [3 /] [6 /] [10-space] [13:] [16:]
#-----------------------------------------------------------------------------

def Is_Valid_Datetime(u_i):
    "validates that user entered correct date format:"
        #month:--------01-------------------------------------------
    e = Exception('You entered an invalid date format!')  
    if  ":" in (u_i[0:2]) or '/' in u_i[0:2] and (u_i[0:2]) not in j.keys():   
                       #print('......month passed validation!')
            print(f' {e} ')
            return False       
    else:
        pass
    #day-----34---------------------------------------------------
    try:
       
        if  ":" and "/" not in (u_i[3:5]) and (u_i[3:5]) in  ["{:02d}".format(item) for item in day]:
   
            #print('......day passed validation!')
            pass
    except Exception as e:
            print(f"{e}")
            return False
        
    #year------6789------------------------------------------------
    b_3 = len(u_i[6:10])
    if  ":" not in (u_i[6:10]) and '/' not in u_i[6:10] and (u_i[6:10]) in ["{:04d}".format(item) for item in year]:
            #print('......Year validated.')
            pass
    else:
            print(f"{e}")
            return False
        
    #hour---------------------------1113141617?---------------------------
    b_4 = len(u_i[11:13]) 
    if  ":" and "/" not in (u_i[11:13]) and (u_i[11:13]) in ["{:02d}".format(item) for item in hour]:
            #print('......hour passed validation!')
            pass
    else:
            print(f"{e}")
            return False
        
    #minute------------------------------------------------------
    b_5 = len(u_i[14:16])
    #for k, v in j: 
    if  ":" and "/" not in (u_i[14:16]) and (u_i[14:16]) in ["{:02d}".format(item) for item in minute]:
           # print('......minute passed validation!')
           pass
    else:
            print(f"{e}")
            return False
           
    #seconds -----------17 19----------------------------------------------   
    b_6 = len(u_i[17:19])
    #for k, v in j: 
    if (u_i[17:19]) in ["{:02d}".format(item) for item in seconds]:
            #print('......seconds passed validation!')
            #print('DATE IS VALID')
            valid = True
            pass
    else:
            print(f"{e}")
            return False
    #return section:---------------------------------------------------------        
    if valid == True:
            return None
    else:
            e_message = 'Error: invalid date format.'
            return e_message
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

#create a try / except section to deal with errors. 

#write code to deal with erroneous errors:
print(f'Welcome! *Please follow directions to avoid errors:')
u_i = input("$> Please enter a date and time exactly as: MM/DD/YYYY HH:MM:SS:  > ")
Is_Valid_Datetime(u_i)
if Is_Valid_Datetime(u_i) == True:
   print(f'DD/MM/YYYY is: {u_i[0:10]}')
   print(f'HR:MIN:SEC is: {u_i[11:20]}' )
   print(f'MM/YYYY is: {u_i[3:10]}')
   if int(u_i[11:13]) >= 12:
        print(f'the time is PM')
   else:
        print(f'The time is: AM')
        
#hour 
# example input:   should work:         07/07/2021 12:31:59

#----------------------------------------------------------------------------

#5.6.3---------------------------------------------------------------------


def Num_Prog():
    "takes user input, performs (x/y)+z and returns result"
    Exception(' ')
    #get user input; make sure it's 3 values:
    try:    
        x,y,z = input('$> Please enter three numbers:  > ')
        int_x = int(x)
        int_y = int(y)
        int_z = int(z)
    #if validation fails, print descriptive error message linked to Exception:    
    except ValueError as e:
        print(f'Python error... you entered a non-number or too many / not enough #: {e} ')
        return None
    #take user input; perform operation, return value:
    try:
        storage_list = f"{int_x},{int_y},{int_z}".split(",")
        #print(storage_list)
        #print(f'You entered: {x}, {y}, {z}')
        op = (int_x/int_y)+int_z
        ret_stmt = print(f'Result of ({int_x} / {int_y} )+ {int_z} = {op}')
        return ret_stmt
    #if y_int == 0:
    except ZeroDivisionError as e_1:
            print(f'Cannot divide by zero! {e_1}')
              
            
#check user entered 3 values
#check for ValueError and ZeroDivisionError
#print descriptive error messages to the console if validation fails
#Remember to have very granular test blocks    
                

Num_Prog()






#check for: 
#user entered 3 values == #ValueError 
#ZeroDivisionError
#descriptive error messages 
#granular testing blocks 


#----------------------------------------------------------------------------
#5.8.4
#---------------------------------------------------------------------------


def File_Txt_To_List(r):
    "converts text from file into list"
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in r:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list




    store_list = list()
    d_file = open(input_file_name, "r")
    #read lines into list:
    r = d_file.readlines()
    print(r)
    for i in r:
        if i.isunique():
            store_list.append(i)
    return store_list
    
#-----------------------------------------------------------------------------

#UNFINISHED***************************

def List_To_Once_Words(r):
    import os
    direc = "C:\\Users\\Administrator\\OneDrive\\Documents\\BU SPRING '21\\521 Information structures with Python\\Assignments\\HW5"
    input_file_name = os.path.join(direc, 'assign5ext.txt')
    d_file = open(input_file_name, "r")
    #read lines into list:
    #r = d_file.readlines()
    res = []
    for i in r:
        res.append(i)#split(", ")))
    #print(res)
    res_set = set(res)
    #print(res_set)
    unique_list = [res_set]
    return unique_list

   
    
   # os.getcwd()  # check working directory
    #change working dir: sorry for going over 80 char:
    #os.chdir("C:\\Users\\Administrator\\OneDrive\\Documents\\BU SPRING '21\\521 Information structures with Python\\Assignments\\HW5")
    #sorry for going over 80 char:
    #direc = "C:\\Users\\Administrator\\OneDrive\\Documents\\BU SPRING '21\\521 Information structures with Python\\Assignments\\HW5"
    #prompt for a file name:
    
    
    
    #input_file_name = open(direc, 'assign5ext.txt')
    
    #open a file
    #d_file = open(input_file_name, "r")
        #read lines into list:
    #r = d_file.readlines()
    



if __name__ == "__main__":
#close file
    input_file_name = input('$> Please enter file_name:  >  ')
    d_file = open(input_file_name, "r")
    r = d_file.readlines()
    List_To_Once_Words(r)


#-------------------------------------------------------------------------
text = d_file.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

#finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

#sort
unique.sort()

#print
print(unique)

d_file.close()








#5.15.5-----------------------------------------------------------------------

def Calc_Compound_Interest(p, percent_interest_rate, num_years):
    "Calucates compound interest non-recursively"
    i = (percent_interest_rate)
    o = int(num_years)
    comp_int = p*(1+i) ** o
    return comp_int

#-----------------------------------------------------------------------------    
#function 2:

    
def Calc_Compound_Interest_Recursive(p, percent_interest_rate, num_years):
    "Calculates compound interest recursively"
    done = False
    for e in range(0, num_years):
        p = (1 + percent_interest_rate) * p
    return p       
#----------------------------------------------------------------------------
#txt = '\n'.join(lines)


#while loop to prompt user for p, %rate, and num_years:
done = False
while not done:
    p = int(input("$> Please enter principal: >"))
    percent_interest_rate = float(input('$> Please enter % interest rate >'))
    num_years = int(input('$> Please enter number of years: >'))
    
    #print(formatted_func)
        
    #validate number of inputs: 
    storage_list = list()
    storage_list.append(p)
    storage_list.append(percent_interest_rate)
    storage_list.append(num_years)
    formatted_func_nr = '{:,.2f}'.format (Calc_Compound_Interest(p, percent_interest_rate, num_years)) 
    formatted_func_rec = '{:,.2f}'.format (Calc_Compound_Interest_Recursive(p, percent_interest_rate, num_years))
    if len(storage_list) == 3:
        done = True
        print(f'non-recursive: {formatted_func_nr}')
        print(f'recursive: {formatted_func_rec}')
    else:
        print('Error: values do not match questions......')



#--------------------------------------
#'{:,.2f}'.format(param)

print(f"{Calc_Compound_Interest(p, percent_interest_rate, num_years):,}")  
'{:,.2f}'.format( Calc_Compound_Interest(p, percent_interest_rate, num_years))
#function 1 -----------------------------------------------------------------    


#Calc_Compound_Interest_Recursive(principle, percent_interest_rate, num_years)        

#print if values are equal when rounded to four decimal places. 


#Calc_Compound_Interest(p, percent_interest_rate, num_years)


#works but needs cleanup 
#Calc_Compound_Interest_Recursive(p, percent_interest_rate, num_years)










    