# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:09:11 2021

@author: James Hardy
@class CS_521 Information structures in Python
"""
#Final Project Main file:
from Classes_final_project import FitnessStatus #PARENT CLASS
    
from Classes_final_project import DoingGreat      #ch

from Classes_final_project import DoingOkay        #ch

from Classes_final_project import NeedsImprovement  #ch


#BMI = round(weight / (height * height), 2)
# 5'9" in CM = 175.26 CM
# 155 pounds = 70.31 Kilos

#--------------------------------------------------------------------------
#takes users height, weight, and activity level in prompts:
#user input:   
#if __name__ == 'main':     
height = float(input('$> Please enter your height in CM:  >'))
weight = float(input('$> Please enter your weight in Kilos:  >'))
act_level = input('$> active, average, or sedentary?  >')



assert height < 300, "error: height outside of program range! The NBA needs you!"
assert weight < 227, "error: weight outside of program range! Go see a doc!"
#assert act_level == ('active' or 'average' or 'sedentary'), 'error! invalid activity level! Use the options! \
#This is not a creative writing class!'


#containers: lists:---------------------------------------------------------
height_list = []
height_list.append(height)
#print(height_list)
weight_list = []
weight_list.append(weight)
#print(weight_list)

#iterators, methods------------------------------------------------------------
for i in height_list:
    if len(height_list) > 1:
        height_list.remove(i)
#print(height_list)


#operations-------------------------------------------------------------------

def Activity_Lev(act_level):
    "prints a different message depending on users activity level"
    if act_level == 'active':
        return f' KEEP IT UP CHAMP! YOU DA MAN!! '
    elif act_level == 'average':
        return f'Okay, good. How can you improve? '
    elif act_level == 'sedentary':
        return f' YOU GOOD FOR NOTHING MAGGOT! DROP AND GIVE ME TEN!!!'
    
def Cm_To_Sq_Meters(height):
    "takes height in cm, converts to sq meters"
    converted_height = height / 100
    return converted_height
 
       
def BMI(converted_height, weight):
    "calculates Body Mass Index from height: square meters, weight: Kilos"
    try:
        body_mass_index = round(weight / (Cm_To_Sq_Meters(height) **2), 2)
        return body_mass_index
    except ZeroDivisionError:
        f"CANNOT DIVIDE BY ZERO!!"
print(f'Your body mass index is:  >{BMI(height, weight)}')

print(f'Activity level analysis:  >{Activity_Lev(act_level)}')

#conditional logic chooses which class to call; depending on BMI:
#---------------------------------------------------------------------------
a1 = DoingOkay(True, True)
a2 = DoingGreat(True, True)
a3 = NeedsImprovement(True, True)
  
if BMI(Cm_To_Sq_Meters(height), weight) > 46:
    print( a3)
elif BMI(Cm_To_Sq_Meters(height), weight) < 30 and act_level == 'active':
    print( a2)
else:
    print( a1)


    
#write Body Mass Index to output file for clean result:------------------
import os
direc = "C:\\Users\\Administrator\\OneDrive\\Documents\\BU SPRING '21\\521 Information structures with Python\\final project"
input_file_name = os.path.join(direc, 'final_project_output.txt')
d_file = open(input_file_name, "w")
d_file.write(str(f'YOUR BODY MASS INDEX WITH HEIGHT: {height} CM and WEIGHT: {weight} Kilos IS: {BMI(Cm_To_Sq_Meters(height), weight)}'))
d_file.close()    
#-------------------------------------------------



