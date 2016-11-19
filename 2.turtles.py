# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:05:55 2016

@author: Martin
"""

import turtle
import random

# Turtle
def turtle1():
      
    turtle.forward(100)
    turtle.left(90)
   
    if round(abs(turtle.pos())) == 0:
        turtle.end_fill()
        turtle.done()
    else:
        turtle1()
   
    
turtle.reset()
turtle.begin_fill()
turtle1()    
    
#########################################################

def turtle2(t, l):
      
    t.forward(l)
    t.right(10)
   
    if l < 50:
        turtle2(t, l * 1.02)
#    else:
#        turtle.end_poly()
#        t.done()
   
# turty.reset()
turty = turtle.Turtle()
turtle2(turty, 1)   


turty.reset()

#########################################################

def turtle3(t, l):
      
    t.forward(l)
    t.right(10)
   
    if l < 20:

        turtle3(t, l + 0.1)
   
   #        turtle.end_poly()
   #     t.done()
    

turty = turtle.Turtle()


turtle3(turty, 0.1)   
turty.reset()

#########################################################

def turtle4(t, start_x, start_y, nKruhu):
    
    turty.penup()
    turty.goto(start_x, start_y)
    turty.pendown()    
    
#    while(True):
    for i in range(20):     
        t.forward(6)
        t.right(20)
        
 #       if (start_x, start_y) == t.pos():
 #           break
        
    if nKruhu != 0:
        turtle4(t, random.gauss(0, 100), random.gauss(0, 100), nKruhu - 1)


turty = turtle.Turtle()
turty.speed(10)

nKruhu = 10
turtle4(turty, 0, 0, nKruhu)   

turty.reset()

#########################################################

def turtle5(t, start_x, start_y):
    
    t.fd(100)
    t.right(120)
    t.fd(100)
    t.left(60)
    t.bk(100)
    t.fd(100)

    if round(abs(turty.pos())) != 0:
        turtle5(t, turty.xcor(), turty.ycor())
        
   
turty = turtle.Turtle()
# turtle.pensize(5)
turty.speed(6)
    

turty.reset()

turty.color('black', 'yellow')
turty.begin_fill()
turtle5(turty, 0, 0)   
turty.end_fill()


#########################################################



def koch(t, length):

    dec = 1 
    
    if length <= 10:
        t.fd(2)
    
    else:
                
        koch(t, length - dec)
        t.left(60)
        
        koch(t, length - dec)
        t.right(120)
        
        koch(t, length - dec)
        t.left(60)
        
        koch(t, length - dec)
    

turty.reset()
koch(turty, 20)

      
      
   
turty = turtle.Turtle()
# turtle.pensize(5)
turty.speed(10)
    
kochLevel = 3
length = 20

turty.reset()
 




