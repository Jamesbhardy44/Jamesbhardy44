# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 13:07:20 2021

@author: James Hardy 
@CS_521 Information structures in python
"""

class Organ(object):
    def __init__(self, organ_name, organ_weight_grams, is_vital_organ, \
                 organ_system, is_transplantable, organ_gender):
        self.organ_name = organ_name
        self.organ_weight_grams = organ_weight_grams
        self.is_vital_organ = is_vital_organ
        self.organ_system = organ_system
        self.is_transplantable = is_transplantable
        self.organ_gender = organ_gender
        
    def __repr__(self):
        return f'{self.organ_name}, {self.organ_weight_grams}, {self.is_vital_organ},\ {self.organ_system}, \
 {self.is_transplantable}, {self.organ_gender}'
#----------------------------------------------------------------- 
o1 = Organ('heart', .5, True, "cardio", True, "male")    
print(o1)
#-----------------------------------------------------------------


class Heart(Organ): #look okay? 
    def __init__(self, heart_lenth_cm, heart_width_grams, heart_thickness_cm, heart_breadth_cm):
        Organ.__init__(self, "Heart", 289.6, True, "Muscular system", True, "Male")
        self.heart_length_cm = heart_lenth_cm
        self.heart_width_grams = heart_width_grams
        self.heart_thickness_cm = heart_thickness_cm
        self.heart_breadth_cm = heart_breadth_cm
       
    def __repr__(self):
         return f' Heart length: {self.heart_length_cm}, Heart width: {self.heart_width_grams},\
 Heart Thickness: {self.heart_thickness_cm},Heart Breadth: {self.heart_breadth_cm}'
        
    def Heart_Status():
        return f'Pumping Blood'
    
    def Heart_Weight(self, organ_weight_grams):
        converted_value = organ_weight_grams / 28.35 # takes grams; converts to oz
        return converted_value
        
h1 = Heart(12, 8.5, 6, 8.21)        
print(h1)        

#-------------------------------------------------------------------------------        
# 
hw = 289.6        
Heart.Heart_Weight(hw, hw)        
 #-----------------------------------------------------------------------------
#organ_name, organ_weight_grams, is_vital_organ, \
                 #organ_system, is_transplantable, organ_gender

class Brain(Organ):
     def __init__(self, brain_volume, organ_weight_grams): #do i need more args?
        Organ.__init__(self, "Brain", 1260, True, "neurological", False, "male")   
        self.brain_volume = brain_volume
        self.organ_weight_grams = organ_weight_grams
        
     def __repr__(self):
         return f' { self.brain_volume}, {self.organ_weight_grams}'
        
     def Brain_Status(self):
         return 'Thinking'
     
     def Brain_Weight(self, organ_weight_grams):
         b_converted_value = organ_weight_grams / 28.35
         return b_converted_value
        
if __name__ == 'main':
      h1 = Heart(12, 260, 6.0, 9.0)      #instantiate heart object   
      print(h1)        

#-------------------------------------------------------------------------------        
# 
      hw = 289.6        
      Heart.Heart_Weight(hw, hw)            
      
  #organ_name, organ_weight_grams, is_vital_organ, \
  #organ_system, is_transplantable, organ_gender  
  
      brain_type_system = 'Neurological'
      is_transplantable = True
      b1 = Brain( 1360, 286)#QUESION POINT--------------
      print(b1)
      
      