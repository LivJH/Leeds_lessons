# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:37:37 2018

@author: gyojh
"""

class Person:
    #to make a person we make this, the person is the class and we need to make
    # attributes (money and happiness)
        def __init__(self, money, happiness):
            self.money = money
            self.happiness = happiness
        
        def work(self):
            """Working increases money but decreases happinesss"""
            # this increaees money by 10 and decreases happiness by 5
            self.money = self.money + 10
            self.happiness = self.happiness - 5
        def consume(self):
            """"Consumption decreases money, increases happiness"""
            self.happiness += 7
            self.money -= 8
    # overwriting the print function if therre are other prints on the page
        def __repr__(self):
            return (f"A person with money = {self.money} "
                    f"and happiness - {self.happiness}")
            
        def interact(self, other):
            """interact with another person; increases happiness
            for both"""
            self.happiness += 1
            other.happiness += 1
        

            # or: self.happiness -= 5
    #this person has 100 money and 10 happiness, this is the format of above  
#now set jitse to work and see how much he remains 
jitse = Person(100, 10)
jitse.work()
print("jitse's money:", jitse.money)
print(f"jitse: money = {jitse.money}, "
      f"happiness = {jitse.happiness}")

rob = Person(500,5)
rob.interact(jitse)
print('After interaction:')
print (jitse)
print(rob)