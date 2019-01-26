# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:17:10 2019

@author: Zhe Shen
"""

#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?

test = [1,2,3,4,5]
test1 = [3,2,1]
def arrMulDiv(arr):
    product = 1
    res = []
    for i in arr:
          product = product * i
          
    
    for i in arr:
        res.append(product / i)
    return res
print(arrMulDiv(test1))

def arrMul(arr):
    product = 1
    res = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product = product * arr[j]
        res.append(product)
        
    return res
    
print(arrMul(test1))
