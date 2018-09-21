# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:41:03 2018

@author: gyojh
"""

class Rational:
    
    def __init__(self,a,b):
        
        #self has 2 parts. it has a and b, storing a as a numerator and b as a
        # denominator
        self.__n = a
        self.__d = b
        
    def getNumerator(self):
        return self.__n
    
    def getDenominator(self):
        return self.__d
    
    # multiply by the right hand side (b)
    def __mul__(self,rhs):
        
        a = self.__n * rhs.getNumerator()
        b = self.__d * rhs.getDenominator()
        return Rational(a,b)
    
    def __repr__(self):
        str = '%d' % self.__n
        str = str + '/'
        str = str + 'd%' % self.__d
        return str
    
    def __neg__(self):
        a = self.__n
        b = -self.__d
        return Rational(a,b)
    
    