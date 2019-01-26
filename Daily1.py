# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 21:26:03 2019

@author: Zhe Shen
"""

#Daily Coding Problem: Problem #1
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
#Bonus: Can you do this in one pass?

arr = [10,15,3,7,5]
k = 13
def findSummand(arr, k):
    for i in range(len(arr)-1):
        temp = arr
        new_arr = [x+temp[i] for x in temp]
        if k in new_arr:
            return True
    return False
print(findSummand(arr,k))