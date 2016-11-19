# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:35:40 2016

@author: Martin
"""

import math

        
def factorialRec(n):
    
    if n < 0:
        print("Muzete zadat pozitivni integer")
    elif n == 1 or n == 0:
        res = 1
    else:
        res = n * factorialRec(n - 1)
        
    return res        
        

def fibonacciRec(n):
    
    if n == 1 or n == 2:
        res = 1   
    else: 
        res = fibonacciRec(n - 2) + fibonacciRec(n - 1)  
        
    return res

       
def GrCommDivRec(x1, x2):
    
#    if x1 == 0 or x2 == 0:   
#        return min(x1, x2)       
    
    min_x = min(x1, x2) 
    max_x = max(x1, x2)     
     
    rem_x = max_x % min_x    
    
    if rem_x == 0:
        return min_x
    else:
        return GrCommDivRec(rem_x, min_x)

           


factorialRec(10)
math.factorial(10) == factorialRec(10)

fibonacciRec(5)

GrCommDivRec(44, 28)







