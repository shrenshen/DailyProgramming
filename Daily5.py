# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:36:38 2019

@author: Zhe Shen
"""

#cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
#For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
#Given this implementation of cons:
#
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
#Implement car and cdr.

def car(pair):
    def return_first(a,b):
        return a
    return pair(return_first)

a = car(cons(2,3))
print(a)

