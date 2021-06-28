# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:47:50 2021

@author: James Hardy
@class CS_521 Information structures in Python
"""

#Final Project Class File:--------------------------------------------------
    
class FitnessStatus(object):
    def __init__(self, does_activities, __is_overweight, exc_freq_hrs_wk, is_on_diet):    
        self.does_activities = does_activities #T/F
        self.__is_overweight = __is_overweight  #T/F
        self.exc_freq_hrs_wk = exc_freq_hrs_wk #int
        self.is_on_diet = is_on_diet  #T/F
    
    def __repr__(self):
        return f' Does Activities: {self.does_activities}, \
is overweight: {self.__is_overweight},hrs/wk of excercise: {self.exc_freq_hrs_wk}, on diet: {self.is_on_diet}'
#----------------------------------------------------------------------------

test = FitnessStatus(True, False, 6, True)            
#print(test)            
#---------------------------------------------------------------------------

class DoingGreat(FitnessStatus):
    def __init__(self, is_losing_weight, is_happy ): #private method
        FitnessStatus.__init__(self, False, False, 6, True )            
        self.is_losing_weight = is_losing_weight
        self.is_happy = is_happy         
    
    def Killin_it(self, is_happy): #public method
        Exception(" f YOU ARE KILLIN' IT BRO!!!")
        try:
            is_happy != True
            return f" DONT WORRY!! YOU GOT THIS!!"
        except Exception as e: 
             f'{Exception}'
    def __repr__(self): #repr / private method
        return f'Awesome Job! Losing weight: { self.is_losing_weight}, Happy: {self.is_happy}'
#-----------------------------------------------------------------------------

test1 = DoingGreat(True, False)
#print(test1)

test1.Killin_it(True)
test1.Killin_it(False)
test1.__repr__()
#------------------------------------------------------------------------
class DoingOkay(FitnessStatus):
    def __init__(self, is_maintaining_weight, is_motivated ):
        FitnessStatus.__init__(self, True, None, 4, False )
        self.is_maintaining_weight = is_maintaining_weight
        self.is_motivated = is_motivated
        
    def __repr__(self):
        return f"You are Doing Okay... Weight maintained: {self.is_maintaining_weight}, \
Motivated: {self.is_motivated} Let's keep it up!"
#----------------------------------------------------------------------------

test2= DoingOkay(True, True)
#print(test2)
#----------------------------------------------------------------------------    
class NeedsImprovement(FitnessStatus):
    def __init__(self, is_trying, showed_up):
        FitnessStatus.__init__(self, False, True, 1, False)
        self.is_trying = is_trying
        self.showed_up = showed_up
        
        
    def __repr__(self):
        return f'We have a long way to go...  Trying: {self.is_trying}, Showed up: {self.showed_up}'
            
            
#-----------------------------------------------------------------------------
#unit tests:
test3 = NeedsImprovement(False, False, )
#print(test3)

#unit testing:    
test = FitnessStatus(True, False, 6, True)            
#print(test)       
#-----------------------------------------------------------------------------   
test1 = DoingGreat(True, False)
#print(test1)
test1.Killin_it(True)
test1.Killin_it(False)
test1.__repr__()    
test2.__repr__()
test3.__repr__()    

            